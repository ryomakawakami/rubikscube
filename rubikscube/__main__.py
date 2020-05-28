import rubikscube.cube.cube as cube

if __name__ == '__main__':
    print('Cube')

    cube = cube.Cube()
    #cube.turn('R1')
    #cube.turn('R2')
    cube.turn('F3')

    print(cube.corners)
    print(cube.edges)

    cube.display()
