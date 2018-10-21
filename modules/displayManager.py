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
        pygame.display.set_caption("Coucou")

        self.loadImgs()

    def loadImgs(self):
        self.imgs = {}
        for i in range(0, 1):
            try:
                img = pygame.image.load(os.path.join(settings.TILES_PATH, str(i) + ".png"))
                self.imgs[i] = pygame.transform.scale(img, (settings.TILE_WIDTH, settings.TILE_HEIGHT))
            except Exception as e:
                print(str(e))

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
                self.baseMapSurface.blit(self.imgs[tile], (startX, startY))
                startX += tileW
            startY += tileH
            startX = 0


    def display(self, currentRect, resources):
        self.screen.fill(Colors.WHITE.value)

        # Display part of map
        self.screen.blit(self.baseMapSurface, (0, 0), currentRect)

        # Display resources
        tileW, tileH = settings.TILE_WIDTH, settings.TILE_HEIGHT
        for resource in resources:
            self.screen.blit(self.imgs[resource._category.value],
                             (resource._position[0] * tileW, resource._position[1] * tileH), currentRect)

        pygame.display.flip()


displayManager = DisplayManager()
