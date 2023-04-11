import random
from Consts import STEP_SIZE, SCR_WIDTH, SCR_HEIGHT, MARGIN
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
            pos = (random.randint(MARGIN, SCR_WIDTH - MARGIN), random.randint(MARGIN, SCR_HEIGHT - MARGIN))
        )

    def walk(self) -> None:
        if (self.get_pos_y() >= SCR_HEIGHT - MARGIN or self.get_pos_y() <= MARGIN or
            self.get_pos_x() >= SCR_WIDTH - MARGIN or self.get_pos_x() <= MARGIN):
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

class SpecieJumper(Specie):
    def __init__(self) -> None:
        super().__init__(
            sense = random.randint(1,3),
            speed = 0,
            angle = random.randint(0,359),
            age = 0,
            pos = (random.randint(MARGIN, SCR_WIDTH - MARGIN), random.randint(MARGIN, SCR_HEIGHT - MARGIN))
        )
        self.max_speed = 7
        self.wait_ticks = random.randint(10,30)
        self.current_wait_ticks = 0

    def __set_max_speed(self):
        self.speed = self.max_speed

    def __decrease_speed(self):
        self.speed -= 0.25

    def walk(self):
        if self.current_wait_ticks > 0:
            self.current_wait_ticks -= 1
            return 
        if (self.get_pos_y() >= SCR_HEIGHT - MARGIN or self.get_pos_y() <= MARGIN or
            self.get_pos_x() >= SCR_WIDTH - MARGIN or self.get_pos_x() <= MARGIN):
            self.set_angle(self.get_angle() + 180)
        else:
            if self.speed <= 0:
                self.current_wait_ticks = self.wait_ticks
                new_jump_angle = random.randint(0,360)
                self.__set_max_speed()
                self.set_angle(new_jump_angle)
                return
        
            self.__decrease_speed()

        angle_radians = radians(self.get_angle())
        step_x = cos(angle_radians)*self.get_speed()*STEP_SIZE
        step_y = sin(angle_radians)*self.get_speed()*STEP_SIZE
        self.pos = (self.get_pos_x() + step_x, self.get_pos_y() + step_y)
        

    def draw_self(self, sense_surfice: Surface, species_surfice: Surface):
        # Sentido
        pygame.draw.circle(sense_surfice, (217,217,217), radius=40*self.get_sense(), center=(self.get_pos_x(), self.get_pos_y())) 

        # Individuo
        pygame.draw.circle(species_surfice, (40, 40*self.get_sense(), 255-40*self.get_age()), radius=10, center=(self.get_pos_x(), self.get_pos_y()))


class SpecieFactory():
    def make_specie_list() -> list:
        # specie = random.choice({SpecieX.__class__, })
        individuos:list = []
        for x in range(0, 12):
            individuos.append(SpecieWanderer())
            individuos.append(SpecieJumper())
        return individuos
                