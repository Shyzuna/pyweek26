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

        for i in range(0, settings.TILES_NUM_HEIGHT + 2 * settings.BORDER_TILES_NUM + 1):  # Col
            line = []
            for j in range(0, settings.TILES_NUM_WIDTH + 2 * settings.BORDER_TILES_NUM + 1):  # Row
                val = 0  # Moon
                if i < (settings.BORDER_TILES_NUM - 1) or j < (settings.BORDER_TILES_NUM - 1)\
                        or i > (settings.TILES_NUM_HEIGHT + settings.BORDER_TILES_NUM + 1)\
                        or j > (settings.TILES_NUM_WIDTH + settings.BORDER_TILES_NUM + 1):
                    val = 9  # Space
                elif i == (settings.BORDER_TILES_NUM - 1) and j == (settings.BORDER_TILES_NUM - 1):
                    val = 1  # TopLeft Corner
                elif i == (settings.BORDER_TILES_NUM - 1)\
                        and j == (settings.TILES_NUM_WIDTH + settings.BORDER_TILES_NUM + 1):
                    val = 3  # TopRight Corner
                elif i == (settings.TILES_NUM_HEIGHT + settings.BORDER_TILES_NUM + 1)\
                        and j == (settings.TILES_NUM_WIDTH + settings.BORDER_TILES_NUM + 1):
                    val = 8  # BottomRight Corner
                elif i == (settings.TILES_NUM_HEIGHT + settings.BORDER_TILES_NUM + 1)\
                        and j == (settings.BORDER_TILES_NUM - 1):
                    val = 6  # BottomLeft Corner
                elif i == (settings.BORDER_TILES_NUM - 1):
                    val = 2  # Top
                elif j == (settings.TILES_NUM_WIDTH + settings.BORDER_TILES_NUM + 1):
                    val = 5  # Right
                elif i == (settings.TILES_NUM_HEIGHT + settings.BORDER_TILES_NUM + 1):
                    val = 7  # Bottom
                elif j == (settings.BORDER_TILES_NUM - 1):
                    val = 4  # Left
                line.append(val)
            self.baseMap.append(line)


    def scroll(self, directionState, deltaTime):
        if directionState[pygame.K_LEFT]:
            if self.currentRect.x > 0:
                scrollSpeed = deltaTime * settings.SCROLL_SPEED_HORIZONTAL
                newPos = self.currentRect.x - scrollSpeed
                if newPos > 0:
                    self.currentRect.x = newPos
                else:
                    self.currentRect.x = 0

        if directionState[pygame.K_UP]:
            if self.currentRect.y > 0:
                scrollSpeed = deltaTime * settings.SCROLL_SPEED_VERTICAL
                newPos = self.currentRect.y - scrollSpeed
                if newPos > 0:
                    self.currentRect.y = newPos
                else:
                    self.currentRect.y = 0

        if directionState[pygame.K_DOWN]:
            if self.currentRect.y < settings.RECT_MAX_Y:
                scrollSpeed = deltaTime * settings.SCROLL_SPEED_VERTICAL
                newPos = self.currentRect.y + scrollSpeed
                if newPos < settings.RECT_MAX_Y:
                    self.currentRect.y = newPos
                else:
                    self.currentRect.y = settings.RECT_MAX_Y

        if directionState[pygame.K_RIGHT]:
            if self.currentRect.x < settings.RECT_MAX_X:
                scrollSpeed = deltaTime * settings.SCROLL_SPEED_HORIZONTAL
                newPos = self.currentRect.x + scrollSpeed
                if newPos < settings.RECT_MAX_X:
                    self.currentRect.x = newPos
                else:
                    self.currentRect.x = settings.RECT_MAX_X

mapManager = MapManager()
