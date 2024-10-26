import os
import pyglet
import pymunk
import pymunk.pyglet_util
from pyglet.window import key

WIDTH = 800
HEIGHT = 600

# pyglet window
window = pyglet.window.Window(WIDTH, HEIGHT, "Bounce")

# pymunk physics space
space = pymunk.Space()
space.gravity = (0, -900) # TRY: change to (0, -500)

# pymunk debug draw setup - to see physics objects
draw_options = pymunk.pyglet_util.DrawOptions()

# music
music = pyglet.media.load('../assets/PitcherPerfectTheme.wav', streaming=False)
music_player = pyglet.media.Player()
music_player.queue(music)
music_player.loop = True
# music_player.play()

balls = []

# create the floor -> a static body
def create_floor():
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, (0, 50), (WIDTH, 50), 5) # floor segment
    shape.elasticity = 0.8
    shape.friction = 1.0
    space.add(body, shape)

def create_walls():
    # left wall
    wallL_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    wallL_shape = pymunk.Segment(wallL_body, (0, 50), (0, HEIGHT), 5)
    wallL_shape.elasticity = 0.8
    space.add(wallL_body, wallL_shape)

    # right wall
    wallR_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    wallR_shape = pymunk.Segment(wallR_body, (WIDTH, 50), (WIDTH, HEIGHT), 5)
    wallR_shape.elasticity = 0.8
    space.add(wallR_body, wallR_shape)

# function calls - create floor, walls
create_floor()
create_walls()

def create_player(): # where the player is a ball
    global player_ball
    mass = 1
    radius = 20
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment, body_type=pymunk.Body.DYNAMIC)
    body.position = (400, 300)

    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.9

    body.linear_damping = 0.1
    body.angular_damping = 0.05

    space.add(body, shape)
    player_ball = body

create_player()

# controls
keys = key.KeyStateHandler()
window.push_handlers(keys)

def update_player_ball(dt):
    linear_force = 500 # force to apply to player's ball to move
    torque = 500 # for rotation

    if keys[key.LEFT]:
        player_ball.apply_force_at_local_point((-linear_force, 0))
        player_ball.torque += torque

    if keys[key.RIGHT]:
        player_ball.apply_force_at_local_point((linear_force, 0))
        player_ball.torque -= torque

    if keys[key.UP]:
        # player_ball.apply_force_at_local_point((0, force))
        player_ball.apply_impulse_at_local_point((0, 25))
    
    if keys[key.DOWN]:
        player_ball.apply_force_at_local_point((0, -linear_force))


# a mouse press will "spawn" or create a ball
# @window.event
# def on_mouse_press(x, y, button, modifiers):
#     create_ball(x, y)

# draw event -> think a "render" function that quite literally renders everything
@window.event # decorator
def on_draw():
    window.clear() # clear before drawing
    space.debug_draw(draw_options) # visualize physics
    # for ball in balls:
    #     ball.draw()

# update physics
def update(dt):
    space.step(dt) # step physics simulation forward by dt seconds
    update_player_ball(dt)

# schedule to update function to run at 60 FPS
pyglet.clock.schedule_interval(update, 1/60.0)

# run pyglet event loop
pyglet.app.run()
