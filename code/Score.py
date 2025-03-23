import sys
from datetime import datetime

import pygame
from pygame.surface import Surface
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_RED, C_GREEN, C_WHITE, C_YELLOW, SCORE_POS
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, player_score:list[int]):
        pygame.mixer.music.load('./asset/menu.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(150, "Game Over!", C_RED, ((WIN_WIDTH / 2), 120))
            score = player_score[0]
            text = 'Enter Player name (4 character):'
            self.score_text(60, text, C_GREEN, ((WIN_WIDTH / 2), 200))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return

                    elif event.key == K_BACKSPACE:
                        name = name[:-1]

                    else:
                        if len(name) < 4:
                            name += event.unicode

            self.score_text(70, name, C_WHITE,((WIN_WIDTH / 2), 320) )
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer.music.load('./asset/menu.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(self.surf, self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_YELLOW, ((WIN_WIDTH / 2), 200))
        self.score_text(20, 'NAME     SCORE           DATE      ', C_YELLOW,((WIN_WIDTH / 2), 280))
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score:05.0f}     {date}', C_YELLOW,
                            SCORE_POS[list_score.index(player_score)])

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"