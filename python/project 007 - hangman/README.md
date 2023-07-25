# Hangman Game

Test your vocabulary with the classic Hangman game! This command-line version provides a challenging and fun experience, complete with visual representations of each stage of the game.
This project involves the creation of the classic pencil and paper game: hangman.
The objective of this project will be to train everything we've seen so far: loop structures, conditional structures, use of libraries and lists, the most interesting thing is the use of our own modules: notice that I created the ascii.py module where all the arts will be used to print on the user's screen, and the words.py module where there is the list of words. The goal is not to pollute the main code located in main.py.

## [Hangman Script](main.py)

### Description:

A traditional word-guessing game where you aim to figure out the hidden word by guessing one letter at a time. Be careful though! Make too many incorrect guesses, and the hangman gets completed, resulting in a loss.

### How to Use:

1. Execute the `main.py` script.
2. Follow the on-screen prompts.
3. Guess letters one by one.
4. The game continues until you've either guessed the word or have made six incorrect guesses.

### Features:

- Large word list to ensure unique challenges each time.
- ASCII art representations for various game stages, including the hangman, trophy, and skull.
- Simple and intuitive user interface.

## Additional Files:

- [words.py](./words.py): Contains a list of words used in the game.
- [ascii.py](./ascii.py): Houses the ASCII art representations for the game.

## Requirements:

- Python
