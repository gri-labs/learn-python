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

    student_entity = StudentEntity(nombre='PepeLast')

    service.add_student(student_entity)

    print("Student add with name: ")
    print(service.get_student_by_name('PepeLast').nombre)
    print("Student add with id: ")
    print(service.get_student_by_name('PepeLast').id)

