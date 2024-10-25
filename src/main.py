import os
import pyglet
import pymunk
import pymunk.pyglet_util

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
music_player.play()

balls = []

# create the floor -> a static body
def create_floor():
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, (0, 50), (WIDTH, 50), 5) # floor segment
    shape.elasticity = 0.8
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

def create_ball(x, y, radius=20):
    mass = 1
    moment = pymunk.moment_for_circle(mass, 0, radius) # calculate moment of inertia
    body = pymunk.Body(mass, moment) # create a dynamic body (affected by forces)
    body.position = x, y # set starting position of the ball

    shape = pymunk.Circle(body, radius=radius) # create a circular shape
    shape.elasticity = 0.9 # elasticity = bouncy

    space.add(body, shape) # add ball to physics space
    balls.append((body, shape)) # store ball for tracking


# a mouse press will "spawn" or create a ball
@window.event
def on_mouse_press(x, y, button, modifiers):
    create_ball(x, y)

# draw event -> think a "render" function that quite literally renders everything
@window.event # decorator
def on_draw():
    window.clear() # clear before drawing
    space.debug_draw(draw_options) # visualize physics
    # for ball in balls:
    #     ball.draw()

def update(dt):
    space.step(dt) # step physics simulation forward by dt seconds

# schedule to update function to run at 60 FPS
pyglet.clock.schedule_interval(update, 1/60.0)

# run pyglet event loop
pyglet.app.run()
