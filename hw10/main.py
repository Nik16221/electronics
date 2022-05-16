import utils
from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_main():
    candidates = utils.load_data()
    code = utils.page_text_all(candidates)
    return code


@app.route("/candidates/<int:pk>")
def page_get_candidate_id(pk):
    candidate = utils.get_candidate_id(pk)
    if candidate is None:
        return "Такого кандидата нет!"
    code = utils.page_text_one(candidate)
    return code


@app.route("/skills/<skill_pk>")
def page_get_candidate_skill(skill_pk):
    candidates = utils.get_candidate_skill(skill_pk)
    if candidates is None:
        return "Такого кандидата нет!"
    code = utils.page_text_all(candidates)
    return code


if __name__ == "__main__":
    app.run(debug=True)
