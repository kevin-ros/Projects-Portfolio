import pygame
import random
import Config

class Spaceship:
    def __init__(self):
        self.type = random.choice(["big", "med", "small","tiny"])
        self.speed = Config.SPACESHIP_SPEEDS[self.type]
        image_path = random.choice(Config.SPACESHIP_IMAGE_PATHS[self.type])
        self.sprite = pygame.image.load(image_path).convert_alpha()
        self.rect = self.sprite.get_rect()
        max_x = max(0, Config.WIDTH - self.rect.width)
        self.rect.topleft = (random.randint(0,max_x), 0)

        spawn_sound_path = random.choice(Config.SPACESHIP_SPAWN_SOUNDS)
        self.spawn_sound = pygame.mixer.Sound(spawn_sound_path)

    def fall(self):
        self.rect = self.rect.move(0,self.speed)

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)