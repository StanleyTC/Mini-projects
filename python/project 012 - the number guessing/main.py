from random import randint

print("Welcome to the Number Guessing Game! \nI'm Thinking of a number between 1 and 100.")
dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def compareNumber(user, computer):
    """
    function to compare user number with computer number. 
    status = 1: user and computer have same number.
    status = 0: they do not have same number and computer have the bigger
    status = -1: they do not have same number and user have the bigger
    """
    if user == computer:
        status = 1
    if user > computer:
        status = -1
    if user < computer:
        status = 0
    return status


computer = randint(1, 100)
if dificulty == 'easy':
    attempts = 10
else:
    attempts = 5



while attempts != 0:
    print(f'You have {attempts} attempts')
    user = int(input('Insert a number: '))

    response=compareNumber(user, computer)

    if response == 1:
        print(f'Congratulations! you win, i was thinking in {computer}')
        break
    if response == -1:
        print('Wrong, Try again, it is a lower number')
        attempts -= 1
    if response == 0:
        print('Wrong, thy again, it is a bigger number')
        attempts -= 1



if attempts == 0:
    print('Sorry, you lost')