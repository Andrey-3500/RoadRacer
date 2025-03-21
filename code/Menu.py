import pygame.image
from pygame.constants import K_DOWN
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect
from code.Const import WIN_WIDTH, C_RED, C_WHITE, MENU_OP, C_GREEN


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/bg1.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):

        menu_option = 0
        pygame.mixer.music.load('./asset/menu.mp3')
        pygame.mixer_music.play(-1)

        while True:


            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(150, 'Road', C_RED, ((WIN_WIDTH / 2 - 170), 120))
            self.menu_text(150, 'Racer', C_RED, ((WIN_WIDTH / 2 + 170), 120))

            for i in range(len(MENU_OP)):
                if i == menu_option:
                    self.menu_text(80, MENU_OP[i], C_GREEN, ((WIN_WIDTH / 2), 280 + 80 * i))

                else:
                    self.menu_text(80, MENU_OP[i], C_WHITE, ((WIN_WIDTH / 2), 280 + 80 * i))


            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == K_DOWN:
                        if menu_option <len(MENU_OP) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1

                        else:
                            menu_option = len(MENU_OP) - 1

                    if event.key == pygame.K_RETURN: #Enter
                        return MENU_OP[menu_option]






    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)