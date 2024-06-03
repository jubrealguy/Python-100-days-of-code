"""The class QuizBrain where all the brain of the Quiz is"""

class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.correct_answer = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        question_current = self.question_list[self.question_no]
        self.question_no += 1
        ans = input(f"Q{self.question_no}: {question_current.text} (True/False): ")
        self.check_answer(ans, question_current.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.correct_answer += 1
            print("You are right")
        else:
            print("You are wrong")
        print(f"The correct answer was: {correct_ans}")
        print(f"Your current score is: {self.correct_answer}/{self.question_no}")
        print()

    def quiz_completed(self):
        print("You have completed the Quiz")
        print(f"Your final score was: {self.correct_answer}/{self.question_no}")

