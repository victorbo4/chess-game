import pygame
import sys
from const import *
from board import Board
from graphics import Graphics
from mouse_controller import MouseController


class ChessGame:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.board = Board()
        self.clock = pygame.time.Clock()
        self.running = True
        self.graphics = Graphics(self.board)
        self.mouse_controller = MouseController()
        pygame.display.set_caption("ChessGame")

    def event_handler(self):
        board = self.board
        mouse_controller = self.mouse_controller
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            # mouse events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col, row = mouse_x // SQ_SIZE, mouse_y // SQ_SIZE

                # if there is a piece
                if board.squares[row][col] is not None:
                    mouse_controller.selected_piece = board.squares[row][col]
                    mouse_controller.selected_pos = (row, col)
                    mouse_controller.initial_pos = event.pos
                    board.squares[row][col] = None

            elif event.type == pygame.MOUSEMOTION:
                if mouse_controller.selected_piece:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.graphics.draw_dragging_piece(self.screen, mouse_controller.selected_piece, mouse_x, mouse_y)

            # release
            elif event.type == pygame.MOUSEBUTTONUP:
                if mouse_controller.selected_piece:
                    mouse_x, mouse_y = event.pos
                    col, row = mouse_x // SQ_SIZE, mouse_y // SQ_SIZE

                    # update pos
                    board.squares[row][col] = mouse_controller.selected_piece
                    mouse_controller.selected_piece = None
                    mouse_controller.selected_pos = None

    def graphics_load(self):
        graphics = self.graphics
        screen = self.screen

        # draw background
        graphics.draw_bg(screen)
        graphics.draw_pieces(screen)

        # draw dragging piece
        if self.mouse_controller.selected_piece:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            graphics.draw_dragging_piece(screen, self.mouse_controller.selected_piece, mouse_x, mouse_y)

    def main_loop(self):
        while self.running:
            self.event_handler()
            self.graphics_load()
            pygame.display.update()
            self.clock.tick(60)
