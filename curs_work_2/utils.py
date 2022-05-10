from classes import BasicWord
import random
import requests


def load_random_word():
    words_dict = requests.get("https://jsonkeeper.com/b/PY6Y")
    words_dict_json = words_dict.json()
    words = []
    for word_dict_json in words_dict_json:
        info_words = BasicWord(
            word_dict_json["word"],
            word_dict_json["subwords"]
        )
        words.append(info_words)
        random.shuffle(words)
    for word in words:
        return word


def score_result(word):
    score = word % 10
    if score == 0:
        return "слов"
    elif score == 1:
        return "слово"
    elif score >= 5:
        return "слов"
    else:
        return "слова"
