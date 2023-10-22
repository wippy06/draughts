import pygame

#size constants
WIDTH, HEIGHT = 800,800

#must be even and >= 8
ROWS = COLS = 8
SQUARE_SIZE = WIDTH//COLS

#RGB colour constants
#Pieces
RED = (255, 0, 0)
BLACK = (0,0,0)
    #outline
GREY = (128,128,128)
    #potential movement
BLUE = (0,0,255)

#checker board
BEIGE = (252,227,173)
BROWN = (107, 34, 0)

CROWN = pygame.transform.scale(pygame.image.load("draughts/assets/crown.png"),(SQUARE_SIZE*0.28,SQUARE_SIZE*0.16))

#AI
AI_ON = True
AI_VS_AI = True
AI = RED
PLAYER = BLACK
DEPTH = 3
    #WEIGHT0 is AI, WEIGHT1 is AI which is playing for player
WEIGHT0 = [2,5,5]
WEIGHT1 = [6,7,1]

PIECESQUARETABLE = [
    [0,4,0,4,0,4,0,4],
    [4,0,3,0,3,0,3,0],
    [0,3,0,2,0,2,0,4],
    [4,0,2,0,1,0,3,0],
    [0,3,0,1,0,2,0,4],
    [4,0,2,0,2,0,3,0],
    [0,3,0,3,0,3,0,4],
    [4,0,4,0,4,0,4,0]
]