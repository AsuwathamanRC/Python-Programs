from question_model import Question
from data import question_data, question_data_2
from quiz_brain import QuizBrain

questionBank = []

# for item in question_data:
#     questionBank.append(Question(item["text"],item["answer"]))

for item in question_data_2:
    questionBank.append(Question(item["question"],item["correct_answer"]))

quiz = QuizBrain(questionBank)

while quiz.still_has_question():
    quiz.nextQuestion()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.questionNumber}")