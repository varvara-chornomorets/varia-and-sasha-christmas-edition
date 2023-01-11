from cls import Vector, Paddle
import pgzrun

WIDTH = 800
HEIGHT = 600

some_position = Vector(700, 500)
platform = Paddle(some_position)


def draw():
    screen.clear()
    platform.draw(screen)


def update(dt):
    platform.update(dt)


def on_mouse_move(pos):
    platform.look_at(pos)


pgzrun.go()

