# 3 coisas: report, verificar se é possivel fazer o cafe e fazer o cafe

class CoffeeMaker:

    # Irei criar os aatributos agua, leite, café, dinheiro
    def __init__(self, water=0, milk=0, coffee=0, money=0, counter=0):
        if counter == 1 or counter == 0:
            self.Water = 300 - water
            self.Milk = 200 - milk
            self.Coffee = 100 - coffee
            self.Money = 100 - money
        else:
            self.Water -= water
            self.Milk -= milk
            self.Coffee -= coffee
            self.Money -= money         
        
    # irei criar a ação de fazer o café caso os ingredientes sejam suficientes
    def makecoffee(self, user):


        # para o espresso:
        if user == 'espresso':
            if (self.Water-50>=0) and (self.Coffee-18>=0):
                self.Water = self.Water -50
                self.Coffee = self.Coffee - 18
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
            print(f'Coffe: {self.Water}g')
            print(f'Milk: {self.Milk}ml')
            print(f'Water: {self.Coffee}ml')
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




