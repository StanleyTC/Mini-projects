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
level = 1
def createBlock():
    block=Blocks(random.randint(-230, 260), level)
    block_list.append(block)



def blocksAndTimmy(level):
    if len(block_list)<=30:
        createBlock()
    for block in block_list:
        for block in block_list:
            block.moving()
            if block.xcor()< -250:
                block.clearr()
                block_list.remove(block)
            # Detecção de colisão
            if abs(block.xcor() - timmy.xcor()) < 20 and abs(block.ycor() - timmy.ycor()) < 20:
                return -1
            if timmy.ycor() > 260:
                sleep(1)
                timmy.resetar()
                level+=1
    return level

                
        


    
game_on =1
while game_on ==1:
    gamestatus = blocksAndTimmy(level)
    if gamestatus != -1:
        level = gamestatus
    if gamestatus == -1:
        game_on = 0
        break
        





done()