#!/usr/bin/env python

from paths import VinaPath, VINA_BIN, BOX_GYRA_BIN, POCKETS
from dockedpose import rmsd_between  # https://gist.github.com/EricTing/4a540c8e13321954d2f3
import luigi
import json
import pybel
import subprocess32
import shlex
import os


class LigPdbqt(luigi.Task):
    tname = luigi.Parameter()

    def run(self):
        vina_path = VinaPath(self.tname)
        lig_sdf = vina_path.lig_sdf
        lig = pybel.readfile("sdf", lig_sdf).next()
        lig.removeh()
        lig.write("pdbqt", self.output().path)

    def output(self):
        ofn = VinaPath(self.tname).lig_pdbqt
        return luigi.LocalTarget(ofn)


class RunVina(luigi.Task):
    """benchmark Vina using the geometric center of the native ligand
    """
    tname = luigi.Parameter()

    def output(self):
        ofn = os.path.splitext(self.requires().output().path)[
            0] + "_vina.pdbqt"
        return luigi.LocalTarget(ofn)

    def requires(self):
        return LigPdbqt(self.tname)

    def run(self):
        lig_pdbqt = self.requires().output().path
        vina_path = VinaPath(self.tname)
        lig_sdf = vina_path.lig_sdf
        prt_pdbqt = vina_path.prt_pdbqt

        cmds = ['perl', BOX_GYRA_BIN, lig_sdf]
        stdout = subprocess32.check_output(cmds)
        box_size, x, y, z = stdout.split()

        cmd = '''%s --receptor %s --ligand %s --center_x %s --center_y %s --center_z %s --size_x %s --size_y %s --size_z %s --cpu 1 --out %s''' % (
            VINA_BIN, prt_pdbqt, lig_pdbqt, x, y, z, box_size, box_size,
            box_size, self.output().path)
        print(cmd)
        vina_out = subprocess32.check_output(shlex.split(cmd))
        ofn = self.output().path + ".txt"
        with open(ofn, 'w') as ofs:
            ofs.write(vina_out)


class RunVinaOnPredictedPocket(RunVina):
    """benchmark Vina using the predicted binding pockets
    """

    def output(self):
        ofn = os.path.splitext(self.requires().output().path)[
            0] + "_pred_vina.pdbqt"
        return luigi.LocalTarget(ofn)

    def run(self):
        lig_pdbqt = self.requires().output().path
        vina_path = VinaPath(self.tname)
        lig_sdf = vina_path.lig_sdf
        prt_pdbqt = vina_path.prt_pdbqt

        cmds = ['perl', BOX_GYRA_BIN, lig_sdf]
        stdout = subprocess32.check_output(cmds)
        box_size, x, y, z = stdout.split()  # only for box_size
        x, y, z = POCKETS[self.tname]  # use the predicted binding pockets

        cmd = '''%s --receptor %s --ligand %s --center_x %s --center_y %s --center_z %s --size_x %s --size_y %s --size_z %s --cpu 1 --out %s''' % (
            VINA_BIN, prt_pdbqt, lig_pdbqt, x, y, z, box_size, box_size,
            box_size, self.output().path)

        print(cmd)
        vina_out = subprocess32.check_output(shlex.split(cmd))
        ofn = self.output().path + ".txt"
        with open(ofn, 'w') as ofs:
            ofs.write(vina_out)


class EvalVinaResult(luigi.Task):
    tname = luigi.Parameter()

    def requires(self):
        return [RunVina(self.tname), RunVinaOnPredictedPocket(self.tname)]

    def _run(self, result):
        result_pdbqt = result.output().path
        result_lig = pybel.readfile("pdbqt", result_pdbqt).next()
        native_lig = pybel.readfile("pdbqt",
                                    LigPdbqt(self.tname).output().path).next()
        result_rmsd = rmsd_between(native_lig, result_lig)

        return result_rmsd

    def run(self):
        result, result_pred_pkt = self.requires()
        result_rmsd = self._run(result)
        result_pred_pkt_rmsd = self._run(result_pred_pkt)
        data = {
            "native_pocket_vina_rmsd": result_rmsd,
            "predicted_pocket_vina_rmsd": result_pred_pkt_rmsd
        }
        with open(self.output().path, 'wb') as ofs:
            ofs.write(json.dumps(data, indent=4, separators=(',', ': ')))

    def output(self):
        ofn = os.path.splitext(LigPdbqt(self.tname).output().path)[0] + '.json'
        return luigi.LocalTarget(ofn)


def main(tname):
    luigi.build(
        [LigPdbqt(tname), RunVina(tname), RunVinaOnPredictedPocket(tname),
         EvalVinaResult(tname)],
        local_scheduler=True)


def test():
    tname = "10gsA00"
    eval = EvalVinaResult(tname)
    luigi.build([eval], local_scheduler=True)


if __name__ == '__main__':
    import sys
    main(sys.argv[1])