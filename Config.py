import pygame

WIDTH = 800
HEIGHT = 600
FPS = 60

SPAWN_SPACESHIP_EVENT = pygame.USEREVENT + 1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PLAYER_SPEED = 12
PLAYER_IMAGE_PATH = "stuff/fighterjet2.0.jpg.png"
PLAYER_DEATH_SOUND = "stuff/pixel-death-66829.mp3"

SPACESHIP_SPEEDS = {
    "big": 8,
    "med": 7,
    "small": 9,
    "tiny": 6
}

SPACESHIP_IMAGE_PATHS = {
    "big": ["stuff/spaceship2.0.png"] * 4,
    "med": ["stuff/spaceship2.0.png"] * 2,
    "small": ["stuff/spaceship2.0.png"] * 2,
    "tiny": ["stuff/spaceship2.0.png"] * 2
}
SPACESHIP_SPAWN_SOUNDS = [
    "stuff/item_respawn-91422.mp3",
    "stuff/take-item-sound-effect-163073.mp3",
]
