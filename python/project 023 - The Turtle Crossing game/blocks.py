from turtle import Turtle
from random import choice
from time import sleep

class Blocks(Turtle):
    def __init__(self, posicion_y):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.posY = posicion_y
        self.posX = 1
        self.shape("square")
        self.shapesize(1, 3)
        self.goto(320, self.posY)
        colors = ["red", "blue", "darkblue", "yellow", "pink", "purple", "black", "orange", "red"]
        self.color(choice(colors))
        self.showturtle()
        
    
    def moving(self):
        x = self.xcor()-self.posX
        self.goto(x, self.posY)
    