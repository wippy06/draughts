from .eval_constants import *

def evaluate(weight, board):
    if board.winner() == "white wins":
        return(float("-inf"))
    elif board.winner() == "black wins":
        return(float("inf"))
    elif board.winner() == "draw":
        return 0
    
    pieceSquareTable = 0        
    pieceValue = 0

    for x in board.pieceListBlack:
        pieceSquareTable += piece_square_table(board,x)
        pieceValue += piece_value(board,x)

    for x in board.pieceListWhite:
        pieceSquareTable -= piece_square_table(board,x)
        pieceValue -= piece_value(board,x)

    return pieceValue*weight[0] + pieceSquareTable*weight[1]

def piece_square_table(board, type):

    pieces = board.get_numPieces(type)
    
    value = 0
    if type == "W" or type == "B":
        for x in pieces:
            value += PIECESQUARETABLEKINGS[x[0]][x[1]]
    else:
        if type == "w":
            for x in pieces:
                value += PIECESQUARETABLEBLACK[x[0]][x[1]]
        else:
            for x in pieces:
                value += PIECESQUARETABLEWHITE[x[0]][x[1]]


    return value

def piece_value(board, type):
    pieces = board.get_numPieces(type)

    if type == "w" or "b":
        type =  MANVALUE
    else:
        type =  KINGVALUE
    
    return int(len(pieces)*type)