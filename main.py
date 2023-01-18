from cls import Vector, Paddle, Ball, Heart, Obstacle, Obstacle2, HeavyObstacle
import pgzrun
import pygame
import math

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
obstacles = []
obstacles2 = []
obstacles3 = []
for i in range(100, 600, 100):
    obstacles.append(Obstacle(Vector(i, 100)))
#for i in range(75, 600, 150):
#    obstacles2.append(Obstacle2(Vector(i, 200)))
for i in range(75, 600, 150):
    obstacles3.append(HeavyObstacle(Vector(i, 200)))


def draw():
    screen.clear()
    platform.draw(screen)
    my_ball.draw(screen)
    for i in range(0, number_of_lives):
        position = Vector(HEART_START_POSITION.x + DISTANCE_BETWEEN_HEARTS * i, HEART_START_POSITION.y)
        Heart(position).draw()
    for obstacle in obstacles:
        obstacle.draw(screen)
    for obstacle in obstacles2:
        obstacle.draw(screen)
    for obstacle in obstacles3:
        obstacle.draw(screen)


def count_lives():
    global number_of_lives
    if my_ball.ball_is_out():
        number_of_lives = number_of_lives - 1


def update(dt):
    platform.update(dt)
    my_ball.update(dt)
    count_lives()

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
        elif obstacle.update(screen, my_ball) == 3:
            my_ball.velocity.x = -my_ball.velocity.x
            my_ball.velocity.y = -my_ball.velocity.y
            obstacles2.remove(obstacle)

    for obstacle in obstacles3:
        if obstacle.update(screen, my_ball) == 1:
            my_ball.velocity.y = -my_ball.velocity.y
            obstacle.lives -= 1
            if obstacle.lives == 0:
                obstacles3.remove(obstacle)
        elif obstacle.update(screen, my_ball) == 2:
            my_ball.velocity.x = -my_ball.velocity.x
            obstacle.lives -= 1
            if obstacle.lives == 0:
                obstacles3.remove(obstacle)
        elif obstacle.update(screen, my_ball) == 3:
             # k = 1 / (math.sqrt(2) / my_ball.velocity.magnitude())
             # if my_ball.position.x < obstacle.position.x:
             #     my_ball.velocity.x = -1 * k
             # elif my_ball.position.x > obstacle.position.x:
             #     my_ball.velocity.x = 1 * k
             # if my_ball.position.y < obstacle.position.y:
             #     my_ball.velocity.y = -1 * k
             # elif my_ball.position.y > obstacle.position.y:
             #     my_ball.velocity.y = 1 * k
            tempvelocity = my_ball.velocity.x
            my_ball.velocity.x = my_ball.velocity.y
            my_ball.velocity.y = tempvelocity
            obstacle.lives -= 1
            if obstacle.lives == 0:
                obstacles3.remove(obstacle)


def on_mouse_move(pos):
    platform.look_at(pos)


pgzrun.go()

