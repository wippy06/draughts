import pygame
from .constants import BLUE, SQUARE_SIZE
from .board import Board

class Game:
    def __init__(self,win):
        self.win = win
        self.selected = None
        self.board = Board()
        self.valid_moves = []

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def winner(self):
        return self.board.winner()

    def select(self,square,row,col):
        #if something is selected try to move unless selection is invalid
        if self.selected:
            result = self._move(square)
            if not result:
                self.selected=None
                self.select(square, row, col)
        
        piece = self.board.is_piece(row,col)

        if piece[0] and self.board.get_turn() == piece[1]:
            self.selected = square
            self.valid_moves = self.board.get_piece_valid_moves(square)
            return True
        
        return False

    def _move(self,square):
        move = self.board.get_move(square, self.valid_moves)
        if self.selected and move in self.valid_moves:
            self.board.move(move)
            self.board.moveCounter +=1
            self.valid_moves = []
        else:
            return False      
        return True

    def draw_valid_moves(self, moves):
        #draw from get legal moves function from chess
        if moves != None and moves != []:
            for move in moves:
                end_point = int(move.__repr__().split(">")[-1])
                row = (end_point-1)//4
                if row %2 ==0:
                    col = 2*(end_point-4*row-0.5)
                else:
                    col = 2*(end_point-4*row-1)
                pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def get_board(self):
        return self.board
    
    def ai_move(self,board):
        if self.board.board != board.board:
            self.board = board
            return True
        else:
            return False