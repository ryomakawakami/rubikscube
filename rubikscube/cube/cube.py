import rubikscube.cube.constant as constant

class Cube:
    def __init__(self):
        # (piece, orientation)
        self.corners = [(i, 0) for i in range(8)]
        self.edges = [(i, 0) for i in range(12)]

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

    # moves is string of primitive moves
    # Returns their product
    def cornerMult(self, moves):
        prod = constant.MOVES_C[moves[-1]]
        temp = [None for i in range(8)]
        for i in reversed(range(0, len(moves) - 1)):
            for j in range(8):
                c, o = prod[j]
                ori = (constant.MOVES_C[moves[i]][c][1] + o) % 3
                temp[j] = (constant.MOVES_C[moves[i]][c][0], ori)
            prod = temp
        return prod

    def edgeMult(self, moves):
        prod = [(i, j) for i, j, _ in constant.MOVES_E[moves[-1]]]
        temp = [None for i in range(12)]
        for i in reversed(range(0, len(moves) - 1)):
            for j in range(12):
                c, o = prod[j]
                ori = constant.MOVES_E[moves[i]][c][1] + o
                if ori == 2:
                    ori = 0
                temp[j] = (constant.MOVES_E[moves[i]][c][0], ori)
            prod = temp
        return prod

    def turn(self, s):
        if s[1] == '1':
            self.corners = [(self.corners[i][0], (self.corners[i][1] + j) % 3) for i, j in constant.MOVES_C[s[0]]]
            self.edges = [(self.edges[i][0], self.edges[i][1] ^ j) for i, j, k in constant.MOVES_E[s[0]]]

        elif s[1] == '2':
            cornerT = self.cornerMult(s[0] + s[0])
            self.corners = [(self.corners[i][0], (self.corners[i][1] + j) % 3) for i, j in cornerT]
            edgeT = self.edgeMult(s[0] + s[0])
            self.edges = [(self.edges[i][0], self.edges[i][1] ^ j) for i, j in edgeT]

        else:
            text = s[0] + s[0] + s[0]
            cornerT = self.cornerMult(text)
            self.corners = [(self.corners[i][0], (self.corners[i][1] + j) % 3) for i, j in cornerT]
            edgeT = self.edgeMult(text)
            self.edges = [(self.edges[i][0], self.edges[i][1] ^ j) for i, j in edgeT]

    def handScramble(self, s):
        pass
