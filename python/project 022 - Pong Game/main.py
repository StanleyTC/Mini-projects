from turtle import Turtle, Screen, done
from player import Players
from ball import Ball
from scoreboard import Scoreboard
from random import randint
from time import sleep

# definitions of screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game from StanleyTC") # You can put whatever name you want here
screen.setup(width=800, height=600)
screen.tracer(0)
# mid line definitions
line = Turtle()
line.hideturtle()
line.speed("fastest")
line.goto(0, 300)
line.setheading(270)
line.pencolor("white")
screen.update()
for i in range(0, 20): # it will cover all the mid center in screen necessary to see
    line.pensize(5)
    line.forward(15)
    line.penup()
    line.forward(15)
    line.pendown()


# Players 1 and 2 created
player1 = Players((-350, 0))
player2 = Players((350, 0))

screen.onkey(key="w", fun=player1.up)
screen.onkey(key="s", fun=player1.down)
screen.onkey(key="Up", fun=player2.up)
screen.onkey(key="Down", fun=player2.down)
screen.listen()



# ball


# scoreboard options
score1=Scoreboard(1)
score1.show_score()

score2=Scoreboard(2)
score2.show_score()

# ball options
ball = Ball()
game_is_on = True
while game_is_on:
    sleep(0.014)
    screen.update()
    ball.move()

# Colisions in top wall
    if ball.ycor()> 280 or ball.ycor()< -280: # width=800, height=450
        ball.saltarY()
# Colisions in players
    if (ball.distance(player2) <50 and ball.xcor()>340) or (ball.distance(player1) <50 and ball.xcor()< -340): 
        ball.saltarX()

# Over the space
    if ball.xcor()>370:
        sleep(1)
        ball.restart_position()
        score1.NewScoreLeft()
    if ball.xcor()<-370:
        sleep(1)
        ball.restart_position()
        score2.NewScoreRight()
done()