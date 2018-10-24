"""
Title: buildingDestroySnap File
Desc: UIBuildingDestroySnap class
Creation Date:  25/10/18
LastMod Date: 25/10/18
TODO:
"""

import pygame
from settings.enums import Colors
from settings import settings
import modules.mapManager
import modules.gameManager

class UIBuildingDestroySnap(object):
    def __init__(self, destroyImg, guiManager):
        self._destroyImg = destroyImg
        self._validPos = False
        self._pos = pygame.mouse.get_pos()
        self._iconPos = pygame.mouse.get_pos()
        self._guiManager = guiManager
        self._tilePos = (-1, -1)
        self._bgSurf = pygame.Surface((settings.TILE_WIDTH, settings.TILE_HEIGHT)).convert_alpha()
        self._bgSurf.fill((255, 0, 0, 80))

    def display(self, screen):
        if self._validPos:
            screen.blit(self._bgSurf, self._pos)
        screen.blit(self._destroyImg, self._iconPos)

    def updatePosition(self, mPos):
        self._pos = mPos
        self._iconPos = mPos
        if self._guiManager.isOnGui():
            self._validPos = False
        else:
            currentRect = modules.mapManager.mapManager.currentRect
            self._tilePos = modules.mapManager.mapManager.getTilePosFromReal(mPos)
            self._validPos = modules.gameManager.gameManager.checkIsBuildingTile(self._tilePos)

            self._pos = (self._tilePos[0] * settings.TILE_WIDTH - currentRect.x,
                         self._tilePos[1] * settings.TILE_HEIGHT - currentRect.y)

    def tryDestroy(self):
        if self._validPos:
            building = modules.gameManager.gameManager.getBuildingAt(self._tilePos)
            modules.gameManager.gameManager.removeBuilding(building)
            print('Deleted building at ' + str(self._tilePos))
        else:
            print('Cannot Delete')