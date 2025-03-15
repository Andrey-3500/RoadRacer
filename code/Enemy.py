#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

import pygame

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self, ):
        self.rect.centery += ENTITY_SPEED[self.name]
