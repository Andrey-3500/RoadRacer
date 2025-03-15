#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
from random import choice

from code.Const import MENU_OP, SPAWN_TIME, EVENT_ENEMY, C_WHITE, C_GREEN, LEVEL_WIN_WIDTH, LEVEL_WIN_HEIGTH

import pygame.display
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code import Entity
from code.Const import WIN_HEIGTH
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code import Game
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):

        Game.window = pygame.display.set_mode(size=(LEVEL_WIN_WIDTH, LEVEL_WIN_HEIGTH))
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()




            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))


            self.level_text(48, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGTH - 20))
            pygame.display.flip()




    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

