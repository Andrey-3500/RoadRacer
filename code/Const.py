import pygame

#C
C_RED = (255, 0, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 255, 0)
C_BLACK = (0, 0, 0)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_SPEED = pygame.USEREVENT + 2


ENTITY_SPEED = {

    'Level1Bg0': 10,
    'Level1Bg1': 10,
    'Level1Bg2': 10,
    'Player'   : 5,
    'Enemy1'   : 6,
    'Enemy2'   : 6,
    'Enemy3'   : 6,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Player': 0,
    'Enemy1': 0,
    'Enemy2': 0,
    'Enemy3': 0,
}

ENTITY_HEALTH = {
    'bg.ong' : 999,
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Player'   : 3,
    'Enemy1'   : 1,
    'Enemy2'   : 1,
    'Enemy3'   : 1,

}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Player'   : 1,
    'Enemy1'   : 1,
    'Enemy2'   : 1,
    'Enemy3'   : 1,

}


#M
MENU_OP = ( 'NEW GAME',
            'SCORE',
            'EXIT')

#P
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
WIN_WIDTH = 840
WIN_HEIGHT = 650

#S
SPAWN_TIME = 2000
SPEED_TIME = 10000

SCORE_POS = {
             0: (WIN_WIDTH / 2, 310),
             1: (WIN_WIDTH / 2, 330),
             2: (WIN_WIDTH / 2, 350),
             3: (WIN_WIDTH / 2, 370),
             4: (WIN_WIDTH / 2, 490),
             5: (WIN_WIDTH / 2, 410),
             6: (WIN_WIDTH / 2, 430),
             7: (WIN_WIDTH / 2, 450),
             8: (WIN_WIDTH / 2, 470),
             9: (WIN_WIDTH / 2, 490),
             }