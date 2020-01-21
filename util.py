############ruuuuuuuuuuuuuuuuu###########################
#                                     #
# You shouldn't need to edit this yet #
#                                     #
#######################################
import curses
from board import Stone
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

WIN_W = 32
WIN_H = 16
WIN_MARGIN = 5
BOARD_SPACING = 2

class Display:
    """
    Class to display the game board on the screen.
    Also responsible for input in this case.
    Attributes
    ----------
    screen : curses screen object
    window : sub-window in which the game is displayed
    """
    def __init__(self, screen):
        self.screen = screen
        curses.curs_set(0)
        curses.noecho()
        self.window = curses.newwin(WIN_H,
                                    WIN_W,
                                    WIN_MARGIN,
                                    WIN_MARGIN)
        self.refresh()
        self._message = ''
        self._cursor_char = '.' 
        self._cursor_location = None

    def print_board(self, piece_at):
        if piece_at == None:
            piece_at = lambda x, y: None
        for x in range(1, 6):
            board_num = str(x)
            self.window.addstr(0, x * BOARD_SPACING, board_num)
        for y in range(1, 6):
            self.window.addch(y, 0, str(y))
            for x in range(1, 6):
                if (x, y) == self._cursor_location:
                    attribute = curses.A_REVERSE
                else :
                    attribute = curses.A_NORMAL
                if piece_at(x, y) == Stone.EMPTY:
                    self.window.addch(y, x * BOARD_SPACING, '.', attribute)
                elif piece_at(x, y) == Stone.WHITE:
                    self.window.addch(y, x * BOARD_SPACING, 'O', attribute)
                elif piece_at(x, y) == Stone.BLACK:
                    self.window.addch(y, x * BOARD_SPACING, 'X', attribute)

    def set_cursor(self, cursor_location):
        """
        Set the location of the game cursor
        usage: s.set_cursor((1,1))
        """
        
        self._cursor_location = cursor_location
        
    def get_cursor(self):
        """
        Return the location of the game cursor
        """
        return self._cursor_location

    def get_input(self):
        """
        Get in string form, the last character that was pressed.
        This will block until a key is pressed when called this way.
        """
        return self.screen.getch()

    def display_message(self, message):
        """
        Dispaly a string on the game board.
        """
        blank_str = " " * len(self._message)
        self.message = message
        self.window.addstr(6, 0, blank_str)
        self.window.addstr(6, 0, message)
        

    def refresh(self):
        """
        Refresh the image that appears on the game board.
        """
        self.window.refresh()
        self.screen.refresh()
