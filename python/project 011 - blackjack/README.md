# Blackjack game

A simple blackjack game created in Python. Test your luck and strategy against the dealer and see who can get closer to 21 without going bust!
This project will probably be a lot of work for anyone who came from zero in python and has followed the projects so far to learn, so it is extremely important to reinforce that it does not look bad if it takes more than 1 day to do the project, the important thing is to be able to do it

```

          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |   
                       |____V||  .  |
                              |____V|

```

## Table of Contents

1. [How to Play](#how-to-play)
2. [Code Structure](#code-structure)
3. [Used Concepts](#used-concepts)

## How to play

1. Run the main project file.
2. An ASCII logo representing a playing card will appear.
3. Accept the invitation to start the game.
4. You will receive two letters initially. If one of them is an Ace, you can choose whether you want it to be worth 1 or 11.
5. Keep hitting until you are satisfied with your hand or until you bust (have more than 21).
6. The dealer will reveal his cards. The objective is to have a hand whose total value is closer to 21 than the dealer's hand, without going over 21.

## Code Structure

The game is divided into several parts:

1. Startup: Here the game displays a logo and welcomes the player.
2. Dealing of cards: The player and the dealer are dealt cards.
3. Player Decisions: The player decides if he wants to continue taking cards.
4. Outcome: Based on the final hand values, it is decided who wins.

The game also has auxiliary functions to display victory or defeat messages.

## Concepts Used

- **Lists**: Used to represent the deck.
- **Random**: Used to distribute cards randomly.
- **Functions**: The code uses functions to modularize and organize the game's actions.
- **Loops**: The `while` loop is used to allow the player to continue taking cards until he decides to stop or bust.


# Jogo BlackJack

Um jogo simples de blackjack criado em Python. Teste sua sorte e estratégia contra o dealer e veja quem chega mais perto de 21 sem estourar!
Esse projeto provavelmente será trabalhoso para quem veio do zero em python e tem seguido os projetos até o momento para aprender, portanto é extremamente importante reforçar que não fique mal se levar mais de 1 dia para fazer o projeto, o importante é conseguir fazer



## Tabela de Conteúdos

1. [Como Jogar](#como-jogar)
2. [Estrutura do Código](#estrutura-do-código)
3. [Conceitos Utilizados](#conceitos-utilizados)

## Como Jogar

1. Execute o arquivo principal do projeto.
2. Será exibido um logo ASCII representando uma carta de baralho.
3. Aceite o convite para começar o jogo.
4. Você receberá duas cartas inicialmente. Se uma delas for um Ás, você pode escolher se quer que ele valha 1 ou 11.
5. Continue pedindo cartas até que você esteja satisfeito com sua mão ou até que você estoure (tenha mais de 21).
6. O dealer revelará suas cartas. O objetivo é ter uma mão cujo valor total seja mais próximo de 21 do que a mão do dealer, sem ultrapassar 21.

## Estrutura do Código

O jogo é dividido em várias partes:

1. Inicialização: Aqui o jogo apresenta um logo e dá as boas-vindas ao jogador.
2. Distribuição de cartas: O jogador e o dealer recebem cartas.
3. Decisões do jogador: O jogador decide se quer continuar pegando cartas.
4. Resultado: Baseado nos valores finais das mãos, decide-se quem vence.

O jogo também conta com funções auxiliares para exibir mensagens de vitória ou derrota.

## Conceitos Utilizados

- **Listas**: Utilizadas para representar o baralho.
- **Random**: Usado para distribuir cartas aleatoriamente.
- **Funções**: O código utiliza funções para modularizar e organizar as ações do jogo.
- **Loops**: O loop `while` é usado para permitir que o jogador continue pegando cartas até decidir parar ou estourar.

Credits ascii arts: Credits for ASCII ART: https://www.asciiart.eu/miscellaneous/playing-cards