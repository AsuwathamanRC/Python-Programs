from question_model import Question
from data import question_data, question_data_2, question_data_api
from quiz_brain import QuizBrain
from ui import QuizInterface

questionBank = []

# for item in question_data:
#     questionBank.append(Question(item["text"],item["answer"]))

# for item in question_data_2:
#     questionBank.append(Question(item["question"],item["correct_answer"]))

# Get questions through API
for item in question_data_api:
    questionBank.append(Question(item["question"],item["correct_answer"]))

quiz = QuizBrain(questionBank)
quizUI = QuizInterface(quiz)

# while quiz.still_has_question():
#     quiz.nextQuestion()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.questionNumber}")