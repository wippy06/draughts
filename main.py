import pygame
from draughts.constants import WIDTH,HEIGHT
from draughts.board import Board

#WIDTH, HEIGHT = 800,800

FPS = 60

#set display size and capiton
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draughts")

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
                pass
                
        board.draw_squares(WIN)
        pygame.display.update()

    pygame.quit()

main()