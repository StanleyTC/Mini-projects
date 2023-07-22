from data import question_data
from random import randint
from question_model import QuestionModel

counter = 0
correctAnswer = 0

while counter < len(question_data):
    choose_quest = question_data[randint(0, len(question_data)-1)]
    question_data.remove(choose_quest)
    user = input(f"True or False - {choose_quest['text']}: ").capitalize()

    question = QuestionModel(choose_quest, user)
    answer = question.verifyAnswer()
    if answer == 1:
        correctAnswer+=1
        print(f'Correct! +1 point, you got {correctAnswer}/{counter+1} correct answers')
    if answer == 0:
        print(f'Wrong..., you got {correctAnswer}/{counter+1} correct answers')

    counter += 1

print(f'Game over, you had {correctAnswer} of {len(question_data)}')