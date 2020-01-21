from curses import wrapper
from util import Display, eprint
from time import sleep
from board import Board
import sys


def main(screen):
    # Create the display object. This is found in util.py
    display = Display(screen)
    board = Board()
    message = 'Hello'
    key_template = "The last key pressed was: \n {} {}"


    while True:
        # See util.py for where these methods are defined
        display.print_board(board.get_stone_at)
        display.display_message(message)
        display.refresh()


        #######################################################
        # Task 1:
        # Move the cursor when they arrow keys are pressed.
        # You can find the libcurses documentation here
        # https://docs.python.org/3/library/curses.html#constants

        input_char = display.get_input()
        display.set_cursor((3,3))

        # These may help you figure out what is going on
        eprint("This appears in the error log.", input_char)
        message = key_template.format(input_char, chr(input_char))

        #
        ######################################################
    
if __name__ == "__main__":
    wrapper(main)
    