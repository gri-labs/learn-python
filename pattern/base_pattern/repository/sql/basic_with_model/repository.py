from student import StudentDTOBasicModel
from student import StudentEntityBasicModel


class RepositoryBasicModel:
    def __init__(self, connector_database):
        self.connector = connector_database

    def get_student_by_id(self, id):
        # Hemos creado una instancia del modelo StudentDTO para la persistencia
        new_student = StudentDTOBasicModel()

        # Hemos asignado el id que nos llega por parámetro

        result = self.connector.execute_and_filter(new_student, filter_by={'id': id})

        # Create new student entity
        student_entity = StudentDTOBasicModel()

        # Hemos asignado los valores del resultado a la entidad
        student_entity.id = result.id
        student_entity.nombre = result.name

        # Hemos devuelto la entidad
        return student_entity

    def add_student(self, student_entity):
        new_student = StudentDTOBasicModel()
        new_student.id = student_entity.id
        new_student.nombre = student_entity.name

        self.connector.add(new_student)

    def delete_student_by_id(self, id):
        new_student = StudentDTOBasicModel()
        new_student.id = id

        self.connector.delete_and_commit(new_student)

    def update_student(self, student_entity):
        new_student = StudentDTOBasicModel()
        new_student.id = student_entity.id
        new_student.nombre = student_entity.name

        self.connector.add(new_student)
