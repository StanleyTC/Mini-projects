from turtle import Turtle, Screen, done
import player1
import player2

# definitions of screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game from StanleyTC") # You can put whatever name you want here
screen.setup(width=800, height=450)
line = Turtle()
# mid line definitions
line.hideturtle()
line.speed("fastest")
line.goto(0, 215)
line.setheading(270)
line.pencolor("white")
for i in range(0, 15): # it will cover all the mid center in screen necessary to see
    line.pensize(5)
    line.forward(15)
    line.penup()
    line.forward(15)
    line.pendown()


# Players 1 and 2 created
player1 = player1.Players()
player2 = player2.Players()


screen.onkey(key="w", fun=player1.up)
screen.onkey(key="s", fun=player1.down)
screen.onkey(key="Up", fun=player2.up)
screen.onkey(key="Down", fun=player2.down)
screen.listen()


done()