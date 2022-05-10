import functions
import random


def main():
    questions = functions.load_questions()

    random.shuffle(questions)
    total_right_answer = 0
    total_score = 0
    print("Игра начинается!")

    for question in questions:
        print(question.build_question())
        question.is_question = True
        question.user_answer = input()
        print(question.build_feedback())

        if question.is_correct():
            total_right_answer += 1
            total_score += question.get_points()

    print(f"Вот и всё!\
       \nОтвечено верно на {total_right_answer} вопроса из {len(questions)}\
       \nВсего набрано {total_score} баллов")

    if __name__ == "__main__":
        main()
main()