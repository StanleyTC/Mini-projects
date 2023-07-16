print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
percentage = float(input('What percentage tipe would you like to give? '))
people = int(input('How many people to split the bill? '))



percentagevalue = bill/100*percentage
finalvalue = bill+percentagevalue
person = finalvalue/people

print(f'Each person should pay: ${person}')