import pygame
from ball import Ball
from platform import Platform

WIDTH = 800
HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce (2024)")
clock = pygame.time.Clock()
running = True
FPS = 60

ball = Ball(400, 300, 20, (255, 0, 0))
platform1 = Platform(300, 500, 200, 40, "darkred")
platforms = [platform1]

# game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray")

    ball.update(platforms)

    ball.draw(screen)

    for platform in platforms:
        platform.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()