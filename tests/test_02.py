import unittest

from board import Board, Stone, InvalidStoneException, InvalidCoordException


class TestBoard(unittest.TestCase):

    def test_01_stone_invalid(self):
        # You can pass this test by just making 
        # Board.set_stone_at raise InvalidStoneException
        board = Board(5,5)
        failure_msg = ("The board should raise InvalidStoneException"
                          " unless stone is Stone.BLACK or stone.WHITE.")
        for stone in ["potato", 3, Stone.EMPTY]:
            with self.assertRaises(InvalidStoneException, msg=failure_msg) as cm:
                board.set_stone_at(1,1, stone)

    def test_02_place_invalid(self):
        board = Board(5,5)
        failure_msg = ("set_stone_at should raise InvalidCoordException"
                          " unless the coordinates are inside the board.")
        for x,y in [(0, 0), (6, 6)]:
            with self.assertRaises(InvalidCoordException, msg=failure_msg) as cm:
                try:
                    board.set_stone_at(x,y, Stone.BLACK)
                except InvalidStoneException as e:
                    pass

    def test_03_place_occupied(self):
        board = Board(5,5)
        failure_msg = ("The board should raise InvalidCoordException"
                          " unless the position on the board is empty.")
        with self.assertRaises(InvalidCoordException, msg=failure_msg) as cm:
            try:
                board.set_stone_at(1,1, Stone.BLACK)
                board.set_stone_at(1,1, Stone.BLACK)
            except InvalidStoneException as e:
                pass
            
    def test_04_place_valid(self):
        failure_msg = ("Placing at a valid location should"
                          " not raise error \"{}\"")
        try:
            board = Board(5,5)
            for x in range(1,6):
                for y in range(1,6):
                    board.set_stone_at(x,y, Stone.BLACK)
            board = Board(5,5)
            for x in range(1,6):
                for y in range(1,6):
                    board.set_stone_at(x,y, Stone.WHITE)
        except Exception as e:
            self.fail(msg = failure_msg.format(repr(e)))
 
    def test_05_get_invalid(self):
        board = Board(5,5)
        failure_msg = ("get_stone_at should raise InvalidCoordException"
                         " unless the coordinates are inside the board.")
        for x,y in [(0, 0), (6, 6)]:
            with self.assertRaises(InvalidCoordException, msg=failure_msg) as cm:
                try:
                    board.get_stone_at(x,y)
                except InvalidStoneException as e:
                    pass

   
    def test_06_get_empty(self):
        failure_msg = ("get_stone_at on an empty place should return Stone.EMPTY")
        board = Board(5,5)
        for x in range(1,6):
            for y in range(1,6):
                self.assertEqual(board.get_stone_at(x,y), Stone.EMPTY, msg=failure_msg)
        
    def test_07_place_get(self):
        board = Board(5,5)
        failure_msg = ("get_stone_at on an occupied place should return the stone")
        board.set_stone_at(1,1, Stone.BLACK)
        self.assertEqual(board.get_stone_at(1,1), Stone.BLACK, msg=failure_msg)
        board.set_stone_at(1,3, Stone.WHITE)
        self.assertEqual(board.get_stone_at(1,3), Stone.WHITE, msg=failure_msg)
        self.assertEqual(board.get_stone_at(1,1), Stone.BLACK, msg=failure_msg)

if __name__ == '__main__':
    unnittest.main()
