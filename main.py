from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = item["question"]
    answer = item["correct_answer"]
    questionObj = Question(question,answer)
    question_bank.append(questionObj)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()