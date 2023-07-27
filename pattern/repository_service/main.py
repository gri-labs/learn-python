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

    print(service.get_student_by_name('PepeLast').nombre)

    student_entity.nombre = 'PepeLast2'

    service.update_student(student_entity)

    print(service.get_student_by_name('PepeLast2').nombre)

    service.delete_student_by_id(student_entity.id)

    print(service.get_student_by_name('PepeLast2').nombre)