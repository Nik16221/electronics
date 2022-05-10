import json


def load_students():
#функция выгружает информацию о студентах
    with open("students.json") as json_file:
        data = json.load(json_file)
    return data


def load_professions():
#функция выгружает информацию о профессиях
    with open("professions.json") as json_file:
        data = json.load(json_file)
    return data


def get_student_by_pk(pk):
#функция выгружает информацию о конкретном студенте по pk
    students = load_students()
    for student in students:
        if pk == student["pk"]:
            return student


def get_profession_by_title(title):
#функция выгружает информацию о конкретной профессии по title
    professions = load_professions()
    for profession in professions:
        if title.title() == profession["title"]:
            return profession


def check_fitness(student, profession):
#функция сравнивает необходимые навыки по профессии с имеющимися навыками и выдает статистику
    student_skills = set(student["skills"]) #определяем множество навыков студента
    profession_skills = set(profession["skills"]) #определяем множество навыков профессии

    has_skills = student_skills.intersection(profession_skills) #определяем какие навыки, необходимые для профессии, знает студент
    lacks_skills = profession_skills.difference(has_skills) #определяем какие навыки, необхоимые для профессии, не знает студент
    fit_percent = round(len(has_skills)/len(profession_skills)*100)

    return {
            "has": list(has_skills),
            "lacks": list(lacks_skills),
            "fit_percent": fit_percent,
        }










