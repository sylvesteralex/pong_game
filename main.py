from window import screen, TOP, BOTTOM, LEFT, RIGHT
from paddle import Paddle
from ball import Ball, BALL_SIZE
from time import sleep
from scoreboard import Scoreboard


def init():
    screen.resetscreen()
    left_paddle, right_paddle = Paddle(), Paddle()
    right_paddle.set_right()
    print(right_paddle.xcor(), right_paddle.ycor())
    left_paddle.set_left()
    ball = Ball()
    right_scoreboard = Scoreboard("right")
    left_scoreboard = Scoreboard("left")
    screen.update()
    game_is_on = True

    while game_is_on:
        screen.update()
        sleep(0.1)
        ball.move()

        # Reflect from paddles
        if ball.distance(right_paddle.xcor(), right_paddle.ycor()) <= BALL_SIZE+10 \
                or ball.distance(right_paddle.xcor(), right_paddle.ycor()+40) <= BALL_SIZE\
                or ball.distance(right_paddle.xcor(), right_paddle.ycor()-40) <= BALL_SIZE:
            ball.x_direction = -1
            ball.move_x += 5
            ball.move_y += 5

        if ball.distance(left_paddle.xcor(), left_paddle.ycor()) <= BALL_SIZE+10 \
                or ball.distance(left_paddle.xcor(), left_paddle.ycor()+40) <= BALL_SIZE\
                or ball.distance(left_paddle.xcor(), left_paddle.ycor()-40) <= BALL_SIZE:
            ball.x_direction = 1
            ball.move_x += 5
            ball.move_y += 5

        # Reflect top and bottom
        if ball.ycor() >= TOP - BALL_SIZE:
            ball.y_direction = -1

        if ball.ycor() <= BOTTOM + BALL_SIZE:
            ball.y_direction = 1

        # Change score
        if ball.xcor() >= RIGHT + BALL_SIZE:
            left_scoreboard.add_point()
            sleep(1)
            ball.reset()
            # game_is_on = False

        if ball.xcor() <= LEFT - BALL_SIZE:
            right_scoreboard.add_point()
            sleep(1)
            ball.reset()
            # game_is_on = False


        screen.onkeypress(right_paddle.move_up, "Up")
        screen.onkeypress(right_paddle.move_down, "Down")
        screen.onkeypress(left_paddle.move_up, "w")
        screen.onkeypress(left_paddle.move_down, "s")
        screen.onkeypress(init, "r")
        screen.listen()

    screen.exitonclick()


if __name__ == "__main__":
    init()
