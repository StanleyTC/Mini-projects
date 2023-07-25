from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.score = 0
        self.color("white")
        self.updateScoreboard()
        # it will always show another turtle in the screen, so we need to hide this second turtle:
        self.hideturtle()
        
    
    def updateScoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()


    def gameOver(self):
        self.goto(0, 0)
        self.write(f"Game over", align="center", font=("Arial", 30, "normal"))
        