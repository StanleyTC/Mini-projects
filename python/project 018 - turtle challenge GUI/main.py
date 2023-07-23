
from random import randint
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

# circle: 20
# line: 50
# circle: 20

# RGB color list
colorList = []
for i in range(0, 100):
    colorList.append(colorGenerate())
    timmy.penup()

print(colorList)
done()