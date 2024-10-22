import pygame


class Ball:
    """
    Ball class.
    """

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel_x = 0
        self.vel_y = 0
        self.GRAVITY = 0.5
        self.acceleration = 0.5
        self.friction = 0.1
        self.MAX_SPEED = 2.5
        self.on_ground = True
        self.DAMPING_FACTOR = 0.75

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self, platforms):

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
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            if self.vel_x > 0:
                self.vel_x -= self.friction # slowly slow down R
                if self.vel_x < 0: # prevents reversing due to friction
                    self.vel_x = 0
            elif self.vel_x < 0:
                self.vel_x += self.friction # slowly slow down L
                if self.vel_x > 0:
                    self.vel_x = 0  
        
        # print(f"x: {self.x}, y: {self.y}")

        # max speed cap
        if self.vel_x > self.MAX_SPEED:
            self.vel_x = self.MAX_SPEED
        elif self.vel_x < -self.MAX_SPEED:
            self.vel_x = -self.MAX_SPEED

        # position updates based on velocities
        self.x += self.vel_x
        self.y += self.vel_y

        # bounce effect
        if self.y + self.radius > 600: # assume screen height = 600
            self.y = 600 - self.radius # position = just touching the floor
            self.vel_y *= -self.DAMPING_FACTOR # reverse velocity/bounce with damping?  
            self.on_ground = True
          
        # Platform collision and bounce
        for platform in platforms: # only for top of platform
            if (
                self.y + self.radius > platform.y  # Ball touches platform from above
                and self.y - self.radius < platform.y + platform.height  # Stay within platform height
                and self.x > platform.x  # Within platform width
                and self.x < platform.x + platform.width
                and self.vel_y > 0  # Only if falling down
            ):
                self.y = platform.y - self.radius  # Adjust position to top of platform
                self.vel_y *= -self.DAMPING_FACTOR  # Bounce with damping
                self.on_ground = True