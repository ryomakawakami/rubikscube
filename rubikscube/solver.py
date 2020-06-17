from rubikscube.tables import Table
import rubikscube.cubie_cube.cube as cubie
import rubikscube.cubie_cube.constant as constant

import copy

class Solver:
    def __init__(self):
        self.table = Table()

    def kociemba(self, cube):
        self.cube = cube
        self.maxLength = 10000

        p = [self.cube.getCO(), self.cube.getEO(), self.cube.getUD1()]

        d = 0
        while d < self.maxLength:
            self.phase1(p, d, '')
            d += 1

    def phase1(self, p, d, solution):
        if d == 0:
            if p == [0, 0, 0]:
                if len(solution) == 0 or (solution[-2] in ['R', 'L', 'F', 'B'] and solution[-1] in ['1', '3']):
                    for i in range(0, len(solution) // 2):
                        print(solution[i*2:i*2+2], end=' ')
                    print()
                    self.p1Length = len(solution) // 2
                    self.phase2start(solution)
        elif d > 0:
            if max(self.table.coPrune[p[0]], self.table.eoPrune[p[1]], self.table.udPrune1[p[2]]) <= d:
                # Should filter out moves depending on last move
                lastMove = solution[-2:]
                for i, move in enumerate(constant.MOVES):
                    if lastMove != '' and move[0] == lastMove[0]:
                        continue
                    newP = [
                        self.table.coMove[p[0]][i],
                        self.table.eoMove[p[1]][i],
                        self.table.udMove1[p[2]][i]
                    ]
                    self.phase1(newP, d - 1, solution + move)

    def phase2start(self, solution):
        cube2 = cubie.Cube()
        cube2.corners = copy.copy(self.cube.corners)
        cube2.edges = copy.copy(self.cube.edges)
        for i in range(0, len(solution) // 2):
            cube2.turn(solution[i*2:i*2+2])
        p = [cube2.getCP(), cube2.getEP(), cube2.getUD2()]
        d = 0
        while d <= self.maxLength - self.p1Length:
            self.phase2(p, d, '')
            d += 1

    def phase2(self, p, d, solution):
        if self.p1Length + len(solution) // 2 > self.maxLength:
            return
        if d == 0:
            if p == [0, 0, 0]:
                currentDepth = self.p1Length + len(solution) // 2
                print("Current: " + str(currentDepth))
                if currentDepth < self.maxLength:
                    print("2: ")
                    for i in range(0, len(solution) // 2):
                        print(solution[i*2:i*2+2], end=' ')
                    print()
                    self.maxLength = currentDepth - 1
                    print(self.maxLength)
        elif d > 0:
            if max(self.table.cpPrune[p[0]], self.table.epPrune[p[1]], self.table.udPrune2[p[2]]) <= d:
                # Should filter out moves depending on last move
                lastMove = solution[-2:]
                for i, move in enumerate(constant.G1):
                    if lastMove != '' and move[0] == lastMove[0]:
                        continue
                    newP = [
                        self.table.cpMove[p[0]][i],
                        self.table.epMove[p[1]][i],
                        self.table.udMove2[p[2]][i]
                    ]
                    self.phase2(newP, d - 1, solution + move)
