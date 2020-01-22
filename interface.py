from support.curses_display import CursesDisplay

class Interface(CursesDisplay):
    def __init__(self, stone_provider, screen, width, height):
        super().__init__(screen, width, height)
        self._stone_provider = stone_provider 
        self.print_board(stone_provider)

    def process_input_and_refresh(self):
        self.refresh()
        input_char = self.get_input()
        key_template = "The last key pressed was: {} {}"
        
