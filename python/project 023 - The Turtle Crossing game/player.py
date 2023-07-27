from turtle import Turtle

class Player:
    def __init__(self):
        self.timmy = Turtle()
        self.timmy.hideturtle()
        self.timmy.color("black")
        self.timmy.shape("turtle")
        self.timmy.speed('fastest')
        self.timmy.penup()
        self.timmy.goto(0,-280)
        self.timmy.setheading(90)
        self.timmy.showturtle()


