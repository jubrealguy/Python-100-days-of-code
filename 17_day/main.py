from data import question_data
from question_model import Question


question_list = []
for item in question_data:
    new_q = Question(item['text'], item['answer'])
    question_list.append(new_q)
print(question_list)