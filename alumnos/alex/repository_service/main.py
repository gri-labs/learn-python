from alumnos.alex.repository_service.infrastructure.connector import ConnectorDatabase
from alumnos.alex.repository_service.infrastructure.repository import Repository
from alumnos.alex.repository_service.application.service import Service
from alumnos.alex.repository_service.domain.model import StudentEntity

if __name__ == '__main__':
    repository = Repository(ConnectorDatabase(
        host='localhost',
        password='root',
        user='root',
        database='gri',
        port=int(3307)
    ))

    service = Service(repository)

    """52student_entity = StudentEntity(nombre='PepeLast')

    service.add_student(student_entity)

    print("Student add with name: ")
    print(service.get_student_by_name('PepeLast').nombre)
    print("Student add with id: ")
    print(service.get_student_by_name('PepeLast').id)"""

    Alex = StudentEntity(0, 'Alex', 'Larrinaga', 33, '1234')
    service.add_student(Alex)
    print(service.get_student_by_id(52).apellido)
    print(service.get_student_by_id(52).edad)
    print(service.get_student_by_id(52).password)
    Alex.change_password('1111')
    Alex.change_edad(34)
    service.update_student_by_id(Alex, 33)
    print(service.get_student_by_id(52).edad)
    print(service.get_student_by_id(52).password)

