from enum import Enum

class Stone(Enum):
    """
    Different options for things that can be on our board.
    """
    BLACK = 'X'
    WHITE = 'O'
    EMPTY = '.'
    def __str__(self):
        return self.value

class Board:
    """
    Stub of class to represent the game board.
    This will be fleshed out in exercise 2.
    """
    def get_stone_at(self, x, y):
        return Stone.EMPTY
    def get_stone_str_at(self, x, y):
        return str(self.get_stone_at(x, y))
    def put_stone_at(x, y, stone):
        pass
