import pygame
from draughtsFolder.constants import WIDTH,HEIGHT, SQUARE_SIZE, PLAYER, AI, DEPTH, AI_ON, AI_VS_AI, LEARN
from draughtsFolder.game import Game
from minimax.algorithm import minimax
import time
import random

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

def playGame(weight0, weight1):
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    game.update()

    transposisitonTableWhite = {}
    transposisitonTableBlack = {}

    clock.tick(FPS)

    plyCount = 0

    while run:

        if game.board.get_turn() == AI and AI_ON and game.winner() == None:
            time_start = time.perf_counter()
            new_board = minimax(game.get_board(), DEPTH, weight0, True, float("-inf"), float("+inf"), transposisitonTableBlack, False)
            time_end = time.perf_counter()
            print(time_end-time_start)

            game.ai_move(new_board)
            game.update()

            plyCount+=1

        if game.board.get_turn() == PLAYER and AI_VS_AI and AI_ON and game.winner() == None:
            time_start = time.perf_counter()
            new_board = minimax(game.get_board(), DEPTH, weight1, False, float("-inf"), float("+inf"), transposisitonTableWhite, False)
            time_end = time.perf_counter()
            print(time_end - time_start)

            game.ai_move(new_board)
            game.update()  

            plyCount+=1   
        
        if game.winner()!=None:
            print(game.winner())
            print(game.board.board)
            print(game.board.board.pdn)
            run = False
            return [game.winner(), plyCount]

        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                print(game.valid_moves, game.board.evaluate(weight0), game.board.evaluate(weight1), game.winner(), game.board.board)

            #checks if game is shut down
            if event.type == pygame.QUIT:
                run = False
                return "end"
            
            #checks is mouse button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                square = get_square_from_row_col(row,col)
                game.select(square, row, col)
                game.update() 

    pygame.quit()

def main():
    run = True
    change = 2
    weight0 = []
    weight1 = []
    game_count = 0

    open('draughtsResults.txt', 'w').close()
    train_start = time.perf_counter()

    while run == True:
        file = open("draughtsResults.txt", "a")
        if change == 2:
            weight0 = [random.randint(1,100),random.randint(1,100)]
            weight1 = [random.randint(1,100),random.randint(1,100)]
        elif change == 1:
            weight1 = [random.randint(1,100),random.randint(1,100)]
        else:
            weight0 = [random.randint(1,100),random.randint(1,100)]

        time_start = time.perf_counter()
        result = playGame(weight0, weight1)
        time_end = time.perf_counter()
        time_diff = round(time_end-time_start) 

        if result=="end":
            train_end = time.perf_counter()
            train_time = round(train_end-train_start) 
            file.write("end.{}.{}".format(train_time, game_count))
            run = False
        elif result[0] == "black wins":
            game_count +=1
            change = 0
        elif result[0] == "white wins":
            game_count +=1
            change = 1
        else:
            game_count +=1
            change = 2

        if run ==True:
            resultString = "{}.{}.{}.{}.{}\n".format(result[0], weight0, weight1, time_diff, result[1])
            file.write(resultString)
        file.close()    
    print("end.{}.{}".format(train_time, game_count))       

if LEARN == True:
    main()
else:
    playGame([6,7,1], [6,7,1])