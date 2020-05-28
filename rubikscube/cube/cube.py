import rubikscube.cube.constant as constant

class Cube:
    def __init__(self):
        # (piece, orientation)
        self.corners = [(i, 0) for i in range(8)]
        self.edges = [(i, 0) for i in range(12)]

    def display(self):
        pass

    # moves is string of primitive moves
    # Returns their product
    def cornerMult(self, moves):
        prod = constant.MOVES_C[moves[-1]]
        temp = [None for i in range(8)]
        for i in reversed(range(0, len(moves) - 1)):
            for j, pair in enumerate(constant.MOVES_C[moves[i]]):
                ori = (prod[pair[0]][1] + pair[1]) % 3
                temp[j] = (prod[pair[0]][0], ori)
            prod = temp
        return prod

    def edgeMult(self, moves):
        prod = constant.MOVES_E[moves[-1]]
        temp = [None for i in range(12)]
        for i in reversed(range(0, len(moves) - 1)):
            for j, pair in enumerate(constant.MOVES_E[moves[i]]):
                ori = (prod[pair[0]][1] + pair[1])
                if ori == 2:
                    ori = 0
                temp[j] = (prod[pair[0]][0], ori)
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
