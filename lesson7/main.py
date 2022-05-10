import functions

def main():
    pk = int(input("Введите номер студента: \n"))
    student = functions.get_student_by_pk(pk) #получаем данные из функции

    if not student:
        print(f"У нас нет такого студента")
        quit()

    student_name = student["full_name"]
    student_skills = ", ".join(student["skills"])
    student_learns = ", ".join(student["learns"])

    print(f"Студент: {student_name}")
    print(f"Знает: {student_skills}")
    print(f"Хочет изучить: {student_learns}")
    print()

    title = input(f"Выберите специальность для оценки студента {student_name}:\n")
    profession = functions.get_profession_by_title(title) #получаем данные из функции
    if not profession:
        print(f"У нас нет такой профессии!")
        quit()

    total = functions.check_fitness(student, profession) #получаем данные из функции
    total_student_skills = ", ".join(total["has"])
    total_student_lacks_skills = ", ".join(total["lacks"])
    total_percent = total["fit_percent"]

    print(f"пригодность: {total_percent}%\n{student_name} знает: {total_student_skills}\n{student_name} не знает: {total_student_lacks_skills}\n")

main()
