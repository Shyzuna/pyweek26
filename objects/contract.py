import pygame

from settings.enums import Colors
from settings import settings


class Contract:

    def __init__(self, contractor, reward, objective):

        self.contractor = contractor
        self.reward = reward
        self.objective = objective
        self.contour = 5
        self.left = objective

    def display(self, screen, windowContour, window, topLeft, fonts, color):
        # Display white window of contract with colored edges
        windowContour.fill(color)
        windowContour.fill(Colors.WHITE.value, window)
        screen.blit(windowContour, topLeft)

        # Display info of contract
        # Replace 200 with length of contract image
        contractorText = fonts['medium'].render('Contractor: ' + self.contractor, 1, Colors.BLACK.value)
        screen.blit(contractorText, (topLeft[0] + 200, topLeft[1] + self.contour * 2))

        rewardText = fonts['medium'].render('Reward: {}'.format(self.reward), 1, Colors.BLACK.value)
        screen.blit(rewardText, (topLeft[0] + 200, topLeft[1] + self.contour * 2 + window.height / 4))

        objectiveText = fonts['medium'].render('Objective: {}'.format(self.objective), 1, Colors.BLACK.value)
        screen.blit(objectiveText, (topLeft[0] + 200, topLeft[1] + self.contour * 2 + 2 * window.height / 4))

        leftText = fonts['medium'].render('Left: {}'.format(self.left), 1, Colors.BLACK.value)
        screen.blit(leftText, (topLeft[0] + 200, topLeft[1] + self.contour * 2 + 3 * window.height / 4))