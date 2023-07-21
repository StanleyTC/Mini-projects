class Ingredients:
    # atributos com o tipo de café, agua, café e leite
    def __init__(self, coffeeKind, water, coffee, milk, defaultwater, defaultcoffee, defaultmilk):
        self.coffeekind = coffeeKind
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.defaultwater = defaultwater
        self.defaultcoffee = defaultcoffee
        self.defaultmilk = defaultmilk
    
    # Função para verificar se tem ingredientes o bastante
    def verifyIngredients(self):
        # espresso
        if self.coffekind == 'espresso' or self.coffeekind=='latte' or self.coffeekind =='cappuccino':
           if self.defaultwater - self.water >=0 and self.:
               lista = [self.defaultwater-self.water, self.defaultcoffee - self.coffee, self.defaultmilk-self.milk]
               return lista