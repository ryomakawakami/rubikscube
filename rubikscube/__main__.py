from rubikscube.cube.cube import Cube

if __name__ == '__main__':
    print("Cube")

    cube = Cube()

    cube.turn("R")
    cube.turn("U")
    cube.turn("R'")
    cube.turn("U'")
    cube.turn("x")
    cube.turn("y")
    cube.turn("z")
    cube.display()
