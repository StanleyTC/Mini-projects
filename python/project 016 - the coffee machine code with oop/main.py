# Try to study OOP with python before starting this project
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from ascii import coffee
from replit import clear


clear()
print(coffee)


machine = 'on'
while machine == 'on':
    # 1. Prompt user by asking "What you like? (espresso/latte/cappuccino)"
    user = input('What would you like? (espresso/latte/cappuccino): ').lower()
    # 2. Turn off the coffee Machine by entering "off" to the prompt
    if user == "off":
        machine = 'off'
        break
    # report function
    if user == "report":
        report = CoffeeMaker()
        print(report.report())
    # discount values:
    error = 'Error, Sorry we have no enought resources :c'
    # espresso

    if user == 'espresso':
        coffee = CoffeeMaker()
        status = coffee.makecoffee('espresso')
        if status == 1:
            money = MoneyMachine()
            moneyStatus = money.calculateMoney()
            if moneyStatus == 1:
                print()
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