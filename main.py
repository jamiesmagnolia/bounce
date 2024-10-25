import pyglet
import pymunk
import pymunk.pyglet_util

WIDTH = 800
HEIGHT = 600

# pyglet window
window = pyglet.window.Window(WIDTH, HEIGHT, "Bounce")

# pymunk physics space
space = pymunk.Space()
space.gravity = (0, -900)

# pymunk debug draw setup - to see physics objects
draw_options = pymunk.pyglet_util.DrawOptions()

def create_floor():
    body = pymunk.Body(body_type=pymunk.Body.STATIC)

balls = []

def draw_circle(x, y, radius=20):
    circle = pyglet.shapes.Circle(x, y, radius, color=(255, 0, 0))
    balls.append(circle)

@window.event
def on_mouse_press(x, y, button, modifiers):
    draw_circle(x, y)


@window.event # decorator
def on_draw():
    window.clear()
    for ball in balls:
        ball.draw()

pyglet.app.run()
