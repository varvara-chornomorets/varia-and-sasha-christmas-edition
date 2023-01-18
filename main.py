from pgzero.actor import Actor

from cls import Vector, Paddle, Bonus, Ball, Heart, Obstacle, Obstacle2
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
obstacles = []
obstacles2 = []
for i in range(100, 600, 100):
    obstacles.append(Obstacle(Vector(i, 100)))
for i in range(75, 600, 150):
    obstacles2.append(Obstacle2(Vector(i, 200)))

is_over = False
bonuses = []
start_time = pygame.time.get_ticks()


def draw():
    screen.clear()
    platform.draw(screen)
    my_ball.draw(screen)
    for bonus in bonuses:
        bonus.draw()
    for i in range(0, number_of_lives):
        position = Vector(HEART_START_POSITION.x + DISTANCE_BETWEEN_HEARTS * i, HEART_START_POSITION.y)
        Heart(position).draw()
    for obstacle in obstacles:
        obstacle.draw(screen)
    for obstacle in obstacles2:
        obstacle.draw(screen)
    if is_over:
        if number_of_lives == 0:
            game_over = Actor("game", center=(WIDTH/2, HEIGHT/2))
        else:
            game_over = Actor("won", center=(WIDTH/2, HEIGHT/2))
        game_over.draw()


def count_lives():
    global number_of_lives
    if my_ball.ball_is_out():
        number_of_lives = number_of_lives - 1


def update(dt):
    global is_over
    global start_time
    global number_of_lives
    current_time = pygame.time.get_ticks()
    if current_time - start_time > 10000:
        bonuses.append(Bonus(Vector(400, -10)))
        start_time = current_time
    for bonus in bonuses:
        bonus.update(dt)
        if bonus.is_cought():
            bonuses.remove(bonus)
            number_of_lives += 1

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

    if number_of_lives <= 0 or (len(obstacles) == len(obstacles2) == 0):
        my_ball.velocity = Vector(0, 0)
        is_over = True


def on_mouse_move(pos):
    platform.look_at(pos)


pgzrun.go()

