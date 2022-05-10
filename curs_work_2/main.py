import utils
from classes import Player


def main():
    user_name = input("Введите свое имя: \n")
    word = utils.load_random_word()
    player_info = Player(user_name)

    print(f'Привет, {user_name.title().replace(" ", "")}!')
    print(f'Составьте {word.counting_subwords()} слов из слова "{str(word.basic_word).upper()}".\
          \nСлова должны быть не короче 3 букв.\
          \nЧтобы закончить игру, угадайте все слова или напишите "stop".')

    while player_info.getting_number_right_subwords() != word.counting_subwords():
        user_word = input("\nВаше слово?\n")
        if user_word.lower() in ("stop", "стоп"):
            print(f"Игра завершена!\nВы угадали {player_info.getting_number_right_subwords()}\
 {utils.score_result(player_info.getting_number_right_subwords())}!")
            quit()
        if len(user_word) < 3:
            print("Слово слишком короткое! Введите другое слово!")
            continue
        if player_info.checking_word_repetition(user_word):
            print("Это слово уже было! Введите другое слово!")
            continue
        if word.subword_verification(user_word):
            player_info.adding_used_words(user_word)
            player_info.adding_right_used_words(user_word)
            print("Верно")
        else:
            player_info.adding_used_words(user_word)
            print("Неверно")

    print(f"слова закончились, игра завершена!\
                \nВы угадали все {player_info.getting_number_right_subwords()}\
 {utils.score_result(player_info.getting_number_right_subwords())}!")


main()
