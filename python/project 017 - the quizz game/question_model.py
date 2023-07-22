class QuestionModel:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def verifyAnswer(self):
        if self.answer == self.text['answer']:
            print('correct')
        else:
            print('wrong')