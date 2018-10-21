import pygame
from pygame.locals import *

from modules.mapGenerator import MapGenerator

if __name__ == '__main__':
    pygame.init()
    mg = MapGenerator()
    print(mg._seed)
    for e in mg.generateSettingsMap():
        print(e)