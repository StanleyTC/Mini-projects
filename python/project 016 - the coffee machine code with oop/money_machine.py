class MoneyMachine:
    def __init__(self):
        ...
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