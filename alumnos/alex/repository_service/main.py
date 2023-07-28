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
        port=int(3307)
    ))

    service = Service(repository)

    student_entity = StudentEntity(nombre='PepeLast')

    service.add_student(student_entity)

    print("Student add with name: ")
    print(service.get_student_by_name('PepeLast').nombre)
    print("Student add with id: ")
    print(service.get_student_by_name('PepeLast').id)

    Alex = StudentEntity(nombre='Alex', apellido='Larrinaga', edad=33, password=1234)
    service.add_student(Alex)
    print(service.get_student_by_name('Alex').password)
    Alex.change_password(1111)
    service.update_student(Alex)

