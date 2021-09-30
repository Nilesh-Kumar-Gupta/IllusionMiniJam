import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, filename, x, y, scale, speed):
        super().__init__()
        self.speed = speed
        self.direction = 'right'
        self.flip = True

        self.index = 0
        self.animation_list = []

        for i in range(3):
            img = pygame.image.load(f'Assets/Sprites/{filename}{i}.png').convert()
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.animation_list.append(img)

        self.img = self.animation_list[0]
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right):

        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
            if self.direction == 'right':
                self.flip = True
                self.direction = 'left'
        elif moving_right:
            dx = self.speed
            if self.direction == 'left':
                self.flip = True
                self.direction = 'right'

        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        pass

    def draw(self, screen):
        self.img = pygame.transform.flip(self.img, self.flip, False)
        self.flip = False
        screen.blit(self.img, self.rect)
