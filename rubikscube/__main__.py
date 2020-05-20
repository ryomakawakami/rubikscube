import rubikscube.cube.cube as cube

if __name__ == '__main__':
    print("Cube")

    cube = cube.Cube()
    cube.handScramble("x R2 F R F' R U2 r' U r U2 x'")
    cube.display()
