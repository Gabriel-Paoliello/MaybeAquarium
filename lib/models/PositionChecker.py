from math import atan2, degrees

class PositionChecker():
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