import pygame
from objects.SolarPanel import SolarPanel
from objects.Battery import Battery
from pygame.locals import *


if __name__ == '__main__':
    pygame.init()

    sp = SolarPanel([1, 1])
    ba = Battery([1, 1])

    while(1):
        sp.update()
        ba.update_capacity(11)
        print("fin")