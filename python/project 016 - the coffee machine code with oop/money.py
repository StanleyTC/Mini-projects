class Money:
    def __init__(self, pennies, nicles, dimes, quarters, moneyMachine):
        self.pennies = pennies
        self.nicles = nicles
        self.dimes = dimes
        self.quarters = quarters
        self.moneyMachine = moneyMachine
        self.total = quarters/4 + dimes/10 + nicles/20 + pennies/100

    def verifyMoney(self, user):
        # Verificar dinheiro da maquina
        if user == 'espresso':
            if self.moneyMachine < 1.5:
                return 0
            else: 
                return 1
        if user == 'latte':
            if self.moneyMachine < 2.5:
                return 0
            else: 
                return 1
        if user == 'cappuccino':
            if self.moneyMachine < 3:
                return 0
            else: 
                return 1
    
    # Calcular, uma vez que a função acima retorne 1
    def calculate(self, user):
        # espresso
        if user == 'espresso':
            if self.total == 1.5:
                return 2
            elif self.total < 1.5:
                return -1
            else:
                return -2
        # latte
        if user == 'latte':
            if self.total == 2.5:
                return 2
            elif self.total < 2.5:
                return -1
            else:
                return -2
        # cappuccino
        if user == 'cappuccino':
            if self.total == 2.5:
                return 2
            elif self.total < 2.5:
                return -1
            else:
                return -2