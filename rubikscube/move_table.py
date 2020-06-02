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

    cpCoord = [[0 for i in range(10)] for j in range(40320)]
    for comb in perms:
        cube.setCP(list(comb))
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

    epCoord = [[0 for i in range(10)] for j in range(40320)]
    for comb in perms:
        cube.setEP(list(comb))
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

    udCoord2 = [[0 for i in range(10)] for j in range(24)]
    for comb in itertools.permutations([8, 9, 10, 11], 4):
        cube.setUDEdges2(list(comb))
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
