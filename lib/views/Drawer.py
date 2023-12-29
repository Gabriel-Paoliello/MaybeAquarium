
from math import cos, radians, sin
import pygame
from pygame import Surface
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
    
    def draw_entities_all(self, foods: list, specimens: list):
        entities_surface = pygame.Surface((SCR_WIDTH, SCR_HEIGHT),pygame.SRCALPHA, 32)
        entities_surface = entities_surface.convert_alpha()
        # Fill the background with white
        self.screen.fill((255, 255, 255))
        
        for specimen in specimens:
            specimen: Specimen = specimen
            self.__draw_specimen(specimen, entities_surface, self.screen)
            
        for food in foods:
            self.__draw_food(food, entities_surface)
            
        self.screen.blit(entities_surface, (0,0))
        
        # Flip the display
        pygame.display.flip()
        
    # def draw_entities(self, entities: list):
    #     entities_surface = pygame.Surface((SCR_WIDTH, SCR_HEIGHT),pygame.SRCALPHA, 32)
    #     entities_surface = entities_surface.convert_alpha()
    #     # Fill the background with white
    #     self.screen.fill((255, 255, 255))
        
    #     for entity in entities:
    #         self.__draw_entity(entity, entities_surface)
            
    #     self.screen.blit(entities_surface, (0,0))
        
    #     # Flip the display
    #     pygame.display.flip()
    
    # def __draw_entity(self, entity: Entity, entities_surface: Surface):
    #     if isinstance(entity, Specimen):
    #         self.__draw_specimen(entity, entities_surface, self.screen)
    #     elif isinstance(entity, Food):
    #         self.__draw_food(entity, entities_surface)
            
    def __draw_specimen(self, specimen: Specimen, specimens_surface: Surface, sense_surface: Surface ):
        # Sentido
        pygame.draw.circle(sense_surface, (217,217,217), radius=specimen.get_sense(), center=specimen.get_pos_tuple()) 
        # Individuo
        pygame.draw.circle(specimens_surface, specimen.get_color(), radius=specimen.get_body_radius(), center=specimen.get_pos_tuple())
        
        angle_radians = radians(specimen.get_angle_degrees())
        point_x = cos(angle_radians)*specimen.get_sense() + specimen.get_pos_x()
        point_y = sin(angle_radians)*specimen.get_sense() + specimen.get_pos_y() 

        pygame.draw.line(sense_surface, (0,0,0), specimen.get_pos_tuple(), (point_x, point_y))
    
    def __draw_food(self, food: Food, specimens_surface: Surface):
        pygame.draw.circle(specimens_surface, (246,190,0), radius=food.get_body_radius(), center=(food.get_pos_x(), food.get_pos_y())) 