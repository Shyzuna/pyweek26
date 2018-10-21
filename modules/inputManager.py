import pygame

class InputManager:

    def __init__(self):
        pass

    def init(self):
        self.directionState = {
            pygame.K_UP: False,
            pygame.K_DOWN: False,
            pygame.K_LEFT: False,
            pygame.K_RIGHT: False,
        }

        self.done = False

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key in self.directionState.keys():
                    self.directionState[event.key] = True
            elif event.type == pygame.KEYUP:
                if event.key in self.directionState.keys():
                    self.directionState[event.key] = False


inputManager = InputManager()