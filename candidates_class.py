class Candidates:
    """ Класс для инициализации кандидатов """

    def __init__(self, pk, name, picture, position, gender, age, skills):
        self.pk = pk
        self.name = name
        self. picture = picture
        self. position = position
        self. gender = gender
        self.age = age
        self.skills = skills

    # Возвращает строковое представление экземпляра
    def __str__(self):
        return f'{self.name}\n{self.position}\n{self.skills}\n'