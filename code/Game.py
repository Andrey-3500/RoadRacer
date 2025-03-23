
import pygame

from code.Const import MENU_OP, WIN_WIDTH, WIN_HEIGHT
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


    def run(self, ):
        while True: # Funcionando
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OP[0]:
                player_score = [0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    score.save(player_score)


            elif menu_return == MENU_OP[1]:
                score.show()

            elif menu_return == MENU_OP[2]:
                pygame.quit()  # Close Window
                quit()  # end pygame

            else:
                pass