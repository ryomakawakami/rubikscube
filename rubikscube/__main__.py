import rubikscube.cubie_cube.cube as cubie

if __name__ == '__main__':
    print('Cube')

    cube = cubie.Cube()

    cube.turn('R1')
    print(cube.getCP(), cube.getEP())
