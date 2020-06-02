import rubikscube.cubie_cube.cube as cubie
import rubikscube.cubie_cube.constant as constant
from rubikscube.tables import Table

import sys

maxLength = 10000

def kociemba(p):
    for d in range(maxLength):
        phase1(p, d, '')

def phase1(p, d, solution):
    if d == 0:
        if p == [0, 0, 0] and len(solution) > 0:
            if solution[-2] in ['R', 'L', 'F', 'B']:
                if solution[-1] == '1':
                    phase2start(solution)
                    print(solution)
    elif d > 0:
        if max(t.coPrune[p[0]], t.eoPrune[p[1]], t.udPrune1[p[2]]) <= d:
            # Should filter out moves depending on last move
            for i, move in enumerate(constant.MOVES):
                newP = [
                    t.coMove[p[0]][i],
                    t.eoMove[p[1]][i],
                    t.udMove1[p[2]][i]
                ]
                phase1(newP, d - 1, solution + move)

def phase2start(solution):
    currentDepth = len(solution) // 2
    cube = cubie.Cube()
    for i in range(0, len(solution), 2):
        cube.turn(solution[i*2, i*2+2])
    p = [cube.getCP(), cube.getEP(), cube.getUD2()]
    for d in range(maxLength - currentDepth + 1):
        phase2(p, d, '')

def phase2(p, d, solution):
    if d == 0:
        if p == [0, 0, 0]:
            print("2: " + solution)
            currentDepth = len(solution) // 2
            maxLength = currentDepth - 1
        elif d > 0:
            if max(t.cpPrune[p[0]], t.epPrune[p[1]], t.udPrune2[p[2]]) <= d:
                # Should filter out moves depending on last move
                for i, move in enumerate(constant.G1):
                    newP = [
                        t.cpMove[p[0]][i],
                        t.epMove[p[1]][i],
                        t.udMove2[p[2]][i]
                    ]
                    phase2(newP, d - 1, solution + move)

t = Table()

cube = cubie.Cube()

cube.scramble()
cube.display()

p = [cube.getCO(), cube.getEO(), cube.getUD1()]
p2 = [cube.getCP(), cube.getEP(), cube.getUD2()]

if __name__ == '__main__':
    print('Cube')

    phase2start('R2')
    #kociemba(p)
