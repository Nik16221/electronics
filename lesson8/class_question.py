class Question:
    def __init__(self, question_text, difficult, right_answer):
        self.question_text = question_text
        self.difficult = int(difficult)
        self.right_answer = right_answer

        self.is_question = False
        self.user_answer = None
        self.score_question = 0


    def __repr__(self):
        return f"\
               \nВопрос: {self.question_text} \
               \nСложность: {self.difficult}/5 \
               \nПравильный ответ: {self.right_answer} \
               \nЗадан ли вопрос: {self.is_question} \
               \nОтвет пользователя: {self.user_answer} \
               \nБаллы за вопрос: {self.score_question}"


    def get_points(self):
        self.score_question = self.difficult*10
        return int(self.score_question)


    def is_correct(self):
        if self.user_answer == self.right_answer:
            return True
        else:
            return False


    def build_question(self):
        return f"\nвопрос: {self.question_text}\nсложность: {self.difficult}/5"


    def build_feedback(self):
        if self.is_correct() is True:
            return f"Ответ верный, получено {self.get_points()} баллов"
        else:
            return f"Ответ неверный, верный ответ: {self.right_answer}"

