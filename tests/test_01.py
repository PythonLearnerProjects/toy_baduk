import unittest
import curses
from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT
from unittest.mock import MagicMock

from interface import Interface
from support.curses_display import _board_to_screen

BOARD_SPACING = 2

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.interface = MockInterface(5,5)
    def test_01_process_directions(self):
        """
        This test checks to see if the cursor location value
        updates when the correct keycode is entered.
        Note the Interface it uses is a fake one constructed
        to give mock input.
        So if you have added methods or changed anythign
        other than process_input_and_refresh, it could fail
        on perfectly valid code.
        """
        directions = [KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT]
        positions = [(3,4), (3,3), (2,3), (3,3)]
        for d, p in zip(directions, positions):
            old_p = self.interface._cursor_location
            self.interface.set_input(d)
            self.interface.process_input_and_refresh()
            msg = "Cursor should have moved from {} to {} with keycode {}".format(old_p, p, d)
            self.assertEqual(self.interface.get_cursor(), p, msg=msg)

    def test_02_process_bounds(self):
        """
        This tests the literal corner cases of moving the cursor.
        It should not move out of bounds.
        """
        self.interface._cursor_location = (5, 5)

        self.interface.set_input(curses.KEY_DOWN)
        self.interface.process_input_and_refresh()
        self.assertEqual(self.interface.get_cursor(), (5, 5))

        self.interface.set_input(curses.KEY_RIGHT)
        self.interface.process_input_and_refresh()
        self.assertEqual(self.interface.get_cursor(), (5, 5))

        self.interface._cursor_location = (1, 1)

        self.interface.set_input(curses.KEY_UP)
        self.interface.process_input_and_refresh()
        self.assertEqual(self.interface.get_cursor(), (1, 1))

        self.interface.set_input(curses.KEY_LEFT)
        self.interface.process_input_and_refresh()
        self.assertEqual(self.interface.get_cursor(), (1, 1))
 
        
    def test_04_print_board(self):
        """
        This tests that the board can be printed correctly.
        """
        Interface.print_board(self.interface, lambda x,y: '.')
        self.assertEqual(self.interface.get_buffer(), ".....\n"\
                                                      ".....\n"\
                                                      ".....\n"\
                                                      ".....\n"\
                                                      ".....")


        Interface.print_board(self.interface, lambda x,y: 'X' if y == x else '.')
        self.assertEqual(self.interface.get_buffer(), "X....\n"\
                                                      ".X...\n"\
                                                      "..X..\n"\
                                                      "...X.\n"\
                                                      "....X")
    def test_04_print_board(self):
        """
        This tests that the margins are printed as expected.
        They should be the letters A B C D ... along the sides,
        and 1 2 3 4 5 along the top/bottom
        Note that it currently assumes you wil print with
        one leading space ' 1', ' 3' '10 etc.
        It is just as correct not to have this.
        """
        Interface.print_background(self.interface)
        self.assertEqual(self.interface.get_margin(0), ' 5 4 3 2 1')
        self.assertEqual(self.interface.get_margin(1), 'ABCDE')
        self.assertEqual(self.interface.get_margin(2), ' 5 4 3 2 1')
        self.assertEqual(self.interface.get_margin(3), 'ABCDE')


        

class MockInterface():
    KEY_UP = curses.KEY_UP
    KEY_DOWN = curses.KEY_DOWN
    KEY_LEFT = curses.KEY_LEFT
    KEY_RIGHT = curses.KEY_RIGHT
    MARGIN_LEFT= 0
    MARGIN_TOP = 1
    MARGIN_RIGHT = 2
    MARGIN_BOTTOM = 3


    def __init__(self, width, height):
        self.input = curses.KEY_UP
        self._cursor_location = (3,3)
        self._width = width
        self._height = height
        self._fake_board_buffer = [[' '] * width for _ in range(height)]
        self._fake_margin_buffer = [[' '] * width,
                                    [' '] * height,
                                    [' '] * width,
                                    [' '] * height]

    def set_input(self,k):
        self.input = k
    def display_message(self, message):
        pass  
    def get_input(self):
        return self.input
    def get_buffer(self):
        return '\n'.join([''.join(x) for x in self._fake_board_buffer])
    def get_margin(self, n):
        return ''.join(self._fake_margin_buffer[n])

    def process_input_and_refresh(self):
        Interface.process_input_and_refresh(self)

    def clear_game_subwindow(self):
        pass

    def clear_background(self):
        pass

    def print_character_at(self, x, y, character):
        self._fake_board_buffer[y-1][x-1] = character
        
    def print_margin(self, margin, n, character):
        self._fake_margin_buffer[margin][n-1] = character


    def print_board(self, stone_provider):
        Interface.print_board(self, stone_provider)

    def print_background(self):
        Interface.print_background(self)

    def clear_game_subwindow(self):
        pass

    def set_cursor(self, location):
        """ Set the location of the game cursor

        Example
        -------
            $ display = CursesDisplay(screen, 5, 5)
            $ display.set_cursor((1,1))
        """
        old_x, old_y = _board_to_screen(*self._cursor_location)

        x, y = location

        x_scr, y_scr = _board_to_screen(x, y)
        assert y_scr > 0 and y_scr < self._height + 1, "y_scr out of bounds {}".format(y_scr)
        assert x_scr > 0 and x_scr < self._width * BOARD_SPACING + 1, "x_scr out of bounds {}".format(x_scr)
        self._cursor_location = x, y 
 

    def get_cursor(self):
        return self._cursor_location

    def display_message(self, message):
        pass

    def refresh(self):
        pass

