import cs1graphics as cg
import math

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
        self.shape.moveTo(self.posX, self.posY)


ball = Ball(100, 100, 10, 10)

print("Initial position: (" + str(ball.get_position_x()) + ", " + str(ball.get_position_x()) + ")")
print("Initial velocity: (" + str(ball.get_velocity_x()) + ", " + str(ball.get_velocity_y()) + ")")

ball.advance()

print("Updated position: (" + str(ball.get_position_x()) + ", " + str(ball.get_position_y()) + ")")
print("Updated velocity: (" + str(ball.get_velocity_x()) + ", " + str(ball.get_velocity_y()) + ")")
