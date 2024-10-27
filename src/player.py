import pyglet
import pymunk
import pymunk.pyglet_util
import typing

class Player:

    def __init__(self, space: pymunk.Space, x: int = 400, y: int = 300, radius: int = 20):
        """
        Create a bouncy ball object.
        :space:
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

    def apply_force(self, force: int, offset: Tuple[int, int] = (0, 0)) -> None:
        """Apply force to the player ball."""
        self.body.apply_force_at_local_point(force, offset)

    def jump(self) -> None:
        """
        Apply a jump impulse.
        
        # TODO: Adjust jump to be more "burst" and less "continuous flying"
        The jump action is supposedly "on impulse" (think: a burst of energy).
        We don't want the ball to float and fly, or move in a general upwards motion 
        if it's not touching the ground.
        
        """
        self.body.apply_impulse_at_local_point((0, 250)) # 250 looks realistic-ish but 3000 just shoots it upwards.

    def is_on_ground(self) -> bool:
        """Check if the player is near the ground."""
        return self.body.position.y <= 70  # Adjust based on floor height