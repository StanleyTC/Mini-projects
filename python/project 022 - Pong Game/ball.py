from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.goto(0,0)
        self.penup()
        self.speed(1)
        self.x = 5
        self.y = 5


    def move(self):
        x = self.xcor()+self.x
        y = self.ycor()+self.y
        self.goto(x, y)


    def saltarY(self):
        self.y *= -1 
        

    def saltarX(self):
        self.x *= -1 

    def restart_position(self):
        self.penup()
        self.goto(0,0)