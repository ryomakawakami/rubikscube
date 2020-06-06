import rubikscube.cubie_cube.cube as cubie
import rubikscube.cubie_cube.constant as constant
import numpy as np

edgeDict = {
    'wr': constant.UR,
    'rw': constant.UR,
    'wg': constant.UF,
    'gw': constant.UF,
    'wo': constant.UL,
    'ow': constant.UL,
    'wb': constant.UB,
    'bw': constant.UB,
    'yr': constant.DR,
    'ry': constant.DR,
    'yg': constant.DF,
    'gy': constant.DF,
    'yo': constant.DL,
    'oy': constant.DL,
    'yb': constant.DB,
    'by': constant.DB,
    'gr': constant.FR,
    'rg': constant.FR,
    'go': constant.FL,
    'og': constant.FL,
    'bo': constant.BL,
    'ob': constant.BL,
    'br': constant.BR,
    'rb': constant.BR
}

cornerDict = {
    'wr': constant.URF,
    'rg': constant.URF,
    'gw': constant.URF,
    'wg': constant.UFL,
    'go': constant.UFL,
    'ow': constant.UFL,
    'wo': constant.ULB,
    'ob': constant.ULB,
    'bw': constant.ULB,
    'wb': constant.UBR,
    'br': constant.UBR,
    'rw': constant.UBR,
    'yg': constant.DFR,
    'gr': constant.DFR,
    'ry': constant.DFR,
    'yo': constant.DLF,
    'og': constant.DLF,
    'gy': constant.DLF,
    'yb': constant.DBL,
    'bo': constant.DBL,
    'oy': constant.DBL,
    'yr': constant.DRB,
    'rb': constant.DRB,
    'by': constant.DRB
}

def toCubie(facelets):
    facelets = np.asarray(facelets).flatten()

    cube = cubie.Cube()

    # Corner permutation
    cp = [0 for i in range(8)]
    for i, pair in enumerate([(8, 27), (6, 18), (0, 9), (2, 36), (47, 26), (45, 17), (51, 44), (53, 35)]):
        key = facelets[pair[0]] + facelets[pair[1]]
        cp[i] = cornerDict[key]
    cube.setCP(cp)

    # Edge permutation
    ep = [0 for i in range(12)]
    for i, pair in enumerate([(5, 28), (7, 19), (3, 10), (1, 37), (50, 34), (46, 25), (48, 16), (52, 43), (23, 30), (21, 14), (41, 12), (39, 32)]):
        key = facelets[pair[0]] + facelets[pair[1]]
        ep[i] = edgeDict[key]
    cube.setEP(ep)

    # Corner orientation
    co = [2 for i in range(8)]
    # U/D face in corner order
    for i, facelet in enumerate([8, 6, 0, 2, 47, 45, 51, 53]):
        if facelets[facelet] in ['w', 'y']:
            co[i] = 0
    # Orientation 1 facelets
    for i, facelet in enumerate([27, 18, 9, 36, 26, 17, 44, 35]):
        if facelets[facelet] in ['w', 'y']:
            co[i] = 1
    cube.directSetCO(co)

    # Edge orientation
    eo = [1 for i in range(12)]
    # Orientation 0 facelets
    for i, facelet in enumerate([(5, 28), (7, 19), (3, 10), (1, 37), (50, 34), (46, 25), (48, 16), (52, 43), (23, 30), (21, 14), (41, 12), (39, 32)]):
        edge = (facelets[facelet[0]], facelets[facelet[1]])

        if not (edge[0] in ['w', 'y'] or edge[1] in ['w', 'y']):      # UD slice edge
            if edge[0] in ['g', 'b']:
                eo[i] = 0
            continue

        if edge[0] in ['w', 'y']:
            eo[i] = 0
    cube.directSetEO(eo)

    return cube
    