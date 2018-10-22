import pygame
import math
from settings import settings
import modules.guiManager


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

        self.mousePos = (0, 0)
        self.mousePosInTiles = (1, 1)
        self.keyPressed = None
        self.done = False

    def loop(self):
        self.keyPressed = None
        for event in pygame.event.get():
            self.refreshMousePos()
            modules.guiManager.guiManager.checkMousePosition(self.mousePos)
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key in self.directionState.keys():
                    self.directionState[event.key] = True
                elif event.key == pygame.K_ESCAPE:
                    self.done = True
                else:
                    self.keyPressed = event.key

            elif event.type == pygame.KEYUP:
                if event.key in self.directionState.keys():
                    self.directionState[event.key] = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                modules.guiManager.guiManager.handleMouseButton(True, self.mousePos)
            elif event.type == pygame.MOUSEBUTTONUP:
                modules.guiManager.guiManager.handleMouseButton(False, self.mousePos)
            else:
                # Mouse scrolling
                mouse_x, mouse_y = self.mousePos
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

    def refreshMousePos(self):
        self.mousePos = pygame.mouse.get_pos()
        # TODO: calculate from cursor position on map and not on screen
        self.mousePosInTiles = (math.ceil(self.mousePos[0] / settings.TILES_NUM_WIDTH),
                                math.ceil(self.mousePos[1] / settings.TILES_NUM_HEIGHT))

inputManager = InputManager()