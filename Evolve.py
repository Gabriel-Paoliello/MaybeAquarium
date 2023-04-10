

import time
import pygame
from Consts import SCR_HEIGHT, SCR_WIDTH, FPS
from Especies import Especie, EspecieFactory
from pygame import Surface

def main():
    # Import and initialize the pygame library
    pygame.init()
    # Set up the drawing window
    screen: Surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    

    individuos:list(Especie) = EspecieFactory.make_especie_list()
    # Run until the user asks to quit
    running = True

    while running:
        start_time = time.time()
        # Did the user click the window close button?
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False
        process(individuos)
        print_screen(screen, individuos)
        end_time = time.time()
        elapsed_time = end_time - start_time
        time.sleep(max(0,(1/FPS) - elapsed_time))


    # Done! Time to quit.
    pygame.quit()

def process(individuos:list):
    for individuo in individuos:
        individuo: Especie = individuo
        individuo.walk()

def print_screen(screen: Surface, individuos:list):
    
    species_surfice = pygame.Surface((SCR_WIDTH, SCR_HEIGHT),pygame.SRCALPHA, 32)
    species_surfice = species_surfice.convert_alpha()
    # Fill the background with white
    screen.fill((255, 255, 255))
    for individuo in individuos:
        individuo: Especie = individuo
        individuo.draw_self(screen, species_surfice)
        screen.blit(species_surfice, (0,0))
        #pygame.draw.circle(screen, (random.randint(0,255), random.randint(0,255), 255), radius=10, center=(individuo.get_pos_x(), individuo.get_pos_y()))

    
    # Flip the display
    pygame.display.flip()

main()