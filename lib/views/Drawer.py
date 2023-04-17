
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
    
    def draw_entities(self, entities: list):
        for specimen in specimens:
            specimen: Specimen = specimen
            specimen.draw_self(screen, specimens_surface)
            
        for food in foods:
            food.draw_self(specimens_surface)
        screen.blit(specimens_surface, (0,0))
        
    def draw_specimens_
    
    def __draw_entity(self, entity: Entity, entities_surface: Surface, secondary_surface: Surface ):
        if isinstance(entity, Specimen):
            self.__draw_specimen(entity, entities_surface, secondary_surface)
        elif isinstance(entity, Food):
            self.__draw_food(entity, entities_surface)
            
    def __draw_specimen(self, specimen: Specimen, specimens_surface: Surface, sense_surface: Surface ):
        # Sentido
        pygame.draw.circle(sense_surface, (217,217,217), radius=specimen.get_sense(), center=specimen.get_pos_tuple()) 
        # Individuo
        pygame.draw.circle(specimens_surface, specimen.get_color(), radius=specimen.BODY_RADIUS, center=specimen.get_pos_tuple())
        
        angle_radians = radians(specimen.get_angle_degrees())
        point_x = cos(angle_radians)*specimen.get_sense() + specimen.get_pos_x()
        point_y = sin(angle_radians)*specimen.get_sense() + specimen.get_pos_y() 

        pygame.draw.line(sense_surface, (0,0,0), specimen.get_pos_tuple(), (point_x, point_y))
    
    def __draw_food(specimen, food: Food, specimens_surface: Surface):
        pygame.draw.circle(specimens_surface, (246,190,0), radius=food.body_radius, center=(food.get_pos_x(), food.get_pos_y())) 