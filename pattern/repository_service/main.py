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

    service.add_student(StudentEntity(nombre='Pepe55555'))

    student_pepe_55555 = service.get_student_by_name('Pepe55555')

    print(student_pepe_55555.nombre)

    print(StudentEntity(nombre=student_pepe_55555.nombre, apellido='Pez').full_name())
