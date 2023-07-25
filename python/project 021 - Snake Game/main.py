from turtle import Screen, done
from snack import Snack
from time import sleep
from food import Food

# Screen definitions
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black") # the screen will get the black color
screen.title("Snack Game")
screen.tracer(0)

snack = Snack()
food = Food()



screen.onkey(key="w", fun=snack.up)
screen.onkey(key="a", fun=snack.left)
screen.onkey(key="s", fun=snack.down)
screen.onkey(key="d", fun=snack.right)




screen.listen()
game_on = 1
while game_on == 1: # if turtle.xcor()>230:
    screen.update()
    sleep(0.1)
    snack.moveForward()


    # Detect collision with food.
    if snack.head.distance(food) < 15: # if distance of snack head is less than 15 to food point
        food.refresh()



done()
