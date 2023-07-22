from data import question_data
from random import randint
from question_model import QuestionModel

choose_quest = question_data[randint(0, len(question_data)-1)]
question_data.remove(choose_quest)
user = input(f"{choose_quest['text']}: ").lower()

question = QuestionModel(choose_quest, user)
print(choose_quest)