from cls import Vector, Paddle, Ball, Heart, Obstacle, Obstacle2
import pgzrun
import pygame

WIDTH = 600
HEIGHT = 600

platform_start_position = Vector(700, 500)
ball_start_pos = Vector(17, 20)
platform = Paddle(platform_start_position)
my_ball = Ball(ball_start_pos)
heart = Heart()
obstacles = []
obstacles2 = []
for i in range(100, 600, 100):
    obstacles.append(Obstacle(Vector(i, 100)))
for i in range(75, 600, 150):
    obstacles2.append(Obstacle2(Vector(i, 200)))


def draw():
    screen.clear()
    platform.draw(screen)
    my_ball.draw(screen)
    heart.draw()
    for obstacle in obstacles:
        obstacle.draw(screen)
    for obstacle in obstacles2:
        obstacle.draw(screen)


def update(dt):
    platform.update(dt)
    my_ball.update(dt)
    for obstacle in obstacles:
        if obstacle.update(screen, my_ball):
            new_velocity = Vector(*obstacle.update(screen, my_ball))
            k = 1/(new_velocity.magnitude()/my_ball.velocity.magnitude())
            my_ball.velocity = new_velocity*k
            obstacles.remove(obstacle)
    for obstacle in obstacles2:
        if obstacle.update(screen, my_ball) == 1:
            my_ball.velocity.y = -my_ball.velocity.y
            obstacles2.remove(obstacle)
        elif obstacle.update(screen, my_ball) == 2:
            my_ball.velocity.x = -my_ball.velocity.x
            obstacles2.remove(obstacle)


def on_mouse_move(pos):
    platform.look_at(pos)


pgzrun.go()

