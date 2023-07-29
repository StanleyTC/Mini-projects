from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.score = 0

        with open("data.txt") as data:
            self.high_score = int(data.read()) # we need to convert to integer beacuse everything it reads is string
        
        self.color("white")
        self.updateScoreboard()
        # it will always show another turtle in the screen, so we need to hide this second turtle:
        self.hideturtle()
        
    
    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, high score: {self.high_score}", align="center", font=("Arial", 24, "normal"))


    def increaseScore(self):
        self.score += 1
        self.updateScoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.score}")
            

        self.score = 0
        self.updateScoreboard()

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write(f"Game over", align="center", font=("Arial", 30, "normal"))
        