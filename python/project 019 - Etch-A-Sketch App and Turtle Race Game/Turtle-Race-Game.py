from turtle import Turtle, Screen
from random import randint

# screen
screen = Screen()
screen.setup(width=500, height=400) # resize the screen to 500 X 400 pixels
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color: ")
print(user_bet)

# colors
colors = ["red", "darkblue", "yellow", "green", "purple", "orange", "black"]

# turtles
def turtle_kinds(name, colors, position, x, y):
    name = Turtle()
    name.color(colors[position])
    name.penup()
    name.shape("turtle")
    name.goto(x, y) 
    return name

#timmy
timmy=turtle_kinds('timmy', colors, 0, x=-230, y =-50)
# tommy 
tommy=turtle_kinds('tommy', colors, 1, x=-230, y =-100)
# alice 
alice=turtle_kinds('alice', colors, 2, x=-230, y =-150)
# bob
bob=turtle_kinds('bob', colors, 6, x=-230, y =0)
# anna 
anna=turtle_kinds('anna', colors, 3, x=-230, y =50)
# jimmy
jimmy=turtle_kinds('jimmy', colors, 4, x=-230, y =100)
#jack
jack=turtle_kinds('jack', colors, 5, x=-230, y =150)

turtles = [timmy, tommy, alice, bob, anna, jimmy, jack]

winning = 0
end = []
while winning == 0:
    for turtle in turtles:
        turtle.forward(randint(1, 10))
        if turtle.xcor()>230:
            winning = turtle.pencolor()
            end.append(winning)
            break
if end[0]== user_bet:
    print(f"You won! The {end[0]} color get there first")
                
if end[0] != user_bet:
    print(f'You lost... The {end[0]} color had win')
                
    



screen.exitonclick()