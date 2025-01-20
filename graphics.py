import pygame
from const import *
from board import Board


class Graphics:

    def __init__(self, board):
        self.board = board

    def draw_bg(self, surface):
        for row in range(SIZE):
            for col in range(SIZE):
                if (row + col) % 2 == 0:
                    color = LIGHTGREEN
                else:
                    color = DARKGREEN

                rect = (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                pygame.draw.rect(surface, color, rect)

    def draw_piece(self, surface, piece, row, col):
        img = pygame.transform.scale(pygame.image.load(f"images/{piece.color}-{piece.name}.png"),
                                           (SQ_SIZE, SQ_SIZE))
        surface.blit(img, (col * SQ_SIZE, row * SQ_SIZE))

    def draw_dragging_piece(self, surface, piece, x, y):
        img = img = pygame.transform.scale(pygame.image.load(f"images/{piece.color}-{piece.name}.png"),
                                           (SQ_SIZE+10, SQ_SIZE+10))
        img_center = (x, y)
        texture_rect = img.get_rect(center=img_center)
        surface.blit(img, texture_rect)

    def draw_pieces(self, surface):
        board = self.board
        for row in range(SIZE):
            for col in range(SIZE):
                if board.squares[row][col] is not None:
                    self.draw_piece(surface, board.squares[row][col], row, col)
                    # img = pygame.transform.scale(pygame.image.load(f"images/{board.squares[row][col].color}-{board.
                    #                                                squares[row][col].name}.png"), (SQ_SIZE, SQ_SIZE))
                    # surface.blit(img, (col * SQ_SIZE, row * SQ_SIZE))



