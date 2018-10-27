import pygame
import os

from settings.enums import Colors
from settings import settings


class Contract:

    def __init__(self, town, reward, objective):

        self.town = town
        self.reward = reward
        self.objective = objective
        self.contour = 5
        self.left = objective
        self.img = pygame.transform.scale(pygame.image.load(os.path.join(settings.GUI_PATH, 'contract.jpg')),
                                          (64, 64))

    def display(self, screen, windowContour, window, topLeft, fonts, color):
        # Display white window of contract with colored edges
        windowContour.fill(color)
        windowContour.fill(Colors.WHITE.value, window)
        screen.blit(windowContour, topLeft)

        # Display image
        imgTopLeft = (topLeft[0] + window.height / 10, topLeft[1] + window.height / 10)
        scaled_img = pygame.transform.scale(self.img, (int(window.width / 4 - window.height / 10), int(window.height * 8 / 10)))
        screen.blit(scaled_img, imgTopLeft)

        # Display info of contract
        # Replace 200 with length of contract image
        townText = fonts['medium'].render('Contractor: ' + self.town, 1, Colors.BLACK.value)
        screen.blit(townText, (topLeft[0] + window.width / 4 + 20, topLeft[1] + self.contour * 2))

        rewardText = fonts['medium'].render('Reward: {}'.format(self.reward), 1, Colors.BLACK.value)
        screen.blit(rewardText, (topLeft[0] + window.width / 4 + 20, topLeft[1] + self.contour * 2 + window.height / 4))

        objectiveText = fonts['medium'].render('Objective: {}'.format(self.objective), 1, Colors.BLACK.value)
        screen.blit(objectiveText, (topLeft[0] + window.width / 4 + 20, topLeft[1] + self.contour * 2 + 2 * window.height / 4))

        leftText = fonts['medium'].render('Left: {}'.format(self.left), 1, Colors.BLACK.value)
        screen.blit(leftText, (topLeft[0] + window.width / 4 + 20, topLeft[1] + self.contour * 2 + 3 * window.height / 4))