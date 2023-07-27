from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.shape("turtle")
        self.speed('fastest')
        self.penup()
        self.goto(0,-280)
        self.setheading(90)
        self.showturtle()
        

    def go_ahead(self):
        if self.ycor()<280:
            self.forward(20)
    

    def go_down(self):
        if self.ycor()>-280:
            self.forward(-20)
    

    def resetar(self):
        self.goto(0,-280)