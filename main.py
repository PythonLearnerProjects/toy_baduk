from curses import wrapper
from interface import Interface
from time import sleep
from board import Board
import sys


def main(screen):
    board = Board()
    display = Interface(board.get_stone_str_at, screen, 19, 19)
    message = 'Hello'
    key_template = "The last key pressed was: {} {}"
    input_char = None
    display.display_message(message)

    while True:
        display.process_input_and_refresh()
    
if __name__ == "__main__":
    wrapper(main)
    
    
