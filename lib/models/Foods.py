from Consts import STEP_SIZE, SCR_WIDTH, SCR_HEIGHT
from pygame import Surface
import pygame
import random

class Food():
    body_radius = STEP_SIZE * 5
    __spawn_ticks = 100 
    def __init__(self) -> None:
        self._pos = (random.randint(20, SCR_WIDTH), random.randint(20, SCR_HEIGHT))
    
    @staticmethod
    def get_spawn_ticks() -> int:
        return Food.__spawn_ticks

    def get_pos_x(self) -> int:
        return self._pos[0]

    def get_pos_y(self) -> int:
        return self._pos[1]
    
    def draw_self(self, specimens_surface: Surface):
        pygame.draw.circle(specimens_surface, (246,190,0), radius=Food.body_radius, center=(self.get_pos_x(), self.get_pos_y())) 