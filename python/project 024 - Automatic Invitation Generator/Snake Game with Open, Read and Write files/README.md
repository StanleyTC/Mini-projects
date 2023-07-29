# Snake Game with High Score Record

In this project, in addition to the game itself, we implemented the ability to record and display the highest score by reading and writing to a `.txt` file. Let's look at the details.

## Game Structure

- **main.py**: It is the main file that manages the game logic.
- **snake.py**: Defines the structure of the snake, including movement and behavior.
- **food.py**: Manages the food that the snake should consume.
- **scoreboard.py**: Controls the score and high score display.

## Analysis of .txt files for High Score

The ability to record the high score between game sessions is implemented using basic file read and write operations in Python.

### How is this done?

- There is a file called `data.txt`. By default, this file contains the value `0`. Each time the game starts and the snake collides with the edges or with itself, the program checks if the current score is greater than the registered high score. If so, it updates the high score.

- **High Score Reading**: At the beginning of each game, the program reads the high score from the `data.txt` file. This is done in the `Scoreboard` class:
  ```python
  with open("data.txt") as data:
      self.high_score = int(data.read())

The `read()` method reads the contents of the file as a string. It is then converted to an integer using `int()`.

**Saving the new High Score:** If the current score is greater than the registered high score, the new score will be written to the data.txt file, replacing the previous value:
```
if self.score > self.high_score:
    self.high_score = self.score
    with open("data.txt", "w") as file:
        file.write(f"{self.score}")
```
By using the practice of reading and writing files, this game becomes more interactive and challenging, as players can try to beat the high score in each new session.

## How to play

1. Use the W, A, S and D keys to move the snake up, left, down and right, respectively.
2. The objective is to eat the food (represented by a blue circle). Each time the snake eats the food, it grows in size and the score increases.
3. If the snake collides with the edges or with itself, the game will restart.
4. Current score and high score are displayed at the top of the screen.



# Snake Game com Registro de High Score

Neste projeto, além do jogo em si, implementamos a capacidade de registrar e exibir a pontuação mais alta através da leitura e gravação em um arquivo `.txt`. Vamos observar os detalhes.

## Estrutura do Jogo

- **main.py**: É o arquivo principal que gerencia a lógica do jogo.
- **snake.py**: Define a estrutura da cobrinha, incluindo movimentação e comportamento.
- **food.py**: Gerencia a comida que a cobrinha deve consumir.
- **scoreboard.py**: Controla a pontuação e a exibição do high score.

## Análise de arquivos.txt para High Score

A capacidade de registrar o high score (pontuação mais alta) entre as sessões do jogo é implementada usando operações básicas de leitura e gravação de arquivos em Python.

### Como isso é feito?

- Há um arquivo chamado `data.txt`. Por padrão, este arquivo contém o valor `0`. Cada vez que o jogo começa e a cobrinha colide com as bordas ou com ela mesma, o programa verifica se a pontuação atual é maior que o high score registrado. Se for, ele atualiza o high score.

- **Leitura do High Score**: No início de cada jogo, o programa lê o high score do arquivo `data.txt`. Isso é feito na classe `Scoreboard`:
  ```python
  with open("data.txt") as data:
      self.high_score = int(data.read())

O método `read()` lê o conteúdo do arquivo como uma string. Em seguida, é convertido para um inteiro usando `int()`.

**Gravação do novo High Score:** Se a pontuação atual for maior que o high score registrado, a nova pontuação será escrita no arquivo data.txt, substituindo o valor anterior:
```
if self.score > self.high_score:
    self.high_score = self.score
    with open("data.txt", "w") as file:
        file.write(f"{self.score}")
```
Ao utilizar a prática de leitura e gravação de arquivos, este jogo se torna mais interativo e desafiador, pois os jogadores podem tentar superar o high score a cada nova sessão.

## Como jogar

1. Use as teclas W, A, S e D para mover a cobrinha para cima, esquerda, baixo e direita, respectivamente.
2. O objetivo é comer a comida (representada por um círculo azul). Cada vez que a cobrinha come a comida, ela cresce em tamanho e a pontuação aumenta.
3. Se a cobrinha colidir com as bordas ou com ela mesma, o jogo será reiniciado.
4. A pontuação atual e o high score são exibidos na parte superior da tela.