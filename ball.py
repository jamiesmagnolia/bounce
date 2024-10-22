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
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # screen floor collisions
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.vel_y *= -self.DAMPING_FACTOR
            self.on_ground = True      

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                self.handle_collision(platform=platform)  
          
        # Platform collision and bounce
        # collided_platform = pygame.sprite.spritecollideany(self, platforms)
        # if collided_platform:
        #     if self.rect.colliderect(platform.rect):
        #         self.handle_collision(platform)

    def handle_collision(self, platform):

        # positive dx = ball's center is to the right of platform's center
        # negative dx = ball's center is to the left of platform's center
        dx = self.rect.centerx - platform.rect.centerx # horizontal distance

        # positive dy = ball's center is below platform's center
        # negative dy = ball's center is above platform's center
        dy = self.rect.centery - platform.rect.centery # vertical distance

        # we're using abs because we're calculating the magnitude of the distance
        # we're interested in the distance (how far) and not the direction
        # if horizontal (dx) > vertical (dy) distance:
        # the ball is more likely hitting the platform from the side
        # if dy > dx: ball is likely hitting the platform from above or below
        if abs(dx) > abs(dy):

            if dx > 0:
                self.rect.left = platform.rect.right

                if self.vel_x < 0:
                    self.vel_x = 0
                # self.vel_x *= -self.DAMPING_FACTOR
            else:
                self.rect.right = platform.rect.left
                if self.vel_x > 0:
                    self.vel_x = 0
                # self.vel_x *= -self.DAMPING_FACTOR

        else:
            
            if dy > 0:
                self.rect.top = platform.rect.bottom
                if self.vel_y < 0:
                    self.vel_y = 0
            else:
                self.rect.bottom = platform.rect.top

                if self.vel_y > 0:
                    self.vel_y *= -self.DAMPING_FACTOR
                    self.on_ground = True
