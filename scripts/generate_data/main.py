from faker import Faker
from connector_database import ConnectorDatabase

fake = Faker()


class Student:
    def __init__(self, name, age, last_name, dni):
        self.name = name
        self.age = age
        self.last_name = last_name
        self.dni = dni


class Generator:
    def __init__(self, quantity, student):
        self.quantity = quantity
        self.student = student

    # EL método "generate" devuelve un generador.
    # Un generador es un tipo especial de función que genera valores en lugar de devolverlos.
    # Estos valores se pueden iterar con un bucle "for".
    # El generador se puede utilizar para generar un número determinado de objetos "Student".

    def generate(self):
        # El bucle se ejecuta tantas veces como dicte el atributo "self.quantity".
        # la variable _ se usa como un nombre i, pero el valor no se usa en el bucle.
        for _ in range(self.quantity):
            # Dentro del bucle "for", se utiliza la declaración "yield"
            # para generar un valor y luego pausar la ejecución del método,
            # permitiendo que el valor generado sea utilizado por el código
            # que llama a este método antes de continuar con la siguiente iteración del bucle.
            yield self.student(
                fake.name(),
                fake.last_name(),
                fake.random_int(min=18, max=80),
                fake.random_int(min=10000000, max=99999999)
            )


if __name__ == '__main__':
    # La clase generador genera objetos de tipo "Student"
    # el método "generate" devuelve un generador
    # que se puede iterar para obtener los objetos "Student"
    generate = Generator(5, Student).generate
    connect = ConnectorDatabase(
        host='localhost',
        user='root',
        password='root',
        database='school',
        port=3308
    )

    # Se itera el generador y se insertan los objetos "Student" en la base de datos.
    # generate() es el método de la clase Generator que devuelve un generador.
    for student in generate():
        connect.execute_and_commit(
            # f-strings es una forma de formatear strings
            f"INSERT INTO students (name, age, last_name, dni) VALUES ('{student.name}', {student.age}, '{student.last_name}', {student.dni})"
        )
