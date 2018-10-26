import pygame

from settings.enums import Colors
from settings import settings


class Contract:

    def __init__(self, contractor, reward, objective):

        self.CONTRACTS_WINDOW_WIDTH = settings.SCREEN_WIDTH - settings.TILE_WIDTH * settings.CONTRACTS_WINDOW_GAP_X
        self.CONTRACTS_WINDOW_HEIGHT = settings.SCREEN_HEIGHT - settings.TILE_HEIGHT * settings.CONTRACTS_WINDOW_GAP_Y
        self.contractor = contractor
        self.reward = reward
        self.objective = objective
        self.contour = 5
        self.window = pygame.Rect(self.contour,
                                  self.contour,
                                  self.CONTRACTS_WINDOW_WIDTH,
                                  (self.CONTRACTS_WINDOW_HEIGHT - 1 * settings.TILE_HEIGHT) / settings.MAX_AVAILABLE_CONTRACTS)
        self.windowContour = pygame.Surface((self.CONTRACTS_WINDOW_WIDTH + 2 * self.contour,
                                             (self.CONTRACTS_WINDOW_HEIGHT - 1 * settings.TILE_HEIGHT) / settings.MAX_AVAILABLE_CONTRACTS
                                             + 2 * self.contour))

    def display(self, screen, topLeft, fonts, color):
        self.windowContour.fill(color)
        self.windowContour.fill(Colors.WHITE.value, self.window)
        screen.blit(self.windowContour, topLeft)

        contractorText = fonts['medium'].render('Contractor: ' + self.contractor, 1, Colors.BLACK.value)
        screen.blit(contractorText, (topLeft[0] + 200, topLeft[1] + self.contour * 2))

        rewardText = fonts['medium'].render('Reward: {}'.format(self.reward), 1, Colors.BLACK.value)
        screen.blit(rewardText, (topLeft[0] + 200, topLeft[1] + self.contour * 2 + self.window.height / 4))

        objectiveText = fonts['medium'].render('Objective: {}'.format(self.objective), 1, Colors.BLACK.value)
        screen.blit(objectiveText, (topLeft[0] + 200, topLeft[1] + self.contour * 2 + 2 * self.window.height / 4))

