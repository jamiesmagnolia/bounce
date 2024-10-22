import pygame
import os
from ball import Ball
from platform import Platform

# Set the position of the window (100 pixels from the left, 50 from the top)
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,50'

# CONSTANTS
WIDTH = 800
HEIGHT = 600
FPS = 60

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialise game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce (2024)")
clock = pygame.time.Clock()

# Initialise pygame mixer for bg-music
pygame.mixer.init()
pygame.mixer.music.load("PitcherPerfectTheme.wav")
pygame.mixer.music.play(-1) # loop music

# Creating game objects.
ball = Ball(400, 300, 20, (255, 0, 0))
platform1 = Platform(300, 300, 200, 40, "darkred")

# Create sprite groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# Add sprites to groups
all_sprites.add(ball)
platforms.add(platform1)

# misc
button_rect = pygame.Rect(700, 520, 50, 50)
music_on = True

# game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                if music_on: 
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                music_on = not music_on # toggle music state?

    all_sprites.update(platforms)

    screen.fill("gray")

    platforms.draw(screen)
    all_sprites.draw(screen)

    # music button
    button_color = GREEN if music_on else RED
    pygame.draw.rect(screen, button_color, button_rect)

     # Draw button text
    # font = pygame.font.Font(None, 36)
    # text = font.render("Music: On" if music_on else "Music: Off", True, BLACK)
    # text_rect = text.get_rect(center=button_rect.center)
    # screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.mixer.music.stop()
pygame.quit()