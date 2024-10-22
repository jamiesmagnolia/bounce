import pygame
from ball import Ball
from platform import Platform

# CONSTANTS
WIDTH = 800
HEIGHT = 600
FPS = 60

# Initialise game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce (2024)")
clock = pygame.time.Clock()

# Creating game objects.
ball = Ball(400, 300, 20, (255, 0, 0))
platform1 = Platform(300, 500, 200, 40, "darkred")

# Create sprite groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# Add sprites to groups
all_sprites.add(ball)
platforms.add(platform1)


# game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(platforms)

    screen.fill("gray")
    
    platforms.draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()