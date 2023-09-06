from faker import Faker
from  import

fake = Faker
class Student:
    def __init__(self, name, age, last_name, dni):


    def __str__(self):
        return f'{self.name} {self.last_name} {self.age} {self.dni}'


class Generator:
    def __init__(self, quantity, student):
        self.quantity = quantity
        self.student = student

    def generate(self):
        for _ in range(self.quantity):
            yield self.student(

            )

    def generate_name(self):
        return fake.

    def generate_last_name(self):
        return fake.

    def generate_age(self):
        return fake.

    def generate_dni(self):
        return fake.


if __name__ == '__main__':
    generate =
    connect = (

    )

    for student in generate():
        connect.(
            f"INSERT INTO students (name, age, last_name, dni) VALUES ('{student.name}', {student.age}, '{student.last_name}', {student.dni})"
        )
