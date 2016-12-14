# Ryan Ge
# December 7, 2016
# ball.py

import pygame, random

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight):
        '''
        Initiate variables for ball class
        :param color: color of the ball
        :param windowWidth: width of the window
        :param windowHeight: height of the window
        '''
        super().__init__()
        self.RADIUS = 10
        self.window_width = windowWidth
        self.window_height = windowHeight

        # Draw the ball
        self.surface = pygame.Surface((self.RADIUS, self.RADIUS))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()

        # Set up ball speed
        self.vy = 8
        self.vx = 5
        if random.random() > 0.5:
            self.vx = -self.vx

    def move(self):
        '''
        Move the ball, and correct direction if collides the wall
        :return: nothing
        '''
        if self.rect.right >= self.window_width or self.rect.left <= 0:
            self.vx = -self.vx
        if self.rect.top <= 0:
            self.vy = -self.vy

        self.rect.left += self.vx
        self.rect.top += self.vy