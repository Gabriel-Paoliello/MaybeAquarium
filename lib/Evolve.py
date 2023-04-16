from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # removes hello from pygame

import time
from Consts import SCR_HEIGHT, SCR_WIDTH, FPS
from models.Entity import Entity
from models.Specimens import Specimen
from models.EntityFactory import EntityFactory
from models.Foods import Food
import pygame
from pygame import Surface


class FPSManager():
    def __init__(self, frames_per_second: int) -> None:
        self.__fps = frames_per_second
        self.__frames_since_start = 0
        
    def start_frame(self) -> None:
        self.start_time = time.time()
        self.__frames_since_start += 1
        
    def end_frame(self) -> None:
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        time.sleep(max(0,(1/self.__fps) - elapsed_time))
        
    def get_frames_since_start(self) -> int:
        return self.__frames_since_start
    
def run():
    # Initialize the pygame library
    pygame.init()
    # Set up the drawing window
    screen: Surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    
    specimens:list = EntityFactory.build_specimen_list(20)
    foods:list = EntityFactory.build_food_list(10)
    # Run until the user asks to quit
    running = True
    fps_manager = FPSManager(FPS)
    while running:
        fps_manager.start_frame()
        running = not did_click_close_button()
        process_foods(foods, fps_manager.get_frames_since_start())
        process_specimens(specimens)
        display_screen(screen, specimens, foods)
        fps_manager.end_frame()
    pygame.quit()

def process_foods(foods: list, current_frame_count: int):
    if(current_frame_count%Food.get_spawn_ticks() == 0):
        foods.append(EntityFactory.build_food())

def did_click_close_button():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

def process_specimens(entities:list):
    for entity in entities:
        specimen: Specimen = entity
        specimen.act(entities)

def display_screen(screen: Surface, specimens:list, foods:list):
    specimens_surface = pygame.Surface((SCR_WIDTH, SCR_HEIGHT),pygame.SRCALPHA, 32)
    specimens_surface = specimens_surface.convert_alpha()
    # Fill the background with white
    screen.fill((255, 255, 255))
    for specimen in specimens:
        specimen: Specimen = specimen
        specimen.draw_self(screen, specimens_surface)
    for food in foods:
        food.draw_self(specimens_surface)
    screen.blit(specimens_surface, (0,0))
    
    # Flip the display
    pygame.display.flip()