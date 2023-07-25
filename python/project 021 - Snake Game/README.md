# Snake Arcade Game

Today we are going to learn how to build our first arcade game, the snake game!
We will make use of the Turtle library again, to show and reinforce that it does not necessarily have to do something involving turtles, we can manipulate the Turtle class and the others to create our own games

## What will this project do?
For this project, class inheritance, splitting, object orientation, classes and the use of the Turtle module and its classes to create classic games will be exercised. With all the projects done so far, it's perfectly doable.

### Orientation
Fortunately, today chatgpt exists, so if you need to know how to do each part, get the codes inside the files, throw them into chatgpt and it will explain it to you in detail, however try to do it yourself! study classes, study objects, study the turtle module, and understand how you can play the snake game.

Initially you will need to create 3 turtles objects in the shape of squares and position them one behind the other to assume the shape of the snake, don't forget to design a nice canvas size, in this case I used 600x600, and put black in the background and white in the 3 squares. Afterwards, you will need to make the 3 objects move, they will be the snake, and for that I played the function that will make the snake move inside a while, so it will always continue to move until the time the player loses; to train classes and objects, I played the movement functions of the snake and the squares created to represent it inside the file [snake.py](snake.py), if you get confused with the logic used, ask an artificial intelligence. Then I programmed the button presses, something we already saw in project 19, and they will invoke functions within the Snake class to change the direction of the first square (note that, thanks to the movement function within the class, the other blocks will follow the first one, so we just need to change the first one), and I also ensured that the user would not be able to make the snake turn in the opposite direction, for that I only needed an IF.

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

For the Scoreboard we will use the write method of the Turtle class, and we'll do that in another new class called scoreboard.py that will follow the inherited class model as well.



## [Main Script](main.py)

### Description:

This script orchestrates the Snake game. It initializes the game window, manages user inputs, checks for game-ending conditions, and updates the game at regular intervals.

### Features:

- **Responsive Controls:** Use `W`, `A`, `S`, `D` for movement.
- **Food Consumption:** The snake can eat food which helps it grow.
- **Dynamic Scoreboard:** Keeps track of your current score.
- **Game-Ending Conditions:** Ends the game if the snake collides with the game boundary or itself.

## Additional Files:

1. **[Snake Script snake.py)](snake.py):** 
   - Defines the snake's body, its motion, and the way it grows.
   - Controls the direction and logic for extending the snake.

2. **[Food Script (food.py)](food.py):** 
   - Represents the food object in the game.
   - Generates food at random positions within the game boundary.

3. **[Scoreboard Script (scoreboard.py)](scoreboard.py):** 
   - Manages and displays the current score.
   - Displays "Game Over" upon game ending conditions.

## Gameplay:

1. Execute the `main.py` script.
2. Control the snake using the `W`, `A`, `S`, `D` keys.
3. Try to eat the food (blue circle). Each time you eat, your score increases and the snake grows longer.
4. Avoid running into the game boundary and the snake itself.
5. Aim to achieve the highest score possible!

## Requirements:

- Python
- Turtle Module (Standard in Python)

## Future Improvements:

- Enhance the UI for a more engaging user experience.
- Introduce varying levels of difficulty.
- Implement additional features like power-ups or obstacles.

