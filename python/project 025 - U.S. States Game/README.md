# U.S. States Guessing Game

## Introduction
The "U.S. States Guessing Game" is an interactive challenge where players are prompted to name the states of the USA. Each time a player guesses correctly, the state's name is displayed on the map. If the player decides to exit or finish the game early, the unguessed states are saved to a CSV file for future review.

![](blank_states_img.gif) 

## Concepts Used

### 1. Python Programming
The game was developed using the Python programming language, which is widely recognized for its simplicity and ability to handle data analysis tasks.

### 2. Turtle Library
The Turtle library is used to provide an interactive graphical interface. It allows:
- Displaying images: In this case, `blank_states_img.gif` serves as the background and represents the map of the USA.
- Creating and managing graphical elements, such as displaying the name of the states.
- Receiving user input through dialog boxes.

### 3. Pandas for Data Analysis
The Pandas library is an essential tool for data analysis in Python. It's used to:
- Load data from the CSV file: The `50_states.csv` file contains the names and coordinates of the states.
- Manipulate data: Removing guessed states from the list, filtering data based on conditions, etc.
- Save data: The unguessed states are saved to a new CSV file (`states to learn.csv`) for review.

### Game Flow
1. The map image of the USA is loaded.
2. The state data is loaded from the CSV file using Pandas.
3. The player is continually prompted to guess a state.
    - If the guess is correct, the state name is displayed on the map, and the state is removed from the list of states to guess.
    - If the player enters "Exit", the game will end.
4. The game ends after 50 rounds or if the player decides to exit early.
5. The unguessed states are saved to a new CSV file for review.

## How to Play
1. Run the `main.py` file.
2. A window with the USA map will appear.
3. Type in the name of a state in the dialog box. If correct, the name will appear on the map.
4. Continue guessing until all states are named or until you decide to exit.
5. To exit before guessing all the states, type "Exit".
6. At the end of the game, check the `states to learn.csv` file to review the states you couldn't guess.

## Conclusion
This is an educational project that is excellent for practicing the concepts seen so far from using the turtle library and now analyzing data with Pandas.



# U.S. States Guessing Game

## Introdução
O jogo "U.S. States Guessing Game" é um desafio interativo onde os jogadores são solicitados a nomear os estados dos EUA. Cada vez que um jogador adivinha corretamente, o nome do estado é mostrado no mapa. Se o jogador decidir sair ou terminar o jogo, os estados não adivinhados são salvos em um arquivo CSV para futuras revisões.

## Conceitos Utilizados

### 1. Programação em Python
O jogo foi desenvolvido usando a linguagem de programação Python, que é amplamente reconhecida por sua simplicidade e capacidade de lidar com tarefas de análise de dados.

### 2. Biblioteca Turtle
A biblioteca Turtle é usada para fornecer uma interface gráfica interativa. Ela permite:
- Mostrar imagens: No caso, `blank_states_img.gif` serve como plano de fundo e representa o mapa dos EUA.
- Criar e gerenciar elementos gráficos, como a escrita do nome dos estados.
- Receber entradas do usuário através de caixas de diálogo.

### 3. Pandas para Análise de Dados
A biblioteca Pandas é uma ferramenta essencial para análise de dados em Python. Ela é usada para:
- Carregar dados do arquivo CSV: O arquivo `50_states.csv` contém os nomes e coordenadas dos estados.
- Manipular os dados: Remover estados adivinhados da lista, filtrar dados com base em condições, etc.
- Salvar dados: Os estados não adivinhados são salvos em um novo arquivo CSV (`states to learn.csv`) para revisão.

### Fluxo do Jogo
1. A imagem do mapa dos EUA é carregada.
2. Os dados dos estados são carregados do arquivo CSV usando o Pandas.
3. O jogador é continuamente solicitado a adivinhar um estado.
    - Se a adivinhação estiver correta, o nome do estado é exibido no mapa e o estado é removido da lista de estados a serem adivinhados.
    - Se o jogador inserir "Exit", o jogo terminará.
4. O jogo termina após 50 rodadas ou se o jogador decidir sair antes.
5. Os estados não adivinhados são salvos em um novo arquivo CSV para revisão.

## Como Jogar
1. Execute o arquivo `main.py`.
2. Uma janela com o mapa dos EUA aparecerá.
3. Digite o nome de um estado na caixa de diálogo. Se estiver correto, o nome aparecerá no mapa.
4. Continue adivinhando até que todos os estados sejam nomeados ou até que você decida sair.
5. Para sair antes de adivinhar todos os estados, digite "Exit".
6. No final do jogo, verifique o arquivo `states to learn.csv` para revisar os estados que você não conseguiu adivinhar.

## Conclusão
Este é um projeto educativo que é excelente para práticar os conceitos vistos até então do uso da biblioteca turtle e agora da analise de dados com Pandas.
