class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.correct_answer = 0
        self.question_list = q_list

    def next_question(self):
        question_current = self.question_list[self.question_no]
        ans = input(f"Q{self.question_no + 1}: {question_current.text} (True/False): ")
        return ans

    def check_answer(self):
        question_current = self.question_list[self.question_no]
        if self.next_question() == question_current.answer:
            self.correct_answer += 1
        self.question_no += 1
        print(f"{self.correct_answer}/{self.question_no}")

