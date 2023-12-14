import random
from typing import TypeVar
from Consts import STEP_SIZE, SCR_WIDTH, SCR_HEIGHT, MARGIN
from pygame import Surface
import pygame
from math import sin, cos, degrees, radians, sqrt, atan2
from models.Foods import Food

from models.PositionChecker import PositionChecker

from models.Entity import Entity

EntityType = TypeVar('EntityType', bound=Entity)

class Specimen(Entity):
    __DEFAULT_BODY_RADIUS: int = int(STEP_SIZE * 10)

    def __init__(self, 
            sense = None,
            speed = None,
            angle = None,
            age = None,
            color = None,
        ) -> None:
        super().__init__()
        if sense is None:    
            sense = random.randint(40,120)
        if speed is None:    
            speed = random.randint(1,3)
        if angle is None:    
            angle = random.randint(0,359)
        if age is None:    
            age = 0
        if color is None:
            color = (255,0,0)

        self._sense:int = sense
        self._speed:float = speed
        self._angle_degress:int = angle
        self._age:int = age
        self._color:tuple = color
        self._body_radius: int = Specimen.__DEFAULT_BODY_RADIUS
        
    def get_body_radius(self) -> int:
        return self._body_radius
    
    def get_sense(self) -> int:
        return self._sense
        
    def get_speed(self) -> float:
        return self._speed

    def get_angle_degrees(self) -> int:
        return self._angle_degress

    def get_age(self) -> int:
        return self._age

    def get_color(self) -> tuple:
        return self._color

    def _set_angle_degrees(self, angle) -> None:
        self._angle_degress = angle % 360

    def _set_color(self, color) -> None:
        self._color = color

    def draw_self(self, sense_surface: Surface, specimens_surface: Surface):
        pass

    def is_in_border(self) -> bool:
        is_in_border_y = self.get_pos_y() >= SCR_HEIGHT - MARGIN or self.get_pos_y() <= MARGIN 
        is_in_border_x = self.get_pos_x() >= SCR_WIDTH - MARGIN or self.get_pos_x() <= MARGIN
        return is_in_border_y or is_in_border_x
    
    def act(self, specimens: list['Specimen'], foods: list[Food]) -> None:
        pass
    
    def _eat(self, food: Food):
        pass
    
    def _identify_close_entities(self, entities: list[EntityType]) -> tuple[list[EntityType], list[EntityType]]:
        entities_in_sense = []
        entities_in_reach = []
        for entity in entities:
            entity: Entity = entity
            if(self != entity):
                is_in_reach = PositionChecker.is_circles_colliding(
                                    self.get_pos_x(), self.get_pos_y(), self.get_body_radius(), 
                                    entity.get_pos_x(), entity.get_pos_y(), entity.get_body_radius() 
                                )
                if (is_in_reach):
                    entities_in_reach.append(entity)
                    entities_in_sense.append(entity)
                else:
                    is_in_sense = PositionChecker.is_circles_colliding(
                                        self.get_pos_x(), self.get_pos_y(), self.get_sense(), 
                                        entity.get_pos_x(), entity.get_pos_y(), entity.get_body_radius() 
                                    )
                    if(is_in_sense):
                        entities_in_sense.append(entity)
        return entities_in_reach, entities_in_sense

class WandererSpecimen(Specimen):
    def __init__(self) -> None:
        super().__init__()

    def get_body_radius(self) -> int:
        return int(super().get_body_radius()*1.5)

    # walks in a random direction or in a forced direction by the direction_degress arg
    def __walk(self, direction_degress: int) -> None:
        self._set_angle_degrees(direction_degress)
        angle_radians = radians(self.get_angle_degrees())
        step_x = cos(angle_radians)*self.get_speed()*STEP_SIZE
        step_y = sin(angle_radians)*self.get_speed()*STEP_SIZE
        self._pos = (self.get_pos_x() + step_x, self.get_pos_y() + step_y)

    def __choose_direction(self, specimens_in_sense: list[Specimen], foods_in_sense: list[Food]) -> int:
        if (self.is_in_border()):
            direction_degrees = self.get_angle_degrees() + 90
        else:
            maybe_direction_degrees: int | None = None
            var_angle = random.randint(-5,5)
            for specimen in specimens_in_sense:
                angle = PositionChecker.calculate_degrees_between_points(
                            self.get_pos_x(), self.get_pos_y(),
                            specimen.get_pos_x(), specimen.get_pos_y()
                        )
                
                #TODO add prioridade e seguir foods
                if(isinstance(specimen, type(self))):
                    maybe_direction_degrees = int(angle + var_angle + 180) #TODO lembrar de arrumar x y ou y x
                elif isinstance(specimen, JumperSpecimen):
                    maybe_direction_degrees = int(angle + var_angle)
                    break
                else:
                    maybe_direction_degrees = int(angle + var_angle)
            if maybe_direction_degrees == None:
                direction_degrees = self.get_angle_degrees() + var_angle
            else:
                direction_degrees = maybe_direction_degrees
                    
        self._set_angle_degrees(direction_degrees)
        return direction_degrees

    def __eat(self, food: Food):
        super()._eat(food)

    
    def __eat_list(self, foods: list[Food]):
        for food in foods:
            self._eat(food)

    def act(self, specimens: list[Specimen], foods: list[Food]) -> None:
        specimens_in_reach, specimens_in_sense = self._identify_close_entities(specimens)
        foods_in_reach, foods_in_sense = self._identify_close_entities(foods)
        
        if len(foods_in_reach) > 0:
            for food in foods_in_reach:
                self.__eat(food)
                foods_in_reach.remove(food)
                foods_in_sense.remove(food)
                foods.remove(food)
            
        elif len(specimens_in_reach) > 0:
            for entity in specimens_in_reach:
                continue # TODO implement procreation
                
        angle_decided = self.__choose_direction(specimens_in_sense, foods_in_sense)
        self.__walk(angle_decided)

    def draw_self(self, sense_surface: Surface, specimens_surface: Surface):
        # Sentido
        pygame.draw.circle(sense_surface, (217,217,217), radius=self.get_sense(), center=self.get_pos_tuple()) 
        # Individuo
        pygame.draw.circle(specimens_surface, self.get_color(), radius=self.get_body_radius(), center=self.get_pos_tuple())
        
        angle_radians = radians(self.get_angle_degrees())
        point_x = cos(angle_radians)*self.get_sense() + self.get_pos_x()
        point_y = sin(angle_radians)*self.get_sense() + self.get_pos_y()

        pygame.draw.line(sense_surface, (0,0,0), self.get_pos_tuple(), (point_x, point_y))

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

    def act(self, specimens: list[Specimen], foods: list[Food]) -> None:
        self.__walk()
        #self.__look_around(entities)

    def __walk(self):
        if self.current_wait_ticks > 0:
            self.current_wait_ticks -= 1
            return 
        if (self.get_pos_y() >= SCR_HEIGHT - MARGIN or self.get_pos_y() <= MARGIN or
            self.get_pos_x() >= SCR_WIDTH - MARGIN or self.get_pos_x() <= MARGIN):
            self._set_angle_degrees(self.get_angle_degrees() + 180)
        else:
            if self._speed <= 0:
                self.current_wait_ticks = self.wait_ticks
                new_jump_angle = random.randint(0,360)
                self.__set_max_speed()
                self._set_angle_degrees(new_jump_angle)
                return
        
            self.__decrease_speed()

        angle_radians = radians(self.get_angle_degrees())
        step_x = cos(angle_radians)*self.get_speed()*STEP_SIZE
        step_y = sin(angle_radians)*self.get_speed()*STEP_SIZE
        self._pos = (self.get_pos_x() + step_x, self.get_pos_y() + step_y)
        

    def draw_self(self, sense_surface: Surface, specimens_surface: Surface):
        # Sentido
        pygame.draw.circle(sense_surface, (217,217,217), radius=self.get_sense(), center=(self.get_pos_x(), self.get_pos_y())) 
        # Individuo
        pygame.draw.circle(specimens_surface, self.get_color(), radius=self.get_body_radius() , center=(self.get_pos_x(), self.get_pos_y()))