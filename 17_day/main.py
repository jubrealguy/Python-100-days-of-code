from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    new_q = Question(item['text'], item['answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
for i in range(len(question_bank)):
    quiz.check_answer()