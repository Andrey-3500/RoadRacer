#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity


from code.Const import WIN_WIDTH, ENTITY_SPEED, WIN_HEIGTH, LEVEL_WIN_HEIGTH
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= LEVEL_WIN_HEIGTH:
            self.rect.bottom = 0
