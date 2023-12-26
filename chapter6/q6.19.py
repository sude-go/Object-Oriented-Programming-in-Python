import cs1graphics as cg

GRAVITY = 9.8


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
        self.posX += self.velX
        self.posY += self.velY
        self.velY -= GRAVITY
        self.shape.moveTo(self.posX, self.posY)


my_ball = Ball(200, 200, 20, 20)

print("Initial position: (" + str(my_ball.get_position_x()) + ", " + str(my_ball.get_position_x()) + ")")
print("Initial velocity: (" + str(my_ball.get_velocity_x()) + ", " + str(my_ball.get_velocity_y()) + ")")

my_ball.advance()

print("Updated position: (" + str(my_ball.get_position_x()) + ", " + str(my_ball.get_position_y()) + ")")
print("Updated velocity: (" + str(my_ball.get_velocity_x()) + ", " + str(my_ball.get_velocity_y()) + ")")
