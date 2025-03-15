import pygame

#C
C_RED = (255, 0, 0)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 255, 0)

#E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {

    'Level1Bg0': 10,
    'Level1Bg1': 10,
    'Level1Bg2': 10,
    'Player'   : 3,
    'Enemy1'   : 6,
    'Enemy2'   : 3,
    'Enemy3'   : 4,

}

#M
MENU_OP = ( 'NEW GAME',
            'SCORE',
            'EXIT')

#K
PLAYER_KEY_UP = {
                    'Player': pygame.K_w
                 }

PLAYER_KEY_DOWN = {
                    'Player': pygame.K_s
                 }

PLAYER_KEY_LEFT = {
                    'Player': pygame.K_a
                 }

PLAYER_KEY_RIGHT = {
                    'Player': pygame.K_d
                 }

#W
WIN_WIDTH = 576
WIN_HEIGTH = 324

LEVEL_WIN_WIDTH = 840
LEVEL_WIN_HEIGTH = 650

SPAWN_TIME = 2000