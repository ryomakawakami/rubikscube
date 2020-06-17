import rubikscube.cubie_cube.cube as cubie
import rubikscube.cubie_cube.constant as constant

from rubikscube.solver import Solver

import rubikscube.scanner.reader.reader as reader
import rubikscube.scanner.filter_cube as filter

import rubikscube.to_cubie

import sys
import os

s = Solver()

cube = cubie.Cube()
cube.scramble()

#####
#imageDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images'))
#pic1 = os.path.join(imageDir, 'r1.jpg')
#pic2 = os.path.join(imageDir, 'r2.jpg')
#bad = os.path.join(imageDir, 'bad.png')

#cubeList = [[[None for i in range(3)] for j in range(3)] for k in range(6)]

#reader.reader(cubeList, pic1)
#reader.reader(cubeList, pic2)

#facelet_cube = filter.filterCube(cubeList)
#cube = rubikscube.to_cubie.toCubie(facelet_cube)
#####

cube.display()

if __name__ == '__main__':
    print('Cube')

    cube = cubie.Cube()
    cube.turn('L1')
    cube.turn('R3')
    cube.turn('F2')
    
    s.kociemba(cube)
