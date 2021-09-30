import pygame
from characters import Player


def start_game(screen_width):
    pygame.init()

    # frame rate
    clock = pygame.time.Clock()
    framerate = 60

    screen_height = int(0.8 * screen_width)

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Shooter')

    moving_left = False
    moving_right = False

    run = True
    player = Player('ghost_char', 100, 100, 2, 5)

    while run:

        clock.tick(framerate)

        screen.fill((0, 0, 0))

        player.move(moving_left, moving_right)
        player.draw(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                break

            # check for key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    break
                if event.key == pygame.K_a:
                    moving_left = True
                    moving_right = False
                elif event.key == pygame.K_d:
                    moving_right = True
                    moving_left = False

            # check for key release
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False

        pygame.display.update()

    pygame.quit()
