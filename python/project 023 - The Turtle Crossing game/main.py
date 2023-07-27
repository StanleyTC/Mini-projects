from turtle import Turtle, Screen, done
from player import Player
from blocks import Blocks
from time import sleep
import random

# Screen definitions
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white") # the screen will get the black color
screen.title("Turtle Crossing game for StanleyTC")
#screen.tracer(0)


# Creating our turtle
timmy = Player()


# Turtle muving
screen.onkey(key="Up", fun=timmy.go_ahead)
screen.onkey(key="Down", fun=timmy.go_down)
screen.listen()



# Blocks coming
block=Blocks(random.randint(-230, 260))
screen.update()
game_on = 1
while game_on ==1:
    block.moving()
    



done()