"""
Title: buildingMouseSnap File
Desc: UIBuildingMouseSnap class
Creation Date:  24/10/18
LastMod Date: 25/10/18
TODO:
"""

import pygame
from settings.enums import Colors
from settings import settings
import modules.mapManager
import modules.gameManager

class UIBuildingMouseSnap(object):
    def __init__(self, building, guiManager):
        self._building = building
        self._validPos = False
        self._pos = pygame.mouse.get_pos()
        self._guiManager = guiManager
        self._tilePos = (-1, -1)
        size = self._building.img.get_size()
        self._bgSurf = pygame.Surface(size).convert_alpha()

    def display(self, screen):
        # should use second image
        self._bgSurf.fill((0, 255, 0, 80) if self._validPos else (255, 0, 0, 80))
        screen.blit(self._building.img, self._pos)
        screen.blit(self._bgSurf, self._pos)

    def updatePosition(self, mPos):
        self._pos = mPos
        if self._guiManager.isOnGui():
            self._validPos = False
        else:
            currentRect = modules.mapManager.mapManager.currentRect
            self._tilePos = modules.mapManager.mapManager.getTilePosFromReal(mPos)
            self._validPos = modules.gameManager.gameManager.checkTileValid(self._tilePos, self._building.allowedSpot)

            self._pos = (self._tilePos[0] * settings.TILE_WIDTH - currentRect.x,
                         self._tilePos[1] * settings.TILE_HEIGHT - currentRect.y)

    def tryBuild(self):
        if self._validPos:
            building = self._building.__class__(self._tilePos)
            modules.gameManager.gameManager.createBuilding(building)
            print('Built at ' + str(self._tilePos))
        else:
            print('Cannot build')
