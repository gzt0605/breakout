# Ryan Ge
# December 13, 2016
# brick.py

import pygame

class Brick(pygame.sprite.Sprite):

    def __init__(self, width, color):
        '''
        Draw a brick
        :param width: width of the brick
        :param color: color of the brick
        '''
        super().__init__()
        self.BRICK_HEIGHT = 8

        # Draw the brick
        self.surface = pygame.Surface((width, self.BRICK_HEIGHT))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()