# Automatic Invitation Generator

This module will start your studies with data analysis in txt files, so you should study how to use the open, read and write methods for this, in addition to understanding about file . Initially, we will remake the snake game that we had done before, but with the ability now to persist the record, saving it in a txt file so that it can be used again (details of the changes are in the new README.md inside the Snake Game folder with Open, Read and Write files).

Once that's done, we'll be ready for the challenge involving the Mail Merge Challenge.

## About the project itself

This project reads a list of names and creates personalized invitations for each person. The generated invitations are saved in an output folder, ready to be sent.

## Table of Contents

1. [How It Works](#how-it-works)
2. [How to Run](#how-to-run)
3. [Code Structure](#code-structure)
4. [Used Concepts](#used-concepts)
5. [Credits](#credits)

## How it works

- A list of names is read from a file called `invited_names.txt`.
- The project then reads a letter template that has a `[name]` placeholder.
- For each name in the list, the placeholder is replaced by the person's name.
- A custom invitation file is generated for each person in the `Output/ReadyToSend` folder.

## How to Run

1. Ensure that the `Input/Names`, `Input/Letters` and `Output/ReadyToSend` directories exist.
2. Add the list of names in the `Input/Names/invited_names.txt` file.
3. The template file should be at `Input/Letters/starting_letter.txt` and contain the placeholder `[name]` where the name should be entered.
4. Run the main script.
5. Check the `Output/ReadyToSend` folder for the generated invites.

## Code Structure

The code is divided into several parts:

1. **Read Names**: Opens and reads the `invited_names.txt` file and stores the names in a list.
2. **Read Template**: Opens and reads the `starting_letter.txt` file to get the template content.
3. **Creating Invitations**: For each name in the list of names, the code creates a personalized invitation by replacing the placeholder `[name]` with the person's name.
4. **Saving Invitations**: Each personalized invitation is saved in a separate file in the `Output/ReadyToSend` folder.

## Concepts Used

- **File Handling**: The project makes extensive use of file read and write operations.
- **Lists**: Lists are used to store the names.
- **Loops**: Loops are used to iterate over each name and create an invite for each one.
- **String Manipulation**: The `replace` method is used to replace the `[name]` placeholder with the actual name.

## Credits

Developed by StanleyTC. This is a hands-on project to demonstrate basic concepts of file and string manipulation in Python.




# Gerador Automático de Convites

Esse módulo irá iniciar seus estudos com analise de dados em arquivos txt, então você deverá estudar como usar os métodos open, read e write para isso, além de entender sobre file . Inicialmente, iremos refazer o jogo da cobrinha que haviamos feito antes, mas com a capacidade agora de persistir o recorde, salvando ele em um arquivo txt para que possa ser utilizado novamente (detalhes das alterações estão no novo README.md dentro da pasta Snake Game with Open, Read and Write files).

Feito isso, estaremos prontos para o desavio envolvendo o Mail Merge Challenge.

## Sobre o projeto em si

Este projeto lê uma lista de nomes e cria convites personalizados para cada pessoa. Os convites gerados são salvos em uma pasta de saída, prontos para serem enviados.

## Tabela de Conteúdos

1. [Como Funciona](#como-funciona)
2. [Como Executar](#como-executar)
3. [Estrutura do Código](#estrutura-do-código)
4. [Conceitos Utilizados](#conceitos-utilizados)
5. [Créditos](#créditos)

## Como Funciona

- Uma lista de nomes é lida de um arquivo chamado `invited_names.txt`.
- O projeto então lê um modelo de carta que possui um espaço reservado `[name]`.
- Para cada nome da lista, o espaço reservado é substituído pelo nome da pessoa.
- Um arquivo de convite personalizado é gerado para cada pessoa na pasta `Output/ReadyToSend`.

## Como Executar

1. Garanta que os diretórios `Input/Names`, `Input/Letters` e `Output/ReadyToSend` existam.
2. Adicione a lista de nomes no arquivo `Input/Names/invited_names.txt`.
3. O arquivo modelo deve estar em `Input/Letters/starting_letter.txt` e conter o espaço reservado `[name]` onde o nome deve ser inserido.
4. Execute o script principal.
5. Verifique a pasta `Output/ReadyToSend` para os convites gerados.

## Estrutura do Código

O código é dividido em várias partes:

1. **Leitura de Nomes**: Abre e lê o arquivo `invited_names.txt` e armazena os nomes em uma lista.
2. **Leitura do Modelo**: Abre e lê o arquivo `starting_letter.txt` para obter o conteúdo modelo.
3. **Criação dos Convites**: Para cada nome na lista de nomes, o código cria um convite personalizado substituindo o espaço reservado `[name]` pelo nome da pessoa.
4. **Salvando os Convites**: Cada convite personalizado é salvo em um arquivo separado na pasta `Output/ReadyToSend`.

## Conceitos Utilizados

- **Manipulação de Arquivos**: O projeto faz uso extensivo de operações de leitura e gravação de arquivos.
- **Listas**: As listas são usadas para armazenar os nomes.
- **Loops**: Loops são usados para iterar sobre cada nome e criar um convite para cada um.
- **String Manipulation**: O método `replace` é usado para substituir o espaço reservado `[name]` pelo nome real.

## Créditos

Desenvolvido por StanleyTC. Este é um projeto prático para demonstrar conceitos básicos de manipulação de arquivos e strings em Python.