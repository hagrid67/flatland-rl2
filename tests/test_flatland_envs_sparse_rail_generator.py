import random

import numpy as np

from flatland.core.grid.grid_utils import Vec2dOperations as Vec2d
from flatland.envs.observations import GlobalObsForRailEnv
from flatland.envs.rail_env import RailEnv
from flatland.envs.rail_generators import sparse_rail_generator
from flatland.envs.schedule_generators import sparse_schedule_generator
from flatland.utils.rendertools import RenderTool


def test_sparse_rail_generator():
    env = RailEnv(width=50,
                  height=50,
                  rail_generator=sparse_rail_generator(num_cities=10,  # Number of cities in map
                                                       num_intersections=10,  # Number of interesections in map
                                                       num_trainstations=50,  # Number of possible start/targets on map
                                                       min_node_dist=6,  # Minimal distance of nodes
                                                       node_radius=3,  # Proximity of stations to city center
                                                       num_neighb=3,  # Number of connections to other cities
                                                       seed=5,  # Random seed
                                                       grid_mode=False  # Ordered distribution of nodes
                                                       ),
                  schedule_generator=sparse_schedule_generator(),
                  number_of_agents=10,
                  obs_builder_object=GlobalObsForRailEnv())
    expected_grid_map = np.zeros((50, 50), dtype=env.rail.transitions.get_type())
    expected_grid_map[1][33] = 8192
    expected_grid_map[2][33] = 32800
    expected_grid_map[3][31] = 4
    expected_grid_map[3][32] = 4608
    expected_grid_map[3][33] = 32800
    expected_grid_map[4][30] = 16386
    expected_grid_map[4][31] = 17411
    expected_grid_map[4][32] = 1097
    expected_grid_map[4][33] = 38505
    expected_grid_map[4][34] = 1025
    expected_grid_map[4][35] = 5633
    expected_grid_map[4][36] = 1025
    expected_grid_map[4][37] = 1025
    expected_grid_map[4][38] = 1025
    expected_grid_map[4][39] = 1025
    expected_grid_map[4][40] = 1025
    expected_grid_map[4][41] = 1025
    expected_grid_map[4][42] = 1025
    expected_grid_map[4][43] = 1025
    expected_grid_map[4][44] = 1025
    expected_grid_map[4][45] = 1025
    expected_grid_map[4][46] = 1025
    expected_grid_map[4][47] = 1025
    expected_grid_map[4][48] = 4608
    expected_grid_map[5][30] = 128
    expected_grid_map[5][31] = 32800
    expected_grid_map[5][33] = 32800
    expected_grid_map[5][35] = 32800
    expected_grid_map[5][48] = 32800
    expected_grid_map[6][30] = 4
    expected_grid_map[6][31] = 2064
    expected_grid_map[6][33] = 32800
    expected_grid_map[6][35] = 128
    expected_grid_map[6][48] = 32800
    expected_grid_map[7][33] = 32872
    expected_grid_map[7][34] = 1025
    expected_grid_map[7][35] = 1025
    expected_grid_map[7][36] = 1025
    expected_grid_map[7][37] = 1025
    expected_grid_map[7][38] = 1025
    expected_grid_map[7][39] = 1025
    expected_grid_map[7][40] = 1025
    expected_grid_map[7][41] = 20994
    expected_grid_map[7][42] = 1025
    expected_grid_map[7][43] = 1025
    expected_grid_map[7][44] = 1025
    expected_grid_map[7][45] = 1025
    expected_grid_map[7][46] = 1025
    expected_grid_map[7][47] = 4608
    expected_grid_map[7][48] = 32800
    expected_grid_map[8][3] = 16386
    expected_grid_map[8][4] = 1025
    expected_grid_map[8][5] = 1025
    expected_grid_map[8][6] = 1025
    expected_grid_map[8][7] = 1025
    expected_grid_map[8][8] = 1025
    expected_grid_map[8][9] = 1025
    expected_grid_map[8][10] = 1025
    expected_grid_map[8][11] = 5633
    expected_grid_map[8][12] = 1025
    expected_grid_map[8][13] = 1025
    expected_grid_map[8][14] = 1025
    expected_grid_map[8][15] = 1025
    expected_grid_map[8][16] = 1025
    expected_grid_map[8][17] = 1025
    expected_grid_map[8][18] = 4608
    expected_grid_map[8][33] = 32800
    expected_grid_map[8][41] = 32800
    expected_grid_map[8][47] = 32800
    expected_grid_map[8][48] = 32800
    expected_grid_map[9][3] = 32800
    expected_grid_map[9][11] = 32800
    expected_grid_map[9][12] = 8192
    expected_grid_map[9][13] = 8192
    expected_grid_map[9][18] = 32800
    expected_grid_map[9][33] = 32800
    expected_grid_map[9][41] = 32800
    expected_grid_map[9][47] = 32800
    expected_grid_map[9][48] = 32800
    expected_grid_map[10][3] = 32800
    expected_grid_map[10][8] = 8192
    expected_grid_map[10][11] = 32800
    expected_grid_map[10][12] = 32800
    expected_grid_map[10][13] = 32800
    expected_grid_map[10][18] = 32800
    expected_grid_map[10][33] = 32800
    expected_grid_map[10][41] = 32800
    expected_grid_map[10][47] = 32800
    expected_grid_map[10][48] = 32800
    expected_grid_map[11][3] = 32800
    expected_grid_map[11][8] = 32800
    expected_grid_map[11][11] = 32800
    expected_grid_map[11][12] = 32800
    expected_grid_map[11][13] = 32800
    expected_grid_map[11][18] = 32800
    expected_grid_map[11][33] = 32800
    expected_grid_map[11][41] = 32800
    expected_grid_map[11][47] = 32800
    expected_grid_map[11][48] = 32800
    expected_grid_map[12][3] = 32800
    expected_grid_map[12][8] = 72
    expected_grid_map[12][9] = 1025
    expected_grid_map[12][10] = 17411
    expected_grid_map[12][11] = 52275
    expected_grid_map[12][12] = 3089
    expected_grid_map[12][13] = 3089
    expected_grid_map[12][14] = 1025
    expected_grid_map[12][15] = 1025
    expected_grid_map[12][16] = 1025
    expected_grid_map[12][17] = 1025
    expected_grid_map[12][18] = 33825
    expected_grid_map[12][19] = 1025
    expected_grid_map[12][20] = 1025
    expected_grid_map[12][21] = 1025
    expected_grid_map[12][22] = 1025
    expected_grid_map[12][23] = 1025
    expected_grid_map[12][24] = 1025
    expected_grid_map[12][25] = 1025
    expected_grid_map[12][26] = 1025
    expected_grid_map[12][27] = 1025
    expected_grid_map[12][28] = 1025
    expected_grid_map[12][29] = 1025
    expected_grid_map[12][30] = 1025
    expected_grid_map[12][31] = 1025
    expected_grid_map[12][32] = 1025
    expected_grid_map[12][33] = 33825
    expected_grid_map[12][34] = 1025
    expected_grid_map[12][35] = 1025
    expected_grid_map[12][36] = 1025
    expected_grid_map[12][37] = 1025
    expected_grid_map[12][38] = 1025
    expected_grid_map[12][39] = 1025
    expected_grid_map[12][40] = 1025
    expected_grid_map[12][41] = 35889
    expected_grid_map[12][42] = 4608
    expected_grid_map[12][47] = 32800
    expected_grid_map[12][48] = 32800
    expected_grid_map[13][3] = 32800
    expected_grid_map[13][10] = 32800
    expected_grid_map[13][11] = 32872
    expected_grid_map[13][12] = 1025
    expected_grid_map[13][13] = 256
    expected_grid_map[13][15] = 8192
    expected_grid_map[13][16] = 8192
    expected_grid_map[13][17] = 8192
    expected_grid_map[13][18] = 32800
    expected_grid_map[13][20] = 8192
    expected_grid_map[13][33] = 32800
    expected_grid_map[13][41] = 32800
    expected_grid_map[13][42] = 32800
    expected_grid_map[13][47] = 32800
    expected_grid_map[13][48] = 32800
    expected_grid_map[14][3] = 32800
    expected_grid_map[14][10] = 128
    expected_grid_map[14][11] = 32800
    expected_grid_map[14][15] = 72
    expected_grid_map[14][16] = 37408
    expected_grid_map[14][17] = 32800
    expected_grid_map[14][18] = 32800
    expected_grid_map[14][20] = 32800
    expected_grid_map[14][33] = 32800
    expected_grid_map[14][41] = 32800
    expected_grid_map[14][42] = 32800
    expected_grid_map[14][47] = 32800
    expected_grid_map[14][48] = 32800
    expected_grid_map[15][3] = 32800
    expected_grid_map[15][11] = 32800
    expected_grid_map[15][15] = 4
    expected_grid_map[15][16] = 1097
    expected_grid_map[15][17] = 1097
    expected_grid_map[15][18] = 3089
    expected_grid_map[15][19] = 1025
    expected_grid_map[15][20] = 3089
    expected_grid_map[15][21] = 1025
    expected_grid_map[15][22] = 1025
    expected_grid_map[15][23] = 1025
    expected_grid_map[15][24] = 1025
    expected_grid_map[15][25] = 1025
    expected_grid_map[15][26] = 1025
    expected_grid_map[15][27] = 1025
    expected_grid_map[15][28] = 1025
    expected_grid_map[15][29] = 1025
    expected_grid_map[15][30] = 1025
    expected_grid_map[15][31] = 1025
    expected_grid_map[15][32] = 1025
    expected_grid_map[15][33] = 33825
    expected_grid_map[15][34] = 1025
    expected_grid_map[15][35] = 1025
    expected_grid_map[15][36] = 1025
    expected_grid_map[15][37] = 1025
    expected_grid_map[15][38] = 1025
    expected_grid_map[15][39] = 1025
    expected_grid_map[15][40] = 1025
    expected_grid_map[15][41] = 35889
    expected_grid_map[15][42] = 37408
    expected_grid_map[15][47] = 32800
    expected_grid_map[15][48] = 32800
    expected_grid_map[16][3] = 32800
    expected_grid_map[16][7] = 8192
    expected_grid_map[16][11] = 32800
    expected_grid_map[16][33] = 32800
    expected_grid_map[16][41] = 32800
    expected_grid_map[16][42] = 32800
    expected_grid_map[16][47] = 32800
    expected_grid_map[16][48] = 32800
    expected_grid_map[17][3] = 32800
    expected_grid_map[17][7] = 32800
    expected_grid_map[17][9] = 8192
    expected_grid_map[17][10] = 8192
    expected_grid_map[17][11] = 32800
    expected_grid_map[17][33] = 32800
    expected_grid_map[17][41] = 32800
    expected_grid_map[17][42] = 32800
    expected_grid_map[17][47] = 32800
    expected_grid_map[17][48] = 32800
    expected_grid_map[18][3] = 32800
    expected_grid_map[18][7] = 32800
    expected_grid_map[18][8] = 8192
    expected_grid_map[18][9] = 32800
    expected_grid_map[18][10] = 32800
    expected_grid_map[18][11] = 32800
    expected_grid_map[18][33] = 32800
    expected_grid_map[18][41] = 32800
    expected_grid_map[18][42] = 32800
    expected_grid_map[18][47] = 32800
    expected_grid_map[18][48] = 32800
    expected_grid_map[19][3] = 72
    expected_grid_map[19][4] = 1025
    expected_grid_map[19][5] = 1025
    expected_grid_map[19][6] = 1025
    expected_grid_map[19][7] = 1097
    expected_grid_map[19][8] = 1097
    expected_grid_map[19][9] = 1097
    expected_grid_map[19][10] = 52275
    expected_grid_map[19][11] = 33825
    expected_grid_map[19][12] = 1025
    expected_grid_map[19][13] = 1025
    expected_grid_map[19][14] = 4608
    expected_grid_map[19][33] = 32800
    expected_grid_map[19][41] = 32800
    expected_grid_map[19][42] = 32800
    expected_grid_map[19][47] = 32800
    expected_grid_map[19][48] = 32800
    expected_grid_map[20][7] = 4
    expected_grid_map[20][8] = 1025
    expected_grid_map[20][9] = 1025
    expected_grid_map[20][10] = 34864
    expected_grid_map[20][11] = 32800
    expected_grid_map[20][14] = 32800
    expected_grid_map[20][33] = 32800
    expected_grid_map[20][41] = 32800
    expected_grid_map[20][42] = 32800
    expected_grid_map[20][47] = 32800
    expected_grid_map[20][48] = 32800
    expected_grid_map[21][10] = 32800
    expected_grid_map[21][11] = 32800
    expected_grid_map[21][14] = 32800
    expected_grid_map[21][24] = 8192
    expected_grid_map[21][33] = 32872
    expected_grid_map[21][34] = 1025
    expected_grid_map[21][35] = 1025
    expected_grid_map[21][36] = 1025
    expected_grid_map[21][37] = 1025
    expected_grid_map[21][38] = 1025
    expected_grid_map[21][39] = 1025
    expected_grid_map[21][40] = 1025
    expected_grid_map[21][41] = 33825
    expected_grid_map[21][42] = 38505
    expected_grid_map[21][43] = 1025
    expected_grid_map[21][44] = 1025
    expected_grid_map[21][45] = 1025
    expected_grid_map[21][46] = 1025
    expected_grid_map[21][47] = 37408
    expected_grid_map[21][48] = 32800
    expected_grid_map[22][10] = 32800
    expected_grid_map[22][11] = 32800
    expected_grid_map[22][14] = 32800
    expected_grid_map[22][22] = 8192
    expected_grid_map[22][24] = 32800
    expected_grid_map[22][27] = 8192
    expected_grid_map[22][33] = 32800
    expected_grid_map[22][41] = 32800
    expected_grid_map[22][42] = 32800
    expected_grid_map[22][47] = 32800
    expected_grid_map[22][48] = 32800
    expected_grid_map[23][10] = 32800
    expected_grid_map[23][11] = 32800
    expected_grid_map[23][14] = 32800
    expected_grid_map[23][22] = 72
    expected_grid_map[23][23] = 17411
    expected_grid_map[23][24] = 1097
    expected_grid_map[23][25] = 17411
    expected_grid_map[23][26] = 1025
    expected_grid_map[23][27] = 3089
    expected_grid_map[23][28] = 1025
    expected_grid_map[23][29] = 1025
    expected_grid_map[23][30] = 1025
    expected_grid_map[23][31] = 1025
    expected_grid_map[23][32] = 1025
    expected_grid_map[23][33] = 33825
    expected_grid_map[23][34] = 1025
    expected_grid_map[23][35] = 1025
    expected_grid_map[23][36] = 1025
    expected_grid_map[23][37] = 1025
    expected_grid_map[23][38] = 1025
    expected_grid_map[23][39] = 1025
    expected_grid_map[23][40] = 1025
    expected_grid_map[23][41] = 3089
    expected_grid_map[23][42] = 34864
    expected_grid_map[23][47] = 32800
    expected_grid_map[23][48] = 32800
    expected_grid_map[24][10] = 32800
    expected_grid_map[24][11] = 32800
    expected_grid_map[24][14] = 32800
    expected_grid_map[24][23] = 32800
    expected_grid_map[24][24] = 4
    expected_grid_map[24][25] = 34864
    expected_grid_map[24][33] = 32800
    expected_grid_map[24][42] = 32800
    expected_grid_map[24][47] = 32800
    expected_grid_map[24][48] = 32800
    expected_grid_map[25][10] = 32800
    expected_grid_map[25][11] = 32800
    expected_grid_map[25][14] = 32800
    expected_grid_map[25][23] = 128
    expected_grid_map[25][25] = 32800
    expected_grid_map[25][33] = 32800
    expected_grid_map[25][42] = 32800
    expected_grid_map[25][47] = 32800
    expected_grid_map[25][48] = 32800
    expected_grid_map[26][10] = 32800
    expected_grid_map[26][11] = 32800
    expected_grid_map[26][14] = 32800
    expected_grid_map[26][25] = 32800
    expected_grid_map[26][33] = 32800
    expected_grid_map[26][42] = 32800
    expected_grid_map[26][47] = 32800
    expected_grid_map[26][48] = 32800
    expected_grid_map[27][10] = 32800
    expected_grid_map[27][11] = 32800
    expected_grid_map[27][14] = 32800
    expected_grid_map[27][25] = 32800
    expected_grid_map[27][33] = 32800
    expected_grid_map[27][42] = 32800
    expected_grid_map[27][47] = 32800
    expected_grid_map[27][48] = 32800
    expected_grid_map[28][10] = 32800
    expected_grid_map[28][11] = 32800
    expected_grid_map[28][14] = 32800
    expected_grid_map[28][25] = 32800
    expected_grid_map[28][33] = 49186
    expected_grid_map[28][34] = 256
    expected_grid_map[28][42] = 32800
    expected_grid_map[28][44] = 8192
    expected_grid_map[28][45] = 8192
    expected_grid_map[28][47] = 32800
    expected_grid_map[28][48] = 32800
    expected_grid_map[28][49] = 8192
    expected_grid_map[29][10] = 32800
    expected_grid_map[29][11] = 32800
    expected_grid_map[29][14] = 32800
    expected_grid_map[29][25] = 32800
    expected_grid_map[29][32] = 16386
    expected_grid_map[29][33] = 37408
    expected_grid_map[29][34] = 8192
    expected_grid_map[29][42] = 32800
    expected_grid_map[29][44] = 72
    expected_grid_map[29][45] = 37408
    expected_grid_map[29][47] = 32800
    expected_grid_map[29][48] = 32800
    expected_grid_map[29][49] = 32800
    expected_grid_map[30][10] = 32800
    expected_grid_map[30][11] = 32800
    expected_grid_map[30][14] = 32800
    expected_grid_map[30][25] = 32800
    expected_grid_map[30][32] = 128
    expected_grid_map[30][33] = 49186
    expected_grid_map[30][34] = 33825
    expected_grid_map[30][35] = 1025
    expected_grid_map[30][36] = 1025
    expected_grid_map[30][37] = 1025
    expected_grid_map[30][38] = 1025
    expected_grid_map[30][39] = 5633
    expected_grid_map[30][40] = 1025
    expected_grid_map[30][41] = 1025
    expected_grid_map[30][42] = 2064
    expected_grid_map[30][45] = 16458
    expected_grid_map[30][46] = 17411
    expected_grid_map[30][47] = 38505
    expected_grid_map[30][48] = 38433
    expected_grid_map[30][49] = 2064
    expected_grid_map[31][10] = 32800
    expected_grid_map[31][11] = 32800
    expected_grid_map[31][14] = 32800
    expected_grid_map[31][25] = 32800
    expected_grid_map[31][30] = 8192
    expected_grid_map[31][31] = 4
    expected_grid_map[31][32] = 17411
    expected_grid_map[31][33] = 34864
    expected_grid_map[31][34] = 32800
    expected_grid_map[31][39] = 32800
    expected_grid_map[31][45] = 32800
    expected_grid_map[31][46] = 32800
    expected_grid_map[31][47] = 32800
    expected_grid_map[31][48] = 32800
    expected_grid_map[32][10] = 32800
    expected_grid_map[32][11] = 32800
    expected_grid_map[32][14] = 32800
    expected_grid_map[32][25] = 32800
    expected_grid_map[32][30] = 72
    expected_grid_map[32][31] = 1025
    expected_grid_map[32][32] = 2064
    expected_grid_map[32][33] = 32872
    expected_grid_map[32][34] = 2064
    expected_grid_map[32][39] = 32800
    expected_grid_map[32][45] = 128
    expected_grid_map[32][46] = 128
    expected_grid_map[32][47] = 32800
    expected_grid_map[32][48] = 32800
    expected_grid_map[33][10] = 32800
    expected_grid_map[33][11] = 32800
    expected_grid_map[33][14] = 32872
    expected_grid_map[33][15] = 1025
    expected_grid_map[33][16] = 1025
    expected_grid_map[33][17] = 1025
    expected_grid_map[33][18] = 1025
    expected_grid_map[33][19] = 1025
    expected_grid_map[33][20] = 1025
    expected_grid_map[33][21] = 1025
    expected_grid_map[33][22] = 1025
    expected_grid_map[33][23] = 1025
    expected_grid_map[33][24] = 1025
    expected_grid_map[33][25] = 35889
    expected_grid_map[33][26] = 1025
    expected_grid_map[33][27] = 1025
    expected_grid_map[33][28] = 1025
    expected_grid_map[33][29] = 1025
    expected_grid_map[33][30] = 1025
    expected_grid_map[33][31] = 1025
    expected_grid_map[33][32] = 1025
    expected_grid_map[33][33] = 34864
    expected_grid_map[33][39] = 32800
    expected_grid_map[33][47] = 32800
    expected_grid_map[33][48] = 32800
    expected_grid_map[34][5] = 16386
    expected_grid_map[34][6] = 1025
    expected_grid_map[34][7] = 1025
    expected_grid_map[34][8] = 1025
    expected_grid_map[34][9] = 1025
    expected_grid_map[34][10] = 33825
    expected_grid_map[34][11] = 3089
    expected_grid_map[34][12] = 1025
    expected_grid_map[34][13] = 1025
    expected_grid_map[34][14] = 33825
    expected_grid_map[34][15] = 1025
    expected_grid_map[34][16] = 1025
    expected_grid_map[34][17] = 1025
    expected_grid_map[34][18] = 1025
    expected_grid_map[34][19] = 1025
    expected_grid_map[34][20] = 1025
    expected_grid_map[34][21] = 1025
    expected_grid_map[34][22] = 1025
    expected_grid_map[34][23] = 1025
    expected_grid_map[34][24] = 1025
    expected_grid_map[34][25] = 2064
    expected_grid_map[34][33] = 32800
    expected_grid_map[34][39] = 32800
    expected_grid_map[34][47] = 32800
    expected_grid_map[34][48] = 32800
    expected_grid_map[35][5] = 32800
    expected_grid_map[35][10] = 32800
    expected_grid_map[35][14] = 32800
    expected_grid_map[35][16] = 8192
    expected_grid_map[35][33] = 32800
    expected_grid_map[35][39] = 32800
    expected_grid_map[35][47] = 32800
    expected_grid_map[35][48] = 32800
    expected_grid_map[36][5] = 32800
    expected_grid_map[36][10] = 32800
    expected_grid_map[36][14] = 32800
    expected_grid_map[36][16] = 32800
    expected_grid_map[36][17] = 8192
    expected_grid_map[36][19] = 8192
    expected_grid_map[36][33] = 32800
    expected_grid_map[36][39] = 32800
    expected_grid_map[36][41] = 8192
    expected_grid_map[36][47] = 32800
    expected_grid_map[36][48] = 32800
    expected_grid_map[37][5] = 32800
    expected_grid_map[37][10] = 32800
    expected_grid_map[37][14] = 32800
    expected_grid_map[37][16] = 32800
    expected_grid_map[37][17] = 49186
    expected_grid_map[37][18] = 1025
    expected_grid_map[37][19] = 2064
    expected_grid_map[37][33] = 32800
    expected_grid_map[37][39] = 32800
    expected_grid_map[37][41] = 32800
    expected_grid_map[37][42] = 16386
    expected_grid_map[37][43] = 256
    expected_grid_map[37][47] = 32800
    expected_grid_map[37][48] = 32800
    expected_grid_map[38][5] = 72
    expected_grid_map[38][6] = 1025
    expected_grid_map[38][7] = 1025
    expected_grid_map[38][8] = 1025
    expected_grid_map[38][9] = 1025
    expected_grid_map[38][10] = 33825
    expected_grid_map[38][11] = 1025
    expected_grid_map[38][12] = 1025
    expected_grid_map[38][13] = 1025
    expected_grid_map[38][14] = 33897
    expected_grid_map[38][15] = 17411
    expected_grid_map[38][16] = 1097
    expected_grid_map[38][17] = 38505
    expected_grid_map[38][18] = 256
    expected_grid_map[38][33] = 32800
    expected_grid_map[38][39] = 32800
    expected_grid_map[38][41] = 32800
    expected_grid_map[38][42] = 32800
    expected_grid_map[38][43] = 8192
    expected_grid_map[38][47] = 32800
    expected_grid_map[38][48] = 32800
    expected_grid_map[39][10] = 32800
    expected_grid_map[39][14] = 32800
    expected_grid_map[39][15] = 32800
    expected_grid_map[39][17] = 32800
    expected_grid_map[39][18] = 4
    expected_grid_map[39][19] = 4608
    expected_grid_map[39][33] = 32800
    expected_grid_map[39][39] = 49186
    expected_grid_map[39][40] = 17411
    expected_grid_map[39][41] = 1097
    expected_grid_map[39][42] = 52275
    expected_grid_map[39][43] = 3089
    expected_grid_map[39][44] = 4608
    expected_grid_map[39][47] = 32800
    expected_grid_map[39][48] = 32800
    expected_grid_map[40][10] = 32800
    expected_grid_map[40][14] = 32800
    expected_grid_map[40][15] = 128
    expected_grid_map[40][17] = 32800
    expected_grid_map[40][18] = 8192
    expected_grid_map[40][19] = 32800
    expected_grid_map[40][33] = 32800
    expected_grid_map[40][39] = 32800
    expected_grid_map[40][40] = 32800
    expected_grid_map[40][42] = 32872
    expected_grid_map[40][43] = 4608
    expected_grid_map[40][44] = 32800
    expected_grid_map[40][47] = 32800
    expected_grid_map[40][48] = 32800
    expected_grid_map[41][10] = 32800
    expected_grid_map[41][14] = 32800
    expected_grid_map[41][17] = 32800
    expected_grid_map[41][18] = 72
    expected_grid_map[41][19] = 37408
    expected_grid_map[41][21] = 8192
    expected_grid_map[41][33] = 32800
    expected_grid_map[41][39] = 32800
    expected_grid_map[41][40] = 128
    expected_grid_map[41][42] = 32800
    expected_grid_map[41][43] = 128
    expected_grid_map[41][44] = 32800
    expected_grid_map[41][47] = 32800
    expected_grid_map[41][48] = 32800
    expected_grid_map[42][10] = 32800
    expected_grid_map[42][14] = 72
    expected_grid_map[42][15] = 1025
    expected_grid_map[42][16] = 1025
    expected_grid_map[42][17] = 33825
    expected_grid_map[42][18] = 17411
    expected_grid_map[42][19] = 52275
    expected_grid_map[42][20] = 5633
    expected_grid_map[42][21] = 3089
    expected_grid_map[42][22] = 1025
    expected_grid_map[42][23] = 1025
    expected_grid_map[42][24] = 1025
    expected_grid_map[42][25] = 1025
    expected_grid_map[42][26] = 1025
    expected_grid_map[42][27] = 1025
    expected_grid_map[42][28] = 1025
    expected_grid_map[42][29] = 1025
    expected_grid_map[42][30] = 4608
    expected_grid_map[42][33] = 32800
    expected_grid_map[42][39] = 32800
    expected_grid_map[42][42] = 32800
    expected_grid_map[42][44] = 32800
    expected_grid_map[42][47] = 32800
    expected_grid_map[42][48] = 32800
    expected_grid_map[43][10] = 32800
    expected_grid_map[43][17] = 32800
    expected_grid_map[43][18] = 128
    expected_grid_map[43][19] = 32800
    expected_grid_map[43][20] = 32800
    expected_grid_map[43][30] = 32800
    expected_grid_map[43][33] = 32800
    expected_grid_map[43][39] = 32800
    expected_grid_map[43][42] = 32800
    expected_grid_map[43][44] = 32800
    expected_grid_map[43][47] = 32800
    expected_grid_map[43][48] = 32800
    expected_grid_map[44][4] = 4
    expected_grid_map[44][5] = 1025
    expected_grid_map[44][6] = 1025
    expected_grid_map[44][7] = 1025
    expected_grid_map[44][8] = 1025
    expected_grid_map[44][9] = 1025
    expected_grid_map[44][10] = 3089
    expected_grid_map[44][11] = 1025
    expected_grid_map[44][12] = 1025
    expected_grid_map[44][13] = 1025
    expected_grid_map[44][14] = 1025
    expected_grid_map[44][15] = 1025
    expected_grid_map[44][16] = 1025
    expected_grid_map[44][17] = 3089
    expected_grid_map[44][18] = 1025
    expected_grid_map[44][19] = 2064
    expected_grid_map[44][20] = 128
    expected_grid_map[44][30] = 72
    expected_grid_map[44][31] = 1025
    expected_grid_map[44][32] = 1025
    expected_grid_map[44][33] = 35889
    expected_grid_map[44][34] = 1025
    expected_grid_map[44][35] = 1025
    expected_grid_map[44][36] = 1025
    expected_grid_map[44][37] = 1025
    expected_grid_map[44][38] = 1025
    expected_grid_map[44][39] = 33825
    expected_grid_map[44][40] = 1025
    expected_grid_map[44][41] = 1025
    expected_grid_map[44][42] = 2064
    expected_grid_map[44][44] = 32800
    expected_grid_map[44][47] = 32800
    expected_grid_map[44][48] = 32800
    expected_grid_map[45][33] = 32872
    expected_grid_map[45][34] = 1025
    expected_grid_map[45][35] = 1025
    expected_grid_map[45][36] = 1025
    expected_grid_map[45][37] = 1025
    expected_grid_map[45][38] = 1025
    expected_grid_map[45][39] = 33825
    expected_grid_map[45][40] = 1025
    expected_grid_map[45][41] = 1025
    expected_grid_map[45][42] = 1025
    expected_grid_map[45][43] = 1025
    expected_grid_map[45][44] = 1097
    expected_grid_map[45][45] = 1025
    expected_grid_map[45][46] = 1025
    expected_grid_map[45][47] = 34864
    expected_grid_map[45][48] = 32800
    expected_grid_map[46][33] = 32800
    expected_grid_map[46][39] = 32800
    expected_grid_map[46][47] = 32800
    expected_grid_map[46][48] = 32800
    expected_grid_map[47][33] = 32800
    expected_grid_map[47][39] = 32800
    expected_grid_map[47][47] = 32800
    expected_grid_map[47][48] = 128
    expected_grid_map[48][33] = 32800
    expected_grid_map[48][39] = 32800
    expected_grid_map[48][47] = 32800
    expected_grid_map[49][33] = 72
    expected_grid_map[49][34] = 1025
    expected_grid_map[49][35] = 1025
    expected_grid_map[49][36] = 1025
    expected_grid_map[49][37] = 1025
    expected_grid_map[49][38] = 1025
    expected_grid_map[49][39] = 2136
    expected_grid_map[49][40] = 1025
    expected_grid_map[49][41] = 1025
    expected_grid_map[49][42] = 1025
    expected_grid_map[49][43] = 1025
    expected_grid_map[49][44] = 1025
    expected_grid_map[49][45] = 1025
    expected_grid_map[49][46] = 1025
    expected_grid_map[49][47] = 2064

    assert np.array_equal(env.rail.grid, expected_grid_map), "actual={}, expected={}".format(env.rail.grid,
                                                                                             expected_grid_map)
    s0 = 0
    s1 = 0
    for a in range(env.get_num_agents()):
        s0 = Vec2d.get_manhattan_distance(env.agents[a].position, (0, 0))
        s1 = Vec2d.get_chebyshev_distance(env.agents[a].position, (0, 0))
    assert s0 == 53, "actual={}".format(s0)
    assert s1 == 36, "actual={}".format(s1)


def test_sparse_rail_generator_deterministic():
    """Check that sparse_rail_generator runs deterministic over different python versions!"""
    random.seed(0)
    np.random.seed(0)

    stochastic_data = {'prop_malfunction': 1.,  # Percentage of defective agents
                       'malfunction_rate': 70,  # Rate of malfunction occurence
                       'min_duration': 2,  # Minimal duration of malfunction
                       'max_duration': 5  # Max duration of malfunction
                       }

    speed_ration_map = {1.: 1.,  # Fast passenger train
                        1. / 2.: 0.,  # Fast freight train
                        1. / 3.: 0.,  # Slow commuter train
                        1. / 4.: 0.}  # Slow freight train

    env = RailEnv(width=25,
                  height=30,
                  rail_generator=sparse_rail_generator(num_cities=5,
                                                       # Number of cities in map (where train stations are)
                                                       num_intersections=4,
                                                       # Number of intersections (no start / target)
                                                       num_trainstations=25,  # Number of possible start/targets on map
                                                       min_node_dist=6,  # Minimal distance of nodes
                                                       node_radius=3,  # Proximity of stations to city center
                                                       num_neighb=3,
                                                       # Number of connections to other cities/intersections
                                                       seed=215545,  # Random seed
                                                       grid_mode=True
                                                       ),
                  schedule_generator=sparse_schedule_generator(speed_ration_map),
                  number_of_agents=1,
                  stochastic_data=stochastic_data,  # Malfunction data generator
                  )
    assert env.rail.get_full_transitions(0, 0) == 0, "[0][0]"
    assert env.rail.get_full_transitions(0, 1) == 0, "[0][1]"
    assert env.rail.get_full_transitions(0, 2) == 0, "[0][2]"
    assert env.rail.get_full_transitions(0, 3) == 0, "[0][3]"
    assert env.rail.get_full_transitions(0, 4) == 0, "[0][4]"
    assert env.rail.get_full_transitions(0, 5) == 0, "[0][5]"
    assert env.rail.get_full_transitions(0, 6) == 0, "[0][6]"
    assert env.rail.get_full_transitions(0, 7) == 0, "[0][7]"
    assert env.rail.get_full_transitions(0, 8) == 0, "[0][8]"
    assert env.rail.get_full_transitions(0, 9) == 0, "[0][9]"
    assert env.rail.get_full_transitions(0, 10) == 0, "[0][10]"
    assert env.rail.get_full_transitions(0, 11) == 0, "[0][11]"
    assert env.rail.get_full_transitions(0, 12) == 0, "[0][12]"
    assert env.rail.get_full_transitions(0, 13) == 0, "[0][13]"
    assert env.rail.get_full_transitions(0, 14) == 0, "[0][14]"
    assert env.rail.get_full_transitions(0, 15) == 0, "[0][15]"
    assert env.rail.get_full_transitions(0, 16) == 0, "[0][16]"
    assert env.rail.get_full_transitions(0, 17) == 0, "[0][17]"
    assert env.rail.get_full_transitions(0, 18) == 0, "[0][18]"
    assert env.rail.get_full_transitions(0, 19) == 0, "[0][19]"
    assert env.rail.get_full_transitions(0, 20) == 0, "[0][20]"
    assert env.rail.get_full_transitions(0, 21) == 0, "[0][21]"
    assert env.rail.get_full_transitions(0, 22) == 0, "[0][22]"
    assert env.rail.get_full_transitions(0, 23) == 0, "[0][23]"
    assert env.rail.get_full_transitions(0, 24) == 0, "[0][24]"
    assert env.rail.get_full_transitions(1, 0) == 0, "[1][0]"
    assert env.rail.get_full_transitions(1, 1) == 0, "[1][1]"
    assert env.rail.get_full_transitions(1, 2) == 0, "[1][2]"
    assert env.rail.get_full_transitions(1, 3) == 0, "[1][3]"
    assert env.rail.get_full_transitions(1, 4) == 0, "[1][4]"
    assert env.rail.get_full_transitions(1, 5) == 0, "[1][5]"
    assert env.rail.get_full_transitions(1, 6) == 0, "[1][6]"
    assert env.rail.get_full_transitions(1, 7) == 0, "[1][7]"
    assert env.rail.get_full_transitions(1, 8) == 0, "[1][8]"
    assert env.rail.get_full_transitions(1, 9) == 0, "[1][9]"
    assert env.rail.get_full_transitions(1, 10) == 0, "[1][10]"
    assert env.rail.get_full_transitions(1, 11) == 0, "[1][11]"
    assert env.rail.get_full_transitions(1, 12) == 0, "[1][12]"
    assert env.rail.get_full_transitions(1, 13) == 0, "[1][13]"
    assert env.rail.get_full_transitions(1, 14) == 0, "[1][14]"
    assert env.rail.get_full_transitions(1, 15) == 0, "[1][15]"
    assert env.rail.get_full_transitions(1, 16) == 0, "[1][16]"
    assert env.rail.get_full_transitions(1, 17) == 0, "[1][17]"
    assert env.rail.get_full_transitions(1, 18) == 0, "[1][18]"
    assert env.rail.get_full_transitions(1, 19) == 0, "[1][19]"
    assert env.rail.get_full_transitions(1, 20) == 0, "[1][20]"
    assert env.rail.get_full_transitions(1, 21) == 0, "[1][21]"
    assert env.rail.get_full_transitions(1, 22) == 0, "[1][22]"
    assert env.rail.get_full_transitions(1, 23) == 0, "[1][23]"
    assert env.rail.get_full_transitions(1, 24) == 0, "[1][24]"
    assert env.rail.get_full_transitions(2, 0) == 0, "[2][0]"
    assert env.rail.get_full_transitions(2, 1) == 0, "[2][1]"
    assert env.rail.get_full_transitions(2, 2) == 0, "[2][2]"
    assert env.rail.get_full_transitions(2, 3) == 0, "[2][3]"
    assert env.rail.get_full_transitions(2, 4) == 0, "[2][4]"
    assert env.rail.get_full_transitions(2, 5) == 0, "[2][5]"
    assert env.rail.get_full_transitions(2, 6) == 0, "[2][6]"
    assert env.rail.get_full_transitions(2, 7) == 0, "[2][7]"
    assert env.rail.get_full_transitions(2, 8) == 0, "[2][8]"
    assert env.rail.get_full_transitions(2, 9) == 0, "[2][9]"
    assert env.rail.get_full_transitions(2, 10) == 0, "[2][10]"
    assert env.rail.get_full_transitions(2, 11) == 0, "[2][11]"
    assert env.rail.get_full_transitions(2, 12) == 0, "[2][12]"
    assert env.rail.get_full_transitions(2, 13) == 0, "[2][13]"
    assert env.rail.get_full_transitions(2, 14) == 0, "[2][14]"
    assert env.rail.get_full_transitions(2, 15) == 0, "[2][15]"
    assert env.rail.get_full_transitions(2, 16) == 0, "[2][16]"
    assert env.rail.get_full_transitions(2, 17) == 0, "[2][17]"
    assert env.rail.get_full_transitions(2, 18) == 0, "[2][18]"
    assert env.rail.get_full_transitions(2, 19) == 0, "[2][19]"
    assert env.rail.get_full_transitions(2, 20) == 0, "[2][20]"
    assert env.rail.get_full_transitions(2, 21) == 0, "[2][21]"
    assert env.rail.get_full_transitions(2, 22) == 0, "[2][22]"
    assert env.rail.get_full_transitions(2, 23) == 0, "[2][23]"
    assert env.rail.get_full_transitions(2, 24) == 0, "[2][24]"
    assert env.rail.get_full_transitions(3, 0) == 0, "[3][0]"
    assert env.rail.get_full_transitions(3, 1) == 0, "[3][1]"
    assert env.rail.get_full_transitions(3, 2) == 0, "[3][2]"
    assert env.rail.get_full_transitions(3, 3) == 16386, "[3][3]"
    assert env.rail.get_full_transitions(3, 4) == 1025, "[3][4]"
    assert env.rail.get_full_transitions(3, 5) == 1025, "[3][5]"
    assert env.rail.get_full_transitions(3, 6) == 1025, "[3][6]"
    assert env.rail.get_full_transitions(3, 7) == 1025, "[3][7]"
    assert env.rail.get_full_transitions(3, 8) == 1025, "[3][8]"
    assert env.rail.get_full_transitions(3, 9) == 1025, "[3][9]"
    assert env.rail.get_full_transitions(3, 10) == 1025, "[3][10]"
    assert env.rail.get_full_transitions(3, 11) == 1025, "[3][11]"
    assert env.rail.get_full_transitions(3, 12) == 4608, "[3][12]"
    assert env.rail.get_full_transitions(3, 13) == 0, "[3][13]"
    assert env.rail.get_full_transitions(3, 14) == 0, "[3][14]"
    assert env.rail.get_full_transitions(3, 15) == 0, "[3][15]"
    assert env.rail.get_full_transitions(3, 16) == 0, "[3][16]"
    assert env.rail.get_full_transitions(3, 17) == 0, "[3][17]"
    assert env.rail.get_full_transitions(3, 18) == 0, "[3][18]"
    assert env.rail.get_full_transitions(3, 19) == 0, "[3][19]"
    assert env.rail.get_full_transitions(3, 20) == 0, "[3][20]"
    assert env.rail.get_full_transitions(3, 21) == 0, "[3][21]"
    assert env.rail.get_full_transitions(3, 22) == 8192, "[3][22]"
    assert env.rail.get_full_transitions(3, 23) == 0, "[3][23]"
    assert env.rail.get_full_transitions(3, 24) == 0, "[3][24]"
    assert env.rail.get_full_transitions(4, 0) == 0, "[4][0]"
    assert env.rail.get_full_transitions(4, 1) == 0, "[4][1]"
    assert env.rail.get_full_transitions(4, 2) == 0, "[4][2]"
    assert env.rail.get_full_transitions(4, 3) == 32800, "[4][3]"
    assert env.rail.get_full_transitions(4, 4) == 0, "[4][4]"
    assert env.rail.get_full_transitions(4, 5) == 0, "[4][5]"
    assert env.rail.get_full_transitions(4, 6) == 0, "[4][6]"
    assert env.rail.get_full_transitions(4, 7) == 0, "[4][7]"
    assert env.rail.get_full_transitions(4, 8) == 0, "[4][8]"
    assert env.rail.get_full_transitions(4, 9) == 0, "[4][9]"
    assert env.rail.get_full_transitions(4, 10) == 0, "[4][10]"
    assert env.rail.get_full_transitions(4, 11) == 0, "[4][11]"
    assert env.rail.get_full_transitions(4, 12) == 32800, "[4][12]"
    assert env.rail.get_full_transitions(4, 13) == 0, "[4][13]"
    assert env.rail.get_full_transitions(4, 14) == 0, "[4][14]"
    assert env.rail.get_full_transitions(4, 15) == 0, "[4][15]"
    assert env.rail.get_full_transitions(4, 16) == 0, "[4][16]"
    assert env.rail.get_full_transitions(4, 17) == 0, "[4][17]"
    assert env.rail.get_full_transitions(4, 18) == 0, "[4][18]"
    assert env.rail.get_full_transitions(4, 19) == 0, "[4][19]"
    assert env.rail.get_full_transitions(4, 20) == 0, "[4][20]"
    assert env.rail.get_full_transitions(4, 21) == 0, "[4][21]"
    assert env.rail.get_full_transitions(4, 22) == 32800, "[4][22]"
    assert env.rail.get_full_transitions(4, 23) == 0, "[4][23]"
    assert env.rail.get_full_transitions(4, 24) == 0, "[4][24]"
    assert env.rail.get_full_transitions(5, 0) == 0, "[5][0]"
    assert env.rail.get_full_transitions(5, 1) == 0, "[5][1]"
    assert env.rail.get_full_transitions(5, 2) == 0, "[5][2]"
    assert env.rail.get_full_transitions(5, 3) == 32800, "[5][3]"
    assert env.rail.get_full_transitions(5, 4) == 0, "[5][4]"
    assert env.rail.get_full_transitions(5, 5) == 0, "[5][5]"
    assert env.rail.get_full_transitions(5, 6) == 0, "[5][6]"
    assert env.rail.get_full_transitions(5, 7) == 0, "[5][7]"
    assert env.rail.get_full_transitions(5, 8) == 0, "[5][8]"
    assert env.rail.get_full_transitions(5, 9) == 0, "[5][9]"
    assert env.rail.get_full_transitions(5, 10) == 0, "[5][10]"
    assert env.rail.get_full_transitions(5, 11) == 0, "[5][11]"
    assert env.rail.get_full_transitions(5, 12) == 32800, "[5][12]"
    assert env.rail.get_full_transitions(5, 13) == 0, "[5][13]"
    assert env.rail.get_full_transitions(5, 14) == 0, "[5][14]"
    assert env.rail.get_full_transitions(5, 15) == 0, "[5][15]"
    assert env.rail.get_full_transitions(5, 16) == 0, "[5][16]"
    assert env.rail.get_full_transitions(5, 17) == 0, "[5][17]"
    assert env.rail.get_full_transitions(5, 18) == 0, "[5][18]"
    assert env.rail.get_full_transitions(5, 19) == 0, "[5][19]"
    assert env.rail.get_full_transitions(5, 20) == 0, "[5][20]"
    assert env.rail.get_full_transitions(5, 21) == 0, "[5][21]"
    assert env.rail.get_full_transitions(5, 22) == 32800, "[5][22]"
    assert env.rail.get_full_transitions(5, 23) == 0, "[5][23]"
    assert env.rail.get_full_transitions(5, 24) == 0, "[5][24]"
    assert env.rail.get_full_transitions(6, 0) == 0, "[6][0]"
    assert env.rail.get_full_transitions(6, 1) == 0, "[6][1]"
    assert env.rail.get_full_transitions(6, 2) == 0, "[6][2]"
    assert env.rail.get_full_transitions(6, 3) == 32800, "[6][3]"
    assert env.rail.get_full_transitions(6, 4) == 0, "[6][4]"
    assert env.rail.get_full_transitions(6, 5) == 0, "[6][5]"
    assert env.rail.get_full_transitions(6, 6) == 0, "[6][6]"
    assert env.rail.get_full_transitions(6, 7) == 0, "[6][7]"
    assert env.rail.get_full_transitions(6, 8) == 0, "[6][8]"
    assert env.rail.get_full_transitions(6, 9) == 0, "[6][9]"
    assert env.rail.get_full_transitions(6, 10) == 0, "[6][10]"
    assert env.rail.get_full_transitions(6, 11) == 0, "[6][11]"
    assert env.rail.get_full_transitions(6, 12) == 32800, "[6][12]"
    assert env.rail.get_full_transitions(6, 13) == 0, "[6][13]"
    assert env.rail.get_full_transitions(6, 14) == 0, "[6][14]"
    assert env.rail.get_full_transitions(6, 15) == 0, "[6][15]"
    assert env.rail.get_full_transitions(6, 16) == 0, "[6][16]"
    assert env.rail.get_full_transitions(6, 17) == 0, "[6][17]"
    assert env.rail.get_full_transitions(6, 18) == 0, "[6][18]"
    assert env.rail.get_full_transitions(6, 19) == 0, "[6][19]"
    assert env.rail.get_full_transitions(6, 20) == 0, "[6][20]"
    assert env.rail.get_full_transitions(6, 21) == 0, "[6][21]"
    assert env.rail.get_full_transitions(6, 22) == 32800, "[6][22]"
    assert env.rail.get_full_transitions(6, 23) == 0, "[6][23]"
    assert env.rail.get_full_transitions(6, 24) == 0, "[6][24]"
    assert env.rail.get_full_transitions(7, 0) == 0, "[7][0]"
    assert env.rail.get_full_transitions(7, 1) == 0, "[7][1]"
    assert env.rail.get_full_transitions(7, 2) == 0, "[7][2]"
    assert env.rail.get_full_transitions(7, 3) == 32800, "[7][3]"
    assert env.rail.get_full_transitions(7, 4) == 0, "[7][4]"
    assert env.rail.get_full_transitions(7, 5) == 0, "[7][5]"
    assert env.rail.get_full_transitions(7, 6) == 0, "[7][6]"
    assert env.rail.get_full_transitions(7, 7) == 0, "[7][7]"
    assert env.rail.get_full_transitions(7, 8) == 0, "[7][8]"
    assert env.rail.get_full_transitions(7, 9) == 0, "[7][9]"
    assert env.rail.get_full_transitions(7, 10) == 0, "[7][10]"
    assert env.rail.get_full_transitions(7, 11) == 0, "[7][11]"
    assert env.rail.get_full_transitions(7, 12) == 32800, "[7][12]"
    assert env.rail.get_full_transitions(7, 13) == 0, "[7][13]"
    assert env.rail.get_full_transitions(7, 14) == 0, "[7][14]"
    assert env.rail.get_full_transitions(7, 15) == 0, "[7][15]"
    assert env.rail.get_full_transitions(7, 16) == 0, "[7][16]"
    assert env.rail.get_full_transitions(7, 17) == 0, "[7][17]"
    assert env.rail.get_full_transitions(7, 18) == 0, "[7][18]"
    assert env.rail.get_full_transitions(7, 19) == 0, "[7][19]"
    assert env.rail.get_full_transitions(7, 20) == 0, "[7][20]"
    assert env.rail.get_full_transitions(7, 21) == 0, "[7][21]"
    assert env.rail.get_full_transitions(7, 22) == 32800, "[7][22]"
    assert env.rail.get_full_transitions(7, 23) == 0, "[7][23]"
    assert env.rail.get_full_transitions(7, 24) == 0, "[7][24]"
    assert env.rail.get_full_transitions(8, 0) == 0, "[8][0]"
    assert env.rail.get_full_transitions(8, 1) == 0, "[8][1]"
    assert env.rail.get_full_transitions(8, 2) == 0, "[8][2]"
    assert env.rail.get_full_transitions(8, 3) == 32800, "[8][3]"
    assert env.rail.get_full_transitions(8, 4) == 0, "[8][4]"
    assert env.rail.get_full_transitions(8, 5) == 8192, "[8][5]"
    assert env.rail.get_full_transitions(8, 6) == 0, "[8][6]"
    assert env.rail.get_full_transitions(8, 7) == 0, "[8][7]"
    assert env.rail.get_full_transitions(8, 8) == 0, "[8][8]"
    assert env.rail.get_full_transitions(8, 9) == 8192, "[8][9]"
    assert env.rail.get_full_transitions(8, 10) == 8192, "[8][10]"
    assert env.rail.get_full_transitions(8, 11) == 0, "[8][11]"
    assert env.rail.get_full_transitions(8, 12) == 32800, "[8][12]"
    assert env.rail.get_full_transitions(8, 13) == 8192, "[8][13]"
    assert env.rail.get_full_transitions(8, 14) == 0, "[8][14]"
    assert env.rail.get_full_transitions(8, 15) == 0, "[8][15]"
    assert env.rail.get_full_transitions(8, 16) == 0, "[8][16]"
    assert env.rail.get_full_transitions(8, 17) == 0, "[8][17]"
    assert env.rail.get_full_transitions(8, 18) == 0, "[8][18]"
    assert env.rail.get_full_transitions(8, 19) == 0, "[8][19]"
    assert env.rail.get_full_transitions(8, 20) == 0, "[8][20]"
    assert env.rail.get_full_transitions(8, 21) == 0, "[8][21]"
    assert env.rail.get_full_transitions(8, 22) == 32800, "[8][22]"
    assert env.rail.get_full_transitions(8, 23) == 0, "[8][23]"
    assert env.rail.get_full_transitions(8, 24) == 0, "[8][24]"
    assert env.rail.get_full_transitions(9, 0) == 8192, "[9][0]"
    assert env.rail.get_full_transitions(9, 1) == 0, "[9][1]"
    assert env.rail.get_full_transitions(9, 2) == 0, "[9][2]"
    assert env.rail.get_full_transitions(9, 3) == 32800, "[9][3]"
    assert env.rail.get_full_transitions(9, 4) == 8192, "[9][4]"
    assert env.rail.get_full_transitions(9, 5) == 32800, "[9][5]"
    assert env.rail.get_full_transitions(9, 6) == 0, "[9][6]"
    assert env.rail.get_full_transitions(9, 7) == 0, "[9][7]"
    assert env.rail.get_full_transitions(9, 8) == 0, "[9][8]"
    assert env.rail.get_full_transitions(9, 9) == 72, "[9][9]"
    assert env.rail.get_full_transitions(9, 10) == 37408, "[9][10]"
    assert env.rail.get_full_transitions(9, 11) == 0, "[9][11]"
    assert env.rail.get_full_transitions(9, 12) == 49186, "[9][12]"
    assert env.rail.get_full_transitions(9, 13) == 3089, "[9][13]"
    assert env.rail.get_full_transitions(9, 14) == 4608, "[9][14]"
    assert env.rail.get_full_transitions(9, 15) == 0, "[9][15]"
    assert env.rail.get_full_transitions(9, 16) == 0, "[9][16]"
    assert env.rail.get_full_transitions(9, 17) == 0, "[9][17]"
    assert env.rail.get_full_transitions(9, 18) == 0, "[9][18]"
    assert env.rail.get_full_transitions(9, 19) == 0, "[9][19]"
    assert env.rail.get_full_transitions(9, 20) == 0, "[9][20]"
    assert env.rail.get_full_transitions(9, 21) == 0, "[9][21]"
    assert env.rail.get_full_transitions(9, 22) == 32800, "[9][22]"
    assert env.rail.get_full_transitions(9, 23) == 0, "[9][23]"
    assert env.rail.get_full_transitions(9, 24) == 0, "[9][24]"
    assert env.rail.get_full_transitions(10, 0) == 32800, "[10][0]"
    assert env.rail.get_full_transitions(10, 1) == 0, "[10][1]"
    assert env.rail.get_full_transitions(10, 2) == 0, "[10][2]"
    assert env.rail.get_full_transitions(10, 3) == 32800, "[10][3]"
    assert env.rail.get_full_transitions(10, 4) == 32800, "[10][4]"
    assert env.rail.get_full_transitions(10, 5) == 32800, "[10][5]"
    assert env.rail.get_full_transitions(10, 6) == 0, "[10][6]"
    assert env.rail.get_full_transitions(10, 7) == 0, "[10][7]"
    assert env.rail.get_full_transitions(10, 8) == 0, "[10][8]"
    assert env.rail.get_full_transitions(10, 9) == 4, "[10][9]"
    assert env.rail.get_full_transitions(10, 10) == 1097, "[10][10]"
    assert env.rail.get_full_transitions(10, 11) == 1025, "[10][11]"
    assert env.rail.get_full_transitions(10, 12) == 37408, "[10][12]"
    assert env.rail.get_full_transitions(10, 13) == 0, "[10][13]"
    assert env.rail.get_full_transitions(10, 14) == 128, "[10][14]"
    assert env.rail.get_full_transitions(10, 15) == 0, "[10][15]"
    assert env.rail.get_full_transitions(10, 16) == 0, "[10][16]"
    assert env.rail.get_full_transitions(10, 17) == 0, "[10][17]"
    assert env.rail.get_full_transitions(10, 18) == 0, "[10][18]"
    assert env.rail.get_full_transitions(10, 19) == 0, "[10][19]"
    assert env.rail.get_full_transitions(10, 20) == 0, "[10][20]"
    assert env.rail.get_full_transitions(10, 21) == 0, "[10][21]"
    assert env.rail.get_full_transitions(10, 22) == 32800, "[10][22]"
    assert env.rail.get_full_transitions(10, 23) == 0, "[10][23]"
    assert env.rail.get_full_transitions(10, 24) == 0, "[10][24]"
    assert env.rail.get_full_transitions(11, 0) == 16458, "[11][0]"
    assert env.rail.get_full_transitions(11, 1) == 17411, "[11][1]"
    assert env.rail.get_full_transitions(11, 2) == 1025, "[11][2]"
    assert env.rail.get_full_transitions(11, 3) == 52275, "[11][3]"
    assert env.rail.get_full_transitions(11, 4) == 3089, "[11][4]"
    assert env.rail.get_full_transitions(11, 5) == 2064, "[11][5]"
    assert env.rail.get_full_transitions(11, 6) == 0, "[11][6]"
    assert env.rail.get_full_transitions(11, 7) == 0, "[11][7]"
    assert env.rail.get_full_transitions(11, 8) == 0, "[11][8]"
    assert env.rail.get_full_transitions(11, 9) == 0, "[11][9]"
    assert env.rail.get_full_transitions(11, 10) == 0, "[11][10]"
    assert env.rail.get_full_transitions(11, 11) == 0, "[11][11]"
    assert env.rail.get_full_transitions(11, 12) == 32800, "[11][12]"
    assert env.rail.get_full_transitions(11, 13) == 0, "[11][13]"
    assert env.rail.get_full_transitions(11, 14) == 0, "[11][14]"
    assert env.rail.get_full_transitions(11, 15) == 0, "[11][15]"
    assert env.rail.get_full_transitions(11, 16) == 0, "[11][16]"
    assert env.rail.get_full_transitions(11, 17) == 0, "[11][17]"
    assert env.rail.get_full_transitions(11, 18) == 0, "[11][18]"
    assert env.rail.get_full_transitions(11, 19) == 0, "[11][19]"
    assert env.rail.get_full_transitions(11, 20) == 0, "[11][20]"
    assert env.rail.get_full_transitions(11, 21) == 0, "[11][21]"
    assert env.rail.get_full_transitions(11, 22) == 32800, "[11][22]"
    assert env.rail.get_full_transitions(11, 23) == 0, "[11][23]"
    assert env.rail.get_full_transitions(11, 24) == 0, "[11][24]"
    assert env.rail.get_full_transitions(12, 0) == 128, "[12][0]"
    assert env.rail.get_full_transitions(12, 1) == 128, "[12][1]"
    assert env.rail.get_full_transitions(12, 2) == 0, "[12][2]"
    assert env.rail.get_full_transitions(12, 3) == 49186, "[12][3]"
    assert env.rail.get_full_transitions(12, 4) == 1025, "[12][4]"
    assert env.rail.get_full_transitions(12, 5) == 1025, "[12][5]"
    assert env.rail.get_full_transitions(12, 6) == 1025, "[12][6]"
    assert env.rail.get_full_transitions(12, 7) == 1025, "[12][7]"
    assert env.rail.get_full_transitions(12, 8) == 1025, "[12][8]"
    assert env.rail.get_full_transitions(12, 9) == 1025, "[12][9]"
    assert env.rail.get_full_transitions(12, 10) == 1025, "[12][10]"
    assert env.rail.get_full_transitions(12, 11) == 1025, "[12][11]"
    assert env.rail.get_full_transitions(12, 12) == 34864, "[12][12]"
    assert env.rail.get_full_transitions(12, 13) == 0, "[12][13]"
    assert env.rail.get_full_transitions(12, 14) == 0, "[12][14]"
    assert env.rail.get_full_transitions(12, 15) == 0, "[12][15]"
    assert env.rail.get_full_transitions(12, 16) == 0, "[12][16]"
    assert env.rail.get_full_transitions(12, 17) == 0, "[12][17]"
    assert env.rail.get_full_transitions(12, 18) == 0, "[12][18]"
    assert env.rail.get_full_transitions(12, 19) == 0, "[12][19]"
    assert env.rail.get_full_transitions(12, 20) == 0, "[12][20]"
    assert env.rail.get_full_transitions(12, 21) == 0, "[12][21]"
    assert env.rail.get_full_transitions(12, 22) == 32800, "[12][22]"
    assert env.rail.get_full_transitions(12, 23) == 0, "[12][23]"
    assert env.rail.get_full_transitions(12, 24) == 0, "[12][24]"
    assert env.rail.get_full_transitions(13, 0) == 0, "[13][0]"
    assert env.rail.get_full_transitions(13, 1) == 0, "[13][1]"
    assert env.rail.get_full_transitions(13, 2) == 0, "[13][2]"
    assert env.rail.get_full_transitions(13, 3) == 32800, "[13][3]"
    assert env.rail.get_full_transitions(13, 4) == 0, "[13][4]"
    assert env.rail.get_full_transitions(13, 5) == 0, "[13][5]"
    assert env.rail.get_full_transitions(13, 6) == 0, "[13][6]"
    assert env.rail.get_full_transitions(13, 7) == 0, "[13][7]"
    assert env.rail.get_full_transitions(13, 8) == 0, "[13][8]"
    assert env.rail.get_full_transitions(13, 9) == 0, "[13][9]"
    assert env.rail.get_full_transitions(13, 10) == 0, "[13][10]"
    assert env.rail.get_full_transitions(13, 11) == 0, "[13][11]"
    assert env.rail.get_full_transitions(13, 12) == 32800, "[13][12]"
    assert env.rail.get_full_transitions(13, 13) == 0, "[13][13]"
    assert env.rail.get_full_transitions(13, 14) == 0, "[13][14]"
    assert env.rail.get_full_transitions(13, 15) == 0, "[13][15]"
    assert env.rail.get_full_transitions(13, 16) == 0, "[13][16]"
    assert env.rail.get_full_transitions(13, 17) == 0, "[13][17]"
    assert env.rail.get_full_transitions(13, 18) == 0, "[13][18]"
    assert env.rail.get_full_transitions(13, 19) == 0, "[13][19]"
    assert env.rail.get_full_transitions(13, 20) == 0, "[13][20]"
    assert env.rail.get_full_transitions(13, 21) == 0, "[13][21]"
    assert env.rail.get_full_transitions(13, 22) == 32800, "[13][22]"
    assert env.rail.get_full_transitions(13, 23) == 0, "[13][23]"
    assert env.rail.get_full_transitions(13, 24) == 0, "[13][24]"
    assert env.rail.get_full_transitions(14, 0) == 0, "[14][0]"
    assert env.rail.get_full_transitions(14, 1) == 0, "[14][1]"
    assert env.rail.get_full_transitions(14, 2) == 0, "[14][2]"
    assert env.rail.get_full_transitions(14, 3) == 32800, "[14][3]"
    assert env.rail.get_full_transitions(14, 4) == 0, "[14][4]"
    assert env.rail.get_full_transitions(14, 5) == 0, "[14][5]"
    assert env.rail.get_full_transitions(14, 6) == 0, "[14][6]"
    assert env.rail.get_full_transitions(14, 7) == 0, "[14][7]"
    assert env.rail.get_full_transitions(14, 8) == 0, "[14][8]"
    assert env.rail.get_full_transitions(14, 9) == 0, "[14][9]"
    assert env.rail.get_full_transitions(14, 10) == 0, "[14][10]"
    assert env.rail.get_full_transitions(14, 11) == 0, "[14][11]"
    assert env.rail.get_full_transitions(14, 12) == 32800, "[14][12]"
    assert env.rail.get_full_transitions(14, 13) == 0, "[14][13]"
    assert env.rail.get_full_transitions(14, 14) == 0, "[14][14]"
    assert env.rail.get_full_transitions(14, 15) == 0, "[14][15]"
    assert env.rail.get_full_transitions(14, 16) == 0, "[14][16]"
    assert env.rail.get_full_transitions(14, 17) == 0, "[14][17]"
    assert env.rail.get_full_transitions(14, 18) == 0, "[14][18]"
    assert env.rail.get_full_transitions(14, 19) == 0, "[14][19]"
    assert env.rail.get_full_transitions(14, 20) == 0, "[14][20]"
    assert env.rail.get_full_transitions(14, 21) == 0, "[14][21]"
    assert env.rail.get_full_transitions(14, 22) == 32800, "[14][22]"
    assert env.rail.get_full_transitions(14, 23) == 0, "[14][23]"
    assert env.rail.get_full_transitions(14, 24) == 0, "[14][24]"
    assert env.rail.get_full_transitions(15, 0) == 0, "[15][0]"
    assert env.rail.get_full_transitions(15, 1) == 0, "[15][1]"
    assert env.rail.get_full_transitions(15, 2) == 0, "[15][2]"
    assert env.rail.get_full_transitions(15, 3) == 32800, "[15][3]"
    assert env.rail.get_full_transitions(15, 4) == 0, "[15][4]"
    assert env.rail.get_full_transitions(15, 5) == 0, "[15][5]"
    assert env.rail.get_full_transitions(15, 6) == 0, "[15][6]"
    assert env.rail.get_full_transitions(15, 7) == 0, "[15][7]"
    assert env.rail.get_full_transitions(15, 8) == 0, "[15][8]"
    assert env.rail.get_full_transitions(15, 9) == 0, "[15][9]"
    assert env.rail.get_full_transitions(15, 10) == 0, "[15][10]"
    assert env.rail.get_full_transitions(15, 11) == 0, "[15][11]"
    assert env.rail.get_full_transitions(15, 12) == 32800, "[15][12]"
    assert env.rail.get_full_transitions(15, 13) == 0, "[15][13]"
    assert env.rail.get_full_transitions(15, 14) == 0, "[15][14]"
    assert env.rail.get_full_transitions(15, 15) == 0, "[15][15]"
    assert env.rail.get_full_transitions(15, 16) == 0, "[15][16]"
    assert env.rail.get_full_transitions(15, 17) == 0, "[15][17]"
    assert env.rail.get_full_transitions(15, 18) == 0, "[15][18]"
    assert env.rail.get_full_transitions(15, 19) == 0, "[15][19]"
    assert env.rail.get_full_transitions(15, 20) == 0, "[15][20]"
    assert env.rail.get_full_transitions(15, 21) == 0, "[15][21]"
    assert env.rail.get_full_transitions(15, 22) == 32800, "[15][22]"
    assert env.rail.get_full_transitions(15, 23) == 0, "[15][23]"
    assert env.rail.get_full_transitions(15, 24) == 0, "[15][24]"
    assert env.rail.get_full_transitions(16, 0) == 0, "[16][0]"
    assert env.rail.get_full_transitions(16, 1) == 0, "[16][1]"
    assert env.rail.get_full_transitions(16, 2) == 0, "[16][2]"
    assert env.rail.get_full_transitions(16, 3) == 32800, "[16][3]"
    assert env.rail.get_full_transitions(16, 4) == 0, "[16][4]"
    assert env.rail.get_full_transitions(16, 5) == 0, "[16][5]"
    assert env.rail.get_full_transitions(16, 6) == 0, "[16][6]"
    assert env.rail.get_full_transitions(16, 7) == 0, "[16][7]"
    assert env.rail.get_full_transitions(16, 8) == 0, "[16][8]"
    assert env.rail.get_full_transitions(16, 9) == 0, "[16][9]"
    assert env.rail.get_full_transitions(16, 10) == 0, "[16][10]"
    assert env.rail.get_full_transitions(16, 11) == 0, "[16][11]"
    assert env.rail.get_full_transitions(16, 12) == 32800, "[16][12]"
    assert env.rail.get_full_transitions(16, 13) == 0, "[16][13]"
    assert env.rail.get_full_transitions(16, 14) == 0, "[16][14]"
    assert env.rail.get_full_transitions(16, 15) == 0, "[16][15]"
    assert env.rail.get_full_transitions(16, 16) == 0, "[16][16]"
    assert env.rail.get_full_transitions(16, 17) == 0, "[16][17]"
    assert env.rail.get_full_transitions(16, 18) == 0, "[16][18]"
    assert env.rail.get_full_transitions(16, 19) == 0, "[16][19]"
    assert env.rail.get_full_transitions(16, 20) == 0, "[16][20]"
    assert env.rail.get_full_transitions(16, 21) == 0, "[16][21]"
    assert env.rail.get_full_transitions(16, 22) == 32800, "[16][22]"
    assert env.rail.get_full_transitions(16, 23) == 0, "[16][23]"
    assert env.rail.get_full_transitions(16, 24) == 0, "[16][24]"
    assert env.rail.get_full_transitions(17, 0) == 0, "[17][0]"
    assert env.rail.get_full_transitions(17, 1) == 0, "[17][1]"
    assert env.rail.get_full_transitions(17, 2) == 0, "[17][2]"
    assert env.rail.get_full_transitions(17, 3) == 32800, "[17][3]"
    assert env.rail.get_full_transitions(17, 4) == 0, "[17][4]"
    assert env.rail.get_full_transitions(17, 5) == 0, "[17][5]"
    assert env.rail.get_full_transitions(17, 6) == 0, "[17][6]"
    assert env.rail.get_full_transitions(17, 7) == 0, "[17][7]"
    assert env.rail.get_full_transitions(17, 8) == 0, "[17][8]"
    assert env.rail.get_full_transitions(17, 9) == 0, "[17][9]"
    assert env.rail.get_full_transitions(17, 10) == 0, "[17][10]"
    assert env.rail.get_full_transitions(17, 11) == 0, "[17][11]"
    assert env.rail.get_full_transitions(17, 12) == 32800, "[17][12]"
    assert env.rail.get_full_transitions(17, 13) == 0, "[17][13]"
    assert env.rail.get_full_transitions(17, 14) == 0, "[17][14]"
    assert env.rail.get_full_transitions(17, 15) == 0, "[17][15]"
    assert env.rail.get_full_transitions(17, 16) == 0, "[17][16]"
    assert env.rail.get_full_transitions(17, 17) == 0, "[17][17]"
    assert env.rail.get_full_transitions(17, 18) == 0, "[17][18]"
    assert env.rail.get_full_transitions(17, 19) == 0, "[17][19]"
    assert env.rail.get_full_transitions(17, 20) == 0, "[17][20]"
    assert env.rail.get_full_transitions(17, 21) == 0, "[17][21]"
    assert env.rail.get_full_transitions(17, 22) == 32800, "[17][22]"
    assert env.rail.get_full_transitions(17, 23) == 0, "[17][23]"
    assert env.rail.get_full_transitions(17, 24) == 0, "[17][24]"
    assert env.rail.get_full_transitions(18, 0) == 0, "[18][0]"
    assert env.rail.get_full_transitions(18, 1) == 0, "[18][1]"
    assert env.rail.get_full_transitions(18, 2) == 0, "[18][2]"
    assert env.rail.get_full_transitions(18, 3) == 32800, "[18][3]"
    assert env.rail.get_full_transitions(18, 4) == 0, "[18][4]"
    assert env.rail.get_full_transitions(18, 5) == 0, "[18][5]"
    assert env.rail.get_full_transitions(18, 6) == 0, "[18][6]"
    assert env.rail.get_full_transitions(18, 7) == 0, "[18][7]"
    assert env.rail.get_full_transitions(18, 8) == 0, "[18][8]"
    assert env.rail.get_full_transitions(18, 9) == 0, "[18][9]"
    assert env.rail.get_full_transitions(18, 10) == 0, "[18][10]"
    assert env.rail.get_full_transitions(18, 11) == 0, "[18][11]"
    assert env.rail.get_full_transitions(18, 12) == 32800, "[18][12]"
    assert env.rail.get_full_transitions(18, 13) == 0, "[18][13]"
    assert env.rail.get_full_transitions(18, 14) == 0, "[18][14]"
    assert env.rail.get_full_transitions(18, 15) == 0, "[18][15]"
    assert env.rail.get_full_transitions(18, 16) == 0, "[18][16]"
    assert env.rail.get_full_transitions(18, 17) == 0, "[18][17]"
    assert env.rail.get_full_transitions(18, 18) == 0, "[18][18]"
    assert env.rail.get_full_transitions(18, 19) == 0, "[18][19]"
    assert env.rail.get_full_transitions(18, 20) == 0, "[18][20]"
    assert env.rail.get_full_transitions(18, 21) == 0, "[18][21]"
    assert env.rail.get_full_transitions(18, 22) == 32800, "[18][22]"
    assert env.rail.get_full_transitions(18, 23) == 0, "[18][23]"
    assert env.rail.get_full_transitions(18, 24) == 0, "[18][24]"
    assert env.rail.get_full_transitions(19, 0) == 0, "[19][0]"
    assert env.rail.get_full_transitions(19, 1) == 0, "[19][1]"
    assert env.rail.get_full_transitions(19, 2) == 0, "[19][2]"
    assert env.rail.get_full_transitions(19, 3) == 32872, "[19][3]"
    assert env.rail.get_full_transitions(19, 4) == 1025, "[19][4]"
    assert env.rail.get_full_transitions(19, 5) == 1025, "[19][5]"
    assert env.rail.get_full_transitions(19, 6) == 1025, "[19][6]"
    assert env.rail.get_full_transitions(19, 7) == 1025, "[19][7]"
    assert env.rail.get_full_transitions(19, 8) == 1025, "[19][8]"
    assert env.rail.get_full_transitions(19, 9) == 1025, "[19][9]"
    assert env.rail.get_full_transitions(19, 10) == 1025, "[19][10]"
    assert env.rail.get_full_transitions(19, 11) == 1025, "[19][11]"
    assert env.rail.get_full_transitions(19, 12) == 6672, "[19][12]"
    assert env.rail.get_full_transitions(19, 13) == 0, "[19][13]"
    assert env.rail.get_full_transitions(19, 14) == 0, "[19][14]"
    assert env.rail.get_full_transitions(19, 15) == 0, "[19][15]"
    assert env.rail.get_full_transitions(19, 16) == 0, "[19][16]"
    assert env.rail.get_full_transitions(19, 17) == 0, "[19][17]"
    assert env.rail.get_full_transitions(19, 18) == 0, "[19][18]"
    assert env.rail.get_full_transitions(19, 19) == 0, "[19][19]"
    assert env.rail.get_full_transitions(19, 20) == 0, "[19][20]"
    assert env.rail.get_full_transitions(19, 21) == 0, "[19][21]"
    assert env.rail.get_full_transitions(19, 22) == 32800, "[19][22]"
    assert env.rail.get_full_transitions(19, 23) == 0, "[19][23]"
    assert env.rail.get_full_transitions(19, 24) == 0, "[19][24]"
    assert env.rail.get_full_transitions(20, 0) == 0, "[20][0]"
    assert env.rail.get_full_transitions(20, 1) == 0, "[20][1]"
    assert env.rail.get_full_transitions(20, 2) == 0, "[20][2]"
    assert env.rail.get_full_transitions(20, 3) == 32800, "[20][3]"
    assert env.rail.get_full_transitions(20, 4) == 0, "[20][4]"
    assert env.rail.get_full_transitions(20, 5) == 0, "[20][5]"
    assert env.rail.get_full_transitions(20, 6) == 0, "[20][6]"
    assert env.rail.get_full_transitions(20, 7) == 0, "[20][7]"
    assert env.rail.get_full_transitions(20, 8) == 0, "[20][8]"
    assert env.rail.get_full_transitions(20, 9) == 0, "[20][9]"
    assert env.rail.get_full_transitions(20, 10) == 0, "[20][10]"
    assert env.rail.get_full_transitions(20, 11) == 0, "[20][11]"
    assert env.rail.get_full_transitions(20, 12) == 32800, "[20][12]"
    assert env.rail.get_full_transitions(20, 13) == 0, "[20][13]"
    assert env.rail.get_full_transitions(20, 14) == 0, "[20][14]"
    assert env.rail.get_full_transitions(20, 15) == 0, "[20][15]"
    assert env.rail.get_full_transitions(20, 16) == 0, "[20][16]"
    assert env.rail.get_full_transitions(20, 17) == 0, "[20][17]"
    assert env.rail.get_full_transitions(20, 18) == 0, "[20][18]"
    assert env.rail.get_full_transitions(20, 19) == 0, "[20][19]"
    assert env.rail.get_full_transitions(20, 20) == 0, "[20][20]"
    assert env.rail.get_full_transitions(20, 21) == 0, "[20][21]"
    assert env.rail.get_full_transitions(20, 22) == 32800, "[20][22]"
    assert env.rail.get_full_transitions(20, 23) == 0, "[20][23]"
    assert env.rail.get_full_transitions(20, 24) == 0, "[20][24]"
    assert env.rail.get_full_transitions(21, 0) == 0, "[21][0]"
    assert env.rail.get_full_transitions(21, 1) == 0, "[21][1]"
    assert env.rail.get_full_transitions(21, 2) == 0, "[21][2]"
    assert env.rail.get_full_transitions(21, 3) == 32800, "[21][3]"
    assert env.rail.get_full_transitions(21, 4) == 0, "[21][4]"
    assert env.rail.get_full_transitions(21, 5) == 0, "[21][5]"
    assert env.rail.get_full_transitions(21, 6) == 0, "[21][6]"
    assert env.rail.get_full_transitions(21, 7) == 0, "[21][7]"
    assert env.rail.get_full_transitions(21, 8) == 0, "[21][8]"
    assert env.rail.get_full_transitions(21, 9) == 0, "[21][9]"
    assert env.rail.get_full_transitions(21, 10) == 0, "[21][10]"
    assert env.rail.get_full_transitions(21, 11) == 0, "[21][11]"
    assert env.rail.get_full_transitions(21, 12) == 32800, "[21][12]"
    assert env.rail.get_full_transitions(21, 13) == 0, "[21][13]"
    assert env.rail.get_full_transitions(21, 14) == 0, "[21][14]"
    assert env.rail.get_full_transitions(21, 15) == 0, "[21][15]"
    assert env.rail.get_full_transitions(21, 16) == 0, "[21][16]"
    assert env.rail.get_full_transitions(21, 17) == 0, "[21][17]"
    assert env.rail.get_full_transitions(21, 18) == 0, "[21][18]"
    assert env.rail.get_full_transitions(21, 19) == 0, "[21][19]"
    assert env.rail.get_full_transitions(21, 20) == 0, "[21][20]"
    assert env.rail.get_full_transitions(21, 21) == 0, "[21][21]"
    assert env.rail.get_full_transitions(21, 22) == 32800, "[21][22]"
    assert env.rail.get_full_transitions(21, 23) == 0, "[21][23]"
    assert env.rail.get_full_transitions(21, 24) == 0, "[21][24]"
    assert env.rail.get_full_transitions(22, 0) == 0, "[22][0]"
    assert env.rail.get_full_transitions(22, 1) == 0, "[22][1]"
    assert env.rail.get_full_transitions(22, 2) == 0, "[22][2]"
    assert env.rail.get_full_transitions(22, 3) == 32800, "[22][3]"
    assert env.rail.get_full_transitions(22, 4) == 0, "[22][4]"
    assert env.rail.get_full_transitions(22, 5) == 0, "[22][5]"
    assert env.rail.get_full_transitions(22, 6) == 0, "[22][6]"
    assert env.rail.get_full_transitions(22, 7) == 0, "[22][7]"
    assert env.rail.get_full_transitions(22, 8) == 0, "[22][8]"
    assert env.rail.get_full_transitions(22, 9) == 0, "[22][9]"
    assert env.rail.get_full_transitions(22, 10) == 0, "[22][10]"
    assert env.rail.get_full_transitions(22, 11) == 0, "[22][11]"
    assert env.rail.get_full_transitions(22, 12) == 32800, "[22][12]"
    assert env.rail.get_full_transitions(22, 13) == 0, "[22][13]"
    assert env.rail.get_full_transitions(22, 14) == 0, "[22][14]"
    assert env.rail.get_full_transitions(22, 15) == 0, "[22][15]"
    assert env.rail.get_full_transitions(22, 16) == 0, "[22][16]"
    assert env.rail.get_full_transitions(22, 17) == 0, "[22][17]"
    assert env.rail.get_full_transitions(22, 18) == 0, "[22][18]"
    assert env.rail.get_full_transitions(22, 19) == 0, "[22][19]"
    assert env.rail.get_full_transitions(22, 20) == 0, "[22][20]"
    assert env.rail.get_full_transitions(22, 21) == 0, "[22][21]"
    assert env.rail.get_full_transitions(22, 22) == 32800, "[22][22]"
    assert env.rail.get_full_transitions(22, 23) == 0, "[22][23]"
    assert env.rail.get_full_transitions(22, 24) == 0, "[22][24]"
    assert env.rail.get_full_transitions(23, 0) == 0, "[23][0]"
    assert env.rail.get_full_transitions(23, 1) == 0, "[23][1]"
    assert env.rail.get_full_transitions(23, 2) == 0, "[23][2]"
    assert env.rail.get_full_transitions(23, 3) == 32800, "[23][3]"
    assert env.rail.get_full_transitions(23, 4) == 0, "[23][4]"
    assert env.rail.get_full_transitions(23, 5) == 0, "[23][5]"
    assert env.rail.get_full_transitions(23, 6) == 0, "[23][6]"
    assert env.rail.get_full_transitions(23, 7) == 0, "[23][7]"
    assert env.rail.get_full_transitions(23, 8) == 0, "[23][8]"
    assert env.rail.get_full_transitions(23, 9) == 0, "[23][9]"
    assert env.rail.get_full_transitions(23, 10) == 0, "[23][10]"
    assert env.rail.get_full_transitions(23, 11) == 0, "[23][11]"
    assert env.rail.get_full_transitions(23, 12) == 32800, "[23][12]"
    assert env.rail.get_full_transitions(23, 13) == 0, "[23][13]"
    assert env.rail.get_full_transitions(23, 14) == 0, "[23][14]"
    assert env.rail.get_full_transitions(23, 15) == 0, "[23][15]"
    assert env.rail.get_full_transitions(23, 16) == 0, "[23][16]"
    assert env.rail.get_full_transitions(23, 17) == 0, "[23][17]"
    assert env.rail.get_full_transitions(23, 18) == 0, "[23][18]"
    assert env.rail.get_full_transitions(23, 19) == 0, "[23][19]"
    assert env.rail.get_full_transitions(23, 20) == 0, "[23][20]"
    assert env.rail.get_full_transitions(23, 21) == 0, "[23][21]"
    assert env.rail.get_full_transitions(23, 22) == 32800, "[23][22]"
    assert env.rail.get_full_transitions(23, 23) == 0, "[23][23]"
    assert env.rail.get_full_transitions(23, 24) == 0, "[23][24]"
    assert env.rail.get_full_transitions(24, 0) == 0, "[24][0]"
    assert env.rail.get_full_transitions(24, 1) == 0, "[24][1]"
    assert env.rail.get_full_transitions(24, 2) == 0, "[24][2]"
    assert env.rail.get_full_transitions(24, 3) == 32800, "[24][3]"
    assert env.rail.get_full_transitions(24, 4) == 0, "[24][4]"
    assert env.rail.get_full_transitions(24, 5) == 0, "[24][5]"
    assert env.rail.get_full_transitions(24, 6) == 0, "[24][6]"
    assert env.rail.get_full_transitions(24, 7) == 0, "[24][7]"
    assert env.rail.get_full_transitions(24, 8) == 0, "[24][8]"
    assert env.rail.get_full_transitions(24, 9) == 8192, "[24][9]"
    assert env.rail.get_full_transitions(24, 10) == 0, "[24][10]"
    assert env.rail.get_full_transitions(24, 11) == 0, "[24][11]"
    assert env.rail.get_full_transitions(24, 12) == 32800, "[24][12]"
    assert env.rail.get_full_transitions(24, 13) == 0, "[24][13]"
    assert env.rail.get_full_transitions(24, 14) == 0, "[24][14]"
    assert env.rail.get_full_transitions(24, 15) == 0, "[24][15]"
    assert env.rail.get_full_transitions(24, 16) == 0, "[24][16]"
    assert env.rail.get_full_transitions(24, 17) == 0, "[24][17]"
    assert env.rail.get_full_transitions(24, 18) == 0, "[24][18]"
    assert env.rail.get_full_transitions(24, 19) == 0, "[24][19]"
    assert env.rail.get_full_transitions(24, 20) == 0, "[24][20]"
    assert env.rail.get_full_transitions(24, 21) == 0, "[24][21]"
    assert env.rail.get_full_transitions(24, 22) == 32800, "[24][22]"
    assert env.rail.get_full_transitions(24, 23) == 0, "[24][23]"
    assert env.rail.get_full_transitions(24, 24) == 0, "[24][24]"
    assert env.rail.get_full_transitions(25, 0) == 0, "[25][0]"
    assert env.rail.get_full_transitions(25, 1) == 0, "[25][1]"
    assert env.rail.get_full_transitions(25, 2) == 0, "[25][2]"
    assert env.rail.get_full_transitions(25, 3) == 32800, "[25][3]"
    assert env.rail.get_full_transitions(25, 4) == 0, "[25][4]"
    assert env.rail.get_full_transitions(25, 5) == 8192, "[25][5]"
    assert env.rail.get_full_transitions(25, 6) == 0, "[25][6]"
    assert env.rail.get_full_transitions(25, 7) == 0, "[25][7]"
    assert env.rail.get_full_transitions(25, 8) == 0, "[25][8]"
    assert env.rail.get_full_transitions(25, 9) == 32800, "[25][9]"
    assert env.rail.get_full_transitions(25, 10) == 0, "[25][10]"
    assert env.rail.get_full_transitions(25, 11) == 8192, "[25][11]"
    assert env.rail.get_full_transitions(25, 12) == 32800, "[25][12]"
    assert env.rail.get_full_transitions(25, 13) == 0, "[25][13]"
    assert env.rail.get_full_transitions(25, 14) == 0, "[25][14]"
    assert env.rail.get_full_transitions(25, 15) == 0, "[25][15]"
    assert env.rail.get_full_transitions(25, 16) == 0, "[25][16]"
    assert env.rail.get_full_transitions(25, 17) == 0, "[25][17]"
    assert env.rail.get_full_transitions(25, 18) == 0, "[25][18]"
    assert env.rail.get_full_transitions(25, 19) == 0, "[25][19]"
    assert env.rail.get_full_transitions(25, 20) == 0, "[25][20]"
    assert env.rail.get_full_transitions(25, 21) == 0, "[25][21]"
    assert env.rail.get_full_transitions(25, 22) == 32800, "[25][22]"
    assert env.rail.get_full_transitions(25, 23) == 0, "[25][23]"
    assert env.rail.get_full_transitions(25, 24) == 0, "[25][24]"
    assert env.rail.get_full_transitions(26, 0) == 8192, "[26][0]"
    assert env.rail.get_full_transitions(26, 1) == 4, "[26][1]"
    assert env.rail.get_full_transitions(26, 2) == 4608, "[26][2]"
    assert env.rail.get_full_transitions(26, 3) == 32800, "[26][3]"
    assert env.rail.get_full_transitions(26, 4) == 0, "[26][4]"
    assert env.rail.get_full_transitions(26, 5) == 32800, "[26][5]"
    assert env.rail.get_full_transitions(26, 6) == 0, "[26][6]"
    assert env.rail.get_full_transitions(26, 7) == 0, "[26][7]"
    assert env.rail.get_full_transitions(26, 8) == 0, "[26][8]"
    assert env.rail.get_full_transitions(26, 9) == 32800, "[26][9]"
    assert env.rail.get_full_transitions(26, 10) == 0, "[26][10]"
    assert env.rail.get_full_transitions(26, 11) == 32800, "[26][11]"
    assert env.rail.get_full_transitions(26, 12) == 32800, "[26][12]"
    assert env.rail.get_full_transitions(26, 13) == 0, "[26][13]"
    assert env.rail.get_full_transitions(26, 14) == 0, "[26][14]"
    assert env.rail.get_full_transitions(26, 15) == 0, "[26][15]"
    assert env.rail.get_full_transitions(26, 16) == 0, "[26][16]"
    assert env.rail.get_full_transitions(26, 17) == 0, "[26][17]"
    assert env.rail.get_full_transitions(26, 18) == 0, "[26][18]"
    assert env.rail.get_full_transitions(26, 19) == 0, "[26][19]"
    assert env.rail.get_full_transitions(26, 20) == 0, "[26][20]"
    assert env.rail.get_full_transitions(26, 21) == 0, "[26][21]"
    assert env.rail.get_full_transitions(26, 22) == 32800, "[26][22]"
    assert env.rail.get_full_transitions(26, 23) == 0, "[26][23]"
    assert env.rail.get_full_transitions(26, 24) == 0, "[26][24]"
    assert env.rail.get_full_transitions(27, 0) == 72, "[27][0]"
    assert env.rail.get_full_transitions(27, 1) == 17411, "[27][1]"
    assert env.rail.get_full_transitions(27, 2) == 1097, "[27][2]"
    assert env.rail.get_full_transitions(27, 3) == 1097, "[27][3]"
    assert env.rail.get_full_transitions(27, 4) == 5633, "[27][4]"
    assert env.rail.get_full_transitions(27, 5) == 3089, "[27][5]"
    assert env.rail.get_full_transitions(27, 6) == 1025, "[27][6]"
    assert env.rail.get_full_transitions(27, 7) == 1025, "[27][7]"
    assert env.rail.get_full_transitions(27, 8) == 1025, "[27][8]"
    assert env.rail.get_full_transitions(27, 9) == 1097, "[27][9]"
    assert env.rail.get_full_transitions(27, 10) == 17411, "[27][10]"
    assert env.rail.get_full_transitions(27, 11) == 1097, "[27][11]"
    assert env.rail.get_full_transitions(27, 12) == 1097, "[27][12]"
    assert env.rail.get_full_transitions(27, 13) == 5633, "[27][13]"
    assert env.rail.get_full_transitions(27, 14) == 1025, "[27][14]"
    assert env.rail.get_full_transitions(27, 15) == 1025, "[27][15]"
    assert env.rail.get_full_transitions(27, 16) == 1025, "[27][16]"
    assert env.rail.get_full_transitions(27, 17) == 1025, "[27][17]"
    assert env.rail.get_full_transitions(27, 18) == 1025, "[27][18]"
    assert env.rail.get_full_transitions(27, 19) == 1025, "[27][19]"
    assert env.rail.get_full_transitions(27, 20) == 1025, "[27][20]"
    assert env.rail.get_full_transitions(27, 21) == 1025, "[27][21]"
    assert env.rail.get_full_transitions(27, 22) == 2064, "[27][22]"
    assert env.rail.get_full_transitions(27, 23) == 0, "[27][23]"
    assert env.rail.get_full_transitions(27, 24) == 0, "[27][24]"
    assert env.rail.get_full_transitions(28, 0) == 0, "[28][0]"
    assert env.rail.get_full_transitions(28, 1) == 32800, "[28][1]"
    assert env.rail.get_full_transitions(28, 2) == 0, "[28][2]"
    assert env.rail.get_full_transitions(28, 3) == 0, "[28][3]"
    assert env.rail.get_full_transitions(28, 4) == 72, "[28][4]"
    assert env.rail.get_full_transitions(28, 5) == 256, "[28][5]"
    assert env.rail.get_full_transitions(28, 6) == 0, "[28][6]"
    assert env.rail.get_full_transitions(28, 7) == 0, "[28][7]"
    assert env.rail.get_full_transitions(28, 8) == 0, "[28][8]"
    assert env.rail.get_full_transitions(28, 9) == 0, "[28][9]"
    assert env.rail.get_full_transitions(28, 10) == 32800, "[28][10]"
    assert env.rail.get_full_transitions(28, 11) == 0, "[28][11]"
    assert env.rail.get_full_transitions(28, 12) == 16386, "[28][12]"
    assert env.rail.get_full_transitions(28, 13) == 34864, "[28][13]"
    assert env.rail.get_full_transitions(28, 14) == 0, "[28][14]"
    assert env.rail.get_full_transitions(28, 15) == 0, "[28][15]"
    assert env.rail.get_full_transitions(28, 16) == 0, "[28][16]"
    assert env.rail.get_full_transitions(28, 17) == 0, "[28][17]"
    assert env.rail.get_full_transitions(28, 18) == 0, "[28][18]"
    assert env.rail.get_full_transitions(28, 19) == 0, "[28][19]"
    assert env.rail.get_full_transitions(28, 20) == 0, "[28][20]"
    assert env.rail.get_full_transitions(28, 21) == 0, "[28][21]"
    assert env.rail.get_full_transitions(28, 22) == 0, "[28][22]"
    assert env.rail.get_full_transitions(28, 23) == 0, "[28][23]"
    assert env.rail.get_full_transitions(28, 24) == 0, "[28][24]"
    assert env.rail.get_full_transitions(29, 0) == 0, "[29][0]"
    assert env.rail.get_full_transitions(29, 1) == 128, "[29][1]"
    assert env.rail.get_full_transitions(29, 2) == 0, "[29][2]"
    assert env.rail.get_full_transitions(29, 3) == 0, "[29][3]"
    assert env.rail.get_full_transitions(29, 4) == 0, "[29][4]"
    assert env.rail.get_full_transitions(29, 5) == 0, "[29][5]"
    assert env.rail.get_full_transitions(29, 6) == 0, "[29][6]"
    assert env.rail.get_full_transitions(29, 7) == 0, "[29][7]"
    assert env.rail.get_full_transitions(29, 8) == 0, "[29][8]"
    assert env.rail.get_full_transitions(29, 9) == 0, "[29][9]"
    assert env.rail.get_full_transitions(29, 10) == 128, "[29][10]"
    assert env.rail.get_full_transitions(29, 11) == 0, "[29][11]"
    assert env.rail.get_full_transitions(29, 12) == 128, "[29][12]"
    assert env.rail.get_full_transitions(29, 13) == 128, "[29][13]"
    assert env.rail.get_full_transitions(29, 14) == 0, "[29][14]"
    assert env.rail.get_full_transitions(29, 15) == 0, "[29][15]"
    assert env.rail.get_full_transitions(29, 16) == 0, "[29][16]"
    assert env.rail.get_full_transitions(29, 17) == 0, "[29][17]"
    assert env.rail.get_full_transitions(29, 18) == 0, "[29][18]"
    assert env.rail.get_full_transitions(29, 19) == 0, "[29][19]"
    assert env.rail.get_full_transitions(29, 20) == 0, "[29][20]"
    assert env.rail.get_full_transitions(29, 21) == 0, "[29][21]"
    assert env.rail.get_full_transitions(29, 22) == 0, "[29][22]"
    assert env.rail.get_full_transitions(29, 23) == 0, "[29][23]"
    assert env.rail.get_full_transitions(29, 24) == 0, "[29][24]"


def test_rail_env_action_required_info():
    np.random.seed(0)
    speed_ration_map = {1.: 0.25,  # Fast passenger train
                        1. / 2.: 0.25,  # Fast freight train
                        1. / 3.: 0.25,  # Slow commuter train
                        1. / 4.: 0.25}  # Slow freight train
    env_always_action = RailEnv(width=50,
                                height=50,
                                rail_generator=sparse_rail_generator(num_cities=10,  # Number of cities in map
                                                                     num_intersections=10,
                                                                     # Number of interesections in map
                                                                     num_trainstations=50,
                                                                     # Number of possible start/targets on map
                                                                     min_node_dist=6,  # Minimal distance of nodes
                                                                     node_radius=3,
                                                                     # Proximity of stations to city center
                                                                     num_neighb=3,
                                                                     # Number of connections to other cities
                                                                     seed=5,  # Random seed
                                                                     grid_mode=False  # Ordered distribution of nodes
                                                                     ),
                                schedule_generator=sparse_schedule_generator(speed_ration_map),
                                number_of_agents=10,
                                obs_builder_object=GlobalObsForRailEnv())
    np.random.seed(0)
    env_only_if_action_required = RailEnv(width=50,
                                          height=50,
                                          rail_generator=sparse_rail_generator(num_cities=10,  # Number of cities in map
                                                                               num_intersections=10,
                                                                               # Number of interesections in map
                                                                               num_trainstations=50,
                                                                               # Number of possible start/targets on map
                                                                               min_node_dist=6,
                                                                               # Minimal distance of nodes
                                                                               node_radius=3,
                                                                               # Proximity of stations to city center
                                                                               num_neighb=3,
                                                                               # Number of connections to other cities
                                                                               seed=5,  # Random seed
                                                                               grid_mode=False
                                                                               # Ordered distribution of nodes
                                                                               ),
                                          schedule_generator=sparse_schedule_generator(speed_ration_map),
                                          number_of_agents=10,
                                          obs_builder_object=GlobalObsForRailEnv())
    env_renderer = RenderTool(env_always_action, gl="PILSVG", )

    for step in range(100):
        print("step {}".format(step))

        action_dict_always_action = dict()
        action_dict_only_if_action_required = dict()
        # Chose an action for each agent in the environment
        for a in range(env_always_action.get_num_agents()):
            action = np.random.choice(np.arange(4))
            action_dict_always_action.update({a: action})
            if step == 0 or info_only_if_action_required['action_required'][a]:
                action_dict_only_if_action_required.update({a: action})
            else:
                print("[{}] not action_required {}, speed_data={}".format(step, a,
                                                                          env_always_action.agents[a].speed_data))

        obs_always_action, rewards_always_action, done_always_action, info_always_action = env_always_action.step(
            action_dict_always_action)
        obs_only_if_action_required, rewards_only_if_action_required, done_only_if_action_required, info_only_if_action_required = env_only_if_action_required.step(
            action_dict_only_if_action_required)

        for a in range(env_always_action.get_num_agents()):
            assert len(obs_always_action[a]) == len(obs_only_if_action_required[a])
            for i in range(len(obs_always_action[a])):
                assert np.array_equal(obs_always_action[a][i], obs_only_if_action_required[a][i])
            assert np.array_equal(rewards_always_action[a], rewards_only_if_action_required[a])
            assert np.array_equal(done_always_action[a], done_only_if_action_required[a])
            assert info_always_action['action_required'][a] == info_only_if_action_required['action_required'][a]

        env_renderer.render_env(show=True, show_observations=False, show_predictions=False)

        if done_always_action['__all__']:
            break
    env_renderer.close_window()


def test_rail_env_malfunction_speed_info():
    np.random.seed(0)
    stochastic_data = {'prop_malfunction': 0.5,  # Percentage of defective agents
                       'malfunction_rate': 30,  # Rate of malfunction occurence
                       'min_duration': 3,  # Minimal duration of malfunction
                       'max_duration': 10  # Max duration of malfunction
                       }
    env = RailEnv(width=50,
                  height=50,
                  rail_generator=sparse_rail_generator(num_cities=10,  # Number of cities in map
                                                       num_intersections=10,
                                                       # Number of interesections in map
                                                       num_trainstations=50,
                                                       # Number of possible start/targets on map
                                                       min_node_dist=6,  # Minimal distance of nodes
                                                       node_radius=3,
                                                       # Proximity of stations to city center
                                                       num_neighb=3,
                                                       # Number of connections to other cities
                                                       seed=5,  # Random seed
                                                       grid_mode=False  # Ordered distribution of nodes
                                                       ),
                  schedule_generator=sparse_schedule_generator(),
                  number_of_agents=10,
                  obs_builder_object=GlobalObsForRailEnv(),
                  stochastic_data=stochastic_data)

    env_renderer = RenderTool(env, gl="PILSVG", )
    for step in range(100):
        action_dict = dict()
        # Chose an action for each agent in the environment
        for a in range(env.get_num_agents()):
            action = np.random.choice(np.arange(4))
            action_dict.update({a: action})

        obs, rewards, done, info = env.step(
            action_dict)

        assert 'malfunction' in info
        for a in range(env.get_num_agents()):
            assert info['malfunction'][a] >= 0
            assert info['speed'][a] >= 0 and info['speed'][a] <= 1
            assert info['speed'][a] == env.agents[a].speed_data['speed']

        env_renderer.render_env(show=True, show_observations=False, show_predictions=False)

        if done['__all__']:
            break
    env_renderer.close_window()


def test_sparse_generator_with_too_man_cities_does_not_break_down():
    np.random.seed(0)

    RailEnv(width=50,
            height=50,
            rail_generator=sparse_rail_generator(
                num_cities=100,  # Number of cities in map
                num_intersections=10,  # Number of interesections in map
                num_trainstations=50,  # Number of possible start/targets on map
                min_node_dist=6,  # Minimal distance of nodes
                node_radius=3,  # Proximity of stations to city center
                num_neighb=3,  # Number of connections to other cities
                seed=5,  # Random seed
                grid_mode=False  # Ordered distribution of nodes
            ),
            schedule_generator=sparse_schedule_generator(),
            number_of_agents=10,
            obs_builder_object=GlobalObsForRailEnv())
