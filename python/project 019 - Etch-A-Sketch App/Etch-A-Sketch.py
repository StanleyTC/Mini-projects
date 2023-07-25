from turtle import Turtle, Screen, done

timmy = Turtle()
screen = Screen()
timmy.speed("fastest")
timmy.color("darkblue")

def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.right(180)
    timmy.forward(10)
    timmy.right(180)


def clockwise():
    timmy.right(10)


def counter_clockwise():
    timmy.left(10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen() # To listen the button being used in keyboard
screen.onkey(key="w", fun=move_forwards) # when space button be pressed, activate move_forwards function
# when we use a function as a argument, we do not use () iin the function beeing called
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)

done()