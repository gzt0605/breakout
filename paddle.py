# Ryan Ge
# December 9, 2016
# Paddle.py

import pygame

class Paddle(pygame.sprite.Sprite):

    def __init__(self, color):
        '''
        Initiate the variables for paddle class
        :param color: color of the paddle
        '''
        super().__init__()
        self.WIDTH = 60
        self.HEIGHT = 10

        # Draw the paddle
        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()

    def move(self):
        '''
        Move the paddle when mouse is moved
        :return: nothing
        '''
        x_pos, _ = pygame.mouse.get_pos()

        # Make the paddle at the center of the paddle
        x_pos -= self.WIDTH / 2

        # Prevent the paddle from moving outside the window
        if x_pos <= 0:
            self.rect.x = 0
        elif x_pos >= 340:
            self.rect.x = 340
        else:
            self.rect.x = x_pos