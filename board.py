#######################################
# Exercise 2: Implement enough of     #
# this class that the stones appear on#
# the board when space is pressed     #
#######################################
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
        self.boardStone = [[Stone.EMPTY,Stone.EMPTY,Stone.EMPTY,Stone.EMPTY,Stone.EMPTY],[Stone.EMPTY,Stone.EMPTY,Stone.EMPTY,Stone.EMPTY,Stone.EMPTY],[Stone.EMPTY,Stone.EMPTY,Stone.EMPTY,Stone.EMPTY,Stone.EMPTY],[Stone.EMPTY,Stone.EMPTY,Stone.EMPTY,Stone.EMPTY,Stone.EMPTY],[Stone.EMPTY,Stone.EMPTY,Stone.EMPTY,Stone.EMPTY,Stone.EMPTY]]
        pass
    def get_stone_at(self, x, y):
        x=x-1
        y=y-1
        return self.boardStone[x][y]
    def set_stone_at(self, x, y, stone, player):
        x=x-1
        y=y-1
        if self.boardStone[x][y] == Stone.EMPTY and player==0:
            self.boardStone[x][y]= Stone.BLACK
            player=1
        elif self.boardStone[x][y] == Stone.EMPTY and player==1:
            self.boardStone[x][y]= Stone.WHITE
            player=0
        return player
    def _neighbors(self, x, y):
        """
        By convention, fields starting with _ are meant to be accessed only from inside the class.
        """
        pass
    def _count_liberties(self, x, y):
        pass
    def is_alive(self, x, y):
        pass
