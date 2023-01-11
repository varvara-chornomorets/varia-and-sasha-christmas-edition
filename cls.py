import math
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
platform = Paddle(platform_start_position)

class Ball:
    def __init__(self, pos: Vector):
        self.position = pos
        self.velocity = Vector(1, 1.5)

    def draw(self, screen):
        screen.draw.filled_circle((self.position.x, self.position.y), BALL_RADIUS, "blue")

    def position(self):
        return Vector(self.position.x, self.position.y)

    def update(self, dt):
        position = Vector(self.position.x, self.position.y)
        if self.position.y < BALL_RADIUS:
            self.velocity.y = -self.velocity.y
        if self.position.y > 475:
            self.velocity.y = -self.velocity.y

        # if self.position.y > WIDTH - PLATFORM_HEIGHT -BALL_RADIUS:
        #     if self.position.x > platform.position.x
        if self.position.x > WIDTH - BALL_RADIUS or self.position.x < BALL_RADIUS:
            self.velocity.x = -self.velocity.x
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

