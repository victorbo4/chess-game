import pygame
import sys
from const import *
from board import Board
from graphics import Graphics


class ChessGame:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.board = Board()
        self.clock = pygame.time.Clock()
        self.running = True
        self.graphics = Graphics(self.board)
        pygame.display.set_caption("ChessGame")

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

    def graphics_load(self):
        graphics = self.graphics
        screen = self.screen

        # draw background
        graphics.draw_bg(screen)
        graphics.draw_pieces(screen)

    def main_loop(self):
        while self.running:
            self.event_handler()
            self.graphics_load()
            pygame.display.update()
            self.clock.tick(60)
