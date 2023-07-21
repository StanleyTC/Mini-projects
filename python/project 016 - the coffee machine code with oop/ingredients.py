class Ingredients:
    # atributos com o tipo de café, agua, café e leite
    def __init__(self, coffeeKind, water, coffee, milk, defaultwater, defaultcoffee, defaultmilk, defaultmoney):
        self.coffeekind = coffeeKind
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.defaultwater = defaultwater
        self.defaultcoffee = defaultcoffee
        self.defaultmilk = defaultmilk
        self.defaultmoney = defaultmoney
    
    # Função para verificar se tem ingredientes o bastante
    def verifyIngredients(self):
        if self.coffeekind == 'espresso' or self.coffeekind=='latte' or self.coffeekind =='cappuccino':
           if self.defaultwater - self.water >=0 and self.defaultcoffee - self.coffee >= 0 and self.defaultmilk-self.milk >=0:
               lista = [self.defaultwater-self.water, self.defaultcoffee - self.coffee, self.defaultmilk-self.milk]
               return lista
           else:
               return 0
           
    # função report
    def report(self):
        print(f'Water: {self.defaultwater}ml')
        print(f'Coffee: {self.defaultcoffee}g')
        print(f'Milk: {self.defaultmilk}ml')
        print(f'Money: {self.defaultmoney}$')
