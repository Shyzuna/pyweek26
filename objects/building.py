import pygame
import uuid

from settings import settings
from settings.enums import BuildingStates


class Building(pygame.sprite.Sprite):

    def __init__(self, position, buildingData):

        pygame.sprite.Sprite.__init__(self)

        self.id = uuid.uuid4()
        self.position = position
        self.current_x = (position[0]) * settings.TILE_WIDTH
        self.current_y = (position[1]) * settings.TILE_HEIGHT
        self.size = buildingData['size']
        self.img = buildingData['animImg'][0]
        self.buildingData = buildingData
        self.state = BuildingStates.OFF
        self.level = 0

    def setPos(self, pos):
        self.position = pos
        self.current_x = (pos[0]) * settings.TILE_WIDTH
        self.current_y = (pos[1]) * settings.TILE_HEIGHT

    def display(self, screen, currentRect):
        screen.blit(self.img, (self.current_x - currentRect.topleft[0],
                               self.current_y - currentRect.topleft[1]))

    def getGuiTipInfo(self):
        pass
        #return self.name, self.desc, self.cost, self.creationTime, self.constructable

    def getGameTip(self):
        pass