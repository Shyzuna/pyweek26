"""
Title: buildingMouseSnap File
Desc: UIBuildingMouseSnap class
Creation Date:  24/10/18
LastMod Date: 24/10/18
TODO:
"""

import pygame
from settings.enums import Colors

class UIBuildingMouseSnap(object):
    def __init__(self, building, guiManager):
        self._building = building
        self._validPos = False
        self._pos = pygame.mouse.get_pos()
        self._guiManager = guiManager

        size = self._building.img.get_size()
        self._bgSurf = pygame.Surface((size[0] + 4, size[1] + 4))

    def display(self, screen):
        # should use second image
        self._bgSurf.fill(Colors.GREEN.value if self._validPos else Colors.RED.value)
        self._bgSurf.blit(self._building.img, (2, 2))
        screen.blit(self._bgSurf, self._pos)

    def updatePosition(self, mPos):
        self._pos = mPos
        if self._guiManager.isOnGui():
            self._validPos = False
        else:
            self._validPos = True
