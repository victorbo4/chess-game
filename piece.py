from const import *


class Piece:

    def __init__(self, pos, name, color, value):
        self.pos = pos
        self.name = name
        self.color = color
        self.value = value


class Pawn(Piece):

    def __init__(self, pos, color):
        super().__init__(pos, 'pawn', color, 1.0)
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1


class Rook(Piece):

    def __init(self, pos, color):
        super().__init__(pos, 'rook', color, 5.0)


class Knight(Piece):

    def __init(self, pos, color):
        super().__init__(pos, 'knight', color, 3.0)


class Bishop(Piece):

    def __init(self, pos, color):
        super().__init__(pos, 'bishop', color, 3.001)


class Queen(Piece):

    def __init(self, pos, color):
        super().__init__(pos, 'queen', color, 9.0)


class King(Piece):

    def __init(self, pos, color):
        super().__init__(pos, 'king', color, 1000.0)