from ascii import gameLogo, vs
from list import lista
from random import randint
from time import sleep
from ascii import gameOver, trophy

counter = 1

# Funcação game won
def gameWon(counter):
    print(f'Congratulations! you finished all possible comparations!')
    sleep(0.5)
    print(f'you made {counter} points!!!')
    sleep(0.5)
    print(trophy)

    
# Funcação game over
def EndGame(counter):
    print(f'Sorry, wrong answer... you lost')
    sleep(0.5)
    print(f'you made {counter} points...')
    sleep(0.5)
    print(gameOver)


# Sortear dois iniciais para comparar
print(gameLogo)
a = lista[randint(0, len(lista)-1)]
b = lista[randint(0, len(lista)-1)]
while b == a:
    b = lista[randint(0, len(lista)-1)]

user = input(f"Compare A: {a['Name']}, a {a['description']} \n{vs} \nAgaint B: {b['Name']}, a {b['description']}: \nWho has more followers? Type 'A' or 'B': ").lower()
lista.remove(a)
lista.remove(b)

# Comparar o que o usuario escolheu:
if user == 'a' and (a['followers']>b['followers']):
    cont = 1
if user == 'b' and (b['followers']>a['followers']):
    cont = 1
    a = b

if user == 'a' and (a['followers']<b['followers']):
    cont = 0
if user == 'b' and (b['followers']<a['followers']):
    cont = 0

# Continuar o jogo se o usuario acertar na primeira rodada:
while cont == 1:
    # Sortear outro item da lista para comparar
    b = lista[randint(0, len(lista)-1)]
    while b == a:
        b = lista[randint(0, len(lista)-1)]
    #Mostrar quantos pontos tem até agora:
    print(f'You already have {counter} points')
    # Perguntar novamente ao usuário: 
    user = input(f"Compare A: {a['Name']}, a {a['description']} \n{vs} \nAgaint B: {b['Name']}, a {b['description']}: \nWho has more followers? Type 'A' or 'B': ").lower()
    if a in lista:
        lista.remove(a)
    if b in lista:
        lista.remove(b)
    # Comparar
    if user == 'a' and (a['followers']>b['followers']):
        counter += 1
    if user == 'b' and (b['followers']>a['followers']):
        counter += 1
        a = b

    if user == 'a' and (a['followers']<b['followers']):
        EndGame(counter)
        break
    if user == 'b' and (b['followers']<a['followers']):
        EndGame(counter)
        break
    # Caso a lista acabe e o usuário acerte todos os valores
    gameWon(counter)

# Encerrar o jogo se o usuario errar na primeira rodada

if cont == 0:
    EndGame(0)
