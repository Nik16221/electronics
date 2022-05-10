class BasicWord:
    def __init__(self, basic_word, subwords):
        self.basic_word = basic_word  # изначальное слово
        self.subwords = subwords  # подслова изначального слова

    def __repr__(self):
        return f"\
        \nизначальное слово: {self.basic_word}\
        \nподслова изначального слова: {self.subwords}"

    def subword_verification(self, user_word):
        """проверка введенного слова в списке допустимых подслов (вернет bool)"""
        return str(user_word).lower() in self.subwords

    def counting_subwords(self):
        """подсчет количества подслов (вернет int)"""
        return len(self.subwords)


class Player:
    def __init__(self, user_name):
        self.user_name = user_name

        self.used_words = []
        self.right_used_words = []

    def __repr__(self):
        return f"\
               \nимя пользователя: {self.user_name}\
               \nдлина списка использованных слов: {len(self.used_words)}"

    def getting_number_subwords(self):
        """получение общего количества введенных слов (возвращает int)"""
        return len(self.used_words)

    def getting_number_right_subwords(self):
        """получение количества введенных верных слов (возвращает int)"""
        return len(self.right_used_words)

    def adding_used_words(self, user_word):
        """добавление слова в список использованных слов (ничего не возвращает)"""
        self.used_words.append(user_word)

    def adding_right_used_words(self, user_word):
        """добавление слова в список правильных использованных слова (ничего не возвращает)"""
        self.right_used_words.append(user_word)

    def checking_word_repetition(self, user_word):
        """проверка использования данного слова до этого (возвращает bool)"""
        return str(user_word).lower() in self.used_words
