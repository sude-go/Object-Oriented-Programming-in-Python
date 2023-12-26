import cs1graphics as cg
import math
import time

STAR_X = 300
STAR_Y = 300
STAR_MASS = 1000


class Ball:
    def __init__(self, px, py, vx, vy):
        self.posX = px
        self.posY = py
        self.velX = vx
        self.velY = vy
        self.shape = cg.Circle(10)
        self.shape.moveTo(self.posX, self.posY)

    def get_position_x(self):
        return self.posX

    def get_position_y(self):
        return self.posY

    def get_velocity_x(self):
        return self.velX

    def get_velocity_y(self):
        return self.velY

    def advance(self):
        distance = math.sqrt((self.posX - STAR_X) ** 2 + (self.posY - STAR_Y) ** 2)
        angle = math.atan2(self.posY - STAR_Y, self.posX - STAR_X)
        gravity = STAR_MASS / distance ** 2
        gravity_x = gravity * math.cos(angle)
        gravity_y = gravity * math.sin(angle)
        self.posX += self.velX
        self.posY += self.velY
        self.velX -= gravity_x
        self.velY -= gravity_y

        if self.posX >= 400 or self.posY >= 400:
            self.velX = -self.velX
            self.velY = -self.velY
        if self.posX <= 0 or self.posY <= 0:
            self.velX = -self.velX
            self.velY = -self.velY
        self.shape.moveTo(self.posX, self.posY)


canvas = cg.Canvas(400, 400)

points = []
for angle in range(0, 360, 72):
    x = STAR_X + 50 * math.cos(math.radians(angle))
    y = STAR_Y + 50 * math.sin(math.radians(angle))
    point = cg.Point(x, y)
    points.append(point)

star = cg.Polygon(points)
star.moveTo(STAR_X, STAR_Y)
star.setFillColor("yellow")
star.setDepth(1)
canvas.add(star)

ball = Ball(100, 100, 5, 10)
canvas.add(ball.shape)

for i in range(100):
    ball.advance()
    canvas.refresh()
    time.sleep(0.1)
