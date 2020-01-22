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
        self.board_stone = list()
        for x in range(width):
            self.board_stone.append([])
            for y in range(height):
                self.board_stone[x].append(Stone.EMPTY)
        pass

    def get_stone_at(self, x, y):
        x=x-1
        y=y-1
        return self.board_stone[x][y]
    def set_stone_at(self, x, y, stone):
        x=x-1
        y=y-1
        if self.board_stone[x][y] == Stone.EMPTY:
            if stone == Stone.BLACK :
                self.board_stone[x][y]= Stone.BLACK
                stone = Stone.WHITE
            elif stone == Stone.WHITE:
                self.board_stone[x][y]= Stone.WHITE
                stone = Stone.BLACK
        
        return stone

    def _neighbors(self, x, y):
        """
        By convention, fields starting with _ are meant to be accessed only from inside the class.
        """
        pass
    def _count_liberties(self, x, y):
        pass
    def is_alive(self, x, y):
        pass