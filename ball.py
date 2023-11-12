from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.initial_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def Bounce_y(self):
        self.y_move *= -1

    def Bounce_x(self):
        self.x_move *= -1
        self.initial_speed *= 0.9

    def rest_position(self):
        self.goto(0, 0)
        self.initial_speed = 0.1


