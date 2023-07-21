from ingredients import Ingredients
from money import Money
from ascii import coffee1

machine = "on"
    
water = 300
milk = 200
coffee = 100
money = 100

print(coffee1)
while machine == "on":
    user = input('What flavor do you want? espresso/latte/cappuccino: ').lower()
    if user == 'espresso':
        cafe1 = Ingredients('espresso', 50, 18, 0, water, coffee, milk, money) # enviando agua usada, cafe usado, leite usado, agua default, cafe default, leite default
        lista = cafe1.verifyIngredients()

    if user == 'latte':
        cafe2 = Ingredients('latte', 200, 24, 150, water, coffee, milk, money) # enviando agua usada, cafe usado, leite usado, agua default, cafe default, leite default
        lista = cafe2.verifyIngredients()

    if user == 'cappuccino':
        cafe3 = Ingredients('espresso', 250, 24, 100, water, coffee, milk, money) # enviando agua usada, cafe usado, leite usado, agua default, cafe default, leite default
        lista = cafe3.verifyIngredients()

    if user == 'report':
        report = Ingredients('report', 0, 0, 0, water, coffee, milk, money)
        report.report()

    # Verificar se os ingredientes possuem recursos: se o valor for 0, não tem recurso
    def wrong(user):
        if user == 'espresso':
            water = lista[0]+50
            coffee = lista[1]+18
            milk = lista[2]
        if user == 'latte':
            water = lista[0]+200
            coffee = lista[1]+24
            milk = lista[2]+150
        if user == 'cappuccino':
            water = lista[0]+250
            coffee = lista[1]+24
            milk = lista[2]+100
            return water, coffee, milk


    if user == 'espresso' or user == 'latte' or user == 'cappuccino':
        if lista == 0:
            print('Error, sorry, not enought resources :C')
        else:
            pennies=float(input('Pennies: '))
            nicles = float(input('nicles: '))
            dimes = float(input('dimes: '))
            quarters = float(input('Quarters: '))
            total = quarters/4 + dimes/10+ nicles/20+ pennies/100
            moneyy = Money(pennies, nicles, dimes, quarters, money)
            moneyResult = moneyy.verifyMoney(user)
            # Vamos verificar: se receber 1 - tem dinheiro na máquina. se receber 0 - não tem dinheiro na máquina
            if moneyResult == 1:
                final = moneyy.calculate(user)
                # se receber 2, somar com o valor da maquina. se receber -1, dinheiro insuficiente, se -2, devolver troco
                if final == 2:
                    money += total
                    print(f'Here is your {user}')
                    water = lista[0]
                    coffee = lista[1]
                    milk = lista[2]
                if final == -1:
                    print('Not enought money')
                    water, coffee, milk = wrong(user)
                if final == -2:
                    if user == 'espresso':
                        money += 1.5
                        print(f'take ${total-1.5} exchange')
                    if user == 'latte':
                        money += 2.5
                        print(f'take ${total-2.5} exchange')
                    if user == 'cappuccino':
                        money += 3
                        print(f'take ${total-3} exchange')

                    water = lista[0]
                    coffee = lista[1]
                    milk = lista[2]

            # repor ingredientes
            if moneyResult == 0:
                water, coffee, milk = wrong(user)
    if user == 'off':
        machine = 'off'
    # Iremos atualizar os valores de agua, leite, café e dinheiro depois de escolhido o pedido e ter pago
