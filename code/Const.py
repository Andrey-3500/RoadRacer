import pygame

#C
C_RED = (255, 0, 0)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 255, 0)

#E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {

    'Level1Bg0': 3,
    'Level1Bg1': 3,
    'Level1Bg2': 3,
    'Player1'  : 3,
    'Enemy1'   : 2,
    'Enemy2'   : 1,

}

#M
MENU_OP = ( 'NEW GAME',
            'SCORE',
            'EXIT')


#W
WIN_WIDTH = 576
WIN_HEIGTH = 324


SPAWN_TIME = 4000