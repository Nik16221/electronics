import json
from class_question import Question

def load_questions():
    with open("questions.json", encoding="utf-8") as file:
        questions_data = json.load(file)
    questions = []

    for question_data in questions_data:
        question = Question(
            question_data["q"],
            question_data["d"],
            question_data["a"],
        )

        questions.append(question)
    return questions
