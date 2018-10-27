"""
Title: buildingUpgradeSnap File
Desc: UIBuildingUpgradeSnap class
Creation Date:  27/10/18
LastMod Date: 27/10/18
TODO:
"""

import pygame
from settings.enums import Colors
from settings import settings
import modules.mapManager
import modules.gameManager
import modules.researchManager
from objects.headquarters import HeadQuarters

class UIBuildingUpgradeSnap(object):
    def __init__(self, upgradeImg, guiManager):
        self._upgradeImg = upgradeImg
        self._validPos = False
        self._pos = pygame.mouse.get_pos()
        self._iconPos = pygame.mouse.get_pos()
        self._guiManager = guiManager
        self._tilePos = (-1, -1)
        self._bgSurf = pygame.Surface((settings.TILE_WIDTH, settings.TILE_HEIGHT)).convert_alpha()
        self._bgSurf.fill((255, 0, 0, 80))
        self._onBuilding = False

    def display(self, screen):
        if self._onBuilding:
            self._bgSurf.fill((0, 255, 0, 80) if self._validPos else (255, 0, 0, 80))
            screen.blit(self._bgSurf, self._pos)
        #screen.blit(self._destroyImg, self._iconPos)

    def updatePosition(self, mPos):
        self._pos = mPos
        self._iconPos = mPos
        if self._guiManager.isOnGui():
            self._validPos = False
        else:
            currentRect = modules.mapManager.mapManager.currentRect
            self._tilePos = modules.mapManager.mapManager.getTilePosFromReal(mPos)
            building = modules.gameManager.gameManager.getBuildingAt(self._tilePos)
            self._onBuilding = building is not None
            self._validPos = building is not None and building.canUpgrade()

            self._pos = (self._tilePos[0] * settings.TILE_WIDTH - currentRect.x,
                         self._tilePos[1] * settings.TILE_HEIGHT - currentRect.y)

    def tryUpgrade(self):
        if self._validPos:
            building = modules.gameManager.gameManager.getBuildingAt(self._tilePos)
            if building is not None and building.canUpgrade():
                if building.lvlUp():
                    print('Upgraded building at ' + str(self._tilePos))
                    if isinstance(building, HeadQuarters):
                        modules.researchManager.researchManager.unlockNewLevel(building.level)
        else:
            print('Cannot Upgrade')
