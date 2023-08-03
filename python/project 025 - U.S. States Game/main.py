import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)





corrects = 0
counter = 1
new_counter = -1

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()



while counter <51:
    new_counter += 1
    answer_state = screen.textinput(f"{corrects} of 50 states correct", "What is the state?").title()

    # If user wants to end program before:
    if answer_state == "Exit":
        break

    if answer_state in all_states:
        corrects += 1
        names = turtle.Turtle()
        names.goto(0,0)
        names.hideturtle()
        names.penup()
        names.speed("fastest")
        state_data = data[data.state == answer_state]
        names.goto(int(state_data.x), int(state_data.y))
        names.write(answer_state)
        all_states.remove(answer_state)

    counter+=1


states_dict = {
    "states missing: ": all_states
}

pandas_dict = pandas.DataFrame(states_dict)

pandas_dict.to_csv("states to learn.csv")

turtle.done()