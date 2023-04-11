from Consts import STEP_SIZE, SCR_WIDTH, SCR_HEIGHT, MARGIN
from pygame import Surface
import pygame
import random

class Food():
    __spawn_ticks = 100 
    def __init__(self) -> None:
        self._pos = (random.randint(20, SCR_WIDTH), random.randint(20, SCR_HEIGHT))
    
    def get_spawn_ticks():
        return Food.__spawn_ticks

    def get_pos_x(self) -> int:
        return self._pos[0]

    def get_pos_y(self) -> int:
        return self._pos[1]
    
    def draw_self(self, species_surface: Surface):
        pygame.draw.circle(species_surface, (246,190,0), radius=6, center=(self.get_pos_x(), self.get_pos_y())) 

class FoodFactory():
    def make_food_list() -> list:
        food:list = []
        for _ in range(0, 10):
            food.append(Food())
        return food