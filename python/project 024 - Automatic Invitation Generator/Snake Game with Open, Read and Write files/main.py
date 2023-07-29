from turtle import Screen, done
from snake import Snake
from time import sleep
from food import Food
from scoreboard import Scoreboard

# Counter to scoreboard
counter = 0

# Screen definitions
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black") # the screen will get the black color
screen.title("snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.onkey(key="w", fun=snake.up)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)




screen.listen()
game_on = 1
while game_on == 1: 
    screen.update()
    sleep(0.1)
    snake.moveForward()
    
    

    # Detect collision with food
    if snake.head.distance(food) < 15: # if distance of snake head is less than 15 to food point
        food.refresh()
        snake.extend()
        scoreboard.increaseScore()


    # Detect collision with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        sleep(0.5)
        snake.reset()
        #game_on = 0
    
    # Detect collision with tail (we will need a for because we have a lot of squares making the tail)
    for segment in snake.segments:
        if segment != snake.head:
            if snake.head.distance(segment) <15:
                scoreboard.reset()
                sleep(0.5)
                snake.reset()
                #game_on = 0

done()
