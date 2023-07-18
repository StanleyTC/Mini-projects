list = []
answer = 'yes'
counter = 1


while answer == 'yes':
    value = input('Inform the task you want at your list: ')
    list.append(value)
    answer = input("Do you want to continue? 'yes' or 'no': ")

print('\nTask list: ')
for task in list:
    print(f'{counter}. {task}')
    counter+=1