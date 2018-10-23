import pygame
import numpy
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
            for j in range(0, settings.TILES_NUM_WIDTH):
                line.append(0)
            self.baseMap.append(line)

        self.baseMap = numpy.pad(self.baseMap, pad_width=settings.BORDER_TILES_NUM, mode='constant', constant_values=1)

    def scroll(self, directionState, deltaTime):
        deltaX = 0
        deltaY = 0

        if directionState[pygame.K_LEFT]:
            if self.currentRect.x > 0:
                scrollSpeed = deltaTime * settings.SCROLL_SPEED_HORIZONTAL
                newPos = self.currentRect.x - scrollSpeed
                if newPos > 0:
                    deltaX -= scrollSpeed
                    self.currentRect.x = newPos
                else:
                    deltaX -= self.currentRect.x
                    self.currentRect.x = 0

        if directionState[pygame.K_UP]:
            if self.currentRect.y > 0:
                scrollSpeed = deltaTime * settings.SCROLL_SPEED_VERTICAL
                newPos = self.currentRect.y - scrollSpeed
                if newPos > 0:
                    deltaY -= scrollSpeed
                    self.currentRect.y = newPos
                else:
                    deltaY -= self.currentRect.y
                    self.currentRect.y = 0

        if directionState[pygame.K_DOWN]:
            if self.currentRect.y < settings.RECT_MAX_Y:
                scrollSpeed = deltaTime * settings.SCROLL_SPEED_VERTICAL
                newPos = self.currentRect.y + scrollSpeed
                if newPos < settings.RECT_MAX_Y:
                    deltaY += scrollSpeed
                    self.currentRect.y = newPos
                else:
                    deltaY += settings.RECT_MAX_Y - self.currentRect.y
                    self.currentRect.y = settings.RECT_MAX_Y

        if directionState[pygame.K_RIGHT]:
            if self.currentRect.x < settings.RECT_MAX_X:
                scrollSpeed = deltaTime * settings.SCROLL_SPEED_HORIZONTAL
                newPos = self.currentRect.x + scrollSpeed
                if newPos < settings.RECT_MAX_X:
                    deltaX += scrollSpeed
                    self.currentRect.x = newPos
                else:
                    deltaX += settings.RECT_MAX_X - self.currentRect.x
                    self.currentRect.x = settings.RECT_MAX_X

        return (deltaX, deltaY)

mapManager = MapManager()
