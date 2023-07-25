from turtle import Screen, done
from snack import Snack
from time import sleep

# Screen definitions
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black") # the screen will get the black color
screen.title("Snack Game")
screen.tracer(0)

snack = Snack()



game_on = 1
while game_on == 1: # if turtle.xcor()>230:
    screen.update()
    sleep(0.1)
    snack.move()




done()
