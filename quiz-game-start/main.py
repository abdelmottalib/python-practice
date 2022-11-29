from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []
for list in question_data:
    list_q = []
    for key in list:
        list_q.append(list[key])
    question = Question(list_q[0], list_q[1])
    questions_bank.append(question)

quiz = QuizBrain(questions_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("you have completed the quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}.")
