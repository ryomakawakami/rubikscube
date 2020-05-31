import rubikscube.cubie_cube.cube as cubie

if __name__ == '__main__':
    print('Cube')

    cube = cubie.Cube()

    #cube.turn('R1')
    #cube.display()

    cube.setUDEdges(0, 1, 2, 3)
    print(cube.getUD())

    cube.display()
