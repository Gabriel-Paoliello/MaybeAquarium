from math import atan2, degrees

# class CollisionCircleDTO():
#     def __init__(self, pos_x: int, pos_y: int, radius: int) -> None:
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.radius = radius

class PositionChecker():
    # @staticmethod
    # def is_entity_colliding(entity1: Entity, entity2: Entity) -> bool:
    #     return CollisionChecker.__is_circles_colliding( entity1.get_pos_x(), entity1.get_pos_y(), entity1.BODY_RADIUS,
    #                                                   entity2.get_pos_x(), entity2.get_pos_y(), entity2.BODY_RADIUS )

    # @staticmethod
    # def is_specimen_sensing(specimen: Specimen, entity: Entity) -> bool:
    #     return EntityCollider.__is_circles_colliding( specimen.get_pos_x(), specimen.get_pos_y(), specimen.get_sense(),
    #                                                   entity.get_pos_x(), entity.get_pos_y(), entity.BODY_RADIUS )
    
    # @staticmethod
    # def is_circle_colliding(circle1: CollisionCircleDTO, circle2: CollisionCircleDTO) -> bool:
    #     return CollisionChecker.__is_circles_colliding( circle1.pos_x, circle1.pos_y, circle1.radius,
    #                                                   circle2.pos_x, circle2.pos_y, circle2.radius )
        
    @staticmethod
    def is_circles_colliding(pos_x1: int, pos_y1: int, radius1: int, pos_x2: int, pos_y2: int, radius2: int) -> bool:
        return PositionChecker.__is_circles_colliding( pos_x1, pos_y1, radius1,
                                                      pos_x2, pos_y2, radius2 )
        
    @staticmethod
    def __is_circles_colliding(pos_x1: int, pos_y1: int, radius1: int, pos_x2: int, pos_y2: int, radius2: int) -> bool:
        diff_x = pos_x1 - pos_x2
        diff_y = pos_y1 - pos_y2
        distance_sqr = (diff_x ** 2) + (diff_y ** 2)
        return distance_sqr <= (radius1 + radius2)**2
    
    @staticmethod
    def calculate_degrees_between_points(pos_x1: int, pos_y1: int, pos_x2: int, pos_y2: int):
        diff_x = pos_x1 - pos_x2
        diff_y = pos_y1 - pos_y2
        return degrees(atan2(diff_y, diff_x))