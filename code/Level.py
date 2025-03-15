#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
from random import choice

from code.Const import MENU_OP, SPAWN_TIME, EVENT_ENEMY, C_WHITE, C_GREEN

import pygame.display
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code import Entity
from code.Const import WIN_HEIGTH
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))


    def run(self):

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


            pygame.display.flip()