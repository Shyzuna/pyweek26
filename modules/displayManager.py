import pygame
import os
from settings import settings
from settings.enums import Colors, ObjectCategory

class DisplayManager:

    def __init__(self):
        pass

    def init(self):
        self.flags = pygame.DOUBLEBUF
        pygame.display.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT),
                                              self.flags)
        pygame.display.set_caption("Operation MoonLight")

        self._tileset = None
        self.loadImgs()

    def loadTileSet(self, tileSize, numberByLine, totalTiles, path):
        toFill = []
        tileset = pygame.image.load(path)
        for i in range(0, totalTiles):
            surf = pygame.Surface(tileSize)
            surf.blit(tileset, (0, 0), pygame.Rect((i % numberByLine) * tileSize[0],
                                                   int(i / numberByLine) * tileSize[1],
                                                   tileSize[0], tileSize[1]))
            surf = pygame.transform.scale(surf, (settings.TILE_WIDTH, settings.TILE_HEIGHT))
            toFill.append(surf)
        return toFill


    def loadImgs(self):

        self._tileset = self.loadTileSet((64, 64), 8, 10, os.path.join(settings.TILES_PATH, 'tilesetMoon.png'))

        self.imgs = {}

        # Load resources images
        for resource in ObjectCategory:
            try:
                img = pygame.image.load(os.path.join(settings.RESOURCES_PATH, resource.value + ".png"))
                self.imgs[resource.value] = pygame.transform.scale(img, (settings.TILE_WIDTH, settings.TILE_HEIGHT))
            except:
                pass

        # Load buildings images
        for resource in ObjectCategory:
            try:
                img = pygame.image.load(os.path.join(settings.RESOURCES_PATH, resource.value + ".png"))
                self.imgs[resource.value] = pygame.transform.scale(img, (settings.TILE_WIDTH, settings.TILE_HEIGHT))
            except:
                pass

    def createBaseMapSurface(self, map):
        self.baseMapSurface = pygame.Surface((settings.MAP_WIDTH, settings.MAP_HEIGHT))
        self.baseMapSurface.fill(Colors.WHITE.value)

        tileW, tileH = settings.TILE_WIDTH, settings.TILE_HEIGHT
        startX = 0
        startY = 0
        for line in map:
            for tile in line:
                self.baseMapSurface.blit(self._tileset[tile], (startX, startY))
                startX += tileW
            startY += tileH
            startX = 0

    def display(self, currentRect, resources, buildings):
        rect = pygame.Rect(0, 0, settings.TILE_WIDTH, settings.TILE_HEIGHT)

        self.screen.fill(Colors.WHITE.value)

        # Display part of map
        self.screen.blit(self.baseMapSurface, (0, 0), currentRect)

        # Display resources
        for resource in resources:
           self.screen.blit(self.imgs[resource._category.value],
                             (resource.current_x - currentRect.topleft[0], resource.current_y - currentRect.topleft[1]))

        # Display buildings
        for y in buildings:
            for x in buildings[y]:
                buildings[y][x].display(self.screen, currentRect)


displayManager = DisplayManager()
