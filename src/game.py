import pyglet
import pymunk
import pymunk.pyglet_util


class Game:
    def __init__(self):
        self.window = pyglet.window.Window(WIDTH, HEIGHT, "Bounce Game")
        self.space = pymunk.Space()
        self.space.gravity = (0, -900)

        self.player = Player(400, 300, 20, self.space)  # Create player
        Floor(self.space, WIDTH, HEIGHT)  # Create floor

        self.on_ground = False  # Track if the player is on the ground

        # Set up collision handlers
        handler = self.space.add_collision_handler(1, 2)
        handler.begin = self.on_ball_floor_collision
        handler.separate = self.on_ball_leave_floor

        # Register key handler
        self.keys = key.KeyStateHandler()
        self.window.push_handlers(self.keys)

        pyglet.clock.schedule_interval(self.update, 1 / 60.0)
        self.window.event(self.on_draw)

    def on_ball_floor_collision(self, arbiter, space, data):
        """Called when the ball touches the floor."""
        self.on_ground = True
        return True

    def on_ball_leave_floor(self, arbiter, space, data):
        """Called when the ball leaves the floor."""
        self.on_ground = False
        return True

    def update(self, dt):
        self.space.step(dt)  # Advance physics simulation
        self.update_player_controls(dt)

    def update_player_controls(self, dt):
        """Handle player movement based on key input."""
        force = 500

        if self.keys[key.LEFT]:
            self.player.apply_force((-force, 0), (0, -10))  # Left movement

        if self.keys[key.RIGHT]:
            self.player.apply_force((force, 0), (0, -10))  # Right movement

        if self.keys[key.UP] and self.on_ground:
            self.player.jump()  # Jump only if on the ground

    def on_draw(self):
        self.window.clear()
        self.space.debug_draw(pymunk.pyglet_util.DrawOptions())
