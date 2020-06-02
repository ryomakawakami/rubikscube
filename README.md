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

Phase 2 move tables only need to have G1 moves.

Something wrong with get UD 2. Adjust set UD edges so the order is set for UD2. Currently, 8,9,10,11 regardless.
