import rubikscube.cubie_cube.cube as cubie
import itertools
import numpy as np

def phase1():
    cube = cubie.Cube()

    coCoord = np.empty(shape=(2187, 18), dtype=np.uint16)
    for i in range(2187):
        cube.setCO(i)
        for j, move in enumerate(['U1', 'R1', 'F1', 'D1', 'L1', 'B1']):
            for k in range(4):  # k = 4 restores to original
                cube.turn(move)
                if k != 3:
                    coCoord[i][3 * j + k] = cube.getCO()

    eoCoord = np.empty(shape=(2048, 18), dtype=np.uint16)
    for i in range(2048):
        cube.setEO(i)
        for j, move in enumerate(['U1', 'R1', 'F1', 'D1', 'L1', 'B1']):
            for k in range(4):  # k = 4 restores to original
                cube.turn(move)
                if k != 3:
                    eoCoord[i][3 * j + k] = cube.getEO()

    udCoord1 = np.empty(shape=(495, 18), dtype=np.uint16)
    for comb in itertools.combinations(range(12), 4):
        cube.setUDEdges(list(comb))
        coord = cube.getUD1()
        for j, move in enumerate(['U1', 'R1', 'F1', 'D1', 'L1', 'B1']):
            for k in range(4):  # k = 4 restores to original
                cube.turn(move)
                if k != 3:
                    udCoord1[coord][3 * j + k] = cube.getUD1()

    return coCoord, eoCoord, udCoord1

def phase2():
    cube = cubie.Cube()

    perms = itertools.permutations(range(8), 8)

    cpCoord = np.empty(shape=(40320, 10), dtype=np.uint16)
    for comb in perms:
        cube.setCP(comb)
        coord = cube.getCP()
        for j, move in enumerate(['U1', 'D1']):
            for k in range(4):  # k = 4 restores to original
                cube.turn(move)
                if k != 3:
                    cpCoord[coord][3 * j + k] = cube.getCP()
        for j, move in enumerate(['R2', 'L2', 'F2', 'B2']):
            cube.turn(move)
            cpCoord[coord][j + 6] = cube.getCP()
            cube.turn(move)

    perms = itertools.permutations(range(8), 8)

    epCoord = np.empty(shape=(40320, 10), dtype=np.uint16)
    for comb in perms:
        cube.setEP(comb)
        coord = cube.getEP()
        for j, move in enumerate(['U1', 'D1']):
            for k in range(4):  # k = 4 restores to original
                cube.turn(move)
                if k != 3:
                    epCoord[coord][3 * j + k] = cube.getEP()
        for j, move in enumerate(['R2', 'L2', 'F2', 'B2']):
            cube.turn(move)
            epCoord[coord][j + 6] = cube.getEP()
            cube.turn(move)

    udCoord2 = np.empty(shape=(24, 10), dtype=np.uint16)
    for comb in itertools.permutations([8, 9, 10, 11], 4):
        cube.setUDEdges2(comb)
        coord = cube.getUD2()
        for j, move in enumerate(['U1', 'D1']):
            for k in range(4):  # k = 4 restores to original
                cube.turn(move)
                if k != 3:
                    udCoord2[coord][3 * j + k] = cube.getUD2()
        for j, move in enumerate(['R2', 'L2', 'F2', 'B2']):
            cube.turn(move)
            udCoord2[coord][j + 6] = cube.getUD2()
            cube.turn(move)

    return cpCoord, epCoord, udCoord2
