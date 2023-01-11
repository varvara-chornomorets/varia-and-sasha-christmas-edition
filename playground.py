from cls import Vector, Paddle
import pgzrun
import math

WIDTH = 800
HEIGHT = 800

some_position = Vector(700, 700)
platform = Paddle(some_position)


def draw():
    screen.clear()
    platform.draw()


def update(dt):
    platform.update(dt)


def on_mouse_move(pos):
    platform.look_at(pos)


pgzrun.go()

