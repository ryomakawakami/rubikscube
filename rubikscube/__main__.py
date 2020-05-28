import rubikscube.cube.cube as cube

if __name__ == '__main__':
    print('Cube')

    cube = cube.Cube()

    cube.turn('R2')
    cube.turn('U1')
    cube.turn('R3')
    cube.turn('U1')
    cube.turn('R3')
    cube.turn('U3')
    cube.turn('R1')
    cube.turn('U3')
    cube.turn('R2')
    cube.turn('U3')
    cube.turn('D1')
    cube.turn('R3')
    cube.turn('U1')
    cube.turn('R1')
    cube.turn('D3')

    print(cube.corners)
    print(cube.edges)

    cube.display()
