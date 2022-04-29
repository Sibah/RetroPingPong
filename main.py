import math
from turtle import Screen
import text
from paddle import Paddle
from ball import Ball
from text import Text
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")

screen.tracer(0)
paddleRight = Paddle()
paddleLeft = Paddle()
text = Text()
text.startCountdown(3)

paddleRight.goto(350, 0)
paddleLeft.goto(-350, 0)

ball = Ball()

score = Score()
screen.listen()

screen.onkey(paddleRight.up, "Up")
screen.onkey(paddleRight.down, "Down")

screen.onkey(paddleLeft.up, "w")
screen.onkey(paddleLeft.down, "s")


def game():
    game_on = True
    while game_on:
        screen.update()
        ball.move()
        time.sleep(ball.movespeed)

        if ball.ycor() > 285 or ball.ycor() < -285:
            ball.bounce_Y()

        if ball.distance(paddleLeft) < 50 and ball.xcor() < -320 or ball.distance(paddleRight) < 50 and ball.xcor() > 320:
            ball.bounce_X()
            score.increase_score(1)

        if ball.xcor() > 400 or ball.xcor() < -400:
            text.gameOver()
            game_on = False


game()


def restart():
    global game_on
    game_on = True
    ball.resetBall()
    text.clearscreen()
    game()



screen.onkey(restart, "r")

screen.exitonclick()
