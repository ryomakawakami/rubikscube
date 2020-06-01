import rubikscube.cubie_cube.cube as cubie
import itertools

def phase1():
    cube = cubie.Cube()

    coCoord = [[0 for i in range(18)] for j in range(2187)]
    for i in range(2187):
        cube.setCO(i)
        for j, move in enumerate(['U1', 'R1', 'F1', 'D1', 'L1', 'B1']):
            for k in range(4):  # k = 4 restores to original
                cube.turn(move)
                if k != 3:
                    coCoord[i][3 * j + k] = cube.getCO()

    eoCoord = [[0 for i in range(18)] for j in range(2048)]
    for i in range(2048):
        cube.setEO(i)
        for j, move in enumerate(['U1', 'R1', 'F1', 'D1', 'L1', 'B1']):
            for k in range(4):  # k = 4 restores to original
                cube.turn(move)
                if k != 3:
                    eoCoord[i][3 * j + k] = cube.getEO()

    udCoord1 = [[0 for i in range(18)] for j in range(495)]
    for i, comb in enumerate(itertools.combinations(range(12), 4)):
        cube.setUDEdges(list(comb))
        for j, move in enumerate(['U1', 'R1', 'F1', 'D1', 'L1', 'B1']):
            for k in range(4):  # k = 4 restores to original
                cube.turn(move)
                if k != 3:
                    udCoord1[i][3 * j + k] = cube.getUD1()

    return coCoord, eoCoord, udCoord1

def phase2():
    pass
