from flask import Flask
from utils import load_candidates, get_all_candidates_object, get_candidates_by_pk, get_candidates_by_skills

# Файл json
MAIN_FILE = "candidates.json"

# Преобразование json файла в python
data = load_candidates(MAIN_FILE)

# Получение списка экземпляров кандидатов
objects = get_all_candidates_object(data)

# Создание экземпляра Flask
app = Flask(__name__)


# Маршрут на главную страницу с выводом всех кандидатов
@app.route("/")
def page_index():
    cand_str = ''
    for cand in objects:
        cand_str += '<pre>' + str(cand) + '</pre>'
    return cand_str


# Маршрут на страницу "кандидаты"  с выводом  кандидатов по pk
@app.route("/candidates/<int:pk>")
def page_candidates(pk):
    return "<pre>" + get_candidates_by_pk(pk, objects) + "</pre>"


# Маршрут на страницу "навыки"  с выводом  кандидатов по навыкам
@app.route("/skills/<skills>")
def page_skills(skills):
    return "<pre>" + get_candidates_by_skills(skills, objects) + "</pre>"


app.run(port=15700)
