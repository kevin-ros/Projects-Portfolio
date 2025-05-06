import pygame
import random
import sys
from Player import Player
from Spaceship import Spaceship
import Config

# Initialization
pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

# Constants
Screen_Width, Screen_Height = Config.WIDTH, Config.HEIGHT
White = (255, 255, 255)
Gray = (100, 100, 100)
Black = (0, 0, 0)

volume = 0.5
brightness = 1.0

screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Alien Invasion")
title_font = pygame.font.SysFont(None, 72)
font = pygame.font.SysFont(None, 48)

menu_background = pygame.image.load("stuff/spacebackground.jpg ")
menu_background = pygame.transform.scale(menu_background, (Screen_Width, Screen_Height))

# Button class
class Button:
    def __init__(self, text, x, y, w, h, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.callback = callback

    def draw(self, screen):
        pygame.draw.rect(screen, Gray, self.rect, border_radius=12)
        text_surf = font.render(self.text, True, White)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.callback()

# Game loop
def game_loop():
    pygame.mixer.music.stop()
    SPAWN_EVENT = Config.SPAWN_SPACESHIP_EVENT
    pygame.time.set_timer(SPAWN_EVENT, 1000)
    background = pygame.image.load("stuff/spacebackground.jpg")

    shoot_cooldown = 200
    last_shot_time = 0

    clock = pygame.time.Clock()
    text_surface = font.render("You Lost!", True, Config.WHITE)
    text_rect = text_surface.get_rect(center=(Config.WIDTH // 2, Config.HEIGHT // 2))

    shade = pygame.Surface((Config.WIDTH, Config.HEIGHT))
    shade.set_alpha(100)
    shade.fill(Config.BLACK)

    spaceships = []
    player = Player()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == SPAWN_EVENT:
                spaceship = Spaceship()
                spaceships.append(spaceship)
                spaceship.spawn_sound.play()
                new_time = random.randint(800, 1500)
                pygame.time.set_timer(SPAWN_EVENT, new_time)

        screen.blit(background, (0, 0))

        for spaceship in list(spaceships):
            spaceship.draw(screen)
            spaceship.fall()
            if spaceship.rect.top > Config.HEIGHT:
                spaceships.remove(spaceship)
            elif spaceship.rect.colliderect(player.rect) and player.alive:
                player.deadSound.play()
                player.alive = False
                spaceships.remove(spaceship)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return

        if player.alive:
            current_time = pygame.time.get_ticks()
            if keys[pygame.K_SPACE]:
                if current_time - last_shot_time >= shoot_cooldown:
                    player.shoot()
                    last_shot_time = current_time
            player.move(keys)
            player.update_bullets(screen)
            player.draw(screen)
        else:
            screen.blit(shade, (0, 0))
            screen.blit(text_surface, text_rect)
        for bullet in list(player.bullets):
                bullet.move()

                if bullet.off_screen():
                    player.bullets.remove(bullet)
                    continue
                for ship in list(spaceships):
                    if bullet.rect.colliderect(ship.rect):
                        player.bullets.remove(bullet)
                        spaceships.remove(ship)
                        break
            # bullet has collided with a spaceship
            # ships_shot +=1

        pygame.display.flip()
        clock.tick(Config.FPS)

# Settings and how-to
def open_settings():
    global volume, brightness
    running = True
    while running:
        screen.fill(Black)
        vol_text = font.render(f"Volume: {volume:.1f} (←/→)", True, White)
        bright_text = font.render(f"Brightness: {brightness:.1f} (↑/↓)", True, White)
        back_text = font.render("Press ESC to go back", True, White)

        screen.blit(vol_text, (100, 200))
        screen.blit(bright_text, (100, 260))
        screen.blit(back_text, (100, 320))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    volume = max(0.0, volume - 0.1)
                elif event.key == pygame.K_RIGHT:
                    volume = min(1.0, volume + 0.1)
                elif event.key == pygame.K_UP:
                    brightness = min(1.0, brightness + 0.1)
                elif event.key == pygame.K_DOWN:
                    brightness = max(0.1, brightness - 0.1)

def how_to_play():
    running = True
    while running:
        screen.fill(Black)
        instructions = [
            "How To Play?",
            "",
            "A / D  : Move your player left and right",
            "SPACE  : Fire at aliens",
            "",
            "Press ESC to return to the main menu",
        ]

        for i, line in enumerate(instructions):
            text = font.render(line, True, White)
            screen.blit(text, (80, 100 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

def quit_game():
    pygame.quit()
    sys.exit()

# Button actions
buttons = [
    Button("Start Game", 300, 180, 200, 60, game_loop),
    Button("Settings", 300, 260, 200, 60, open_settings),
    Button("How To Play", 300, 340, 200, 60, how_to_play),
    Button("Quit", 300, 420, 200, 60, quit_game),
]

# Main menu loop
def main():
    pygame.mixer.music.load("stuff/ambient-cyberpunk-cinematic-8411.mp3")
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1,0.0)
    while True:
        screen.blit(menu_background, (0, 0))
        title_text = title_font.render("Alien Invasion", True, White)
        title_rect = title_text.get_rect(center=(Screen_Width // 2, 80))
        screen.blit(title_text, title_rect)

        for button in buttons:
            button.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.check_click(event.pos)

if __name__ == "__main__":
    main()
#Change arrows to left and right
#Do stuff on maingame.py
