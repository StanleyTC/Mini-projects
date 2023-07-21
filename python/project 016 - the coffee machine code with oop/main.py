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
    # Milk: -=100
from ingredients import Ingredients

machine = "on"
    
ingredients = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 100
}

while machine == "on":
    user = input('What flavor do you want? espresso/latte/cappuccino: ').lower()
    if user == 'espresso':
        cafe1 = Ingredients('espresso', 50, 18, 0, 300, 100, 200) # enviando agua usada, cafe usado, leite usado, agua default, cafe default, leite default
    if user == 'latte':
        ...
    if user == 'cappuccino':
        ...
