from turtle import Screen
from Paddle1 import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PingPong")

paddle_1 = Paddle((380, 0))
paddle_2 = Paddle((-380, 0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(fun=paddle_1.Up, key="Up")
screen.onkey(fun=paddle_1.Down, key="Down")
screen.onkey(fun=paddle_2.Up, key="w")
screen.onkey(fun=paddle_2.Down, key="s")
is_game_on = True

while is_game_on:
    time.sleep(ball.initial_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.Bounce_y()

    if ball.distance(paddle_1) < 30 or ball.xcor() > 380 or ball.distance(paddle_2) < 30 or ball.xcor() < -380:

        ball.Bounce_x()

    if ball.xcor() > 380:
        score_board.Update_r_scores()
        ball.rest_position()
    if ball.xcor() < -380:
        score_board.Update_l_scores()
        ball.rest_position()

screen.exitonclick()
