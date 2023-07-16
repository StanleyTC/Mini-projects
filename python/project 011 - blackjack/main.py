from ascii import ascii_card, game_over, trophy
from time import sleep
from random import randint
from replit import clear

cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
print(ascii_card)
sleep(0.5)
print('Welcome to blackjack!')
sleep(0.5)
totalplayer = 0
totaldealer = 0
counter = 1


user = input('Do you want to start? types yes or no: ').lower()
while user == "yes":

    print(f'ROUND {counter}!')

    # player
    card = randint(0,12)
    player = cards[card]
    if counter == 1:
        anothercard = randint(0,12)
        player2 = cards[anothercard]
        print(f'You got {player} and {player2}')
    else:
        print(f'You got {player}')
    if player == 'Ace':
        totalplayer += int(input('Do you want to sum 1 or 11? type the value: '))
    if player2 == 'Ace':
        totalplayer += int(input('Do you want to sum 1 or 11? type the value: '))
    elif player == 'Queen' or player == 'Jack' or player == 'King':
        totalplayer+=10
    else:
        totalplayer += (card+1)
    sleep(0.25)
    if anothercard > -1:
        totalplayer += (anothercard+1)
    anothercard = -1
    print(f'You have {totalplayer} points!')
    
    # dealer
    card2 = randint(0, 12)
    dealer = cards[card2]
    newcarde = randint(0, 12)
    dealer2 = cards[newcarde]

    if dealer == 'Ace' and totaldealer <= 11:
        totaldealer += 11
    else:
        totaldealer += (newcarde)

    if dealer2 == 'Ace' and totaldealer <= 11:
        totaldealer += 11
    else:
        totaldealer += (newcarde)


    if counter == 1:
        print(f'Dealer got a {dealer} at the first card...')
    
    # Continue the game
    counter += 1
    if totalplayer >= 21:
        break
    user = input('Want to continue? yes or no: ').lower()

def win():
    clear()
    sleep(1)
    print('Oh... Congratulations!')
    sleep(1)
    print('You win!')
    sleep(0.5)
    print(trophy)


def lost():
    clear()
    sleep(1)
    print('Oh... sorry')
    sleep(1)
    print('You lost')
    sleep(0.5)
    print(game_over)


if totalplayer> 21:
    lost()


if totalplayer == 21:
    win()

else:
    if totalplayer == totaldealer:
        print(f'Same results! you got {totalplayer} and dealer got {totaldealer}')
    elif totalplayer > totaldealer or totaldealer >21:
        win()
    else:
        lost()
    
# yes... I could use functions