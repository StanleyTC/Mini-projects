# Rock, Paper, Scissors game

This project is the classic game between rock, paper and scissors made in python, another project to reinforce what has been done so far with the programming concepts used in other projects.

```
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Art Credits: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe 
```

## Table of Contents

1. [How It Works](#how-it-works)
2. [How to Play](#how-to-play)
3. [Code Structure](#code-structure)
4. [Used Programming Concepts](#used-programming-concepts)
5. [Credits](#credits)

## How it works

- You choose between rock (1), paper (2) or scissors (3).
- The computer also chooses one of the options.
- The choice of both is revealed and the winner is determined by the classic rule: rock crushes scissors, scissors cut paper and paper covers rock.

## How to play

1. Run the script.
2. Type `1` for stone, `2` for paper and `3` (or any other number) for scissors.
3. See the computer's choice and find out the result of the match.

## Code Structure

The code is divided into several parts:

1. **User Input**: Where you choose your move.
2. **Computer decision**: The computer makes a random choice.
3. **Choice Reveal**: The choice of both user and computer is shown with the help of ASCII art.
4. **Winner Determination**: The code compares the picks and decides the outcome of the match.

## Used Programming Concepts

- **ASCII Artwork**: We use ASCII artwork to visually illustrate rock, paper, scissors choices.
- **Random number generation**: We use the `randint` function of the `random` module to generate the computer's choice.
- **Flow Control**: We use `if/elif/else` structures to control the flow of the game, displaying artwork and determining the result.
- **Timer**: We use the `sleep` function of the `time` module to create pauses and improve the user experience.

## Credits

Developed by StanleyTC. The code uses ASCII art that was obtained [here](https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe). This is a project to demonstrate basic concepts of random number generation, flow control and string manipulation in Python.


# Jogo de Pedra, Papel e Tesoura

Esse projeto é o classico jogo entre pedra, papel e tesoura feito em python, mais um projeto para reforçar o que já foi feito até então com os conceitos de programação utilizados em outros projetos.

## Tabela de Conteúdos

1. [Como Funciona](#como-funciona)
2. [Como Jogar](#como-jogar)
3. [Estrutura do Código](#estrutura-do-código)
4. [Conceitos de Programação Utilizados](#conceitos-de-programação-utilizados)
5. [Créditos](#créditos)

## Como Funciona

- Você escolhe entre pedra (1), papel (2) ou tesoura (3).
- O computador também escolhe uma das opções.
- A escolha de ambos é revelada e o vencedor é determinado pela regra clássica: pedra esmaga tesoura, tesoura corta papel e papel cobre pedra.

## Como Jogar

1. Execute o script.
2. Digite `1` para pedra, `2` para papel e `3` (ou qualquer outro número) para tesoura.
3. Veja a escolha do computador e descubra o resultado da partida.

## Estrutura do Código

O código é dividido em várias partes:

1. **Entrada do usuário**: Onde você escolhe sua jogada.
2. **Decisão do computador**: O computador faz uma escolha aleatória.
3. **Revelação das escolhas**: A escolha de ambos, usuário e computador, é mostrada com a ajuda de artes ASCII.
4. **Determinação do vencedor**: O código compara as escolhas e decide o resultado da partida.

## Conceitos de Programação Utilizados

- **Arte ASCII**: Usamos artes ASCII para ilustrar visualmente as escolhas de pedra, papel e tesoura.
- **Geração de números aleatórios**: Usamos a função `randint` do módulo `random` para gerar a escolha do computador.
- **Controle de fluxo**: Usamos estruturas `if/elif/else` para controlar o fluxo do jogo, exibindo artes e determinando o resultado.
- **Temporização**: Utilizamos a função `sleep` do módulo `time` para criar pausas e melhorar a experiência do usuário.

## Créditos

Desenvolvido por StanleyTC. O código utiliza artes ASCII que foram obtidas [aqui](https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe). Este é um projeto para demonstrar conceitos básicos de geração de números aleatórios, controle de fluxo e manipulação de strings em Python.


