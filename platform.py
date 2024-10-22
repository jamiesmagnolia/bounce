import pygame

class Platform(pygame.sprite.Sprite):
    """
    Platform class.
    """

    def __init__(self, x, y, width, height, color):
        """
        Create a Platform object.
        """
        super().__init__(self, x, y, width, height, color)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(top_left=(x, y))

    # def draw(self, screen):
    #     pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))