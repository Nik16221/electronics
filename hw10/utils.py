import json


def load_data():
    """Выгружаем данные из файла json"""
    with open("candidates.json", "rt", encoding="utf-8") as file:
        date = json.load(file)
    return date


def get_candidate_id(pk):
    """выгружаем информацию о кандидате по введенному PK"""
    candidates = load_data()
    for candidate in candidates:
        if candidate["id"] == pk:
            return candidate


def get_candidate_skill(skill_pk):
    """выгружаем кандидатов с заданным скилом"""
    skill_candidates = []
    candidates = load_data()

    for candidate in candidates:
        if skill_pk.lower() in candidate["skills"].lower().strip().split(", "):
            skill_candidates.append(candidate)
            return skill_candidates


def page_text_all(candidates):
    """вывод данных в заданном формате(несколько кандидатов)"""
    info = ""

    for candidate in candidates:
        info += f"{candidate['name']}\n"
        info += f"{candidate['position']}\n"
        info += f"{candidate['skills']}\n"
        info += "\n"
    return "<pre>" + info + "<pre>"


def page_text_one(candidate):
    """вывод данных в заданном формате(один кандидат)"""

    info = ""

    info += f"<img src={candidate['picture']}>\n"
    info += f"{candidate['name']}\n"
    info += f"{candidate['position']}\n"
    info += f"{candidate['skills']}\n"
    info += "\n"
    return "<pre>" + info + "<pre>"
