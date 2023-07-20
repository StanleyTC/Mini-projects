# 3 coisas: report, verificar se é possivel fazer o cafe e fazer o cafe

class CoffeeMaker:

    # Irei criar os aatributos agua, leite, café, dinheiro
    def __init__(self, water=0, milk=0, coffee=0, money=0):
        self.Water = 300
        self.Milk = 200
        self.Coffee = 100
        self.Money = 100
    
        
    # irei criar a ação de fazer o café caso os ingredientes sejam suficientes
    def makecoffee(self, user):


        # para o espresso:
        if user == 'espresso':
            if (self.Water-50>=0) and (self.Coffee-18>=0):
                water = self.Water -50
                coffee = self.coffee - 18
                return 1

            else:
                return 0
        # para o latte:
        if user == 'latte':
            if (self.Water-200>=0) and (self.Coffee-24>=0) and (self.Milk-150>=0):
                self.Water -= 200
                self.Coffee -= 34
                self.Milk -= 150
                return 1
            else:
                return 0
        # para o cappuccino
        if user == 'cappuccino':
            if (self.Water-250>=0) and (self.Coffee-24>=0) and (self.Milk - 100>=0):
                self.Water -= 250
                self.Coffee -= 24
                self.Milk -= 100
                return 1
            else:
                return 0
        
        # irei criar a ação de report
        if user == 'report':
            print(f'Coffe: {water}g')
            print(f'Milk: {coffee}ml')
            print(f'Water: {milk}ml')
            print(f'Money: ${self.Money}')
            
            
    # Trazer de volta os valores se o dinheiro for invalido
    def rebootMoney(self, returnFromMoney):
        if returnFromMoney == 1.5:
                self.Water += 50
                self.Coffee += 18
        if returnFromMoney == 2.5:
                self.Water += 200
                self.Coffee += 34
                self.Milk += 150
        if returnFromMoney == 3.5:
                self.Water += 250
                self.Coffee += 24




