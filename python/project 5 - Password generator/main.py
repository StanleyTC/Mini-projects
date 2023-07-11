from random import randint, shuffle

letters = int(input('How many letters would you like in your password? '))
symbols = int(input('How many symbols would you like? '))
numbers = int(input('How many numbers would you like? '))

listletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listsymbols = ['@', '#', '$', '!', '%', '&', '*']
listnumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']  

password = []

# letters
for i in range(0, letters):
    password.append(listletters[randint(0, len(listletters) - 1)])

# symbols
for i in range(0, symbols):
    password.append(listsymbols[randint(0, len(listsymbols) - 1)])

# numbers
for i in range(0, numbers):
    password.append(listnumbers[randint(0, len(listnumbers) - 1)])

shuffle(password)  

password = ''.join(password)
print(password)
