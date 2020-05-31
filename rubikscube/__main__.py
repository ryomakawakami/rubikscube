import rubikscube.cubie_cube.cube as cubie

if __name__ == '__main__':
    print('Cube')

    cube = cubie.Cube()

    #cube.turn('R1')
    #cube.display()

    #cube.setCO(1494)
    #print(cube.getCO())

    cube.setEO(2047)
    print(cube.getEO())

    cube.display()
