from window import screen, TOP, BOTTOM, LEFT, RIGHT, WIDTH, HEIGHT
from turtle import Turtle


# MOV_X = (TOP*(1+(1-(HEIGHT/WIDTH))))/10
# MOV_Y = TOP/10
#
MOV_X = 10
MOV_Y = 0
BALL_SIZE = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white", "white")
        self.shape("circle")
        self.penup()
        self.move_x = 10
        self.move_y = 0
        self.x_direction = 1
        self.y_direction = 1

    def move(self):
        # new_x = self.xcor() + MOV_X * self.x_direction
        # new_y = self.ycor() + MOV_Y * self.y_direction
        new_x = self.xcor() + self.move_x * self.x_direction
        new_y = self.ycor() + self.move_y * self.y_direction
        self.goto(new_x, new_y)

    def reset(self):
        self.goto(0, 0)
        self.move_x = 10
        self.move_y = 0
