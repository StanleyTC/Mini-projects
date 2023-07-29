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