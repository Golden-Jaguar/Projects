from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
"""You change the questions by going to https://opentdb.com/ and adding new ones to the question_data in data.py"""
question_bank = []
for obj in question_data:
    ob = obj
    question_bank.append(Question(ob["question"], ob["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number} ")
