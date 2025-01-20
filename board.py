from const import *
from piece import *

import pygame


class Board:

    def __init__(self):
        self.squares = []
        self.create_squares()

    def create_squares(self):
        for i in range(SIZE):
            self.squares.append([])
            for j in range(SIZE):
                self.squares[i].append(None)

        row_pawn_w, row_other_w = (6, 7)
        row_pawn_b, row_other_b = (1, 0)

        # pawn
        for i in range(SIZE):
            self.squares[row_pawn_w][i] = Pawn([row_pawn_w, i], 'white')
            self.squares[row_pawn_b][i] = Pawn([row_pawn_b, i], 'black')

        # knight
        self.squares[row_other_w][1] = Knight([row_other_w, 1], 'knight', 'white', 3.0)
        self.squares[row_other_b][1] = Knight([row_other_b, 1], 'knight', 'black', 3.0)
        self.squares[row_other_w][6] = Knight([row_other_w, 6], 'knight', 'white', 3.0)
        self.squares[row_other_b][6] = Knight([row_other_b, 6], 'knight', 'black', 3.0)

        # rook
        self.squares[row_other_w][0] = Rook([row_other_w, 0], 'rook', 'white', 5.0)
        self.squares[row_other_b][0] = Rook([row_other_b, 0], 'rook', 'black', 5.0)
        self.squares[row_other_w][7] = Rook([row_other_w, 7], 'rook', 'white', 5.0)
        self.squares[row_other_b][7] = Rook([row_other_b, 7], 'rook', 'black', 5.0)

        # bishop
        self.squares[row_other_w][2] = Bishop([row_other_w, 2], 'bishop', 'white', 3.001)
        self.squares[row_other_b][2] = Bishop([row_other_b, 2], 'bishop', 'black', 3.001)
        self.squares[row_other_w][5] = Bishop([row_other_w, 5], 'bishop', 'white', 3.001)
        self.squares[row_other_b][5] = Bishop([row_other_b, 5], 'bishop', 'black', 3.001)

        # queen
        self.squares[row_other_w][3] = Queen([row_other_w, 3], 'queen', 'white', 9.0)
        self.squares[row_other_b][3] = Queen([row_other_b, 3], 'queen', 'black', 9.0)

        # king
        self.squares[row_other_w][4] = King([row_other_w, 4], 'king', 'white', 1000.0)
        self.squares[row_other_b][4] = King([row_other_b, 4], 'king', 'black', 1000.0)










