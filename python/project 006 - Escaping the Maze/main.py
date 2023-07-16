# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%
# Solution of this puzzle:

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        while front_is_clear() is False:
            # turn_left()
            if right_is_clear() is False:
                turn_left()
            if right_is_clear() is True:
                turn_right()