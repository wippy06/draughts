import pygame
from draughtsFolder.constants import WIDTH,HEIGHT, SQUARE_SIZE, PLAYER, AI, DEPTH, AI_ON, AI_VS_AI, WEIGHT0, WEIGHT1
from draughtsFolder.game import Game
from minimax.algorithm import minimax
import time

FPS = 60

#set display size and capiton
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draughts")

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row,col

def get_square_from_row_col(row,col):
    square = -1
    if row%2 ==0:
        square = 4*row+col/2+.5
    else:
        square = 4*row+col/2+1
    if square % 1 == 0:
        return int(square)
    return square

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    game.update()

    transposisitonTableWhite = {}
    transposisitonTableBlack = {}

    clock.tick(FPS)

    while run:

        if game.board.get_turn() == AI and AI_ON and game.winner() == None:
            time_start = time.perf_counter()
            new_board = minimax(game.get_board(), DEPTH, WEIGHT0, True, float("-inf"), float("+inf"), transposisitonTableBlack)
            time_end = time.perf_counter()
            print(time_end-time_start)

            game.ai_move(new_board)
            game.update()

        if game.board.get_turn() == PLAYER and AI_VS_AI and AI_ON and game.winner() == None:
            time_start = time.perf_counter()
            new_board = minimax(game.get_board(), DEPTH, WEIGHT1, False, float("-inf"), float("+inf"), transposisitonTableWhite)
            time_end = time.perf_counter()
            print(time_end - time_start)

            game.ai_move(new_board)
            game.update()     
        
        if game.winner()!=None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            
            #checks if game is shut down
            if event.type == pygame.QUIT:
                run = False
            
            #checks is mouse button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                square = get_square_from_row_col(row,col)
                game.select(square, row, col)
                game.update() 

    pygame.quit()

#runs the main function
main()