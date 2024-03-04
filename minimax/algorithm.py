from copy import deepcopy
from draughtsFolder.constants import DEPTH

def minimax(position, depth, weight, maxPlayer, alpha, beta, transpositionTable):

    positionKey = hash(str(position.board))

    if positionKey in transpositionTable and depth != DEPTH:
        return transpositionTable[positionKey]

    if depth == 0 or position.winner() != None:
        return position

    bestPos = None

    if maxPlayer:
        bestEval = float("-inf")
        moves = get_all_moves(position)
        for move in moves:

            position.move(move)
            evaluation = minimax(position, depth-1, weight, False, alpha, beta, transpositionTable).evaluate(weight)
            bestEval = max(bestEval, evaluation)
            if bestEval == evaluation:
                bestPos = move
            position.unmove()

            alpha = max(alpha, bestEval)
            if beta <= alpha:
                #print("max")
                break

            
    else:
        bestEval = float("inf")
        moves = get_all_moves(position)
        for move in moves:

            position.move(move)
            evaluation = minimax(position, depth-1, weight, True, alpha, beta, transpositionTable).evaluate(weight)
            bestEval = min(bestEval, evaluation)
            if bestEval == evaluation:
                bestPos = move
            position.unmove()

            beta = min(beta, bestEval)
            if beta <= alpha:
                #print("min")
                break 

    position.move(bestPos)
    newPos = deepcopy(position)
    position.unmove()

    if depth != 1:
        transpositionTable[positionKey] = newPos
    
    return newPos

def get_all_moves(board):
    return board.get_all_valid_moves()
 