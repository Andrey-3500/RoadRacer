#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGTH, LEVEL_WIN_WIDTH, LEVEL_WIN_HEIGTH
from code.Enemy import Enemy
from code.Player import Player
from random import randint

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position = (0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (0, LEVEL_WIN_HEIGTH)))
                return list_bg

            case 'Player':
                return Player('Player',(LEVEL_WIN_WIDTH/2 - 90, LEVEL_WIN_HEIGTH - 150))

            case 'Enemy1':
                return Enemy('Enemy1', (randint (190, LEVEL_WIN_WIDTH - 250) , -190))

            case 'Enemy2':
                return Enemy('Enemy2', (randint (190, LEVEL_WIN_WIDTH - 250) , -190))

            case 'Enemy3':
                return Enemy('Enemy3', (randint (190, LEVEL_WIN_WIDTH - 250) , -190))
