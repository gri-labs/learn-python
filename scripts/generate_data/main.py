from faker import Faker
from connector_database import ConnectorDatabase

fake = Faker()


class Student:
    def __init__(self, name, age, last_name, dni):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.dni = dni


#  Esta función genera estudiantes ficticios utilizando la biblioteca Faker
#  y que utiliza la palabra clave yield para producir un estudiante en cada iteración.
def generate_students(quantity, student_class):
    for _ in range(quantity):
        yield student_class(
            name=fake.first_name(),
            last_name=fake.last_name(),
            age=fake.random_int(min=18, max=99),
            dni=fake.random_int(min=10000000, max=99999999)
        )


if __name__ == '__main__':
    # Instancio el conector a la base de datos
    connect = ConnectorDatabase(
        host='localhost',
        user='root',
        password='root',
        database='school',
        port=3308
    )

    # Se llama a la función generate_students para obtener un generador
    # El generador se asigna a la variable students_generator
    students_generator = generate_students(100, Student)

    # Se utiliza el bucle for para iterar sobre el generador
    # En cada iteración se obtiene un objeto de tipo Student
    # Dentro del bucle for, se crea la query y se ejecuta
    # no es necesario el next() porque el bucle for lo hace por nosotros
    for student in students_generator:
        query = f"""
            INSERT INTO students (name, age, last_name, dni)
            VALUES ('{student.name}', {student.age}, '{student.last_name}', {student.dni})
        """
        connect.execute_and_commit(query)