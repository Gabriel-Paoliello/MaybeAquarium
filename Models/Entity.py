from random import randint
from Consts import MARGIN, SCR_HEIGHT, SCR_WIDTH

class Entity():
    BODY_RADIUS: int | None = None

    def __init__(self,
            pos = None,
        ) -> None:
        if pos is None:    
            pos = (randint(MARGIN, SCR_WIDTH - MARGIN), randint(MARGIN, SCR_HEIGHT - MARGIN))

        self._pos:tuple = pos
    def get_pos_x(self) -> int:
        return self._pos[0]

    def get_pos_y(self) -> int:
        return self._pos[1]

    def get_pos_tuple(self) -> tuple:
        return ( self.get_pos_x(), self.get_pos_y() )
    

