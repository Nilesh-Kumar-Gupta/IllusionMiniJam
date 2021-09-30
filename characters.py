import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, spritesheet, x, y, scale, speed):
        super().__init__()
        self.speed = speed
        self.direction = 'right'
        self.flip = False
        self.sprite = pygame.Surface((30, 40))
        self.sprite.set_colorkey((0, 0, 0))
        self.sprite.blit(spritesheet, (0, 0), (0, 0, 30, 40))
        self.sprite = pygame.transform.scale(self.sprite, (int(self.sprite.get_width() * scale), int(self.sprite.get_height() * scale)))
        self.rect = self.sprite.get_rect()
        self.rect.center = (x, y)


    def move(self, moving_left, moving_right):

        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
            if self.direction == 'right':
                self.flip = True
                self.direction = 'left'
        if moving_right:
            dx = self.speed
            if self.direction == 'left':
                self.flip = True
                self.direction = 'right'

        self.rect.x += dx
        self.rect.y += dy


    def draw(self, screen):
        self.sprite = pygame.transform.flip(self.sprite, self.flip, False)
        self.flip = False
        screen.blit(self.sprite, self.rect)
