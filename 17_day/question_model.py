"""The Question Model"""
class Question:
    def __init__(self, q_text, q_answer):
        """Attributes of the Question class"""
        self.text = q_text
        self.answer = q_answer