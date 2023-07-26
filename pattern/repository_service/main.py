from pattern.repository_service.infrastructure.connector import ConnectorDatabase
from pattern.repository_service.infrastructure.repository import Repository
from pattern.repository_service.application.service import Service
from pattern.repository_service.domain.model import StudentEntity

if __name__ == '__main__':
    repository = Repository(ConnectorDatabase(
        host='localhost',
        password='root',
        user='root',
        database='gri',
        port=int(3308)
    ))

    service = Service(repository)

    service.add_student(StudentEntity(nombre='Pepe'))

    student = service.get_student_by_id(5)

    model_student = StudentEntity(id=student.id, nombre='Juan', apellido='Perez')

    print(model_student.full_name())
