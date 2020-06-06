import rubikscube.cubie_cube.cube as cubie
import rubikscube.cubie_cube.constant as constant
from rubikscube.tables import Table

import rubikscube.scanner.reader.reader as reader
import rubikscube.scanner.filter_cube as filter

import rubikscube.to_cubie

import sys
import os

maxLength = 10000
p1Length = 0

def kociemba(p):
    d = 0
    while d < maxLength:
        phase1(p, d, '')
        d += 1

def phase1(p, d, solution):
    if d == 0:
        if p == [0, 0, 0] and len(solution) > 0:
            if solution[-2] in ['R', 'L', 'F', 'B']:
                if solution[-1] == '1':
                    for i in range(0, len(solution) // 2):
                        print(solution[i*2:i*2+2], end=' ')
                    print()
                    p1Length = len(solution) // 2
                    phase2start(solution)
    elif d > 0:
        if max(t.coPrune[p[0]], t.eoPrune[p[1]], t.udPrune1[p[2]]) <= d:
            # Should filter out moves depending on last move
            lastMove = solution[-2:]
            for i, move in enumerate(constant.MOVES):
                if lastMove != '' and move[0] == lastMove[0]:
                    continue
                newP = [
                    t.coMove[p[0]][i],
                    t.eoMove[p[1]][i],
                    t.udMove1[p[2]][i]
                ]
                phase1(newP, d - 1, solution + move)

def phase2start(solution):
    currentDepth = len(solution) // 2
    cube2 = cubie.Cube()
    cube2.corners = cube.corners
    cube2.edges = cube.edges
    for i in range(0, len(solution) // 2):
        cube2.turn(solution[i*2:i*2+2])
    p = [cube2.getCP(), cube2.getEP(), cube2.getUD2()]
    d = 0
    while d <= maxLength - currentDepth:
        phase2(p, d, '')
        d += 1

def phase2(p, d, solution):
    if d == 0:
        if p == [0, 0, 0]:
            global maxLength
            currentDepth = len(solution) // 2 + p1Length
            if currentDepth < maxLength:
                print("2: ")
                for i in range(0, len(solution) // 2):
                    print(solution[i*2:i*2+2], end=' ')
                print()
                maxLength = currentDepth - 1
    elif d > 0:
        if max(t.cpPrune[p[0]], t.epPrune[p[1]], t.udPrune2[p[2]]) <= d:
            # Should filter out moves depending on last move
            lastMove = solution[-2:]
            for i, move in enumerate(constant.G1):
                if lastMove != '' and move[0] == lastMove[0]:
                    continue
                newP = [
                    t.cpMove[p[0]][i],
                    t.epMove[p[1]][i],
                    t.udMove2[p[2]][i]
                ]
                phase2(newP, d - 1, solution + move)

t = Table()

#cube = cubie.Cube()
#cube.scramble()

#####
imageDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images'))
pic1 = os.path.join(imageDir, 'r1.jpg')
pic2 = os.path.join(imageDir, 'r2.jpg')
bad = os.path.join(imageDir, 'bad.png')

cubeList = [[[None for i in range(3)] for j in range(3)] for k in range(6)]

reader.reader(cubeList, pic1)
reader.reader(cubeList, pic2)

facelet_cube = filter.filterCube(cubeList)
cube = rubikscube.to_cubie.toCubie(facelet_cube)
#####

cube.display()

p = [cube.getCO(), cube.getEO(), cube.getUD1()]

if __name__ == '__main__':
    print('Cube')

    #phase2start('R2')
    kociemba(p)
