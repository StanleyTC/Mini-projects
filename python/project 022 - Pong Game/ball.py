from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.goto(0,0)
        self.penup()
        self.speed(2)
        self.x = 5
        self.y = 5


    def move(self):
        x = self.xcor()+self.x
        y = self.ycor()+self.y
        self.goto(x, y)

    
    def saltar(self):
        self.y *= -1 