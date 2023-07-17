from random import randint

print("Welcome to the Number Guessing Game! \nI'm Thinking of a number between 1 and 100.")
dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def compareNumber(user):
    """
    function to compare user number with computer number. status = 1: user and computer have same number.
    status = 0: they do not have same number and computer have the bigger
    status = -1: they do not have same number and user have the bigger
    """
    computer = randint(1, 100)
    if user == computer:
        status = 1
    elif user > computer:
        status = -1
    else:
        status = 0
        return status



if dificulty == 'easy':
    attempts = 5
else:
    attempts = 10

while attempts != 0:

    user = int(input('Insert a number: '))
    response = compareNumber(user)
    if response == 0:
        break
    elif response == -1:
        print('Wrong, Try again, it is a lower number')
        attempts =- 1
    else:
        print('Wrong, thy again, it is a bigger number')
        attempts =- 1
    