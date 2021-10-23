import pygame
WIN_WITH = 720 #tamaño del display
WIN_HEIGHT = 480 #tamaño del display
TPIXEL = 35
PLAYERPIXEL = 70 #Tamaño predeterminado de pixeles de los personajes
ENEMYPIXEL = 70 #tamaño predeterminado de pixeles de los enemigos

#listas de imagenes
DOWNImages = []
RIGHTImages = []
LEFTImages = []
UPImages = []
RUPImages = []
RDOWNImages = []
LUPImages = []
LDOWNImages = []
RPUNCHImages = []
LPUNCHImages = []
#Listas de imagenes enemy
#DOWNenemy = []
RIGHTenemy = []
LEFTenemy = []
#UPenemy = []


# EN que capa quieres que el sprite aparezca / sprite jugador position
PLAYER_LAYER = 4 
ENEMY_LAYER = 5
BLOCK_LAYER = 2
GROUND_LAYER = 1

PLAYER_SPEED = 2
ENEMY_SPEED = 3
#tamaño default de nuestras imagenes
DEFAULT_IMAGE_SIZE = (70, 70)
RED = (255,0,0) #RGB 
WHITE = (255, 255, 255) #RGB
BLUE = (0,0,255) #RGB
BlACK = (0,0,0) #RGB
#framerate
FPS = 120 #frames per second

PLAYER_HITBOX = (70,70)
PLAYER_PUNCHBOX = (34,34)
Maps=[]

Australia=pygame.image.load('assets_test/mapas/mapa2_magenta.png')
AustraliaResized=pygame.transform.scale(Australia,(WIN_WITH,WIN_HEIGHT))
USA=pygame.image.load('assets_test/mapas/mapa1_magenta.png')
USAResized=pygame.transform.scale(USA,(WIN_WITH,WIN_HEIGHT))
#Japon=pygame.image.load('assets_test/mapas/Japon.png')
#JaponResized=pygame.transform.scale(Japon,(WIN_WITH,WIN_HEIGHT))
#Francia=pygame.image.load('assets_test/mapas/Francia.png')
#FranciaResized=pygame.transform.scale(Francia,(WIN_WITH,WIN_HEIGHT))

Maps.append(Australia)
Maps.append(USAResized)
#Maps.append(JaponResized)
#Maps.append(FranciaResized)


tilemap = [
'BBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
'B................E..........B',
'B...........................B',
'B....BBB....................B',
'B...P.......................B',
'B...........................B',
'B...........................B',
'B...........................B',
'B.....BBB........E..........B',
'B.......B...................B',
'B.......B...................B',
'B..E........................B',
'B......E.........E..........B',
'B...........................B',
'B...........................B',
'B...........................B',
'B...........................B',
'B...........................B',
'BBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]