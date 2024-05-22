import pygame

#size constants
WIDTH, HEIGHT = 800,800

#must be even and >= 8
ROWS = COLS = 8
SQUARE_SIZE = WIDTH//COLS

#RGB colour constants
    #Pieces
RED = (255,255,255)
BLACK = (0, 0, 0)
    #outline
GREY = (128,128,128)
    #potential movement
BLUE = (0,200,0)
    #checker board
BEIGE = (252,227,173)
BROWN = (107, 34, 0)

CROWN = pygame.transform.scale(pygame.image.load("draughtsFolder/assets/crown.png"),(SQUARE_SIZE*0.28,SQUARE_SIZE*0.16))

#AI
AI_ON = True
AI_VS_AI = False

#True == RED, False == Blue
AI = False
PLAYER = True

DEPTH = 3
LEARN = False