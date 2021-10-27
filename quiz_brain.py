class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    def still_has_questions(self):
        count = len(self.question_list)

        if(self.question_number < count):
            return True
        else:
            print("You've completed the quiz")
            print(f"Your final score was {self.score}/{len(self.question_list)}")
            False

    def next_question(self):
        current_question = self.question_list[self.question_number]

        answered = input(f"Q.{self.question_number+1}: {current_question.text} (True/False)?:")
        self.check_answer(answered,current_question.answer)
        self.question_number += 1

    def check_answer(self,answered,correct_answer):
        if (answered == correct_answer):
            self.score += 1
            print(f"Congratulations!")
        else:
            print("Wrong Answer :( ")
        print(f"Your actual score is {self.score} / {len(self.question_list)}")
        print(f"The correct answer was {correct_answer}")
        print("\n")