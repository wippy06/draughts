import pygame

#size constants
WIDTH, HEIGHT = 800,800

#must be even and >= 8
ROWS = COLS = 8
SQUARE_SIZE = WIDTH//COLS

#RGB colour constants
    #Pieces
RED = (255, 0, 0)
BLACK = (0,0,170)
    #outline
GREY = (0,0,0)
    #potential movement
BLUE = (0,200,0)
    #checker board
BEIGE = (252,227,173)
BROWN = (107, 34, 0)

CROWN = pygame.transform.scale(pygame.image.load("draughts/assets/crown.png"),(SQUARE_SIZE*0.28,SQUARE_SIZE*0.16))

#AI
AI_ON = False
AI_VS_AI = False
AI = BLACK
PLAYER = RED
DEPTH = 3
    #WEIGHT0 is AI, WEIGHT1 is AI which is playing for player
WEIGHT0 = [6,7,1]
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