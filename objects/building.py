import pygame
import uuid


class Building(pygame.sprite.Sprite):

    def __init__(self, position, size, connections, uid):

        pygame.sprite.Sprite.__init__(self)

        self.id = uuid.uuid4()
        self.position = position
        self.size = size
        self.connections = connections
        self.uid = uid

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