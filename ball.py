import pygame


class Ball(pygame.sprite.Sprite):
    """
    Ball class.
    At the moment, player input is handled in this class as well. # TODO: refactor into separate input management
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

        self.radius = radius
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
        
        # horizontal movement management
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x += -self.acceleration
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x += self.acceleration   

        # jump 
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and (self.on_ground is True):
            self.vel_y -= 10
            self.on_ground = False

        # friction when no key is pressed
        if not (keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d]):
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

        dx = self.rect.centerx - platform.rect.centerx
        dy = self.rect.centery - platform.rect.centery

        

        # # vertical collisions
        # # ball falls and lands on platform
        # if self.vel_y > 0 and self.rect.bottom >= platform.rect.top: # 5 pixels tolerance due to rounding errors
        #     self.rect.bottom = platform.rect.top
        #     self.vel_y *= -self.DAMPING_FACTOR
        #     self.on_ground = True

        # # ball jumps and hits platform from bottom
        # elif self.vel_y < 0 and self.rect.top <= platform.rect.bottom:
        #     self.rect.top = platform.rect.bottom
        #     self.vel_y *= -self.DAMPING_FACTOR

        # # if abs(dy) > abs(dx):
        # elif self.vel_x > 0 and self.rect.right >= platform.rect.left:
        #     # Ball hits the left side of the platform
        #     self.rect.right = platform.rect.left
        #     self.vel_x = 0  # Reverse horizontal velocity

        # elif self.vel_x < 0 and self.rect.left <= platform.rect.right:
        #     # Ball hits the right side of the platform
        #     self.rect.left = platform.rect.right
        #     self.vel_x = 0  # Reverse horizontal velocity
            
        # else:
        
        # if self.vel_x > 0 and self.rect.right >= platform.rect.left:
        #     self.rect.right = platform.rect.left
        #     self.vel_x *= -self.DAMPING_FACTOR
        #     # self.vel_x = 0

        # elif self.vel_x > 0 and self.rect.left <= platform.rect.right:
        #     self.rect.left = platform.rect.right
        #     self.vel_x *= -self.DAMPING_FACTOR
        #     # self.vel_x = 0

        # attempt 2
        # # collision with top of platform
        # if self.rect.bottom > platform.rect.top:
        #     self.rect.bottom = platform.rect.top
        #     self.vel_y *= -self.DAMPING_FACTOR
        #     self.on_ground = True # consider a platform top a ground

        # # collision of the top of the ball with the bottom of the platform
        # if self.rect.top < platform.rect.bottom:
        #     self.rect.top = platform.rect.bottom
        #     self.vel_y *= self.DAMPING_FACTOR

        # # collision of the right side of the ball with the left side of a platform
        # if self.rect.right > platform.rect.left:
        #     self.rect.right = platform.rect.left
        #     self.vel_x *= -self.DAMPING_FACTOR


        # # Calculate the difference in position between ball and platform
        # dx = self.rect.centerx - platform.rect.centerx  # Horizontal distance
        # dy = self.rect.centery - platform.rect.centery  # Vertical distance

        # # If vertical collision (ball lands on platform from above)
        # if abs(dy) < platform.rect.height / 2 + self.radius and self.vel_y > 0:
        #     # Ensure the ball lands on the platform's top
        #     self.rect.bottom = platform.rect.top
        #     self.vel_y *= -self.DAMPING_FACTOR # bounce, slowdown, stop
        #     self.on_ground = True  # Mark the ball as on the ground

        # # Handle horizontal collisions if not landing
        # elif abs(dx) < platform.rect.width / 2 + self.radius:
        #     if dx > 0:  # Ball hits from the right
        #         self.rect.left = platform.rect.right
        #         if self.vel_x < 0:
        #             self.vel_x *= -self.DAMPING_FACTOR
        #     else:  # Ball hits from the left
        #         self.rect.right = platform.rect.left
        #         if self.vel_x > 0:
        #             self.vel_x *= -self.DAMPING_FACTOR

        pass