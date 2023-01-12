from cls import Vector, Paddle, Ball, Heart, Enemy
import pgzrun
import pygame

WIDTH = 600
HEIGHT = 600

platform_start_position = Vector(700, 500)
ball_start_pos = Vector(17, 20)
platform = Paddle(platform_start_position)
my_ball = Ball(ball_start_pos)
heart = Heart()
enemies = []
for i in range(100, 600, 100):
    enemies.append(Enemy(Vector(i, 100)))


def draw():
    screen.clear()
    platform.draw(screen)
    my_ball.draw(screen)
    heart.draw()
    for enemy in enemies:
        enemy.draw(screen)


def update(dt):
    platform.update(dt)
    my_ball.update(dt)
    for enemy in enemies:
        if enemy.update(screen, my_ball):
            new_velocity = Vector(*enemy.update(screen, my_ball))
            k = 1/(new_velocity.magnitude()/my_ball.velocity.magnitude())
            my_ball.velocity = new_velocity*k
            enemies.remove(enemy)


def on_mouse_move(pos):
    platform.look_at(pos)


pgzrun.go()

