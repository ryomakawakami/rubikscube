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
