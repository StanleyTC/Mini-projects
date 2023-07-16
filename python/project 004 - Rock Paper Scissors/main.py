# ASCII arts Credits to https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe 

from ascii import rock, paper, scissors
from random import randint
from time import sleep

print('Welcome to rock paper scissors game!')
sleep(0.5)
user = int(input('Choose 1 - rock, 2 - paper, 3 or any other number - scissors: '))
computer = randint(1, 3)


# print user choice in screen
sleep(0.5)
if user == 1:
    print(f'user: \n{rock}')
elif user == 2:
    print(f'user: \n{paper}')
else:
    print(f'user: \n{scissors}')

# print computer choice in screen
sleep(0.5)
if computer == 1:
    print(f'me: \n{rock}')
elif computer == 2:
    print(f'me: \n{paper}')
else:                                           # 1 = pedra, 2 - papel, 3 - tesoura
    print(f'me: \n{scissors}')

sleep(0.5)


#possibilities
if (user ==1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
    print('Congrats! you won')

if (computer == 1 and user ==3) or (computer == 2 and user == 1) or (computer == 3 and user ==2):
    print('oh, sorry... I won!')

if computer == user:
    print('tied!')