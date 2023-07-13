# Credits for hangman ascii art: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
# Credits for random words used: https://randomwordgenerator.com
# Credits for skull and trophy: https://ascii.co.uk/art

from ascii import hangman, opening, skull, trophy
from words import words
from random import randint
from time import sleep
print(opening)
sleep(0.5)
value = input('Type something to start: ')
sleep(0.5)

errors=0
word = (words[randint(0, len(words)-1)])
guessed = ['_']*len(word)
print(guessed)

while errors<6 and '_' in guessed:
    # Showing the _ _ _ _ ...


    user = input('Type a letter: ')
    for i in range(0, len(word)):
        if user == word[i]:
            guessed[i] = user
#        else:
#            print(f'sorry, no word')
#            errors +=1
#            print(hangman[errors])
    if user not in word:
        print('sorry, no word')
        errors += 1
        print(hangman[errors])
    print(guessed)

if errors == 6:
    sleep(0.5)
    print(hangman[errors])
    print('Game over! you lost')
    sleep(0.5)
    print(skull)

if '_' not in guessed:
    sleep(0.5)
    print('Congratulations! you won')
    print(trophy)