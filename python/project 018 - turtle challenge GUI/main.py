
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
        timmy.dot(10, choice(colorList))
        timmy.penup()
        timmy.forward(25)
    timmy.right(180)
    timmy.forward(250)
    timmy.left(270)
    timmy.forward(25)
    timmy.right(90)

    
print(colorList)
done()