import pygame
from .constants import BROWN, ROWS, BEIGE, SQUARE_SIZE, COLS, BLACK, RED
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
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

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)

        if row == ROWS or row==0:
            piece.make_king()
            if piece.colour == BLACK:
                self.black_kings +=1
            else:
                self.red_kings +=1

    def get_piece(self, row, col):
        return self.board[row][col]

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

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col-1
        right = piece.col+1
        row = piece.row

        if piece.colour == RED or piece.king:
            moves.update(self._traverse_left(row-1, max(row-3,-1),-1,piece.colour,left))
            moves.update(self._traverse_right(row-1, max(row-3,-1),-1,piece.colour,right))

        if piece.colour == BLACK or piece.king:
            moves.update(self._traverse_left(row+1, min(row-3, ROWS),1,piece.colour,left))
            moves.update(self._traverse_right(row+1, min(row-3, ROWS),1,piece.colour,right))

        return moves

    def _traverse_left(self, start, stop, step, colour, left, skipped = []):
        moves = {}
        last = []
        for r in range(start,stop,step):
            if left<0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,left)] = last + skipped

                else:
                    moves[(r,left)] = last

                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, colour, left-1, skipped = last))
                    moves.update(self._traverse_right(r+step, row, step, colour, left+1, skipped = last))
                break

            elif current.colour == colour:
                break
            else:
                last = [current]

            left -=1
        
        return moves

    def _traverse_right(self, start, stop, step, colour, right, skipped = []):
        moves = {}
        last = []
        for r in range(start,stop,step):
            if right>=COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped

                else:
                    moves[(r,right)] = last

                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, colour, right-1, skipped = last))
                    moves.update(self._traverse_right(r+step, row, step, colour, right+1, skipped = last))
                break

            elif current.colour == colour:
                break
            else:
                last = [current]

            right +=1

        return moves
