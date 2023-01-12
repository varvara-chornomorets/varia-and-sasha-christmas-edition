from cls import Vector, Paddle, Ball, Heart
import pgzrun
import pygame

WIDTH = 600
HEIGHT = 600

platform_start_position = Vector(700, 500)
ball_start_pos = Vector(17, 20)
platform = Paddle(platform_start_position)
my_ball = Ball(ball_start_pos)
heart = Heart()


def draw():
    screen.clear()
    platform.draw(screen)
    my_ball.draw(screen)
    heart.draw()


def update(dt):
    platform.update(dt)
    my_ball.update(dt)


def on_mouse_move(pos):
    platform.look_at(pos)


pgzrun.go()

