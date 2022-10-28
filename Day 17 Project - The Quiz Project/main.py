from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score is: {quiz.score}/{quiz.q_number}")
