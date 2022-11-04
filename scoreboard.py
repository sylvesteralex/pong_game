from turtle import Turtle
from window import screen, RIGHT, LEFT, TOP

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self, left_right):
        super().__init__()
        self.points = 0
        self.color("white", "white")
        self.penup()
        self.hideturtle()
        if left_right == "right":
            self.goto(RIGHT-150, TOP-40)
        if left_right == "left":
            self.goto(LEFT+150, TOP-40)
        self.write(f"Score: {self.points}", False, "center", FONT)

    def add_point(self):
        self.points += 1
        self.clear()
        self.write(f"Score: {self.points}", False, "center", FONT)
        screen.update()

