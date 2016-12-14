# Ryan Ge
# November 30, 2016
# breakout.py

import pygame, sys, ball, paddle, brick
from pygame.locals import *

def main():
    '''
    Main function for the game
    :return: nothing
    '''

    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    NUM_TURNS = 3

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Initiate and set up a pygame window
    pygame.init()
    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    pygame.display.set_caption('Breakout')
    main_surface.fill(WHITE)

    # Assigninitial values to the variables and set up sprite groups
    life_used = 0

    bricks = pygame.sprite.Group()
    ball_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()

    y_pos = BRICK_Y_OFFSET

    # Loop through each row to set up the bricks
    for color in [RED, ORANGE, YELLOW, GREEN, CYAN]:
        # Two rows for each color
        for i in range(2):
            for k in range(BRICKS_PER_ROW):
                # Draw the individual brick
                block = brick.Brick(BRICK_WIDTH, color)
                block.rect.x = k * (BRICK_WIDTH + BRICK_SEP)
                block.rect.y = y_pos

                # Blit the brick onto the screen and add it to its sprite group
                main_surface.blit(block.surface, block.rect)
                bricks.add(block)

            # Update the y position for each row
            y_pos += block.BRICK_HEIGHT + BRICK_SEP

    # Set up the paddle and add it to its sprite group
    my_paddle = paddle.Paddle(BLACK)
    my_paddle.rect.x = APPLICATION_WIDTH / 2
    my_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    paddle_group.add(my_paddle)

    # Set up the ball
    my_ball = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT)
    my_ball.rect.x = APPLICATION_WIDTH / 2
    my_ball.rect.y = APPLICATION_HEIGHT / 2
    ball_group.add(my_ball)

    # Main pygame loop (for displaying results)
    while True:

        # Inside the loop that plays the game, when there are bricks and lives left
        while bricks.has(bricks) and life_used < NUM_TURNS:

            # Re-draw the whole surface
            main_surface.fill(WHITE)
            main_surface.blit(my_paddle.surface, my_paddle.rect)

            # Update ball position and draw it on the screen
            my_ball.move()
            main_surface.blit(my_ball.surface, my_ball.rect)

            # Detect for collision between the ball and paddle
            if pygame.sprite.spritecollide(my_paddle, ball_group, False):
                my_ball.vy = -my_ball.vy

            # Detect collision between the ball and bricks
            for a_block in bricks:

                # Bounce back the ball and remove the brick if they collide
                if pygame.sprite.spritecollide(a_block, ball_group, False):
                    my_ball.vy = -my_ball.vy
                    bricks.remove(a_block)
                else:
                    # Re-draw the brick if nothing happens
                    main_surface.blit(a_block.surface, a_block.rect)

            # Detect for pygame events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                # Detect mouse movement to move the paddle
                if event.type == MOUSEMOTION:
                    my_paddle.move()

            # Process after the player misses the ball
            if my_ball.rect.bottom > APPLICATION_HEIGHT - PADDLE_Y_OFFSET + abs(my_ball.vy):

                # Test if there are lives left
                life_used += 1
                if life_used == NUM_TURNS:
                    break

                # Respain the ball
                my_ball.rect.x = APPLICATION_WIDTH / 2
                my_ball.rect.y = APPLICATION_HEIGHT / 2
                my_ball.vx = abs(my_ball.vx)
                my_ball.vy = abs(my_ball.vy)

            pygame.display.update()

        # Display game results
        main_surface.fill(WHITE)
        result_font = pygame.font.SysFont("Helvetica", 30)
        if life_used == 3:
            result_label = result_font.render('You Lost!', 1, BLACK)
            main_surface.blit(result_label, (APPLICATION_WIDTH / 3, APPLICATION_HEIGHT / 3))

        else:
            result_label = result_font.render('You Won!', 1, BLACK)
            main_surface.blit(result_label, (APPLICATION_WIDTH / 3, APPLICATION_HEIGHT / 3))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

main()