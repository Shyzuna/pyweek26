import pygame

from settings import settings

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
                elif event.key == pygame.K_ESCAPE:
                    self.done = True
            elif event.type == pygame.KEYUP:
                if event.key in self.directionState.keys():
                    self.directionState[event.key] = False
            else:
                # Mouse scrolling
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x < settings.SCROLL_MOUSE_MARGIN:
                    self.directionState[pygame.K_LEFT] = True
                else:
                    self.directionState[pygame.K_LEFT] = False

                if mouse_x > settings.SCROLL_MOUSE_MAX_X:
                    self.directionState[pygame.K_RIGHT] = True
                else:
                    self.directionState[pygame.K_RIGHT] = False

                if mouse_y < settings.SCROLL_MOUSE_MARGIN:
                    self.directionState[pygame.K_UP] = True
                else:
                    self.directionState[pygame.K_UP] = False

                if mouse_y > settings.SCROLL_MOUSE_MAX_Y:
                    self.directionState[pygame.K_DOWN] = True
                else:
                    self.directionState[pygame.K_DOWN] = False


inputManager = InputManager()