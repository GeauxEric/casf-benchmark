from os import path, makedirs

DAT = "/work/jaydy/dat/website-core-set/"
DOMAIN_DAT = "/work/jaydy/dat/dom"
VINA_INPUT = "/work/jaydy/dat/website-core-set/input"
VINA_BIN = "/project/michal/apps/autodock_vina_1_1_2_linux_x86/bin/vina"
GEAUX_OUTPUT = "/work/jaydy/dat/website-core-set/output"
BOX_GYRA_BIN = "/project/michal/apps/autodock_vina_1_1_2_linux_x86/bin/box-gyration.pl"


class Path:
    def __init__(self, id):
        self.id = id
        self.dat_dir = path.join(DAT, self.id)
        self.complex_pdb = path.join(self.dat_dir, self.id + "_complex.pdb")
        self.protein_pdb = path.join(self.dat_dir, self.id + "_protein.pdb")
        self.ligand_sdf = path.join(self.dat_dir, self.id + "_ligand.sdf")
        self.work_dir = path.join("/work/jaydy/working/casf_benchmark",
                                  self.id)

        try:
            makedirs(self.work_dir)
        except:
            pass


class ModelPath:
    def __init__(self, id, version="0.7"):
        """
        Keyword Arguments:
        id -- complex id
        """
        self.id = id
        self.version = version
        self.dat_dir = "/work/jaydy/dat/pred_pkt_casf"
        self.prt_pdb = path.join(self.dat_dir, "models-" + self.version,
                                 self.id + ".pdb")
        self.prt_pdbqt = path.join(self.dat_dir,
                                   "models-" + self.version + '-pdbqt',
                                   self.id + ".pdbqt")
        self.lig_sdf = VinaPath(self.id).lig_sdf
        self.work_dir = path.join(
            "/work/jaydy/working/casf_model_" + self.version, self.id)

        try:
            makedirs(self.work_dir)
        except Exception:
            pass


class Domain:
    def __init__(self, id):
        self.id = id
        self.dat_dir = path.join(DOMAIN_DAT, self.id)


class VinaPath:
    def __init__(self, id):
        "Paths for the inputs and outputs benchmarking CASF using Vina"
        self.id = id
        self.lig_pdbqt = path.join(VINA_INPUT, 'ligand-pdbqt',
                                   self.id[:4] + "_ligand.pdbqt")
        self.lig_sdf = path.join(VINA_INPUT, 'ligand-sdf',
                                 self.id[:4] + "_ligand.sdf")
        self.prt_pdbqt = path.join(VINA_INPUT, 'protein-pdbqt',
                                   self.id + '.pdbqt')


POCKETS = {'10gsA00': [11.563, 8.003, 26.912],
           '1a30A00': [7.47, 26.262, 6.276],
           '1bcuH00': [7.858, 20.856, 50.256],
           '1e66A01': [5.471, 65.63, 63.832],
           '1f8bA00': [26.185, 17.753, 62.924],
           '1f8cA00': [26.204, 17.694, 62.887],
           '1f8dA00': [26.2, 17.668, 62.842],
           '1gpkA01': [5.516, 65.263, 63.998],
           '1h23A01': [5.367, 65.283, 64.428],
           '1hfsA00': [35.559, 35.811, 25.149],
           '1hnnA00': [29.606, 42.742, 20.07],
           '1igjD00': [-9.459, 21.774, 26.464],
           '1jyqA00': [-26.021, 42.781, 32.13],
           '1kelL00': [-18.877, 34.471, 19.885],
           '1lbkB00': [10.458, 35.166, -4.443],
           '1lolA00': [0.907, 41.054, 46.433],
           '1loqA00': [40.59, 38.286, 36.261],
           '1lorA00': [40.59, 38.383, 36.093],
           '1mq6A00': [8.297, 8.736, 23.165],
           '1n1mA05': [81.689, 73.466, 96.891],
           '1n2vA00': [16.407, 17.43, 19.915],
           '1nvqA00': [4.892, 7.046, 16.971],
           '1o3fA00': [41.588, -2.473, 29.322],
           '1o5bB00': [8.56, 4.145, 24.575],
           '1os0A00': [36.545, 40.838, -4.286],
           '1oytH00': [14.513, -12.348, 20.997],
           '1p1qC00': [45.911, 25.921, 42.059],
           '1ps3A01': [32.635, 65.617, 8.342],
           '1q8tA00': [7.935, 9.122, 3.157],
           '1q8uA00': [8.038, 8.982, 3.235],
           '1r5yA00': [16.543, 17.183, 19.914],
           '1slnA00': [-17.629, 93.891, 82.488],
           '1sqaA00': [22.337, 16.808, 32.822],
           '1u1bA00': [-23.622, -33.381, 16.033],
           '1u33A01': [12.651, 17.396, 41.838],
           '1utoA00': [44.087, 22.62, 51.527],
           '1vsoA00': [40.517, 4.52, 7.246],
           '1w3kA00': [60.886, 41.348, 38.519],
           '1w3lA00': [61.316, 41.326, 38.52],
           '1w4oA00': [37.34, -1.868, 12.808],
           '1xd0A01': [12.749, 17.923, 42.607],
           '1yc1A00': [1.375, 34.256, -3.091],
           '1z95A00': [26.576, 2.677, 3.474],
           '1zeaH00': [44.576, 51.754, 86.858],
           '2brbA00': [15.739, -2.686, 12.121],
           '2cbjA02': [32.435, 42.488, 21.885],
           '2cetA00': [1.041, 10.752, 5.856],
           '2d1oA00': [30.798, 7.271, 15.066],
           '2d3uA02': [7.791, 33.606, 76.582],
           '2fvdA00': [-0.548, 28.374, 9.522],
           '2g70A00': [29.042, 42.54, 19.563],
           '2gssA00': [7.64, 2.17, 25.748],
           '2hb1A00': [45.845, 13.406, 1.665],
           '2iwxA00': [57.284, 76.559, -3.975],
           '2j62A02': [33.345, 42.441, 21.667],
           '2jdmB00': [12.194, 3.904, -3.928],
           '2jduC00': [-39.916, 20.78, 12.055],
           '2jdyA00': [-5.65, -17.02, -5.158],
           '2obfA00': [30.456, 42.485, 19.671],
           '2oleA00': [-2.953, 7.919, -3.348],
           '2p4yA00': [18.602, 5.16, 16.456],
           '2pcpB00': [-6.103, -25.242, -13.302],
           '2pq9A01': [57.892, 9.005, 27.879],
           '2qbpA00': [45.665, 13.632, 1.555],
           '2qbrA00': [46.134, 13.651, 1.855],
           '2qftA01': [57.201, 8.971, 27.968],
           '2qmjA02': [-16.714, -6.949, -10.045],
           '2r23A00': [-9.107, 6.685, 62.887],
           '2v00A00': [-1.408, 6.714, 9.378],
           '2v7aA00': [-42.495, -48.746, -10.359],
           '2vo5A03': [29.994, 47.813, -1.879],
           '2votA03': [29.312, 46.979, -1.633],
           '2vvnA02': [8.411, -10.811, 3.22],
           '2vw5A00': [38.605, -9.762, 37.376],
           '2w66A02': [8.931, -11.364, 3.498],
           '2wcaA02': [-8.808, -13.295, 8.373],
           '2wegA00': [16.664, 5.411, 14.323],
           '2wtvA00': [2.056, -9.797, -2.684],
           '2x00A00': [3.244, 25.159, -2.859],
           '2x0yA02': [32.739, 44.139, 21.247],
           '2x8zA00': [28.589, 2.061, -43.947],
           '2x97A00': [28.557, -2.009, 44.933],
           '2xb8A00': [15.981, 5.489, 36.04],
           '2xbvA00': [11.206, 64.325, 2.981],
           '2xdlA00': [66.899, 35.626, 25.956],
           '2xhmA00': [-16.0, 23.696, -10.731],
           '2xnbA00': [27.479, 28.175, 25.873],
           '2xy9A00': [14.234, -3.846, -22.418],
           '2xysA00': [-43.191, 6.917, -15.965],
           '2y5hA00': [-2.468, 10.548, 24.151],
           '2yfeA00': [14.689, 18.571, 41.918],
           '2ygeA00': [20.553, -34.163, -4.063],
           '2ykiA00': [1.92, 9.734, 24.927],
           '2ymdB00': [9.874, 7.71, 6.685],
           '2zcqA00': [16.89, 55.208, 38.188],
           '2zcrA00': [16.853, 54.751, 37.905],
           '2zjwA00': [36.571, -5.139, 8.826],
           '2zwzA01': [-2.241, 28.253, 20.922],
           '2zx6A01': [-2.296, 28.208, 21.093],
           '2zxdA01': [-2.119, 28.335, 21.697],
           '3acwA00': [56.063, 12.579, 53.045],
           '3ag9B00': [11.277, 5.496, 13.991],
           '3b3sA00': [35.763, -1.374, 39.49],
           '3b3wA00': [36.184, -1.495, 39.627],
           '3b68A00': [26.501, 2.981, 2.677],
           '3bfuA00': [-31.513, -5.066, 42.526],
           '3bkkA00': [46.034, 46.336, 45.015],
           '3bpcA00': [28.418, -3.299, -0.035],
           '3cftA00': [-21.334, 0.104, -25.965],
           '3cj2A02': [-24.299, 8.452, -15.25],
           '3coyA00': [15.45, 10.155, 1.575],
           '3cyxA00': [21.779, 26.112, 16.761],
           '3d4zA01': [32.231, 65.162, 8.083],
           '3dd0A00': [-4.664, 3.532, 14.41],
           '3dxgA00': [37.227, -1.898, 13.014],
           '3e93A00': [46.096, 32.82, 32.574],
           '3ehyA00': [-2.674, -5.72, -5.423],
           '3ejrA02': [31.992, 66.441, 7.417],
           '3f17A00': [2.944, -5.842, 5.399],
           '3f3aA00': [-27.517, -3.118, -20.132],
           '3f3cA00': [27.586, 31.518, 19.87],
           '3f3eA00': [26.782, 31.505, 19.644],
           '3f80A00': [23.247, -15.254, 6.851],
           '3fcqA00': [36.257, 40.239, -4.309],
           '3fk1A01': [57.493, 8.901, 27.894],
           '3fv1A00': [-6.592, 15.713, 19.473],
           '3g0wA00': [53.936, 2.848, 2.99],
           '3g2zA00': [-5.192, 53.501, 11.526],
           '3gbbA00': [0.357, 44.127, 1.699],
           '3gcsA00': [-17.834, -2.225, 17.941],
           '3ge7A00': [16.677, 17.03, 19.983],
           '3gnwA01': [28.436, 8.198, 36.97],
           '3gy4A00': [-0.232, 17.434, 17.775],
           '3hucA00': [19.887, 2.615, -23.008],
           '3i3bA01': [-12.289, -27.33, -26.915],
           '3imcA00': [15.41, 10.115, 1.845],
           '3ivgB00': [1.225, -10.286, 35.706],
           '3jvsA00': [31.5, -6.432, 23.469],
           '3kgpA00': [-28.711, 85.973, -12.067],
           '3kv2A00': [24.917, -12.504, -4.314],
           '3kwaA00': [-4.393, 3.72, 14.375],
           '3l3nA00': [43.257, 7.081, 113.067],
           '3l4uA02': [-4.656, -17.437, -20.709],
           '3l4wA02': [42.191, 91.139, 34.443],
           '3lkaA00': [3.103, -5.709, 5.433],
           '3mfvA00': [-20.353, 13.659, -5.187],
           '3muz101': [13.133, 26.28, 76.192],
           '3mygA00': [-6.613, 29.153, 78.702],
           '3n7aA00': [45.789, 1.848, 22.883],
           '3n86A00': [31.798, 27.853, -2.133],
           '3noxA04': [47.448, 49.002, 39.77],
           '3nq3A00': [10.526, -1.425, 2.386],
           '3nw9A00': [-2.509, 20.32, 13.626],
           '3oe5A00': [19.17, -28.707, 11.895],
           '3ov1A00': [-10.79, 11.382, -2.316],
           '3owjA00': [22.061, 6.991, 15.328],
           '3oztA00': [34.517, -2.289, -11.963],
           '3pe2A00': [21.974, -30.349, 15.317],
           '3pwwA00': [-1.329, 6.219, 9.497],
           '3pxfA00': [123.765, 131.974, 68.436],
           '3s8oA00': [10.387, -9.624, -2.258],
           '3su2A00': [-14.283, -6.569, 14.907],
           '3su3A00': [-14.215, -6.322, 14.889],
           '3su5A00': [-14.237, -6.534, 14.586],
           '3u9qA00': [4.675, -0.342, 20.53],
           '3udhA00': [22.861, 34.664, 43.142],
           '3ueuA00': [-3.233, 9.481, 20.505],
           '3uexA00': [-2.451, 15.416, 18.71],
           '3uo4A00': [6.203, 29.615, 6.226],
           '3uriA00': [2.881, 33.043, 15.131],
           '3utuH00': [14.421, -12.218, 20.912],
           '3vd4A01': [-12.71, -25.996, -26.495],
           '3vh9A00': [18.64, -30.139, -9.233],
           '3zsoB00': [-9.188, 46.331, 0.33],
           '3zsxB00': [-9.248, 46.231, 0.647],
           '4de1A00': [-5.216, 53.172, 11.552],
           '4de2A00': [-5.171, 53.562, 11.502],
           '4desA00': [21.181, 0.275, -5.966],
           '4dewA00': [21.651, 42.401, 39.043],
           '4djrB00': [17.806, 35.564, 16.822],
           '4djvA00': [23.271, 12.908, 23.898],
           '4g8mA00': [7.376, 26.454, 20.145],
           '4gidA00': [42.185, -3.765, 12.269],
           '4gqqA01': [11.835, -19.221, 113.343],
           '4tmnE00': [52.33, 17.161, -4.254]}

MODEL_PKTS = {'0.5': {'10gsA00': [25.975, -3.178, 21.224],
                      '1a30A00': [13.219, 22.402, 6.516],
                      '1bcuH00': [8.014, 20.912, 49.724],
                      '1e66A01': [5.393, 65.596, 64.304],
                      '1f8bA00': [26.178, 17.761, 62.934],
                      '1f8cA00': [26.203, 17.699, 62.892],
                      '1f8dA00': [26.193, 17.674, 62.85],
                      '1gpkA01': [5.44, 64.923, 64.043],
                      '1hfsA00': [35.613, 35.701, 25.157],
                      '1hnnA00': [28.554, 52.273, 21.398],
                      '1igjD00': [-9.469, 21.484, 26.526],
                      '1jyqA00': [-7.099, 52.147, 38.545],
                      '1lbkB00': [10.381, 34.261, -5.698],
                      '1lolA00': [0.828, 41.061, 46.374],
                      '1loqA00': [40.7, 38.051, 36.101],
                      '1lorA00': [40.852, 38.303, 36.092],
                      '1mq6A00': [8.319, 8.547, 23.315],
                      '1n1mA05': [83.298, 75.293, 97.887],
                      '1n2vA00': [16.343, 17.436, 19.892],
                      '1nvqA00': [4.65, 7.2, 17.027],
                      '1o3fA00': [41.587, -2.433, 29.317],
                      '1o5bB00': [8.467, 4.052, 24.616],
                      '1os0A00': [36.538, 40.84, -4.286],
                      '1oytH00': [14.169, -12.417, 21.607],
                      '1p1qC00': [45.561, 25.976, 41.82],
                      '1ps3A01': [32.296, 65.502, 8.219],
                      '1q8tA00': [8.148, 9.006, 3.16],
                      '1q8uA00': [8.028, 8.856, 3.014],
                      '1r5yA00': [16.511, 17.191, 19.914],
                      '1slnA00': [-17.544, 93.86, 82.598],
                      '1sqaA00': [22.386, 16.859, 32.792],
                      '1u1bA00': [-23.696, -33.457, 16.143],
                      '1utoA00': [44.041, 22.625, 51.497],
                      '1vsoA00': [40.77, 4.473, 7.309],
                      '1w3kA00': [60.905, 41.228, 38.543],
                      '1w3lA00': [61.329, 41.218, 38.546],
                      '1w4oA00': [37.317, -1.869, 12.748],
                      '1yc1A00': [16.662, 26.484, 10.023],
                      '1z95A00': [26.612, 2.669, 3.463],
                      '1zeaH00': [39.401, 49.718, 81.638],
                      '2brbA00': [15.811, -2.653, 12.106],
                      '2cbjA02': [32.212, 42.603, 21.922],
                      '2d1oA00': [30.739, 7.203, 15.015],
                      '2fvdA00': [10.471, 18.897, 26.31],
                      '2gssA00': [10.092, 6.544, 26.482],
                      '2hb1A00': [45.835, 13.396, 1.661],
                      '2iwxA00': [57.238, 76.522, -4.031],
                      '2j62A02': [33.239, 42.464, 21.665],
                      '2j78A00': [2.673, 11.589, 3.209],
                      '2jdmB00': [12.124, 3.904, -3.933],
                      '2jduC00': [-42.426, -0.995, 2.847],
                      '2jdyA00': [-5.657, -17.01, -5.048],
                      '2oleA00': [-2.946, 7.964, -3.388],
                      '2p4yA00': [18.789, 4.971, 16.402],
                      '2pcpB00': [-7.785, -27.201, -12.836],
                      '2pq9A01': [57.908, 8.963, 27.742],
                      '2qbpA00': [45.654, 13.583, 1.562],
                      '2qbrA00': [46.137, 13.63, 1.822],
                      '2qftA01': [64.642, 11.262, 2.552],
                      '2v00A00': [-1.595, 6.463, 9.172],
                      '2v7aA00': [-42.485, -47.734, -9.935],
                      '2vvnA02': [8.45, -10.885, 2.932],
                      '2vw5A00': [38.585, -9.916, 37.321],
                      '2w66A02': [8.478, -11.03, 3.417],
                      '2wcaA02': [-8.931, -13.317, 8.232],
                      '2wegA00': [16.684, 5.414, 14.316],
                      '2wtvA00': [2.199, -9.734, -2.624],
                      '2x00A00': [26.369, 7.19, 2.173],
                      '2x97A00': [28.531, -2.007, 44.943],
                      '2xb8A00': [16.342, 5.843, 36.927],
                      '2xbvA00': [11.238, 64.435, 3.036],
                      '2xdlA00': [66.992, 35.563, 25.96],
                      '2xhmA00': [-15.974, 23.669, -10.762],
                      '2xnbA00': [27.639, 28.348, 26.073],
                      '2xy9A00': [14.203, -3.857, -22.455],
                      '2xysA00': [-25.009, 28.6, -6.86],
                      '2y5hA00': [-2.454, 10.584, 24.2],
                      '2yfeA00': [14.686, 18.59, 41.981],
                      '2ygeA00': [20.544, -34.205, -4.082],
                      '2ykiA00': [1.909, 9.739, 24.796],
                      '2zcqA00': [17.442, 54.583, 37.982],
                      '2zcrA00': [16.99, 54.771, 37.949],
                      '2zjwA00': [33.608, -15.649, 1.331],
                      '2zwzA01': [-2.1, 28.555, 21.558],
                      '2zxdA01': [-1.954, 28.603, 21.859],
                      '3acwA00': [55.866, 11.825, 52.821],
                      '3b3sA00': [35.83, -1.439, 39.502],
                      '3b3wA00': [36.192, -1.409, 39.601],
                      '3b68A00': [35.417, 13.89, 12.842],
                      '3bfuA00': [-31.511, -4.975, 42.491],
                      '3bkkA00': [46.019, 46.35, 45.01],
                      '3bpcA00': [26.624, -4.201, 0.492],
                      '3cftA00': [-21.361, 0.097, -25.986],
                      '3coyA00': [23.464, 18.35, -12.224],
                      '3cyxA00': [21.653, 26.046, 16.684],
                      '3d4zA01': [32.116, 65.285, 7.959],
                      '3dd0A00': [-4.664, 3.546, 14.414],
                      '3dxgA00': [37.201, -1.952, 12.905],
                      '3e93A00': [45.582, 32.317, 32.671],
                      '3ehyA00': [-2.69, -5.72, -5.427],
                      '3ejrA02': [31.975, 66.723, 7.499],
                      '3f17A00': [2.961, -5.84, 5.385],
                      '3f3aA00': [-42.335, 5.541, -9.503],
                      '3f3cA00': [27.577, 31.501, 19.843],
                      '3f80A00': [23.237, -15.25, 6.828],
                      '3fcqA00': [36.243, 40.24, -4.316],
                      '3fk1A01': [57.532, 8.781, 27.669],
                      '3g0wA00': [55.091, -11.572, 1.229],
                      '3g2zA00': [-5.136, 53.488, 11.519],
                      '3gbbA00': [0.453, 44.175, 1.676],
                      '3gcsA00': [-18.486, 2.089, 21.601],
                      '3ge7A00': [-4.359, 1.394, 12.184],
                      '3gnwA01': [28.463, 8.163, 36.997],
                      '3gy4A00': [-0.21, 17.409, 17.794],
                      '3hucA00': [19.495, 2.598, -22.553],
                      '3i3bA01': [-12.212, -27.466, -26.843],
                      '3imcA00': [15.317, 10.11, 1.778],
                      '3ivgB00': [-19.281, -6.858, 21.504],
                      '3jvsA00': [15.519, -2.172, 11.945],
                      '3kgpA00': [-28.836, 85.934, -12.097],
                      '3kv2A00': [15.623, -23.132, -13.546],
                      '3kwaA00': [0.412, -19.093, 17.576],
                      '3l3nA00': [43.237, 7.048, 113.051],
                      '3lkaA00': [3.107, -5.704, 5.427],
                      '3mfvA00': [-20.331, 13.646, -5.181],
                      '3muz101': [13.047, 26.402, 76.24],
                      '3mygA00': [-6.546, 29.187, 78.802],
                      '3n7aA00': [45.323, 2.008, 22.527],
                      '3n86A00': [31.994, 27.637, -2.414],
                      '3noxA04': [42.66, 54.208, 35.782],
                      '3nw9A00': [-2.223, 20.036, 13.455],
                      '3oe5A00': [19.08, -28.583, 11.737],
                      '3ov1A00': [-10.708, 11.351, -2.246],
                      '3owjA00': [22.352, 8.353, 15.02],
                      '3oztA00': [34.378, -2.269, -11.789],
                      '3pe2A00': [21.935, -30.064, 15.426],
                      '3pwwA00': [-1.506, 5.961, 9.322],
                      '3pxfA00': [90.372, 147.182, 51.208],
                      '3s8oA00': [10.483, -9.625, -2.092],
                      '3u9qA00': [4.756, -0.478, 20.55],
                      '3udhA00': [22.827, 34.879, 43.232],
                      '3uo4A00': [6.329, 29.361, 6.278],
                      '3uriA00': [2.73, 32.247, 15.214],
                      '3utuH00': [14.257, -12.199, 21.068],
                      '3vd4A01': [-12.516, -26.002, -26.788],
                      '3vh9A00': [18.698, -30.112, -9.227],
                      '3zsoB00': [-9.086, 46.395, 0.028],
                      '4de1A00': [-5.218, 53.22, 11.521],
                      '4de2A00': [-9.903, 65.082, -2.988],
                      '4desA00': [43.405, -17.164, -4.709],
                      '4dewA00': [21.67, 42.389, 38.986],
                      '4djrB00': [19.424, 29.824, 13.36],
                      '4djvA00': [23.173, 13.014, 23.595],
                      '4g8mA00': [7.228, 26.424, 20.169],
                      '4gidA00': [42.303, -3.795, 12.331],
                      '4tmnE00': [52.321, 17.169, -4.256]},
              '0.7': {'10gsA00': [25.975, -3.178, 21.224],
                      '1a30A00': [13.219, 22.402, 6.516],
                      '1bcuH00': [8.014, 20.912, 49.724],
                      '1e66A01': [4.57, 65.345, 65.551],
                      '1f8bA00': [26.204, 17.788, 62.886],
                      '1f8cA00': [26.216, 17.72, 62.855],
                      '1f8dA00': [26.206, 17.694, 62.812],
                      '1gpkA01': [4.535, 64.679, 65.429],
                      '1hfsA00': [35.574, 35.781, 25.116],
                      '1hnnA00': [28.554, 52.273, 21.398],
                      '1igjD00': [-14.778, 20.913, 32.98],
                      '1jyqA00': [-7.099, 52.147, 38.545],
                      '1lbkB00': [10.381, 34.261, -5.698],
                      '1lolA00': [0.828, 41.061, 46.374],
                      '1loqA00': [40.533, 38.181, 36.273],
                      '1lorA00': [40.655, 38.55, 36.152],
                      '1mq6A00': [8.319, 8.547, 23.315],
                      '1n1mA05': [83.298, 75.293, 97.887],
                      '1n2vA00': [16.343, 17.436, 19.892],
                      '1nvqA00': [4.65, 7.2, 17.027],
                      '1o3fA00': [41.587, -2.433, 29.317],
                      '1o5bB00': [8.467, 4.052, 24.616],
                      '1os0A00': [36.542, 40.833, -4.284],
                      '1oytH00': [14.169, -12.417, 21.607],
                      '1p1qC00': [45.561, 25.976, 41.82],
                      '1ps3A01': [32.296, 65.502, 8.219],
                      '1q8tA00': [8.148, 9.006, 3.16],
                      '1q8uA00': [8.028, 8.856, 3.014],
                      '1r5yA00': [16.511, 17.191, 19.914],
                      '1slnA00': [-17.58, 93.869, 82.551],
                      '1sqaA00': [22.386, 16.859, 32.792],
                      '1u1bA00': [-23.696, -33.457, 16.143],
                      '1u33A01': [12.051, 17.947, 43.141],
                      '1utoA00': [44.041, 22.625, 51.497],
                      '1vsoA00': [40.77, 4.473, 7.309],
                      '1w3kA00': [59.187, 45.498, 34.65],
                      '1w3lA00': [61.332, 41.315, 38.54],
                      '1w4oA00': [37.3, 4.391, 16.549],
                      '1xd0A01': [12.147, 18.485, 43.908],
                      '1yc1A00': [1.411, 34.212, -3.106],
                      '1z95A00': [26.647, 2.71, 3.415],
                      '2brbA00': [15.811, -2.653, 12.106],
                      '2cbjA02': [32.212, 42.603, 21.922],
                      '2d1oA00': [23.202, 0.897, 13.708],
                      '2fvdA00': [-0.442, 28.365, 9.179],
                      '2gssA00': [10.092, 6.544, 26.482],
                      '2hb1A00': [45.835, 13.396, 1.661],
                      '2iwxA00': [57.303, 76.542, -3.976],
                      '2j62A02': [38.394, 68.711, 23.23],
                      '2j78A00': [1.326, 10.713, 8.811],
                      '2jdmB00': [10.181, 13.76, -4.217],
                      '2jduC00': [-39.818, 20.814, 12.026],
                      '2jdyA00': [-5.657, -17.01, -5.048],
                      '2oleA00': [-2.946, 7.964, -3.388],
                      '2p4yA00': [18.733, 5.117, 16.393],
                      '2pq9A01': [57.908, 8.963, 27.742],
                      '2qbpA00': [45.654, 13.583, 1.562],
                      '2qbrA00': [46.137, 13.63, 1.822],
                      '2qftA01': [64.642, 11.262, 2.552],
                      '2v00A00': [-1.409, 6.773, 9.512],
                      '2v7aA00': [-42.485, -47.734, -9.935],
                      '2vo5A03': [28.906, 43.081, 1.459],
                      '2votA03': [29.35, 47.189, -1.706],
                      '2vvnA02': [8.45, -10.885, 2.932],
                      '2vw5A00': [38.588, -9.834, 37.399],
                      '2w66A02': [8.478, -11.03, 3.417],
                      '2wcaA02': [-8.931, -13.317, 8.232],
                      '2wegA00': [10.641, -7.913, -2.764],
                      '2wtvA00': [2.199, -9.734, -2.624],
                      '2x00A00': [3.206, 25.135, -2.919],
                      '2x97A00': [28.531, -2.007, 44.943],
                      '2xb8A00': [16.342, 5.843, 36.927],
                      '2xbvA00': [11.238, 64.435, 3.036],
                      '2xdlA00': [66.846, 35.645, 25.89],
                      '2xhmA00': [-15.974, 23.669, -10.762],
                      '2xnbA00': [27.639, 28.348, 26.073],
                      '2xy9A00': [14.203, -3.857, -22.455],
                      '2xysA00': [-25.009, 28.6, -6.86],
                      '2y5hA00': [-2.454, 10.584, 24.2],
                      '2yfeA00': [14.721, 18.573, 41.968],
                      '2ygeA00': [20.527, -34.179, -4.08],
                      '2ykiA00': [1.882, 9.736, 25.01],
                      '2zcqA00': [-1.085, 69.629, 41.745],
                      '2zcrA00': [16.99, 54.771, 37.949],
                      '2zjwA00': [36.544, -4.933, 8.79],
                      '2zwzA01': [-2.1, 28.555, 21.558],
                      '2zxdA01': [-1.954, 28.603, 21.859],
                      '3acwA00': [55.866, 11.825, 52.821],
                      '3b3sA00': [33.641, 21.479, 45.24],
                      '3b3wA00': [36.192, -1.409, 39.601],
                      '3b68A00': [26.487, 3.013, 2.633],
                      '3bfuA00': [-31.511, -4.975, 42.491],
                      '3bkkA00': [46.019, 46.35, 45.01],
                      '3bpcA00': [23.618, -3.266, -7.764],
                      '3cftA00': [-21.358, 0.098, -25.996],
                      '3coyA00': [15.444, 10.232, 1.533],
                      '3cyxA00': [21.653, 26.046, 16.684],
                      '3d4zA01': [32.116, 65.285, 7.959],
                      '3dd0A00': [-4.664, 3.526, 14.39],
                      '3dxgA00': [37.201, -1.952, 12.905],
                      '3e93A00': [45.582, 32.317, 32.671],
                      '3ehyA00': [-2.703, -5.717, -5.445],
                      '3ejrA02': [31.975, 66.723, 7.499],
                      '3f17A00': [2.942, -5.824, 5.416],
                      '3f3aA00': [-42.335, 5.541, -9.503],
                      '3f3cA00': [27.577, 31.501, 19.843],
                      '3f80A00': [23.254, -15.273, 6.855],
                      '3fcqA00': [28.199, 55.325, -5.701],
                      '3fk1A01': [57.532, 8.781, 27.669],
                      '3g0wA00': [53.894, 2.883, 2.945],
                      '3g2zA00': [-5.136, 53.488, 11.519],
                      '3gbbA00': [5.854, 60.303, 3.047],
                      '3gcsA00': [-18.486, 2.089, 21.601],
                      '3ge7A00': [16.669, 17.035, 19.978],
                      '3gnwA01': [28.463, 8.163, 36.997],
                      '3gy4A00': [-0.21, 17.409, 17.794],
                      '3hucA00': [19.495, 2.598, -22.553],
                      '3i3bA01': [13.357, -24.783, -3.149],
                      '3imcA00': [15.317, 10.11, 1.778],
                      '3ivgB00': [1.239, -10.162, 35.763],
                      '3jvsA00': [5.603, -0.953, 22.329],
                      '3kgpA00': [-11.549, 90.595, 14.446],
                      '3kv2A00': [24.936, -12.503, -4.32],
                      '3kwaA00': [-4.384, 3.729, 14.367],
                      '3l3nA00': [43.237, 7.048, 113.051],
                      '3l4uA02': [-4.578, -17.29, -20.691],
                      '3lkaA00': [3.111, -5.691, 5.446],
                      '3mfvA00': [-20.336, 13.658, -5.186],
                      '3muz101': [13.047, 26.402, 76.24],
                      '3mygA00': [-0.669, 32.359, 62.209],
                      '3n7aA00': [45.323, 2.008, 22.527],
                      '3n86A00': [31.994, 27.637, -2.414],
                      '3noxA04': [46.423, 50.41, 38.25],
                      '3nq3A00': [10.843, -1.356, 2.118],
                      '3nw9A00': [-2.223, 20.036, 13.455],
                      '3oe5A00': [19.08, -28.583, 11.737],
                      '3ov1A00': [-10.708, 11.351, -2.246],
                      '3owjA00': [-10.719, 4.355, 20.831],
                      '3oztA00': [34.378, -2.269, -11.789],
                      '3pe2A00': [21.987, -30.264, 15.232],
                      '3pwwA00': [-1.298, 6.287, 9.62],
                      '3pxfA00': [106.316, 129.221, 64.024],
                      '3s8oA00': [10.483, -9.625, -2.092],
                      '3u9qA00': [4.618, -0.341, 20.533],
                      '3udhA00': [22.537, 34.92, 43.251],
                      '3uo4A00': [6.329, 29.361, 6.278],
                      '3uriA00': [2.857, 33.125, 15.125],
                      '3utuH00': [14.257, -12.199, 21.068],
                      '3vd4A01': [13.547, -23.517, -3.731],
                      '3vh9A00': [29.105, -29.545, 13.009],
                      '3zsoB00': [-9.07, 46.281, 0.23],
                      '4de1A00': [-5.218, 53.22, 11.521],
                      '4de2A00': [-5.209, 53.638, 11.463],
                      '4desA00': [21.178, 0.277, -5.939],
                      '4dewA00': [21.664, 42.395, 38.992],
                      '4djrB00': [19.424, 29.824, 13.36],
                      '4djvA00': [22.799, 12.86, 24.019],
                      '4g8mA00': [7.228, 26.424, 20.169],
                      '4gidA00': [42.534, -3.622, 12.207],
                      '4tmnE00': [55.368, 13.398, -12.337]}}
