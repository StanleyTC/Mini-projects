from ascii import coffee
from replit import clear


clear()


def money(user):
    pennies=float(input('Pennies: '))
    nicles = float(input('nicles: '))
    dimes = float(input('dimes: '))
    quarters = float(input('Quarters: '))
    totalValue = (quarters/4 + dimes/10 + nicles/20 + pennies/100)
    # Expresso, Latte, Cappucino
    # 1.5$, 2.5$, 3.0$
    if user == 'espresso':
        if totalValue<1.5 or status['Money']- (totalValue-1.5) < 0:
            print('Error! money problem')
            status['Coffee'] += 18
            status['Water'] += 50
        elif totalValue == 1.5:
            print("Done! that's your espresso")
            status['Money'] += totalValue
        else:
            if status['Money']- (totalValue-3) >= 0:
                status['Money'] += totalValue
                status['Money']= status['Money']- (totalValue-1.5)
                print(f'Here, take {totalValue-1.5}&, it is your exchange')
    if user == 'latte':
        if totalValue<2.5 or status['Money']- (totalValue-2.5) < 0:
            print('Error! money problem! take it back')
            status['Coffee'] += 24
            status['Water'] += 200
            status['Milk'] += 150
        elif totalValue == 2.5:
            print("Done! that's your cappuccino")
            status['Money'] += totalValue
        else:
            if status['Money']- (totalValue-2.5) >= 0:
                status['Money'] += totalValue
                status['Money']= status['Money']- (totalValue-2.5)
                print(f'Here, take {totalValue-2.5}&, it is your exchange')

    if user == 'cappuccino':
        if totalValue<3 or status['Money']-(totalValue-3)<0:
            print('Error! not enought money')
            status['Coffee'] += 24
            status['Water'] += 250
            status['Milk'] += 100
        elif totalValue == 3:
            print("Done! that's your cappuccino")
            status['Money'] += totalValue
        else:
            if status['Money']-(totalValue-3)>=0:
                status['Money'] += totalValue
                status['Money']= status['Money']- (totalValue-3)
                print(f'Here, take {totalValue-3}&, it is your exchange')



status={
    'Water': 300, 
    'Milk': 200, 
    'Coffee': 100,
    'Money': 100
    }



print(coffee)



machine = 'on'
while machine == 'on':




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
            calculateMoney = 1
        else:
            print(error)
        # Calcular preço
        if calculateMoney == 1:
            money(user)
            calculateMoney = 0
    # latte
    if user == 'latte':
        if status['Coffee'] - 24 >= 0 and status['Water'] - 200 >= 0 and status['Milk'] - 150 >= 0:
            status['Coffee'] -= 24
            status['Water'] -= 200
            status['Milk'] -= 150
            calculateMoney = 1
        else:
            print(error)
        # Calcular preço
        if calculateMoney == 1:
            money(user)
            calculateMoney = 0
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
            money(user)
            calculateMoney = 0


    # Caso o dono queira reabastecer
    if user == "refuel":
        status['Coffee'] = status['Coffee'] + int(input('How much coffe to refuel? '))
        status['Milk'] = status['Milk'] + int(input('How much Milk to refuel? '))
        status['Water'] = status['Water'] + int(input('How much Water to refuel? '))
        status['Money'] = status['Money'] + int(input('How much Money to refuel? '))