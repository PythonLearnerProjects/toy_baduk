from enum import Enum

class Stone(Enum):
    BLACK = 1
    WHITE = 2
    EMPTY = 0

class Board:
    """
    This is a class to hold our game board object.
    It doesn't matter how it is implemented as long as 
    calling board.put_stone_at(1,1, Stone.BLACK) will later mean that
    board.get_stone_at(1,1) == Stone.BLACK
    """
    def __init__(self, width, height):
        """
        This is called an initialiser. If you need to do some setup when the 
        board is created with board = Board(), do it here.
        perhaps making something to store the stones in might be worthwhile?
        """
        pass
    def get_stone_at(self, x, y):
        return Stone.EMPTY
    def set_stone_at(self, x, y, stone):
        pass
    def _neighbors(self, x, y):
        """
        By convention, fields starting with _ are meant to be accessed only from inside the class.
        """
        pass
    def _count_liberties(self, x, y):
        pass
    def is_alive(self, x, y):
        pass