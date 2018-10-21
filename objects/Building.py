import pygame


class Building(pygame.sprite.Sprite):

    def __init__(self, position, size, connections):

        pygame.sprite.Sprite.__init__(self)

        self.position = position
        self.size = size
        self.connections = connections

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
