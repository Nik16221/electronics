import random
user_name = input("Как Вас зовут?\n")
score_count = 0
print(f"{user_name.title()}, начнем игру!")


def count_play():
    play = 0
    with open("history.txt") as file:
        for line in file:
            play += 1
    return play


def maximum():
    total_score = []
    with open("history.txt", encoding="utf-8") as file:
        for line in file:
            name, score = line.strip().split(" ")
            total_score.append(score)
            max_score = max(total_score)
    return max_score


def congratulations():
    if int(score_count) >= int(maximum()):
        print(f"{user_name} набрал {score_count} очков!!! ЭТО НОВЫЙ РЕКОРД!!!")
    else:
        print(f"{user_name} набрал {score_count} очков!")
    print(f"Всего игр сыграно: {count_play()}\nМаксимальный рекорд: {maximum()}")


with open("words.txt", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        new_line = random.sample(line, len(line))
        new_line = "".join(new_line)
        user_answer = input(f"Угадайте слово: {new_line}\n")
        if user_answer.lower() == line:
            score_count += 10
            print(f"Верно! Вы получаете 10 очков.")
            print()
        else:
            print(f"Неверно! Верный ответ – {line}")
            print()

with open("history.txt", "a", encoding="utf-8") as file:
    file.write(f"{user_name.title()} {score_count}\n")

congratulations()

