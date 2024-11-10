
# create question class with an init() and two attributes for text and answer

class Question:
    # please be mindful of variable naming conventions
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer