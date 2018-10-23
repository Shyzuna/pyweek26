import pygame
import uuid

from settings import settings


class Building(pygame.sprite.Sprite):

    def __init__(self, position, size, connections, img):

        pygame.sprite.Sprite.__init__(self)

        self.id = uuid.uuid4()
        self.position = position
        self.current_x = (position[0] - 1) * settings.TILE_WIDTH
        self.current_y = (position[1] - 1) * settings.TILE_HEIGHT
        self.size = size
        self.connections = connections
        self.img = img

    def connection(self, resource):
        if resource in self.connections['inputs']:
            self.connections['inputs'][resource] = True
        if resource in self.connections['outputs']:
            self.connections['outputs'][resource] = True

    def disconnection(self, resource):
        if resource in self.connections['inputs']:
            self.connections['inputs'][resource] = False
        if resource in self.connections['outputs']:
            self.connections['outputs'][resource] = False

    def display(self, screen, currentRect):
        screen.blit(self.img, (self.current_x - currentRect.topleft[0],
                               self.current_y - currentRect.topleft[1]))


