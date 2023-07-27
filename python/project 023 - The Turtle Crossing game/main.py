from turtle import Turtle, Screen, done, ontimer
from player import Player
from blocks import Blocks
from time import sleep
import random

# Screen definitions
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white") # the screen will get the black color
screen.title("Turtle Crossing game by StanleyTC")



# Creating our turtle
timmy = Player()


# Turtle muving
screen.onkey(key="Up", fun=timmy.go_ahead)
screen.onkey(key="Down", fun=timmy.go_down)
screen.listen()



# Blocks coming
block_list = []

def createBlock():
    block=Blocks(random.randint(-230, 260))
    block_list.append(block)





    

counter=0
game_on=1
while game_on ==1:

    
    if len(block_list)<=30:
        createBlock()
    for block in block_list:
        for block in block_list:
            block.moving()
            if block.xcor()< -50:
                block.clearr()
                block_list.remove(block)







done()