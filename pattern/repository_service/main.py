from pattern.repository_service.infrastructure.connector import ConnectorDatabase
from pattern.repository_service.infrastructure.repository import Repository
from pattern.repository_service.application.service import Service
from pattern.repository_service.domain.model import StudentEntityRepositoryService
from pattern.repository_service.domain.model import get_count_adults
from pattern.repository_service.domain.model import get_count_minors

if __name__ == '__main__':
    repository = Repository(ConnectorDatabase(
        host='localhost',
        password='root',
        user='root',
        database='school',
        port=int(3308)
    ))

    service = Service(repository)

    service.add_student(StudentEntityRepositoryService(
        name='PepeLast',
        last_name='Perez',
        age=18,
        password='12345678',
    ))

    pepe_last = service.get_student_by_name('PepeLast')

    new_password = pepe_last.generate_random_password('abcede123456789', 10)
    pepe_last.password = new_password

    service.update_student(pepe_last)

    print("Full name: ", pepe_last.get_full_name())

    print("Is adult: ", pepe_last.is_adult())

    print("Is minor: ", pepe_last.is_minor())

    students = service.get_all_students()

    print("Count adults: ", get_count_adults(students))
    print("Count minors: ", get_count_minors(students))

    print("Delete student: ", service.delete_student_by_id(pepe_last.id))

    print("Exist student: ", service.get_student_by_id(pepe_last.id))




