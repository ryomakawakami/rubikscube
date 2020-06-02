import rubikscube.cubie_cube.constant as constant
from scipy.special import comb
import random

class Cube:
    def __init__(self):
        # (piece, orientation)
        self.corners = [[i, 0] for i in range(8)]
        self.edges = [[i, 0] for i in range(12)]

    ##################################################
    ####            Corner orientation            ####

    def getCO(self):
        c = 0
        for i in range(7):
            c = 3 * c + self.corners[i][1]
        return c

    def setCO(self, c):
        sum = 0

        # 6 to 0
        for i in range(6, -1, -1):
            digit = c % 3
            c //= 3
            self.corners[i][1] = digit
            sum += digit

        x = sum % 3
        if x == 1:
            x = 2
        elif x == 2:
            x = 1
        self.corners[7][1] = x

    ################################################
    ####            Edge orientation            ####

    def getEO(self):
        c = 0
        for i in range(11):
            c = 2 * c + self.edges[i][1]
        return c

    def setEO(self, c):
        sum = 0

        # 10 to 0
        for i in range(10, -1, -1):
            digit = c % 2
            c >>= 1
            self.edges[i][1] = digit
            sum += digit

        self.edges[11][1] = sum % 2

    ##########################################
    ####            UD slice 1            ####

    def getUD1(self):
        occupied = [False for i in range(12)]

        for i in range(12):
            # If edge is UD slice edge
            if self.edges[i][0] >= constant.FR:
                occupied[i] = True

        c = 0
        k = 3
        n = 11
        while k >= 0:
            if occupied[n]:
                k -= 1
            else:
                c += comb(n, k, exact=True)
            n -= 1

        return c

    # Given a clean cube, set UD edges to x, a list
    # Easiest way to implement setUD
    def setUDEdges(self, x):
        count1 = 0
        count2 = 8
        for i in range(12):
            if i in x:
                self.edges[i][0] = count2
                count2 += 1
            else:
                self.edges[i][0] = count1
                count1 += 1
    
    ##########################################
    ####            UD slice 2            ####

    def getUD2(self):
        arr = []
        for i in range(12):
            edge = self.edges[i][0]
            if edge >= constant.FR:
                arr.append(edge)

        x = 0
        for i in range(3, 0, -1):
            c = 0
            for j in range(i - 1, -1, -1):
                if arr[j] > arr[i]:
                    c += 1
            x = (x + c) * i

        return self.getUD1() * 24 + x
        #return x

    ##################################################
    ####            Corner permutation            ####

    def getCP(self):
        x = 0
        for i in range(7, 0, -1):   # 7 to 1
            c = 0
            for j in range(i - 1, -1, -1):  # i - 1 to 0
                if self.corners[j][0] > self.corners[i][0]:
                    c += 1
            x = (x + c) * i
        return x

    def setCP(self, corners):
        self.corners = [[corner, 0] for corner in corners]

    ################################################
    ####            Edge permutation            ####

    def getEP(self):
        x = 0
        for i in range(7, 0, -1):   # 7 to 1
            c = 0
            for j in range(i - 1, -1, -1):  # i - 1 to 0
                if self.edges[j][0] > self.edges[i][0]:
                    c += 1
            x = (x + c) * i
        return x

    def setEP(self, edges):
        for i, edge in enumerate(edges):
            self.edges[i][0] = edge

    ################################################

    def display(self):
        # 0 to 54, with order being WWW * 3 + OOO GGG RRR BBB * 3 + YYY * 3
        facelets = ['' for i in range(54)]

        # Centers
        facelets[4] = 'w'
        facelets[22] = 'o'
        facelets[25] = 'g'
        facelets[28] = 'r'
        facelets[31] = 'b'
        facelets[49] = 'y'

        colors_c = [None for i in range(8)]
        for i, pair in enumerate(self.corners):
            corner, ori = pair
            baseColors = constant.CORNER_COLOR[corner]
            if ori == 0:
                colors_c[i] = baseColors
            elif ori == 1:
                colors_c[i] = (baseColors[2], baseColors[0], baseColors[1])
            else:
                colors_c[i] = (baseColors[1], baseColors[2], baseColors[0])

        colors_e = [None for i in range(12)]
        for i, pair in enumerate(self.edges):
            edge, ori = pair
            baseColors = constant.EDGE_COLOR[edge]
            if ori == 0:
                colors_e[i] = baseColors
            elif ori == 1:
                colors_e[i] = (baseColors[1], baseColors[0])

        indices = ((8, 15, 14), (6, 12, 11), (0, 9, 20), (2, 18, 17),
            (47, 38, 39), (45, 35, 36), (51, 44, 33), (53, 41, 42))
        for i, colors in enumerate(colors_c):
            m, n, o = indices[i]
            facelets[m], facelets[n], facelets[o] = colors

        indices = ((5, 16), (7, 13), (3, 10), (1, 19),
            (50, 40), (46, 37), (48, 34), (52, 43),
            (26, 27), (24, 23), (32, 21), (30, 29))
        for i, colors in enumerate(colors_e):
            m, n = indices[i]
            facelets[m], facelets[n] = colors

        UR, UF, UL, UB, DR, DF, DL, DB, FR, FL, BL, BR = range(12)

        # Print
        for i in [0, 3, 6]:
            print('      ' + facelets[i] + ' ' + facelets[i + 1] + ' ' + facelets[i + 2])
        for i in [9, 21, 33]:
            s = ''
            for j in range(i, i + 12):
                s += facelets[j] + ' '
            print(s)
        for i in [45, 48, 51]:
            print('      ' + facelets[i] + ' ' + facelets[i + 1] + ' ' + facelets[i + 2])

    def turn(self, s):
        self.corners = [[self.corners[i][0], (self.corners[i][1] + j) % 3] for i, j in constant.MOVES_C[s]]
        self.edges = [[self.edges[i][0], self.edges[i][1] ^ j] for i, j in constant.MOVES_E[s]]

    def scramble(self):
        self.mixEven(self.corners)
        self.mixEven(self.edges)
        if random.randint(0, 1) == 1:
            self.corners[0], self.corners[1] = self.corners[1], self.corners[0]
            self.edges[0], self.edges[1] = self.edges[1], self.edges[0]

        sum = 0
        for i in range(7):
            x = random.randint(0, 2)
            self.corners[i][1] = x
            sum += x
        if sum % 3 == 0:
            self.corners[7][1] = 0
        elif sum % 3 == 1:
            self.corners[7][1] = 2
        else:
            self.corners[7][1] = 1
            
        sum = 0
        for i in range(11):
            x = random.randint(0, 1)
            self.edges[i][1] = x
            sum += x
        if sum % 2 == 0:
            self.edges[11][1] = 0
        else:
            self.edges[11][1] = 1

    def mixEven(self, x):
        N = len(x)
        for i in range(N - 3):
            r = random.randint(i, N - 1)
            if i != r:
                x[i], x[r] = x[r], x[i]
                x[N-1], x[N-2] = x[N-2], x[N-1]
