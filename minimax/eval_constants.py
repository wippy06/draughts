MANVALUE = 8
KINGVALUE = 12

PIECESQUARETABLEBLACK = [
    [0,1,0,1,0,1,0,1],
    [2,0,2,0,2,0,2,0],
    [0,3,0,3,0,3,0,3],
    [4,0,4,0,4,0,4,0],
    [0,5,0,5,0,5,0,5],
    [6,0,6,0,6,0,6,0],
    [0,7,0,7,0,7,0,7],
    [8,0,8,0,8,0,8,0]
]

PIECESQUARETABLEWHITE = list(reversed(PIECESQUARETABLEBLACK))

PIECESQUARETABLEKINGS = [
    [0,8,0,8,0,8,0,8],
    [1,0,9,0,9,0,9,0],
    [0,9,0,10,0,10,0,1],
    [1,0,10,0,7,0,9,0],
    [0,9,0,7,0,10,0,1],
    [1,0,10,0,10,0,9,0],
    [0,9,0,9,0,9,0,1],
    [8,0,8,0,8,0,8,0]
]