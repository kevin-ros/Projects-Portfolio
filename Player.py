import pygame
import Config
from Bullet import Bullet

class Player:
    def __init__(self):
        self.speed = Config.PLAYER_SPEED
        self.sprite = pygame.image.load(Config.PLAYER_IMAGE_PATH).convert_alpha()
        self.rect = self.sprite.get_rect()
        self.rect.centerx = Config.WIDTH // 2
        self.rect.bottom = Config.HEIGHT - 20
        self.alive = True
        self.deadSound = pygame.mixer.Sound(Config.PLAYER_DEATH_SOUND)
        self.bullets = []

    def move(self,keys):
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect = self.rect.move(-self.speed, 0)
        if keys[pygame.K_d] and self.rect.right < Config.WIDTH:
            self.rect = self.rect.move(self.speed, 0)
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.append(bullet)

    def update_bullets(self, surface):
        updated_bullets = []
        for bullet in self.bullets:
            bullet.move()
            bullet.draw(surface)
            if bullet.off_screen() == False:
                updated_bullets.append(bullet)

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)
