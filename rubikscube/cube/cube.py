import cubie_rep.cube.constant as constant

class Cube:
    def __init__(self):
        self.coords = [0, 0, 0]

    def display(self):
        pass

    def turn(self, s):
        self.corners = [(self.corners[i][0], (self.corners[i][1] + j) % 3) for i, j in constant.MOVES_C[s]]
        self.edges = [(self.edges[i][0], self.edges[i][1] ^ j) for i, j in constant.MOVES_E[s]]
