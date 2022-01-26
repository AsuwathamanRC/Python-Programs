import html

class QuizBrain():
    def __init__(self, questionList):
        self.questionNumber = 0
        self.questionList = questionList
        self.score = 0
        self.current_question = None

    def still_has_question(self):
        if self.questionNumber == len(self.questionList):
            return False
        else:
            return True

    def nextQuestion(self):
        self.currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        ques = html.unescape(self.currentQuestion.question)
        return f"Q.{self.questionNumber}: {ques} (True/False)?: "
        # user_answer = input(f"Q.{self.questionNumber}: {ques} (True/False)?: ")
        # self.check_answer(user_answer, currentQuestion.answer)

    def check_answer(self, user_answer):
        correct_answer = self.currentQuestion.answer
        if user_answer.lower() == correct_answer.lower():
            # print("You got it right!")
            self.score += 1
            return True
        else:
            # print("That's wrong.")
            return False

        # print(f"The correct answer was: {correct_answer}.")
        # print(f"Your current score is: {self.score}/{self.questionNumber}\n")