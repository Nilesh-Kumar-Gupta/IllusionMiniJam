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

    spritesheet = pygame.image.load('D:/Pycharm Projects/venv/assets/img/character_sprite/global.png').convert()

    moving_left = False
    moving_right = False

    run = True
    player = Player(spritesheet, 50, 50, 3, 5)

    while run:

        clock.tick(framerate)

        screen.fill((123, 42, 50))

        player.move(moving_left, moving_right)
        player.draw(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                break

            # check for key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                if event.key == pygame.K_d:
                    moving_right = True
                if event.key == pygame.K_ESCAPE:
                    run = False

            # check for ky release
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False

        pygame.display.update()

    pygame.quit()
