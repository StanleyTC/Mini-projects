Today we are going to learn how to build our first arcade game, the snake game!
We will make use of the Turtle library again, to show and reinforce that it does not necessarily have to do something involving turtles, we can manipulate the Turtle class and the others to create our own games

## What will this project do?
For this project, class inheritance, splitting, object orientation, classes and the use of the Turtle module and its classes to create classic games will be exercised. With all the projects done so far, it's perfectly doable.

### Orientation
Fortunately, today chatgpt exists, so if you need to know how to do each part, get the codes inside the files, throw them into chatgpt and it will explain it to you in detail, however try to do it yourself! study classes, study objects, study the turtle module, and understand how you can play the snake game.

Initially you will need to create 3 turtles objects in the shape of squares and position them one behind the other to assume the shape of the snake, don't forget to design a nice canvas size, in this case I used 600x600, and put black in the background and white in the 3 squares. Afterwards, you will need to make the 3 objects move, they will be the snake, and for that I played the function that will make the snake move inside a while, so it will always continue to move until the time the player loses; to train classes and objects, I played the movement functions of the snake and the squares created to represent it inside the file [snack.py](snack.py), if you get confused with the logic used, ask an artificial intelligence. Then I programmed the button presses, something we already saw in project 19, and they will invoke functions within the Snack class to change the direction of the first square (note that, thanks to the movement function within the class, the other blocks will follow the first one, so we just need to change the first one), and I also ensured that the user would not be able to make the snake turn in the opposite direction, for that I only needed an IF.

### Next steps
Make a collision system with food to increase it by one square, then create a dashboard, then a collision system with the wall for the user to lose, and finally a collision system for the squares that form the snake so that the user loses too (as you already know, you always lose in this game, its objective is always to try to break your record).
Remember that to inherit a class, we need to create a class, and in the new class that will inherit it, reference it.
Example
```
class Test:
    def __init__(self):
        ...

class second(Test): # this class will inherit the Test class
    def __init__(self):
        super().__init__()
        ...
```
We'll use inherited classes to create a class just for the snake's food that will inherit some methods and attributes from the Turtle class to speed up our work.