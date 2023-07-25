from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # i want to cut the default size in half so i use 0.5 which 
                                                         # represents half, the default size is 20 so i change both height and width to 10
        self.color("blue")
        self.speed("fastest")
        self.refresh() 
        
    
    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280)) # the circle food will random appear in x position and y position