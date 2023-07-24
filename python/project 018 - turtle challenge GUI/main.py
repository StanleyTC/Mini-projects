from random import randint, choice
from turtle import Turtle, done

def colorGenerate():
    """
    Generate random colors in hexadecimal with rgb
    """
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    color_code = f"#{r:02x}{g:02x}{b:02x}"
    return color_code


# Turtle atributes
timmy = Turtle()
color = colorGenerate()
timmy.color(color)
timmy.speed("fastest")

# starting further down the screen
timmy.setheading(225)
timmy.penup()
timmy.forward(300)
timmy.pendown()
timmy.setheading(0)
# circle: 20
# line: 50
# circle: 20

# RGB color list
colorList = []
for i in range(0, 100):
    colorList.append(colorGenerate())

# Turtle making the dots:
for i in range(0, 10):
    for j in range(0, 10):
        timmy.dot(20, choice(colorList))
        timmy.penup()
        timmy.forward(50)
    timmy.right(180)
    timmy.forward(500)
    timmy.left(270)
    timmy.forward(50)
    timmy.right(90)

    
print(colorList)
done()