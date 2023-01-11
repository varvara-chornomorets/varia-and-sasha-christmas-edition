import math

from pgzero.actor import Actor
from pgzero.rect import Rect


WIDTH = 600
HEIGHT = 600
PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 20
BALL_RADIUS = 15


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


class Paddle:
    def __init__(self, pos):
        self.position = pos
        self.velocity = Vector(0, 0)
        self.goal = Vector(0, 0)

    def draw(self, screen):
        screen.draw.filled_rect(Rect((self.position.x-50, self.position.y-10), (PLATFORM_WIDTH, PLATFORM_HEIGHT)), "yellow")

    def position(self):
        return Vector(self.position.x, self.position.y)

    def look_at(self, pos):
        self.goal = Vector(pos[0], pos[1])

    def update(self, dt):
        position = Vector(self.position.x, self.position.y)
        desired = self.goal - position
        self.velocity = desired

        self.position.x += self.velocity.x


platform_start_position = Vector(700, 500)
ball_start_pos = Vector(17, 20)


class Ball:
    def __init__(self, pos: Vector):
        self.position = pos
        self.velocity = Vector(2, 3)

    def draw(self, screen):
        screen.draw.filled_circle((self.position.x, self.position.y), BALL_RADIUS, "blue")

    def position(self):
        return Vector(self.position.x, self.position.y)

    def update(self, dt, platform):
        position = Vector(self.position.x, self.position.y)
        if self.position.y < BALL_RADIUS:
            self.velocity.y = -self.velocity.y
        if platform_start_position.y - 10 - BALL_RADIUS + 5 > self.position.y > platform_start_position.y - 10 - BALL_RADIUS:
            if platform.position.x + WIDTH + 2 * BALL_RADIUS > self.position.x > platform.position.x - 2 * BALL_RADIUS:
                self.velocity.y = -self.velocity.y


        if self.position.x > WIDTH - BALL_RADIUS or self.position.x < BALL_RADIUS:
            self.velocity.x = -self.velocity.x
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y


class Heart:
    def __init__(self):
        self.actor = Actor('xconvert.com', center=(400, 400))
        self.velocity = Vector(0, 0)
        self.goal = Vector(0, 0)

    def draw(self):
        self.actor.draw()

    # def position(self):
    #     return Vector(self.actor.x, self.actor.y)
    #
    # def look_at(self, pos):
    #     self.goal = Vector(pos[0], pos[1])
    #     self.actor.angle = self.actor.angle_to((pos[0] + self.velocity.x, pos[1] + self.velocity.y)) - 90
    #
    # def update(self, dt):
    #     position = Vector(self.actor.x, self.actor.y)
    #     desired = self.goal - position
    #     desired = desired.normalized() * 10
    #     self.velocity += desired
    #     if self.velocity.magnitude() > 150:
    #         self.velocity = self.velocity.normalized() * 150
    #     self.actor.x += self.velocity.x * dt
    #     self.actor.y += self.velocity.y * dt
