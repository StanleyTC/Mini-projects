from turtle import Turtle, Screen

# screen
screen = Screen()
screen.setup(width=500, height=400) # resize the screen to 500 X 400 pixels
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color: ")
print(user_bet)

# colors
colors = ["red", "darkblue", "yellow", "green", "purple", "orange"]

# turtles
def turtle_kinds(name, colors, position, x, y):
    name = Turtle()
    name.color(colors[position])
    name.penup()
    name.shape("turtle")
    name.goto(x, y) 


#timmy
turtle_kinds('jimmy', colors, 0, x=-230, y =-100)
# tommy 
turtle_kinds('tommy', colors, 1, x=-230, y =-100)
# alice 
alice = Turtle()
alice.color(colors[4])
alice.penup()
alice.shape("turtle")
alice.goto(x=-230, y =-100)
# anna 
ana = Turtle()
ana.color(colors[2])
ana.penup()
ana.shape("turtle")
ana.goto(x=-230, y =-100)
# jimmy
jimmy = Turtle()
jimmy.color(colors[5])
timmy.penup()
timmy.shape("turtle")
timmy.goto(x=-230, y =-100)
#jack
jack = Turtle()
jack.color(colors[6])
jack.penup()
jack.shape("turtle")
jack.goto(x=-230, y =-100)



screen.exitonclick()