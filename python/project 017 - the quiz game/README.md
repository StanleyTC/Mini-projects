# Quiz Game 🎮

The "Quiz Game" is a game of questions and answers where the player must answer if the statement is "True" or "False". The game displays random questions and keeps track of the user's correct answers. At the end, it presents the number of hits and a performance message.

```
 ,--.--------. ,--.-,,-,--,    ,----.            _,.---._                  .=-.-.                      _,---.   ,---.            ___      ,----.  
/==/,  -   , -/==/  /|=|  | ,-.--` , \         ,-.' - ,  `.   .--.-. .-.-./==/_ /,--,----.         _.='.'-,  \.--.'  \    .-._ .'=.'\  ,-.--` , \ 
\==\.-.  - ,-.|==|_ ||=|, ||==|-  _.-`        /==/ ,    -  \ /==/ -|/=/  |==|, |/==/` - ./        /==.'-     /\==\-/\ \  /==/ \|==|  ||==|-  _.-` 
 `--`\==\- \  |==| ,|/=| _||==|   `.-.       |==| - .=.  ,  ||==| ,||=| -|==|  |`--`=/. /        /==/ -   .-' /==/-|_\ | |==|,|  / - ||==|   `.-. 
      \==\_ \ |==|- `-' _ /==/_ ,    /       |==|  : ;=:  - ||==|- | =/  |==|- | /==/- /         |==|_   /_,-.\==\,   - \|==|  \/  , /==/_ ,    / 
      |==|- | |==|  _     |==|    .-'        |==|,  '='  ,  ||==|,  \/ - |==| ,|/==/- /-.        |==|  , \_.' /==/ -   ,||==|- ,   _ |==|    .-'  
      |==|, | |==|   .-. ,|==|_  ,`-._        \==\ _   -    ;|==|-   ,   |==|- /==/, `--`\       \==\-  ,    /==/-  /\ - |==| _ /\   |==|_  ,`-._ 
      /==/ -/ /==/, //=/  /==/ ,     /         '.='.  ,  ; -\/==/ , _  .'/==/. \==\-  -, |        /==/ _  ,  \==\ _.\=\.-/==/  / / , /==/ ,     / 
      `--`--` `--`-' `-`--`--`-----``            `--`--'' `--`--`..---'  `--`-` `--`.-.--`        `--`------' `--`       `--`./  `--``--`-----``
```

## 📄 Project Files

- **main.py**: Main file that runs the game. It starts by clearing the screen, displaying ASCII art from the game, then goes into a question-and-answer loop until all questions are asked. At the end, it evaluates the player's performance and shows a corresponding message.

- **data.py**: Contains a list of dictionaries with the questions and the correct answers.

- **question_model.py**: Defines the `QuestionModel` class, responsible for receiving a question and the player's answer and checking if the answer is correct.

## 📚 How It Works

1. The game starts displaying ASCII art.
2. A question is randomly chosen from `data.py` and presented to the player.
3. The player responds with "True" or "False".
4. The answer is checked and points are tallied.
5. The process is repeated until all questions are asked.
6. The player's performance is evaluated and a corresponding message is shown.

## ⚙️ Dependencies

- **replit**: Used to clear the screen.
- **time**: Used to add pauses between interactions.

## 🎖️ Results

- **10 or more hits**: The player is congratulated for his excellent results.
- **6-9 hits**: The player receives a message of satisfactory results.
- **Less than 6 hits**: The player is informed that the results were not good.

## 📌 Observations

For a better visual experience, you might consider adding a screenshot of the game or some ASCII art representing the quiz.

## 🚀 How to Play

1. Clone this repository.
2. Navigate to the game's directory.
3. Run `main.py` to start the game.



# Quiz Game 🎮

O "Quiz Game" é um jogo de perguntas e respostas onde o jogador deve responder se a afirmação é "Verdadeira" ou "Falsa". O jogo exibe perguntas aleatórias e mantém o controle das respostas corretas do usuário. Ao final, ele apresenta o número de acertos e uma mensagem de desempenho.


## 📄 Arquivos do Projeto

- **main.py**: Arquivo principal que executa o jogo. Ele começa limpando a tela, exibindo uma arte ASCII do jogo, depois entra em um loop de perguntas e respostas até que todas as perguntas sejam feitas. No final, ele avalia o desempenho do jogador e mostra uma mensagem correspondente.

- **data.py**: Contém uma lista de dicionários com as perguntas e as respostas corretas.

- **question_model.py**: Define a classe `QuestionModel`, responsável por receber uma pergunta e a resposta do jogador e verificar se a resposta está correta.

## 📚 Como Funciona

1. O jogo começa exibindo uma arte ASCII.
2. Uma pergunta é escolhida aleatoriamente do `data.py` e apresentada ao jogador.
3. O jogador responde com "True" ou "False".
4. A resposta é verificada e os pontos são contabilizados.
5. O processo é repetido até que todas as perguntas sejam feitas.
6. O desempenho do jogador é avaliado e uma mensagem correspondente é mostrada.

## ⚙️ Dependências

- **replit**: Usado para limpar a tela.
- **time**: Usado para adicionar pausas entre as interações.

## 🎖️ Resultados

- **10 ou mais acertos**: O jogador é parabenizado por seus excelentes resultados.
- **6-9 acertos**: O jogador recebe uma mensagem de resultados satisfatórios.
- **Menos de 6 acertos**: O jogador é informado de que os resultados não foram bons.

## 📌 Observações

Para uma melhor experiência visual, você pode considerar adicionar uma imagem do jogo ou alguma arte ASCII representando o quiz. 

## 🚀 Como Jogar

1. Clone este repositório.
2. Navegue até o diretório do jogo.
3. Execute `main.py` para começar o jogo.