import pygame
from draughts.constants import WIDTH,HEIGHT, SQUARE_SIZE
from draughts.board import Board

#WIDTH, HEIGHT = 800,800

FPS = 60

#set display size and capiton
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draughts")

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row,col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

 
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            
            #checks if game is shut down
            if event.type == pygame.QUIT:
                run = False
            
            #checks is mouse button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row,col)
                board.move(piece, 4,3)

        #draws the board        
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

#runs the main function
main()