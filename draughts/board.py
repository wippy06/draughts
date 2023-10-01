import pygame
from .constants import BROWN, ROWS, BEIGE, SQUARE_SIZE, COLS, BLACK, RED
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.black_left = self.red_left = 12
        self.black_kings = self.red_kings = 0

        #runs the create_board function on start up to set pieces
        self.create_board()

    def draw_squares(self,win):
        #background colour
        win.fill(BROWN)
        #adding Beige squares in checker board pattern
        for row in range (ROWS):
            #row%2 determines if first square is missed out or not
            for col in range (row % 2, ROWS, 2):
                pygame.draw.rect(win, BEIGE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        #adding pieces when first starting game into an array
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):

                #(row+1)%2 determines if pieces are placed in odd or even coloums and col%2 sees if col is odd or even
                if col %2 == (row+1)%2:

                    #adding black pieces to array if in the first 3 rows
                    if row<3:
                        self.board[row].append(Piece(row,col, BLACK))
                    
                    #adding red pieces to array if in the last 3 rows
                    elif row>4:
                        self.board[row].append(Piece(row,col, RED))
                    
                # else adds 0s to the array
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self,win):
        #draws squares and pieces
        self.draw_squares(win)
        #cycles through squares in the array to check if piece needs to be drawn
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    #piece is drawn if the space in the array is not 0
                    piece.draw(win)