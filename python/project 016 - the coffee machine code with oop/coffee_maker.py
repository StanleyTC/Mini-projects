# 3 coisas: report, verificar se é possivel fazer o cafe e fazer o cafe

class CoffeeMaker:

    # Irei criar os aatributos agua, leite, café, dinheiro
    def __init__(self, water=0, milk=0, coffee=0, money=0):
        self.Water = 300-water
        self.Milk = 200-milk
        self.Coffee = 100-coffee
        self.Money = 100-money
    
    # irei criar a ação de report
    def report(self):
        print(f'Coffe: {self.Coffee}g')
        print(f'Milk: {self.Milk}ml')
        print(f'Water: {self.Water}ml')
        print(f'Money: ${self.Money}')
    
    
    # irei criar a ação de fazer o café caso os ingredientes sejam suficientes
    def makecoffee(self, user):
        # para o espresso:
        if user == 'espresso':
            if (self.Water-50>=0) and (self.Coffee-18>=0):
                self.Water -= 50
                self.Coffe -= 18
                return 1
            else:
                return 0
        # para o latte:
        if user == 'latte':
            if (self.Water-200>=0) and (self.Coffee-24>=0) and (self.Milk-150>=0):
                self.Water -= 200
                self.Coffe -= 34
                self.Milk -= 150
                return 1
            else:
                return 0
        # para o cappuccino
        if user == 'cappuccino':
            if (self.Water-250>=0) and (self.Coffee-24>=0) and (self.Milk - 100>=0):
                self.Water -= 250
                self.Coffe -= 24
                self.Milk -= 100
                return 1
            else:
                return 0