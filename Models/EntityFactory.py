from Models.Entity import Entity
from Models.Specimens import Specimen, JumperSpecimen, WandererSpecimen
from Models.Foods import Food

class EntityFactory():
    @staticmethod
    def build_specimen_list(size: int) -> list:
        specimens:list = []
        while len(specimens) < size:
            specimens.append(WandererSpecimen())
            specimens.append(JumperSpecimen())
        return specimens
    
    @staticmethod
    def build_food_list(size: int) -> list:
        food:list = []
        while len(food) < size:
            food.append(Food())
        return food
    
    @staticmethod
    def build_food() -> Food:
        return Food()