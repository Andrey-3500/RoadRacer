#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys
from random import choice
from code.Const import EVENT_SPEED, SPEED_TIME, SPAWN_TIME, ENTITY_SPEED, EVENT_ENEMY, C_WHITE, C_GREEN, WIN_WIDTH, WIN_HEIGHT, C_BLACK, C_RED
import pygame.display
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code import Entity, Const
from code.Const import WIN_HEIGHT
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code import Game
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        player = (EntityFactory.get_entity('Player'))
        player.score = player_score[0]
        self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_SPEED, SPEED_TIME, 12)

    def run(self, player_score: list[int]):
        pygame.mixer.music.load('./asset/level.wav')
        pygame.mixer_music.play(-1)
        Game.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if ent.name == 'Player':
                    self.level_text(48, f'Score: {player_score[0]:.0f}', C_BLACK, (10, 75))
                    self.level_text(48, f'Vidas: {ent.health}', C_GREEN, (10, 45))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                    if Const.SPAWN_TIME >= 10:
                        Const.SPAWN_TIME -= 10

                if event.type == EVENT_SPEED:
                    for chave in ENTITY_SPEED:
                            ENTITY_SPEED[chave] += 1


                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player) and ent.name == 'Player':
                        player_score[0] = ent.score

                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return player_score

            pygame.display.flip()

            #collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            EntityMediator.give_score(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

