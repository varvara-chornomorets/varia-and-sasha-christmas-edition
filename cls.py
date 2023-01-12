import math
from pgzero.rect import Rect
from pgzero.actor import Actor


WIDTH = 600
HEIGHT = 600
PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 20
BALL_RADIUS = 15
OBSTACLE_RADIUS = 15
OBSTACLE_WIDTH = 100
OBSTACLE_HEIGHT = 20
platform_x = 0


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

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __str__(self):
        return f"({self.x}, {self.y})"


class Paddle:
    def __init__(self, pos):
        self.position = pos
        self.velocity = Vector(0, 0)
        self.goal = Vector(0, 0)

    def draw(self, screen):
        screen.draw.filled_rect(Rect((self.position.x-100, self.position.y-10), (PLATFORM_WIDTH, PLATFORM_HEIGHT)), "yellow")

    def position(self):
        return Vector(self.position.x, self.position.y)

    def look_at(self, pos):
        self.goal = Vector(pos[0], pos[1])

    def update(self, dt):
        position = Vector(self.position.x, self.position.y)
        desired = self.goal - position
        self.velocity = desired

        self.position.x += self.velocity.x
        global platform_x
        platform_x = self.position.x


class Ball:
    def __init__(self, pos: Vector):
        self.position = pos
        self.velocity = Vector(2, 3)

    def draw(self, screen):
        screen.draw.filled_circle((self.position.x, self.position.y), BALL_RADIUS, "blue")

    def position(self):
        return Vector(self.position.x, self.position.y)

    def update(self, dt):
        global platform_x
        position = Vector(self.position.x, self.position.y)
        if self.position.y < BALL_RADIUS:
            self.velocity.y = -self.velocity.y

        if 490 < self.position.y < 510:
            if platform_x - 115 < self.position.x < platform_x + 115:
                self.velocity.x = -self.velocity.x

        if 475 < self.position.y < 480:
            if platform_x - 100 < self.position.x < platform_x + 100:
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


class Obstacle:
    def __init__(self, pos: Vector):
        self.position = pos

    def draw(self, screen):
        screen.draw.filled_circle((self.position.x, self.position.y), OBSTACLE_RADIUS, "red")

    def update(self, screen, ball: Ball):
        dist = math.sqrt((ball.position.x - self.position.x)**2 + (ball.position.y - self.position.y)**2)
        if dist < OBSTACLE_RADIUS:
            return (ball.position.x - self.position.x), (ball.position.y - self.position.y)
        else:
            return False


class Obstacle2:
    def __init__(self, pos: Vector):
        self.position = pos

    def draw(self, screen):
        screen.draw.filled_rect(Rect((self.position.x-50, self.position.y-10), (OBSTACLE_WIDTH, OBSTACLE_HEIGHT)), "red")

    def update(self, screen, ball: Ball):
        if self.position.y - 10 < ball.position.y < self.position.y + 10:
            if self.position.x - 65 < ball.position.x < self.position.x + 65:
                print(self.position.x, self.position.y, ball.position.x, ball.position.y)
                return 2
        elif self.position.y - 25 < ball.position.y < self.position.y + 25:
            if self.position.x - 50 < ball.position.x < self.position.x + 50:
                return 1
        else:
            return False
