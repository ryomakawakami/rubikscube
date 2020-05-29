import cubie_rep.cube.cube as cubie

if __name__ == '__main__':
    print('Cube')

    cube = cubie.Cube()

    cube.handScramble('R1 U1 R3 F3 R1 U1 R3 U3 R3 F1 R2 U3 R3')

    cube.display()
