import pygame


class Ball(pygame.sprite.Sprite):
    """
    Ball class.
    """

    def __init__(self, x, y, radius, color):
        """
        Create ball object.
        """
        super().__init__() # initialise Sprite class

        # image surface to draw on
        # rect allows pygame to handle positioning and rendering
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y)) # use rect positioning

        # CONSTANTS
        self.GRAVITY = 0.5
        self.MAX_SPEED = 2.5
        self.DAMPING_FACTOR = 0.75

        self.vel_x = 0
        self.vel_y = 0
        self.acceleration = 0.5
        self.friction = 0.1
        self.on_ground = True

    def update(self, platforms):
        """
        Updates ball's attributes (e.g. positions, velocity)
        """

        # constant gravity applies to the ball
        self.vel_y += self.GRAVITY

        keys = pygame.key.get_pressed()
        
        # horizontal movements
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x += -self.acceleration
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x += self.acceleration   

        # jump 
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.vel_y -= 10
            self.on_ground = False

        # friction when no key is pressed
        if not keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x *= (1 - self.friction)
        
        # max cap on horizontal velocity
        self.vel_x = max(min(self.vel_x, self.MAX_SPEED), -self.MAX_SPEED)

        # position updates based on velocities
        self.x += self.vel_x
        self.y += self.vel_y

        # screen floor collisions
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.vel_y *= -self.DAMPING_FACTOR
            self.on_ground = True        
          
        # Platform collision and bounce
        collided_platform = pygame.sprite.spritecollideany(self, platforms)
        if collided_platform:
            self.rect.bottom = collided_platform.rect.top
            self.vel_y *= -self.DAMPING_FACTOR
            self.on_ground = True