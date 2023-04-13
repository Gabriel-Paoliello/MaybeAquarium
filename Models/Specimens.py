import random
from Consts import STEP_SIZE, SCR_WIDTH, SCR_HEIGHT, MARGIN
from pygame import Surface
import pygame
from math import sin, cos, radians

from Models.Entity import Entity

class SpecimenFactory():
    __specimen_list: list = None

    def get_specimen_list() -> list:
        if SpecimenFactory.__specimen_list is None:
            SpecimenFactory.__specimen_list = SpecimenFactory.__make_specimen_list()
        return SpecimenFactory.__specimen_list

    def __make_specimen_list() -> list:
        specimens:list = []
        for _ in range(0, 12):
            specimens.append(WandererSpecimen())
            specimens.append(JumperSpecimen())
        return specimens

class Specimen(Entity):
    def __init__(self, 
            sense = None,
            speed = None,
            angle = None,
            age = None,
            pos = None,
        ) -> None:
        super().__init__()
        if sense is None:    
            sense = random.randint(1,3)
        if speed is None:    
            speed = random.randint(1,3)
        if angle is None:    
            angle = random.randint(0,359)
        if age is None:    
            age = 0

        self._sense:int = sense
        self._speed:int = speed
        self._angle:int = angle
        self._age:int = age
        
    def get_sense(self) -> int:
        return self._sense
        
    def get_speed(self) -> int:
        return self._speed

    def get_angle(self) -> int:
        return self._angle

    def get_age(self) -> int:
        return self._age

    def _set_angle(self, angle) -> None:
        self._angle = angle

    def walk(self) -> None:
        pass

    def draw_self(self, sense_surface: Surface, specimens_surface: Surface):
        pass


class WandererSpecimen(Specimen):
    def __init__(self) -> None:
        super().__init__()

    def walk(self) -> None:
        if (self.get_pos_y() >= SCR_HEIGHT - MARGIN or self.get_pos_y() <= MARGIN or
            self.get_pos_x() >= SCR_WIDTH - MARGIN or self.get_pos_x() <= MARGIN):
            self._set_angle(self.get_angle() + 180)
        else:
            var_angle = random.randint(-5,5)
            self._set_angle(self.get_angle() + var_angle)

        angle_radians = radians(self.get_angle())
        step_x = cos(angle_radians)*self.get_speed()*STEP_SIZE
        step_y = sin(angle_radians)*self.get_speed()*STEP_SIZE
        self._pos = (self.get_pos_x() + step_x, self.get_pos_y() + step_y)
        

    def draw_self(self, sense_surface: Surface, specimens_surface: Surface):
        # Sentido
        pygame.draw.circle(sense_surface, (217,217,217), radius=40*self.get_sense(), center=self.get_pos_tuple()) 
        # Individuo
        pygame.draw.circle(specimens_surface, (40*self.get_speed(), 40*self.get_sense(), 255-40*self.get_age()), radius=10, center=self.get_pos_tuple())
        
        angle_radians = radians(self.get_angle())
        point_x = cos(angle_radians)*40*self.get_sense() + self.get_pos_x()
        point_y = sin(angle_radians)*40*self.get_sense() + self.get_pos_y() 

        pygame.draw.line(sense_surface, (0,0,0), self.get_pos_tuple(), (point_x, point_y))

    def look_around(self, specimen_list: list):
        for specimen in specimen_list:
            if()
        

class JumperSpecimen(Specimen):
    def __init__(self) -> None:
        super().__init__(
            speed = 0,
        )
        self.max_speed = 7
        self.wait_ticks = random.randint(10,30)
        self.current_wait_ticks = 0

    def __set_max_speed(self):
        self._speed = self.max_speed

    def __decrease_speed(self):
        self._speed -= 0.25

    def walk(self):
        if self.current_wait_ticks > 0:
            self.current_wait_ticks -= 1
            return 
        if (self.get_pos_y() >= SCR_HEIGHT - MARGIN or self.get_pos_y() <= MARGIN or
            self.get_pos_x() >= SCR_WIDTH - MARGIN or self.get_pos_x() <= MARGIN):
            self._set_angle(self.get_angle() + 180)
        else:
            if self._speed <= 0:
                self.current_wait_ticks = self.wait_ticks
                new_jump_angle = random.randint(0,360)
                self.__set_max_speed()
                self._set_angle(new_jump_angle)
                return
        
            self.__decrease_speed()

        angle_radians = radians(self.get_angle())
        step_x = cos(angle_radians)*self.get_speed()*STEP_SIZE
        step_y = sin(angle_radians)*self.get_speed()*STEP_SIZE
        self._pos = (self.get_pos_x() + step_x, self.get_pos_y() + step_y)
        

    def draw_self(self, sense_surface: Surface, specimens_surface: Surface):
        # Sentido
        pygame.draw.circle(sense_surface, (217,217,217), radius=40*self.get_sense(), center=(self.get_pos_x(), self.get_pos_y())) 
        # Individuo
        pygame.draw.circle(specimens_surface, (40, 40*self.get_sense(), 255-40*self.get_age()), radius=10, center=(self.get_pos_x(), self.get_pos_y()))
        