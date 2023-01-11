from cls import Vector, Paddle, Ball
import pgzrun

WIDTH = 600
HEIGHT = 600

platform_start_position = Vector(700, 500)
ball_start_pos = Vector(17, 20)
platform = Paddle(platform_start_position)
my_ball = Ball(ball_start_pos)


def draw():
    screen.clear()
    platform.draw(screen)
    my_ball.draw(screen)


def update(dt):
    platform.update(dt)
    my_ball.update(dt)


def on_mouse_move(pos):
    platform.look_at(pos)


pgzrun.go()

