# import pygame

# class Platform(pygame.sprite.Sprite):
#     """
#     Platform class.
#     """

#     def __init__(self, x, y, width, height, color):
#         super().__init__()  # Initialize the Sprite class
#         self.image = pygame.Surface((width, height))
#         self.image.fill(color)
#         self.rect = self.image.get_rect(topleft=(x, y))

#     # def draw(self, screen):
#     #     pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))