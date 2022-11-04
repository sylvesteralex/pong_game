from turtle import Turtle
from window import screen, TOP, BOTTOM

DIST = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white", "white")
        self.shapesize(5, 1, 1)
        self.penup()

    def set_right(self):
        self.goto(350, 0)

    def set_left(self):
        self.goto(-360, 0)

    def move_up(self):
        y = self.ycor()
        if y < (TOP - 60):
            x = self.xcor()
            new_y = self.ycor() + DIST
            self.goto(x, new_y)

    def move_down(self):
        y = self.ycor()
        if y > (BOTTOM + 80):
            x = self.xcor()
            new_y = self.ycor() - DIST
            self.goto(x, new_y)
