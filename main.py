import sys
from curses import wrapper
import curses
import json
from util import Display, eprint
from time import sleep
from board import Board, Stone
import websocket, ssl


def main(screen):
    if sys.argv[1] == "-m":
      multiplayer = True
      initial_turn = Stone.BLACK if sys.argv[2] == 'b' else Stone.WHITE
    else:
      multiplayer = False
      initial_turn = Stone.BLACK
    # Create the display object. This is found in util.py
    x=3
    y=3
    display = Display(screen)
    message = ''
    key_template = "The last key pressed was: \n {} {}"
    board = Board(5, 5)
    turn = Stone.BLACK
    ws = websocket.create_connection("wss://ma4192ic8e.execute-api.us-west-2.amazonaws.com/Prod/",
      sslopt={"cert_reqs": ssl.CERT_NONE})

    while True:
        # See util.py for where these methods are defined
        display.set_cursor((x,y))
        display.print_board(board.get_stone_at)
        display.display_message(message)
        display.refresh()

        if turn != initial_turn and multiplayer:
            data = json.loads(ws.recv())
            display.display_message(repr(data))
            display.refresh()
            x,y = data
            board.set_stone_at(x, y, turn)
            turn = Stone.BLACK if turn == Stone.WHITE else Stone.WHITE
        else:
            done = False
            input_char = display.get_input()
            if input_char == curses.KEY_RIGHT:
                x=x+1
            elif input_char == curses.KEY_DOWN:
                y=y+1
            elif input_char == curses.KEY_UP:
                y=y-1
            elif input_char == curses.KEY_LEFT:
                x=x-1
            elif input_char == 32:
                msg = "{{\"message\": \"sendmessage\", \"data\" : \"[{},{}]\" }}".format(x,y)
                ws.send(msg)
                board.set_stone_at(x, y, turn)
                turn = Stone.BLACK if turn == Stone.WHITE else Stone.WHITE
                data = json.loads(ws.recv())
        display.set_cursor((x,y))
        
    
if __name__ == "__main__":
    wrapper(main)
    
