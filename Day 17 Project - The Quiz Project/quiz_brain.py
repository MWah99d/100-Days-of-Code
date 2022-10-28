class QuizBrain:

    def __init__(self, question_list):
        self.q_number = 0
        self.questions = question_list
        self.score = 0

    def still_has_questions(self):
        return self.q_number < len(self.questions)

    def next_question(self):
        current_question = self.questions[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/False): ").title()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.q_number}\n")
