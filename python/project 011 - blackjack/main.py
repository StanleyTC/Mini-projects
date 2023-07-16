from ascii import ascii_card, game_over
from time import sleep
from random import randint, random

cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
print(ascii_card)
sleep(0.5)
print('Welcome to blackjack!')
sleep(0.5)
totalplayer = 0
totaldealer = 0
counter = 1


user = input('Do you want to start? types yes or no: ').lower()
while user == "yes" and totalplayer <= 21:

    print(f'ROUND {counter}!')

    # player
    card = randint(0,12)
    player = cards[card]
    print(f'You got {player}')
    if player == 'Ace':
        totalplayer += int(input('Do you want to sum 1 or 11? type the value: '))
    elif player == 'Queen' or player == 'Jack' or player == 'King':
        totalplayer+=10
    else:
        totalplayer += (card+1)
    sleep(0.25)
    print(f'You have {totalplayer} points!')
    
    # dealer
    card2 = randint(0, 12)
    dealer = cards[card2]


    if dealer == 'Ace' and totaldealer <= 11:
        totaldealer += 11
    else:
        totaldealer += (card2)
    if counter == 1:
        print(f'Dealer got a {dealer} and he has {totaldealer} points')
    
    # Continue the game
    counter += 1
    user = input('Want to continue? yes or no: ').lower()


if totalplayer> 21:
    print()