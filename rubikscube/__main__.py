import rubikscube.cubie_cube.cube as cubie
import rubikscube.move_table as move_table
import rubikscube.pruning_table as pruning_table

if __name__ == '__main__':
    print('Cube')

    coMove, eoMove, udMove1 = move_table.phase1()
    coPrune = pruning_table.generateCO(coMove)

    cube = cubie.Cube()

    cube.turn('R1')
    cube.turn('U1')
    cube.turn('R3')
    cube.turn('R1')
    print(cube.getCO())
    print(coPrune[cube.getCO()])
