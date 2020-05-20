import rubikscube.cube.constant as constant
import string

class Cube:
    def __init__(self):
        self.facelets = ['' for i in range(54)]

        for i, color in enumerate(constant.COLORS):
            for j in range(9):
                self.facelets[9 * i + j] = color

    def display(self):
        u = ''
        for i in range(9):
            if i % 3 == 0:
                u += '\n      '
            u += self.facelets[i] + ' '
        m = ['', '', '']
        for i in [9, 18, 27, 36]:
            for j in range(i, i + 9):
                m[int((j - i) / 3)] += self.facelets[j] + ' '
        d = ''
        for i in range(45, 54):
            if i % 3 == 0:
                d += '      '
            d += self.facelets[i] + ' '
            if i % 3 == 2:
                d += '\n'
        print(u)
        for i in range(3):
            print(m[i])
        print(d)

    def turn(self, s):
        if len(s) == 1:
            temp = ['' for i in range(54)]
            for i, index in enumerate(constant.MOVES[s]):
                temp[index] = self.facelets[i]
            
            self.facelets = temp

        else:
            self.facelets = [self.facelets[i] for i in constant.MOVES[s[0]]]

    def handScramble(self, s):
        raw = s.strip().split(' ')
        moves = []

        for move in raw:
            if move.startswith(('U', 'L', 'F', 'R', 'B', 'D', 'M', 'S', 'E', 'x', 'y', 'z')):
                if len(move) == 1:
                    moves.append(move)          # U
                    continue
                if len(move) == 2:
                    if move[1] == "'":
                        moves.append(move)      # U'
                        continue
                    if move[1] == "2":
                        moves.append(move[0])   # U2
                        moves.append(move[0])
                        continue
                if len(move) == 3:
                    if move[1] == "2" and move[2] == "'":
                        moves.append(move[0])   # U2'
                        moves.append(move[0])
                        continue

            if move.startswith(('u', 'l', 'f', 'r', 'b', 'd')):
                t = constant.WIDE[move[0]]
                if len(move) == 1:
                    moves.append(t[0])              # u
                    moves.append(t[1])
                    continue
                if len(move) == 2:
                    if move[1] == "'":
                        moves.append(t[0] + "'")    # u'
                        moves.append(t[1] + "'")
                        continue
                    if move[1] == "2":
                        moves.append(t[0])          # u2
                        moves.append(t[1])
                        moves.append(t[0])
                        moves.append(t[1])
                        continue
                if len(move) == 3:
                    if move[1] == "2" and move[2] == "'":
                        moves.append(t[0])          # u2'
                        moves.append(t[1])
                        moves.append(t[0])
                        moves.append(t[1])
                        continue


            print("Error: " + move + " is invalid.")
            return

        for move in moves:
            self.turn(move)
                

            
