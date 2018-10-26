import pygame

from settings.enums import Colors
from settings import settings


class Contract:

    def __init__(self, contractor, reward, objective):

        self.contractor = contractor
        self.reward = reward
        self.objective = objective
        self.contour = 5
        self.window = pygame.Rect(self.contour,
                                  self.contour,
                                  settings.CONTRACTS_WINDOW_WIDTH,
                                  settings.CONTRACTS_WINDOW_HEIGHT / settings.MAX_AVAILABLE_CONTRACTS)
        self.windowContour = pygame.Surface((settings.CONTRACTS_WINDOW_WIDTH + 2 * self.contour,
                                             settings.CONTRACTS_WINDOW_HEIGHT / settings.MAX_AVAILABLE_CONTRACTS + 2 * self.contour))

    def display(self, screen, topLeft, fonts):
        self.windowContour.fill(Colors.BLACK.value)
        self.windowContour.fill(Colors.WHITE.value, self.window)
        screen.blit(self.windowContour, topLeft)
        # TODO: blit text to display contract info

