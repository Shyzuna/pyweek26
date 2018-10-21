import pygame
from settings import settings

class MapManager:

    def __init__(self):
        pass

    def init(self):
        self.resourcesObject = []

        # Current displayed part of map
        self.currentRect = pygame.Rect(0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

        self.createBaseMap()

    def createBaseMap(self):
        self.baseMap = []

        for i in range(0, settings.TILES_NUM_HEIGHT):
            line = []
            for j in range(0, settings.TILES_NUM_WITDH):
                line.append(0)
            self.baseMap.append(line)

    def scroll(self, directionState, deltaTime):
        deltaX = 0
        deltaY = 0

        if directionState[pygame.K_LEFT]:
            if self.currentRect.x > 0:
                deltaX -= deltaTime * settings.SCROLL_SPEED_HORIZONTAL
                self.currentRect.x -= deltaTime * settings.SCROLL_SPEED_HORIZONTAL

        if directionState[pygame.K_UP]:
            if self.currentRect.y > 0:
                deltaY -= deltaTime * settings.SCROLL_SPEED_VERTICAL
                self.currentRect.y -= deltaTime * settings.SCROLL_SPEED_VERTICAL

        if directionState[pygame.K_DOWN]:
            if self.currentRect.y < settings.MAP_HEIGHT + settings.SCREEN_HEIGHT:
                deltaY += deltaTime * settings.SCROLL_SPEED_VERTICAL
                self.currentRect.y += deltaTime * settings.SCROLL_SPEED_VERTICAL

        if directionState[pygame.K_RIGHT]:
            if self.currentRect.x < settings.MAP_WIDTH + settings.SCREEN_WIDTH:
                deltaX += deltaTime * settings.SCROLL_SPEED_HORIZONTAL
                self.currentRect.x += deltaTime * settings.SCROLL_SPEED_HORIZONTAL

        return (deltaX, deltaY)

mapManager = MapManager()
