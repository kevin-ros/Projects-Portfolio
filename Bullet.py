import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.speed = 15
        self.sprite = pygame.image.load("stuff/finalbullet.png").convert_alpha()
        self.rect = self.sprite.get_rect(center=(x,y))

    def move(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)
    def off_screen(self):
        return self.rect.bottom < 0