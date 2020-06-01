import rubikscube.cubie_cube.cube as cubie
import rubikscube.move_table as move_table
import rubikscube.pruning_table as pruning_table

if __name__ == '__main__':
    print('Cube')

    #coMove, eoMove, udMove1 = move_table.phase1()
    #coPrune = pruning_table.generate(coMove)
    #eoPrune = pruning_table.generate(eoMove)
    #udPrune1 = pruning_table.generate(udMove1)

    cube = cubie.Cube()

    cube.scramble()
    cube.display()
