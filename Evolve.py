import time
import pygame
from Consts import SCR_HEIGHT, SCR_WIDTH, FPS
from Models.Specimens import Specimen, SpecimenFactory
from Models.Foods import Food, FoodFactory
from pygame import Surface

def main():
    # Import and initialize the pygame library
    pygame.init()
    # Set up the drawing window
    screen: Surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    
    specimens:list(Specimen) = SpecimenFactory.get_specimen_list()
    foods:list(Food) = FoodFactory.make_food_list()
    ticks = 0
    # Run until the user asks to quit
    running = True

    while running:
        if(ticks < Food.get_spawn_ticks()):
            ticks += 1
        else:
            ticks = 0
            foods.append(Food())
        start_time = time.time()
        # Did the user click the window close button?
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False
        process(specimens)
        print_screen(screen, specimens, foods)
        end_time = time.time()
        elapsed_time = end_time - start_time
        time.sleep(max(0,(1/FPS) - elapsed_time))


    # Done! Time to quit.
    pygame.quit()

def process(specimens:list):
    for specimen in specimens:
        specimen: Specimen = specimen
        specimen.walk()

def print_screen(screen: Surface, specimens:list, foods:list):
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
    #pygame.draw.circle(screen, (random.randint(0,255), random.randint(0,255), 255), radius=10, center=(specimen.get_pos_x(), specimen.get_pos_y()))
    
    # Flip the display
    pygame.display.flip()

main()