import pygame
import draughts
from .constants import CROWN, BROWN, ROWS, BEIGE, SQUARE_SIZE, COLS, BLACK, RED, GREY
from minimax.evaluate import evaluate

class Board:
    def __init__(self):
        self.board = draughts.get_board("american")
        self.board2D = self.convert_to_2d()
        self.pieceListWhite = ["w","W"]
        self.pieceListBlack = ["b","B"]
    
    def convert_to_2d(self):
        board_str = str(self.board).replace(" ","").replace("\n","")
        board_1D = [board_str[i:i+8] for i in range(0, len(board_str), 8)]
        board_2D = []
        for x in board_1D:
            board_2D.append([x[i:i+1] for i in range(0, len(x), 1)])
        return board_2D

    def draw_squares(self,win):
        #background colour
        win.fill(BROWN)
        #adding Beige squares in checker board pattern
        for row in range (8):
            #row%2 determines if first square is missed out or not
            for col in range (row % 2, 8, 2):
                pygame.draw.rect(win, BEIGE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, move):
        self.board.push(move)
        self.board2D = self.convert_to_2d()

    def unmove(self):
        self.board.pop()
        self.board2D = self.convert_to_2d()

    def get_all_pieces(self, colour):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece!= 0 and piece.colour == colour:
                    pieces.append(piece)
        return pieces    

    def draw(self,win):
        #draws squares and pieces
        self.draw_squares(win)

        radius = SQUARE_SIZE//2 - SQUARE_SIZE*0.15

        for row in range(ROWS):
            y = SQUARE_SIZE*row + SQUARE_SIZE//2

            for col in range(COLS):
                x = SQUARE_SIZE*col + SQUARE_SIZE//2

                if self.board2D[row][col] == "b" or self.board2D[row][col] == "B":
                    pygame.draw.circle(win, GREY, (x, y), radius+SQUARE_SIZE*0.02)
                    pygame.draw.circle(win, BLACK, (x, y), radius)

                elif self.board2D[row][col] == "w" or self.board2D[row][col] == "W":
                    pygame.draw.circle(win, GREY, (x, y), radius+SQUARE_SIZE*0.02)
                    pygame.draw.circle(win, RED, (x, y), radius)

                if self.board2D[row][col].isupper():
                    win.blit(CROWN, (x-CROWN.get_width()//2, y-CROWN.get_height()//2))

    def winner(self):
        if self.board.game_over:
            if self.board.result != "1-0":
                return "white wins"
            elif self.board.result != "0-1":
                return "black wins"
            else:
                return "draw"
        return None
        
    def get_all_valid_moves(self):
        capture_moves = []
        normal_moves = []
        for x in self.board.legal_moves:
            if self.board.is_capture(x) == True:
                capture_moves.append(x)
                continue
            normal_moves.append(x)

        if capture_moves!=[]:
            for i in capture_moves:
                for x in capture_moves:
                    if i.__repr__() in x.__repr__() and i.__repr__()!=x.__repr__():
                        capture_moves.remove(i)
                        break
            return capture_moves 
        return normal_moves
    
    def get_piece_valid_moves(self, square):
        #only takes co-ordinate for square
        allMoves = self.get_all_valid_moves()
        moves = []
        for x in allMoves:
            if str(square) == x.__repr__().split("-")[0].split(" ")[-1]:
                moves.append(x)
        return moves
    
    def get_numPieces(self, type):
        list_of_cords = []
        for row in range(8):
            for col in range(8):
                if self.board2D[row][col] == type:
                    list_of_cords.append([row,col])
        return list_of_cords

    def is_piece(self, row,col):
        isPiece = False
        colour = False
        if self.board2D[row][col] != ".":
            isPiece = True
            if self.board2D[row][col] == "b" or self.board2D[row][col] == "B":
                colour = False
            else:
                colour = True

        #returns if there is a piece and what colour that piece is
        return [isPiece, colour]

    def get_turn(self):
        #true is white
        #false is black
        if str(self.board.turn) == "Color.WHITE":
            return True
        return False
    
    def get_move(self, square, valid_moves):
        #only takes co-ordinate for square
        move = None
        for x in valid_moves:
            if str(square) == x.__repr__().split(">")[-1]:
                move = x
                break
        return move
    
    def evaluate(self, weight):
        return evaluate(weight, self)
            