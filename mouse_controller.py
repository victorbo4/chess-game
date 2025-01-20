import pygame
from const import *


class MouseController:

    def __init__(self):
        self.selected_piece = None
        self.selected_pos = [0, 0]
        self.initial_pos = [0, 0]
        self.mouse_pos = [0, 0]

    def update_mouse_pos(self, pos):
        self.mouse_pos = pos

    def save_initial(self, pos):
        self.initial_pos = pos
