import curses
import string
import sys

WIN_W = 32
WIN_H = 16
WIN_MARGIN = 5
BOARD_SPACING = 2

def _board_to_screen(x, y):
    x = (x - 1) * BOARD_SPACING
    y = y - 1
    return x, y

class CursesDisplay:
    """ Class to display the game board on the screen.
    Also responsible for input in this case.
    """
    UP = curses.KEY_UP
    DOWN = curses.KEY_DOWN
    LEFT = curses.KEY_LEFT
    RIGHT = curses.KEY_RIGHT

    def __init__(self, screen, width, height):
        self._width = width
        self._height = height
        self._screen = screen
        self._background = curses.newwin(height + 2,
                                    width * BOARD_SPACING + 4,
                                    WIN_MARGIN,
                                    WIN_MARGIN)
 
        self._window = curses.newwin(height,
                                    width * 2,
                                    WIN_MARGIN + 1,
                                    WIN_MARGIN + 2)
        self._textpad = curses.newpad(10, width * 4)
        self._x_labels = string.ascii_uppercase
        self._y_labels = [str(x) for x in range(1, height + 1)]
        self._cursor_location = (1, 1)

        screen.clear()
        curses.curs_set(0)
        curses.noecho()
        self._window.attron(curses.A_NORMAL)
        self._textpad.idlok(True)
        self._textpad.scrollok(True)
        self.print_background()
        self.refresh()

    def print_board(self, stone_provider):
        """ Re-print the game board. 

        Arguments
        ---------
        stone_provider: function(x,y) -> str
            Takes an x and y numerical location between
            1 and board.width or board.height and outputs
            a string of length 1 representing the piece at
            that location.
        """
        self._window.clear()
        self._window.chgat(curses.A_NORMAL) 
        for y in range(0, self._height):
            for x in range(0, self._width):
                stone = stone_provider(x + 1, y + 1)
                assert(len(str(stone)) == 1)
                self._window.addch(y, x * BOARD_SPACING, str(stone))

    def print_background(self):
        """ Re-print the background for the game board.
        """
        self._background.clear()
        for x in range(0, self._width):
            label= self._x_labels[x]
            self._background.addch(0, (x + 1) * BOARD_SPACING, label)
            self._background.addch((self._height + 1), (x + 1) * BOARD_SPACING, label)
        for y in range(0, self._width):
            label = self._y_labels[y].rjust(2, ' ')
            self._background.addstr(y + 1, 0, label)
            self._background.addstr(y + 1, (self._width + 1) * BOARD_SPACING, label)

    def set_cursor(self, location):
        """ Set the location of the game cursor

        Example
        -------
            $ display = CursesDisplay(screen, 5, 5)
            $ display.set_cursor((1,1))
        """

        old_x, old_y = _board_to_screen(*self._cursor_location)
        self._window.chgat(old_y, old_x, 1, curses.A_NORMAL) 

        x, y = location

        x_scr, y_scr = _board_to_screen(x, y)
        assert y_scr >= 0 and y_scr < self._height, "Y out of bounds"
        assert x_scr >= 0 and x_scr < self._height, "X out of bounds"
        self._cursor_location = x, y 

        self._window.chgat(y_scr, x_scr, 1, curses.A_REVERSE) 
        
    def get_cursor(self):
        """
        Return the location of the game cursor
        
        Returns
        -------
        (int, int)
            The board position of the cursor.
        """
        return self._cursor_location

    def get_input(self):
        """
        Get in string form, the last character that was pressed.
        This will block until a key is pressed when called this way.
        
        Returns
        -------
        int
            integer representing key pressed. 
            See https://docs.python.org/3.7/library/curses.html#constants
            for details.
        """
        return self._screen.getch()

    def display_message(self, message):
        """
        Dispaly a string on the pad below game board.

        Parameters
        ----------
        message: str
            The string to display.
        """
        self._textpad.addstr(message + '\n')
        

    def refresh(self):
        """
        Refresh the image that appears on the game board.
        """
        self._screen.refresh()
        self._background.refresh()
        self._window.refresh()
        self._textpad.refresh(0, 0, self._height + 8, 5, 100, 100)
