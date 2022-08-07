import json
from candidates_class import Candidates


def load_candidates(filename):
    """ Преобразует json файдл в python файл"""

    with open(filename, "r", encoding="utf-8") as file:
        file = file.read()
        python_file = json.loads(file)
    return python_file


def get_all_candidates_object(filename):
    """ Возвращает список экземпляров кандидатов"""

    candidates_list = []
    for item in filename:
        candidate = Candidates(
                item['pk'], item['name'], item['picture'],
                item['position'], item['gender'], item['age'], item['skills'])
        candidates_list.append(candidate)
    return candidates_list


def get_candidates_by_pk(pk, filename):
    """Возращает экземляр кандидата по пк и его ссылку на фото"""

    for candidate in filename:
        if pk == candidate.pk:
            return f"<img src='({candidate.picture})'>\n\n" + str(candidate)
    else:
        return "Not found"


def get_candidates_by_skills(skill_name, filename):
    """ Возвращает экземпляры кандидатов по их навыкам"""

    flag = False
    skill_name_list = ''
    for candidate in filename:
        if skill_name.strip().lower() in candidate.skills.strip().lower():
            skill_name_list += str(candidate) + "\n"
            flag = True
    if flag:
        return skill_name_list
    else:
        return "Not found"
