from ingredients import Ingredients
from money import Money

machine = "on"
    
water = 300
milk = 200
coffee = 100
money = 100


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
        report = Ingredients('report')
        report.report()

    # Verificar se os ingredientes possuem recursos: se o valor for 0, não tem recurso
    if user == 'espresso' or user == 'latte' or user == 'cappuccino':
    if lista == 0:
        print('Error, sorry, not enought resources :C')
    else:
        pennies=float(input('Pennies: '))
        nicles = float(input('nicles: '))
        dimes = float(input('dimes: '))
        quarters = float(input('Quarters: '))
        total = quarters/4 + dimes/10+ nicles/20+ pennies/100
        money = Money(pennies, nicles, dimes, quarters, money)
        moneyResult = money.verifyMoney(user)
        # Vamos verificar: se receber 1 - tem dinheiro na máquina. se receber 0 - não tem dinheiro na máquina
        if moneyResult == 1:
            final = money.calculate(user)
            # se receber 2, somar com o valor da maquina. se receber -1, dinheiro insuficiente, se -2, devolver troco
            if final == 2:
                money += total
                print(f'Here is your {user}')
            if final == -1:
                print('Not enought money')
            if final == -2:
                if user == 'cappuccino':
                    money += 1.5
                    print(f'take ${total-1.5} exchange')
                if user == 'latte':
                    money += 2.5
                    print(f'take ${total-2.5} exchange')
                if user == 'cappuccino':
                    money += 3
                    print(f'take ${total-3} exchange')
    # Iremos atualizar os valores de agua, leite, café e dinheiro depois de escolhido o pedido e ter pago
    water = lista[0]
    coffee = lista[1]
    milk = lista[2]
