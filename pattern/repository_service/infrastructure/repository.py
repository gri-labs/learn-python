from pattern.repository_service.infrastructure.storage import StudentDTO
from pattern.repository_service.domain.model import StudentEntity


class Repository:
    def __init__(self, connector_database):
        self.connector = connector_database

    def get_student_by_filter(self, filter_by):
        # Hemos creado una instancia del modelo StudentDTO para la persistencia
        new_student = StudentDTO()

        # Hemos asignado el id que nos llega por parámetro

        result = self.connector.execute_and_filter(new_student, filter_by=filter_by)

        # Create new student entity
        student_entity = StudentEntity()

        # Hemos asignado los valores del resultado a la entidad
        student_entity.id = result.id
        student_entity.nombre = result.nombre

        # Hemos devuelto la entidad
        return student_entity

    def get_student_by_id(self, id):
        # Hemos creado una instancia del modelo StudentDTO para la persistencia
        new_student = StudentDTO()

        # Hemos asignado el id que nos llega por parámetro

        result = self.connector.execute_and_filter(new_student, filter_by={'id': id})

        # Create new student entity
        student_entity = StudentEntity()

        # Hemos asignado los valores del resultado a la entidad
        student_entity.id = result.id
        student_entity.nombre = result.nombre

        # Hemos devuelto la entidad
        return student_entity

    def add_student(self, student_entity):
        new_student = StudentDTO()
        new_student.nombre = student_entity.nombre

        self.connector.add(new_student)

    def delete_student_by_id(self, id):
        new_student = StudentDTO()
        new_student.id = id

        self.connector.delete_by_id(new_student)

    def update_student(self, student_entity):
        new_student = StudentDTO()
        new_student.id = student_entity.id
        new_student.nombre = student_entity.nombre

        self.connector.update(new_student)
