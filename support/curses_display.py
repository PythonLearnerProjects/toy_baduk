import curses
import sys

WIN_W = 32
WIN_H = 16
WIN_MARGIN = 5
BOARD_SPACING = 2

def _board_to_screen(x, y):
    x = (x - 1) * BOARD_SPACING + 1
    y = y
    return x, y

class CursesDisplay:
    """ Class to display the game board on the screen.
    Also responsible for input in this case.
    """
    KEY_UP = curses.KEY_UP
    KEY_DOWN = curses.KEY_DOWN
    KEY_LEFT = curses.KEY_LEFT
    KEY_RIGHT = curses.KEY_RIGHT
    MARGIN_LEFT= 0
    MARGIN_TOP = 1
    MARGIN_RIGHT = 2
    MARGIN_BOTTOM = 3

    def __init__(self, screen, width, height):
        """
        Arguments
        ---------
            screen: curses screen object
                Provided by curses.wrapper via main()
            width: int
                width of game board 
            height: int
                height of game board 
        """

        self._width = width
        self._height = height
        self._screen = screen
        # TODO: Get rid of all the magic numbers in this and in print_*
        self._background = curses.newwin(height + 4,
                                    width * BOARD_SPACING + 6,
                                    WIN_MARGIN,
                                    WIN_MARGIN)
 
        self._window = curses.newwin(height + 2,
                                    width * 2 + 2,
                                    WIN_MARGIN + 1,
                                    WIN_MARGIN + 2)
        self._textpad = curses.newpad(10, width * 4)
        self._cursor_location = (1, 1)

        screen.clear()
        curses.curs_set(0)
        curses.noecho()
        self._textpad.idlok(True)
        self._textpad.scrollok(True)
        self.refresh()

    def clear_game_subwindow(self):
        """ Clears the subwindow displaying the game board.
        """
        self._window.clear()
        self._window.border()

    def clear_background(self):
        """ Clears the subwindow displaying the game board.
        """
        self._background.clear()


    def print_character_at(self, x, y, character):
        """ Print a character on the game board
        Arguments
        ---------
            x: int
                x location of target must be inside game board
            y: int
                y location of target must be inside game board
            character: str of length 1
                character to print
        """
        x_scr, y_scr = _board_to_screen(x, y)
        self._window.chgat(curses.A_NORMAL, 1) 
        assert str(character) == character
        assert len(character) == 1
        assert x_scr > 0 and x_scr < self._width * BOARD_SPACING + 2, "x out of bounds"
        assert y_scr > 0 and y_scr < self._height + 2, "y out of bounds"
        self._window.addch(y_scr, x_scr, character)
        
    def print_margin(self, margin, n, character):
        """ Print a character on the margin around the game board
        Arguments
        ---------
            n: int
                distance down the margin
            character: str of length 1
                character to print
        """
        assert str(character) == character
        n = n + 1
        assert n > 0
        if margin == self.MARGIN_LEFT:
            assert len(character) <= 2
            assert n < self._height + 3, "n out of bounds"
            self._background.addstr(n, 0, character)
        elif margin == self.MARGIN_TOP:
            assert len(character) == 1
            assert n < (self._width + 1) * BOARD_SPACING + 2, "n out of bounds"
            self._background.addch(0, (n) * BOARD_SPACING, character)
        elif margin == self.MARGIN_RIGHT:
            assert len(character) <= 2
            assert n < self._height + 3, "n out of bounds"
            self._background.addstr(n, (self._width + 1) * BOARD_SPACING + 2, character)
        elif margin == self.MARGIN_BOTTOM:
            assert len(character) == 1
            assert n < (self._width + 1) * BOARD_SPACING + 2, "n out of bounds"
            self._background.addch((self._height + 3), (n) * BOARD_SPACING, character)

    def set_cursor(self, location):
        """ Set the location of the game cursor

        Example
        -------
            $ display = CursesDisplay(screen, 5, 5)
            $ display.set_cursor((1,1))
        """
        return
        old_x, old_y = _board_to_screen(*self._cursor_location)
        self._window.chgat(old_y, old_x, 1, curses.A_NORMAL) 

        x, y = location

        x_scr, y_scr = _board_to_screen(x, y)
        assert y_scr > 0 and y_scr < self._height + 1, "y_scr out of bounds {}".format(y_scr)
        assert x_scr > 0 and x_scr < self._width * BOARD_SPACING + 2, "x_scr out of bounds {}".format(x_scr)
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
        self._textpad.refresh(0, 0, self._height + 10, 5, 100, 100)
