from copy import deepcopy
from draughts.constants import PLAYER, AI

def minimax(position, depth, max_player):
    #position is an object
    #depth is an int to show how far to go
    #max_player checks if ai wants to maximise sore or minimise score

    if depth == 0 or position.winner(AI) != None or position.winner(PLAYER) != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float("-inf")
        best_move = None
        for move in get_all_moves(position, AI):
            evaluation = minimax(move, depth-1, False)[0]
            maxEval = max(maxEval,evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    
    else:
        minEval = float("inf")
        best_move = None
        for move in get_all_moves(position, PLAYER):
            evaluation = minimax(move, depth-1, True)[0]
            minEval = min(minEval,evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move

def simulate_move(piece, move, board, skip):
    board.move(piece, move[0],move[1])
    if skip:
        board.remove(skip)

    return board

def get_all_moves(board,colour):
    moves = []

    for piece in board.get_all_pieces(colour):
        valid_moves = board.get_valid_moves(piece)
        for move,skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)

    return moves
