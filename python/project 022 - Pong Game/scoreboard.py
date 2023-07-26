from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, value):
        super().__init__()
        self.score = 0
        self.value = value
        self.color("white")
        self.hideturtle()
        self.penup()
        if self.value ==1:
            self.goto(-50, 150) # (width=800, height=450)
        if self.value ==2:
            self.goto(50, 150)
        
        self.show_score()
    

    def show_score(self):
        self.write(f"{self.score}", align="left", font=("Arial", 50, "normal"))     


    
    def NewScoreLeft(self):
        self.clear()
        self.score+=1
        self.write(f"{self.score}", align="right", font=("Arial", 50, "normal"))
    
    def NewScoreRight(self):
        self.clear()
        self.score+=1
        self.write(f"{self.score}", align="right", font=("Arial", 50, "normal"))