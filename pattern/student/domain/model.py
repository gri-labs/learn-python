import random


class StudentEntityRepositoryService():
    def __init__(self, id=0, name="", last_name="", age=0, password=""):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.age = age
        self.password = password

    # TODO: Implementar un cambio de password
    def generate_random_password(self, base_password, length=8):
        new_password = ""

        for i in range(length):
            new_password += random.choice(base_password)

        return new_password

    # TODO: Implementa el nombre completo de los usuarios
    def get_full_name(self):
        return self.name + " " + self.last_name

    # TODO es mayor de edad?

    def is_adult(self):
        return self.age >= 18

    # TODO es menor de edad?

    def is_minor(self):
        return self.age < 18


def get_count_adults(students):
    count = 0

    for student in students:
        if student.is_adult():
            count += 1

    return count


def get_count_minors(students):
    count = 0

    for student in students:
        if student.is_minor():
            count += 1

    return count
