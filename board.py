from enum import Enum

class Stone(Enum):
    BLACK = 'X'
    WHITE = 'O'
    EMPTY = '.'
    def __str__(self):
        return self.value

class Board:
    def get_stone_at(self, x, y):
        return Stone.EMPTY
    def put_stone_at(x, y, stone):
        pass
