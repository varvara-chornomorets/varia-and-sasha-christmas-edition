from cls import Vector, Paddle, Ball, Heart
import pgzrun
import pygame

WIDTH = 600
HEIGHT = 600

platform_start_position = Vector(700, 500)
ball_start_pos = Vector(17, 20)
platform = Paddle(platform_start_position)
my_ball = Ball(ball_start_pos)
number_of_lives = 3
HEART_START_POSITION = Vector(20, 20)
DISTANCE_BETWEEN_HEARTS = 23
positions = []


def draw():
    screen.clear()
    platform.draw(screen)
    my_ball.draw(screen)
    for i in range(0, number_of_lives):
        position = Vector(HEART_START_POSITION.x + DISTANCE_BETWEEN_HEARTS * i, HEART_START_POSITION.y)
        Heart(position).draw()


def count_lives():
    global number_of_lives
    if my_ball.ball_is_out():
        number_of_lives = number_of_lives - 1



def update(dt):
    platform.update(dt)
    my_ball.update(dt)
    count_lives()



def on_mouse_move(pos):
    platform.look_at(pos)


pgzrun.go()

