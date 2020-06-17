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

        self.p1soln = []
        self.p2soln = []
        self.solutions = []

        p = [self.cube.getCO(), self.cube.getEO(), self.cube.getUD1()]

        d = 0
        while d < self.maxLength:
            self.phase1(p, d)
            d += 1

    def phase1(self, p, d):
        if len(self.p1soln) > self.maxLength:
            return

        if d == 0:
            if p == [0, 0, 0]:
                if len(self.p1soln) == 0 or (self.p1soln[-1][0] in ['R', 'L', 'F', 'B'] and self.p1soln[-1][1] in ['1', '3']):
                    for s in self.p1soln:
                        print(s, end=' ')
                    print()
                    self.p1Length = len(self.p1soln)
                    self.phase2start()
        elif d > 0:
            if max(self.table.coPrune[p[0]], self.table.eoPrune[p[1]], self.table.udPrune1[p[2]]) <= d:
                # Should filter out moves depending on last move
                lastMove = 'X'
                if len(self.p1soln) > 0:
                    lastMove = self.p1soln[-1]

                for i, move in enumerate(constant.MOVES):
                    if move[0] == lastMove[0]:
                        continue
                    newP = [
                        self.table.coMove[p[0]][i],
                        self.table.eoMove[p[1]][i],
                        self.table.udMove1[p[2]][i]
                    ]
                    self.p1soln.append(move)
                    self.phase1(newP, d - 1)
                    self.p1soln.pop()

    def phase2start(self):
        cube2 = cubie.Cube()
        cube2.corners = copy.copy(self.cube.corners)
        cube2.edges = copy.copy(self.cube.edges)
        for s in self.p1soln:
            cube2.turn(s)
        p = [cube2.getCP(), cube2.getEP(), cube2.getUD2()]
        d = 0

        self.p2soln = []

        n = len(self.solutions)
        while d <= self.maxLength - self.p1Length:
            self.phase2(p, d, n)
            d += 1

    def phase2(self, p, d, numSolutions):
        if numSolutions != len(self.solutions):
            return

        if self.p1Length + len(self.p2soln) > self.maxLength:
            return
        if d == 0:
            if p == [0, 0, 0]:
                currentDepth = self.p1Length + len(self.p2soln)

                self.maxLength = currentDepth - 1
                print(self.maxLength)

                self.solutions.append(self.p1soln + self.p2soln)

                print(self.solutions)
        elif d > 0:
            if max(self.table.cpPrune[p[0]], self.table.epPrune[p[1]], self.table.udPrune2[p[2]]) <= d:
                # Should filter out moves depending on last move
                lastMove = 'X'
                if len(self.p2soln) > 0:
                    lastMove = self.p2soln[-1]

                for i, move in enumerate(constant.G1):
                    if move[0] == lastMove[0]:
                        continue
                    newP = [
                        self.table.cpMove[p[0]][i],
                        self.table.epMove[p[1]][i],
                        self.table.udMove2[p[2]][i]
                    ]
                    self.p2soln.append(move)
                    self.phase2(newP, d - 1, numSolutions)
                    self.p2soln.pop()
