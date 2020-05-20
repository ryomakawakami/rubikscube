from rubikscube.cube.cube import Cube

if __name__ == '__main__':
    print("Cube")

    cube = Cube()

    cube.turn("R")
    cube.turn("U")
    cube.turn("R'")
    cube.turn("U'")
    cube.display()
