from support.curses_display import CursesDisplay
import string

class Interface(CursesDisplay):
    """ Class to handle the user interface stuff.

    Inherets from CursesDisplay which is mostly support code
    to interact with the curses library.
    This keeps the boilerplate out of the way. 
    """
    def __init__(self, stone_provider, screen, width, height):
        """
        Arguments
        ---------
            stone_provider: function
                Takes an x and y numerical location between
                1 and board.width or board.height and outputs
                a string of length 1 representing the piece at
                that location.
            screen: curses screen object
                Provided by curses.wrapper via main()
            width: int
                width of game board 
            height: int
                height of game board 
        """
        super().__init__(screen, width, height)
        self._stone_provider = stone_provider 
        self.print_board(stone_provider)
        self.print_background()
        self.set_cursor((1,1))

    def process_input_and_refresh(self):
        """ Main UI portion of game loop.
        """
        self.refresh()
        keycode = self.get_input()
        ####################################################################
        #
        # Exercise 1a: If elif else.
        #
        # Update this function so that the cursor moves with the
        #   arrow keys
        # You should not need to edit any other file, but reading 
        # support/curses_display.py may be illuminating.
        #
        # keycode will be a number representing the key that was pressed.
        # 
        # Your code should be between here and the other line of ####
        ###################################################################

        # You do not need to keep the code inside this region. 
        # It's simply to make it easier to figure out what's going on.


        key_template = "The last key pressed was: {} {}"
        if keycode <= 255:
            display_msg = chr(keycode)
        elif keycode == self.KEY_UP:
            display_msg = "The Up arrow"
        else:
            display_msg = "Another non-ascii key"
        self.display_message(key_template.format(keycode, display_msg))
        x_old, y_old = self.get_cursor()
        x_new, y_new = x_old, y_old



        #
        ###################################################################
        self.set_cursor((x_new,y_new))


    def print_background(self):
        """ Re-print the background for the game board.
        """
        self.clear_background()
        ####################################################################
        #
        # Exercise 1b: For loops
        # Update this function so that margin around the board is printed
        #
        # You should not need to edit any other file, but reading 
        # support/curses_display.py may be illuminating.
        #
        # Note that the CursesDisplay class from which this one inherits
        # contains some constants
        # MARGIN_TOP, MARGIN_LEFT etc. which can be used to specify
        # which margin self.print_margin() should print in.
        # Your code should be between here and the other line of ####


        x_labels = string.ascii_uppercase
        y_labels = [str(x).rjust(2, ' ') for x in range(1, self._height + 1)]


        #self.print_margin(self.MARGIN_TOP, 1, x_labels[0])
        #self.print_margin(self.MARGIN_TOP, self._width, 'X')
        #self.print_margin(self.MARGIN_BOTTOM, 1, 'X')
        #self.print_margin(self.MARGIN_BOTTOM, self._width, 'X')
        #self.print_margin(self.MARGIN_LEFT, 1, 'X')
        #self.print_margin(self.MARGIN_LEFT, self._height, 'X')
        #self.print_margin(self.MARGIN_RIGHT, 1, 'X')
        #self.print_margin(self.MARGIN_RIGHT, self._height, 'X')
        ###################################################################


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
        self.clear_game_subwindow()
        ####################################################################
        #
        # Exercise 1c: Nested for loops
        # Update this function so that the board is printed
        # You should not need to edit any other file, but reading 
        # support/curses_display.py may be illuminating.
        #
        # stone_provider will be provided, and at this point just
        # returns Stone.EMPTY. Simply call it with 
        # stone_provider(x, y) 
        #   
        # Your code should be between here and the other line of ####
        ###################################################################

        # You do not need to keep the code inside this region. 
        # It's simply to make it easier to figure out what's going on.




        ###################################################################


