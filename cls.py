import math
import pgzrun


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

    def draw(self):
        screen.draw.filled_rect(Rect((self.position.x-50, self.position.y-10), (100, 20)), "yellow")

    def position(self):
        return Vector(self.position.x, self.position.y)

    def look_at(self, pos):
        self.goal = Vector(pos[0], pos[1])

    def update(self, dt):
        position = Vector(self.position.x, self.position.y)
        desired = self.goal - position
        self.velocity = desired

        self.position.x += self.velocity.x


WIDTH = 800
HEIGHT = 800

some_position = Vector(700, 700)
platform = Paddle(some_position)


def draw():
    screen.clear()
    platform.draw()

def update(dt):
    platform.update(dt)


def on_mouse_move(pos):
    platform.look_at(pos)


pgzrun.go()
