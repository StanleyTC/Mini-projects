from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.color("black")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(-280, 260)
        self.clear()
        self.show_score()

    
    def show_score(self):
        self.clear()
        self.write(f"Level {self.level}", align="left", font=("Arial", 16, "normal"))  
    

    def update_score(self, new_level):
        self.level = new_level
        self.show_score()
