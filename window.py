from turtle import Screen

MARGIN = 100
WIDTH, HEIGHT = 800, 600
TOP, BOTTOM = (HEIGHT/2), -(HEIGHT/2)
LEFT, RIGHT = -(WIDTH/2), (WIDTH/2)


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
