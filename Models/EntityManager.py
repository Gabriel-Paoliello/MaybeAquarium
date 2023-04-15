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
    
class EntityCollider():
    @staticmethod
    def is_entity_colliding(entity1: Entity, entity2: Entity) -> bool:
        return EntityCollider.__is_circles_colliding( entity1.get_pos_x(), entity1.get_pos_y(), entity1.BODY_RADIUS,
                                                      entity2.get_pos_x(), entity2.get_pos_y(), entity2.BODY_RADIUS )

    @staticmethod
    def is_specimen_sensing(specimen: Specimen, entity: Entity) -> bool:
        return EntityCollider.__is_circles_colliding( specimen.get_pos_x(), specimen.get_pos_y(), specimen.get_sense(),
                                                      entity.get_pos_x(), entity.get_pos_y(), entity.BODY_RADIUS )
    @staticmethod
    def __is_circles_colliding(pos_x1, pos_y1, radius1, pos_x2, pos_y2, radius2) -> bool:
        diff_x = pos_x1 - pos_x2
        diff_y = pos_y1 - pos_y2
        distance_sqr = (diff_x ** 2) + (diff_y ** 2)
        return distance_sqr <= (radius1 + radius2)**2