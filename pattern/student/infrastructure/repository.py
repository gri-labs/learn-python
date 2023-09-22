from pattern.student.infrastructure.storage import StudentDTORepositoryService
from pattern.student.domain.model import StudentEntityRepositoryService


class Repository:
    def __init__(self, connector_database):
        self.connector = connector_database

    def get_student_by_filter(self, filter_by):
        # Hemos creado una instancia del modelo StudentDTO para la persistencia
        new_student = StudentDTORepositoryService()

        # Hemos asignado el id que nos llega por parámetro

        result = self.connector.get_by_filter(new_student, filter_by=filter_by)

        # Create new employ entity
        student_entity = StudentEntityRepositoryService()

        # Hemos asignado los valores del resultado a la entidad
        student_entity.id = result.id
        student_entity.name = result.name
        student_entity.last_name = result.last_name
        student_entity.age = result.age
        student_entity.password = result.password

        # Hemos devuelto la entidad
        return student_entity

    def get_student_by_id(self, id):
        # Hemos creado una instancia del modelo StudentDTO para la persistencia
        new_student = StudentDTORepositoryService()

        # Hemos asignado el id que nos llega por parámetro

        result = self.connector.get_by_filter(new_student, id=id)

        student_entity = StudentEntityRepositoryService()

        # Hemos asignado los valores del resultado a la entidad
        student_entity.id = result.id
        student_entity.name = result.name
        student_entity.last_name = result.last_name
        student_entity.age = result.age
        student_entity.password = result.password

        # Hemos devuelto la entidad
        return student_entity

    def add_student(self, student_entity):
        new_student = StudentDTORepositoryService()
        new_student.id = student_entity.id
        new_student.name = student_entity.name
        new_student.last_name = student_entity.last_name
        new_student.age = student_entity.age
        new_student.password = student_entity.password

        self.connector.add(new_student)

    def update_student(self, student_entity):
        new_student = StudentDTORepositoryService()
        new_student.id = student_entity.id
        new_student.name = student_entity.name
        new_student.last_name = student_entity.last_name
        new_student.age = student_entity.age
        new_student.password = student_entity.password

        self.connector.update(new_student)

    def delete_student_by_id(self, id):
        new_student = StudentDTORepositoryService()
        new_student.id = id

        return self.connector.delete(new_student)
