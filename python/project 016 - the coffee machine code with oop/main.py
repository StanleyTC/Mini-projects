# Espresso 1.5
    # water: 50 ml
    # coffe: 18g
# Latte 2.5
    # Water: 200ml
    # coffee: 24g
    # Milk: 150g
# Cappuccino 3
    # Water: 250ml
    # Coffee: 24g
    # Milk: =100
from ingredients import Ingredients

machine = "on"
    
water = 300
milk = 200
coffee = 100
money = 100


while machine == "on":
    user = input('What flavor do you want? espresso/latte/cappuccino: ').lower()
    if user == 'espresso':
        cafe1 = Ingredients('espresso', 50, 18, 0, water, coffee, milk) # enviando agua usada, cafe usado, leite usado, agua default, cafe default, leite default
        lista = cafe1.verifyIngredients()

    if user == 'latte':
        cafe2 = Ingredients('latte', 200, 24, 150, water, coffee, milk) # enviando agua usada, cafe usado, leite usado, agua default, cafe default, leite default
        lista = cafe2.verifyIngredients()

    if user == 'cappuccino':
        cafe3 = Ingredients('espresso', 250, 24, 100, water, coffee, milk) # enviando agua usada, cafe usado, leite usado, agua default, cafe default, leite default
        lista = cafe3.verifyIngredients()



    # Verificar se os ingredientes possuem recursos: se o valor for 0, não tem recurso
    if lista == 0:
        print('Error, sorry, not enought money :C')
    else:
        pennies=float(input('Pennies: '))
        nicles = float(input('nicles: '))
        dimes = float(input('dimes: '))
        quarters = float(input('Quarters: '))
    # Iremos atualizar os valores de agua, leite, café e dinheiro depois de escolhido o pedido e ter pago
    water = lista[0]
    coffee = lista[1]
    milk = lista[2]
