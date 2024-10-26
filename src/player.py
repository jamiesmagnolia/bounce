import pyglet
import pymunk
import pymunk.pyglet_util


class Player:
    """
    The ball.
    """

    def __init__(self, x, y, radius, space):
        """
        Create a bouncy ball.
        """
        mass = 1
        moment = pymunk.moment_for_circle(mass=mass, inner_radius=0, outer_radius=radius)

        self.body = pymunk.Body(mass, body_type=pymunk.Body.DYNAMIC)
        self.body.position = (x, y)

        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 0.9
        self.shape.friction = 1.0
        self.shape.collision_type = 1

        space.add(self.body, self.shape)

    def apply_force(self, force, offset=(0, 0)):
        """Apply force to the player ball."""
        self.body.apply_force_at_local_point(force, offset)

    def jump(self):
        """Apply a jump impulse."""
        self.body.apply_impulse_at_local_point((0, 3000))

    def is_on_ground(self):
        """Check if the player is near the ground."""
        return self.body.position.y <= 70  # Adjust based on floor height