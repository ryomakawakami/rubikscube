# Order of corners and edges
URF, UFL, ULB, UBR, DFR, DLF, DBL, DRB = range(8)
UR, UF, UL, UB, DR, DF, DL, DB, FR, FL, BL, BR = range(12)

FACE_MOVE = ('U', 'R', 'F', 'D', 'L', 'B')

# "Replaced by" representation (e.g. In U, URF is replaced by UBR with orientation 0)
# (corner piece, orientation)
MOVES_C = {
    'U1': ((3, 0), (0, 0), (1, 0), (2, 0), (4, 0), (5, 0), (6, 0), (7, 0)),
    'U2': ((2, 0), (3, 0), (0, 0), (1, 0), (4, 0), (5, 0), (6, 0), (7, 0)),
    'U3': ((1, 0), (2, 0), (3, 0), (0, 0), (4, 0), (5, 0), (6, 0), (7, 0)),
    'R1': ((4, 2), (1, 0), (2, 0), (0, 1), (7, 1), (5, 0), (6, 0), (3, 2)),
    'R2': ((7, 0), (1, 0), (2, 0), (4, 0), (3, 0), (5, 0), (6, 0), (0, 0)),
    'R3': ((3, 2), (1, 0), (2, 0), (7, 1), (0, 1), (5, 0), (6, 0), (4, 2)),
    'F1': ((1, 1), (5, 2), (2, 0), (3, 0), (0, 2), (4, 1), (6, 0), (7, 0)),
    'F2': ((5, 0), (4, 0), (2, 0), (3, 0), (1, 0), (0, 0), (6, 0), (7, 0)),
    'F3': ((4, 1), (0, 2), (2, 0), (3, 0), (5, 2), (1, 1), (6, 0), (7, 0)),
    'D1': ((0, 0), (1, 0), (2, 0), (3, 0), (5, 0), (6, 0), (7, 0), (4, 0)),
    'D2': ((0, 0), (1, 0), (2, 0), (3, 0), (6, 0), (7, 0), (4, 0), (5, 0)),
    'D3': ((0, 0), (1, 0), (2, 0), (3, 0), (7, 0), (4, 0), (5, 0), (6, 0)),
    'L1': ((0, 0), (2, 1), (6, 2), (3, 0), (4, 0), (1, 2), (5, 1), (7, 0)),
    'L2': ((0, 0), (6, 0), (5, 0), (3, 0), (4, 0), (2, 0), (1, 0), (7, 0)),
    'L3': ((0, 0), (5, 1), (1, 2), (3, 0), (4, 0), (6, 2), (2, 1), (7, 0)),
    'B1': ((0, 0), (1, 0), (3, 1), (7, 2), (4, 0), (5, 0), (2, 2), (6, 1)),
    'B2': ((0, 0), (1, 0), (7, 0), (6, 0), (4, 0), (5, 0), (3, 0), (2, 0)),
    'B3': ((0, 0), (1, 0), (6, 1), (2, 2), (4, 0), (5, 0), (7, 2), (3, 1))
}

# Still "replaced by"
# (edge piece, orientation)
MOVES_E = {
    'U1': ((3, 0), (0, 0), (1, 0), (2, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0)),
    'U2': ((2, 0), (3, 0), (0, 0), (1, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0)),
    'U3': ((1, 0), (2, 0), (3, 0), (0, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0)),
    'R1': ((8, 0), (1, 0), (2, 0), (3, 0), (11, 0), (5, 0), (6, 0), (7, 0), (4, 0), (9, 0), (10, 0), (0, 0)),
    'R2': ((4, 0), (1, 0), (2, 0), (3, 0), (0, 0), (5, 0), (6, 0), (7, 0), (11, 0), (9, 0), (10, 0), (8, 0)),
    'R3': ((11, 0), (1, 0), (2, 0), (3, 0), (8, 0), (5, 0), (6, 0), (7, 0), (0, 0), (9, 0), (10, 0), (4, 0)),
    'F1': ((0, 0), (9, 1), (2, 0), (3, 0), (4, 0), (8, 1), (6, 0), (7, 0), (1, 1), (5, 1), (10, 0), (11, 0)),
    'F2': ((0, 0), (5, 0), (2, 0), (3, 0), (4, 0), (1, 0), (6, 0), (7, 0), (9, 0), (8, 0), (10, 0), (11, 0)),
    'F3': ((0, 0), (8, 1), (2, 0), (3, 0), (4, 0), (9, 1), (6, 0), (7, 0), (5, 1), (1, 1), (10, 0), (11, 0)),
    'D1': ((0, 0), (1, 0), (2, 0), (3, 0), (5, 0), (6, 0), (7, 0), (4, 0), (8, 0), (9, 0), (10, 0), (11, 0)),
    'D2': ((0, 0), (1, 0), (2, 0), (3, 0), (6, 0), (7, 0), (4, 0), (5, 0), (8, 0), (9, 0), (10, 0), (11, 0)),
    'D3': ((0, 0), (1, 0), (2, 0), (3, 0), (7, 0), (4, 0), (5, 0), (6, 0), (8, 0), (9, 0), (10, 0), (11, 0)),
    'L1': ((0, 0), (1, 0), (10, 0), (3, 0), (4, 0), (5, 0), (9, 0), (7, 0), (8, 0), (2, 0), (6, 0), (11, 0)),
    'L2': ((0, 0), (1, 0), (6, 0), (3, 0), (4, 0), (5, 0), (2, 0), (7, 0), (8, 0), (10, 0), (9, 0), (11, 0)),
    'L3': ((0, 0), (1, 0), (9, 0), (3, 0), (4, 0), (5, 0), (10, 0), (7, 0), (8, 0), (6, 0), (2, 0), (11, 0)),
    'B1': ((0, 0), (1, 0), (2, 0), (11, 1), (4, 0), (5, 0), (6, 0), (10, 1), (8, 0), (9, 0), (3, 1), (7, 1)),
    'B2': ((0, 0), (1, 0), (2, 0), (7, 0), (4, 0), (5, 0), (6, 0), (3, 0), (8, 0), (9, 0), (11, 0), (10, 0)),
    'B3': ((0, 0), (1, 0), (2, 0), (10, 1), (4, 0), (5, 0), (6, 0), (11, 1), (8, 0), (9, 0), (7, 1), (3, 1))
}

# Colors in orientation 0 with reference facelet first (and cw order for corners)
CORNER_COLOR = {
    URF: ('w', 'r', 'g'),
    UFL: ('w', 'g', 'o'),
    ULB: ('w', 'o', 'b'),
    UBR: ('w', 'b', 'r'),
    DFR: ('y', 'g', 'r'),
    DLF: ('y', 'o', 'g'),
    DBL: ('y', 'b', 'o'),
    DRB: ('y', 'r', 'b')
}

EDGE_COLOR = {
    UR: ('w', 'r'),
    UF: ('w', 'g'),
    UL: ('w', 'o'),
    UB: ('w', 'b'),
    DR: ('y', 'r'),
    DF: ('y', 'g'),
    DL: ('y', 'o'),
    DB: ('y', 'b'),
    FR: ('g', 'r'),
    FL: ('g', 'o'),
    BL: ('b', 'o'),
    BR: ('b', 'r')
}
