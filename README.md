# rubikscube

Run

```
python -m rubikscube
```

This project references http://kociemba.org/cube.htm.

The corner 0 is URF, 1 is UFL, and so on. Similarly for edges.

```
CORNERS = ('URF', 'UFL', 'ULB', 'UBR', 'DFR', 'DLF', 'DBL', 'DRB')
EDGES = ('UR', 'UF', 'UL', 'UB', 'DR', 'DF', 'DL', 'DB', 'FR', 'FL', 'BL', 'BR')
```

---

## Facelet Representation

For facelet representation, put your scramble in facelet_rep/main, and run

```
python -m facelet_rep
```

## Cubie Representation

For cubie representation, put your scramble in cubie_rep/main. R is 'R1', R2 is 'R2', R' is 'R3'. Then run

```
python -m cubie_rep
```

This implementation uses multiplication for a whole sequence of moves.

---

## Todo

Great test case (10 -> 4 -> 3)

```
cube = cubie.Cube()
cube.turn('L1')
cube.turn('R3')
cube.turn('F2')
```

Kociemba's implementation

Push move and then pop after recursive call. Have a list of solutions to add to when solution is found as well.

https://github.com/hkociemba/RubiksCube-TwophaseSolver/blob/0e77bf86791e6fae3d5dfa2ee2ecd6622ee11a7f/solver.py#L99