from Consts import STEP_SIZE, SCR_WIDTH, SCR_HEIGHT
from pygame import Surface
import pygame
import random

from models.Entity import Entity

class Food(Entity):
    __DEFAULT_BODY_RADIUS = int(STEP_SIZE * 5)
    __spawn_ticks = 100 
    def __init__(self) -> None:
        super().__init__()
    
    @staticmethod
    def get_spawn_ticks() -> int:
        return Food.__spawn_ticks

    def get_pos_x(self) -> int:
        return self._pos[0]

    def get_pos_y(self) -> int:
        return self._pos[1]
    
    def get_body_radius(self) -> int:
        return Food.__DEFAULT_BODY_RADIUS
    
    def draw_self(self, specimens_surface: Surface):
        pygame.draw.circle(specimens_surface, (246,190,0), radius=self.get_body_radius(), center=(self.get_pos_x(), self.get_pos_y())) 