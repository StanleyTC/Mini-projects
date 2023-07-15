from ascii import hammer

person = {}
list = []
answer = "yes"

print(hammer)
print('Welcome to the secret auction program.')

while answer == "yes":
    person["name"] = input('What is your name? ')
    person["bid"] = float(input('What is your bid? $'))
    list.append(person.copy())
    answer = input("Do you want to add a new person? yes or no: ").lower()


bigger = 0

for person in list:
    if person["bid"] > bigger:
        bigger = person["bid"]
        winnername = person["name"]

print(f'The winner is {winnername} with a bid of ${bigger}')