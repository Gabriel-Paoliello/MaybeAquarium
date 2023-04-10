import random
from Consts import STEP_SIZE, SCR_WIDTH, SCR_HEIGHT
from pygame import Surface
import pygame
from math import sin, cos, radians

class Specie:
    def __init__(self, sense, speed, angle, age, pos) -> None:
        self.sense:int = sense
        self.speed:int = speed
        self.angle:int = angle
        self.age:int = age
        self.pos:tuple(int,int) = pos

    def get_pos_x(self) -> int:
        return self.pos[0]

    def get_pos_y(self) -> int:
        return self.pos[1]

    def get_sense(self) -> int:
        return self.sense
        
    def get_speed(self) -> int:
        return self.speed

    def get_angle(self) -> int:
        return self.angle

    def get_age(self) -> int:
        return self.age

    def set_angle(self, angle) -> None:
        self.angle = angle
        return None

    def walk(self) -> None:
        pass

    def draw_self(self, sense_surfice: Surface, species_surfice: Surface):
        pass

class SpecieWanderer(Specie):
    def __init__(self) -> None:
        super().__init__(
            sense = random.randint(1,3),
            speed = random.randint(1,3),
            angle = random.randint(0,359),
            age = 0,
            pos = (random.randint(20, SCR_WIDTH), random.randint(20, SCR_HEIGHT))
        )

    def walk(self):
        if (self.get_pos_y() >= SCR_HEIGHT or self.get_pos_y() <= 0 or
            self.get_pos_x() >= SCR_WIDTH or self.get_pos_x() <= 0):
            self.set_angle(self.get_angle() + 180)
        else:
            var_angle = random.randint(-5,5)
            self.set_angle(self.get_angle() + var_angle)

        angle_radians = radians(self.get_angle())
        step_x = cos(angle_radians)*self.get_speed()*STEP_SIZE
        step_y = sin(angle_radians)*self.get_speed()*STEP_SIZE
        self.pos = (self.get_pos_x() + step_x, self.get_pos_y() + step_y)
        

    def draw_self(self, sense_surfice: Surface, species_surfice: Surface):
        # Sentido
        pygame.draw.circle(sense_surfice, (217,217,217), radius=40*self.get_sense(), center=(self.get_pos_x(), self.get_pos_y())) 

        # Individuo
        pygame.draw.circle(species_surfice, (40*self.get_speed(), 40*self.get_sense(), 255-40*self.get_age()), radius=10, center=(self.get_pos_x(), self.get_pos_y()))

class SpecieFactory():
    def make_specie_list() -> list:
        # specie = random.choice({SpecieX.__class__, })
        individuos:list = []
        for x in range(0, 10):
            individuos.append(SpecieWanderer())
        return individuos
                