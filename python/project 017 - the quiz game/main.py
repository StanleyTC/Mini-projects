from data import question_data
from random import randint
from question_model import QuestionModel
from replit import clear
from time import sleep 
from ascii import trophy, quiz


clear()

sleep(0.5)
print(quiz)
counter = 0
correctAnswer = 0
finalCounter = len(question_data)

while counter < finalCounter:
    choose_quest = question_data[randint(0, len(question_data)-1)]
    question_data.remove(choose_quest)
    user = input(f"True or False - {choose_quest['text']}: ").capitalize()
    sleep(0.25)

    question = QuestionModel(choose_quest, user)
    answer = question.verifyAnswer()
    if answer == 1:
        correctAnswer+=1
        print(f'Correct! +1 point, you got {correctAnswer}/{counter+1} correct answers')
    if answer == 0:
        print(f'Wrong..., you got {correctAnswer}/{counter+1} correct answers')

    counter += 1


if correctAnswer >= 10:
    sleep(0.5)
    print(f'Congratulations!, you had {correctAnswer} of {finalCounter}!, good results')
    sleep(0.25)
    print(trophy)
elif correctAnswer >= 6:
    sleep(0.5)
    print(f'Good, satisfactory results, {correctAnswer} of {finalCounter}, keep going!')
else:
    sleep(0.5)
    print(f'Sorry, you got {correctAnswer} of {finalCounter}, not good results')