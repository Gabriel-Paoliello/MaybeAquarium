
import pygame
from models.Entity import Entity
from models.Specimens import Specimen
from models.Foods import Food
from Consts import SCR_WIDTH, SCR_HEIGHT

class Drawer():
    def __init__(self, ) -> None:
        # Initialize the pygame library
        pygame.init()
        # Set up the drawing window
        self.screen: pygame.Surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    
    def draw_entity(self, entity: Entity):
        if isinstance(entity, Specimen):
            self.__draw_specimen(entity)
        elif isinstance(entity, Food):
            self.__draw_food(entity)
            
    def __draw_specimen(self, specimen: Specimen):
        pass
    
    def __draw_food(self, food: Food):
        pass