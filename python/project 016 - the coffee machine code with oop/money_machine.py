class MoneyMachine:
    # creating atributes money
    def __init__(self, pennies, nicles, dimes, quarters):
        self.pennies = pennies
        self.nicles = nicles
        self.dimes = dimes
        self.quarters = quarters
        self.totalMoney = pennies/100+nicles/20+dimes/10+quarters/4


    # verify money
    def verifyMoney(self, user, machineMoney):
        """
        Verificar se é possivel obter o café com o dinheiro colocado.
        Se o usuario inserir o valor exato, irá retornar -1,
        Se o usuario inserir mais, irá retornar a diferença,
        Se o usuario inserir menos, irá retornar 0,
        se a maquina não ter troco, irá retornar -2
        """
        # espresso:
        if user == 'espresso':
            if self.totalMoney ==1.5:
                return -1
            elif self.totalMoney >1.5:
                if machineMoney >= self.totalMoney-150:
                    return self.totalMoney-1.5
                else:
                    return -2
            else:
                return 0
        # latte:
        if user == 'latte':
            if self.totalMoney ==2.5:
                return -1
            elif self.totalMoney >2.5:
                if machineMoney >= self.totalMoney - 2.5:
                    return self.totalMoney - 2.5
                else:
                    return -2
            else:
                return 0
        # cappuccino:
        if user == 'cappuccino':
            if self.totalMoney ==3:
                return -1
            elif self.totalMoney > 3:
                if machineMoney >= self.totalMoney -3:
                    return self.totalMoney - 3
                else:
                    return -2
            else:
                return 0
