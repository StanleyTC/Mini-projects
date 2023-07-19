from ascii import coffee
from replit import clear


clear()


status={
    'Water': 300, 
    'Milk': 200, 
    'Coffee': 100,
    'Money': 100
    }

machine = 'on'
while machine == 'on':


    # print(coffee)

    # 1. Prompt user by asking "What you like? (espresso/latte/cappuccino)"
    user = input('What would you like? (espresso/latte/cappuccino): ').lower()
    # 2. Turn off the coffee Machine by entering "off" to the prompt
    if user == "off":
        machine = 'off'
        break

    # 3. print report
    if user == 'report':
        print(f"Water: {status['Water']} \nMilk: {status['Milk']} \nCoffee: {status['Coffee']} \nMoney: {status['Money']}")

    # discount values:
    error = 'Error, Sorry we have no enought resources :c'
    # espresso

    if user == 'espresso':
        if status['Coffee'] - 18 >= 0 and status['Water'] - 50 >= 0:
            status['Coffee'] -= 18
            status['Water'] -= 50
        else:
            print(error)
    # latte
    if user == 'latte':
        if status['Coffee'] - 24 >= 0 and status['Water'] - 200 >= 0 and status['Milk'] - 150 >= 0:
            status['Coffee'] -= 24
            status['Water'] -= 200
            status['Milk'] -= 150
        else:
            print(error)
    # cappuccino
    if user == 'cappuccino':
        if status['Coffee'] - 24 >= 0 and status['Water'] - 250 >= 0 and status['Milk'] - 100 >= 0:
            status['Coffee'] -= 24
            status['Water'] -= 250
            status['Milk'] -= 100
            calculateMoney = 1
        else:
            print(error)
        # Calcular preço
        if calculateMoney == 1:
            pennies=float(input('Pennies: '))
            nicles = float(input('nicles: '))
            dimes = float(input('dimes: '))
            quarters = float(input('Quarters: '))
            totalValue = (quarters/4 + dimes/10 + nicles/20 + pennies/100)
            if totalValue<3:
                print('Error! not enought money')
                status['Coffee'] += 24
                status['Water'] += 250
                status['Milk'] += 100
            elif totalValue == 3:
                print("Done! that's your coffee")
            else:
                status['Money']= status['Money']- (totalValue-3)
                print(f'Here, take {totalValue-3}')

        # Expresso, Latte, Cappucino
        # 1.5$, 2.5$, 3.0$




