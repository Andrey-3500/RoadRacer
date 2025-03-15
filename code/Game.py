
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGTH, MENU_OP
from code.Level import Level
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGTH))

    def run(self, ):
        while True: # Funcionando
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in MENU_OP[0]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OP[2]:
                pygame.quit()  # Close Window
                quit()  # end pygame

            else:
                pass