from support.curses_display import CursesDisplay

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

    def process_input_and_refresh(self):
        """ Main UI portion of game loop.
        """
        self.refresh()
        keycode = self.get_input()
        ####################################################################
        #
        # Exercise 1: Update this function so that the cursor moves with the
        #   arrow keys
        # You should not need to edit any other file, but reading 
        # support/curses_display.py may be illuminating.
        #

        key_template = "The last key pressed was: {} {}"
        if keycode <= 255:
            display_char = chr(keycode)
        else:
            display_char = "Not a character"
        self.display_message(key_template.format(keycode, display_char))



        #
        ###################################################################
