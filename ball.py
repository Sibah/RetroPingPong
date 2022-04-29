from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.turtlesize(0.61, 0.61)
        self.goto(0, 0)
        self.y = random.randint(1, 5)
        self.x = random.randint(3, 20)
        self.movespeed = 0.05

    def move(self):
        self.goto(self.xcor() - self.x, self.ycor() - self.y)

    def bounce_Y(self):
        self.y *= -1

    def bounce_X(self):
        self.x *= -1
        self.movespeed *= 0.9

    def resetBall(self):
        self.goto(0, 0)
        self.y = random.randint(1, 5)
        self.x = random.randint(3, 20)
        self.movespeed = 0.05

