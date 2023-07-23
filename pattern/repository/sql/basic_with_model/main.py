from connector import ConnectorDatabase
from repository import Repository
from student import Student

if __name__ == '__main__':
    model_student = Student()

    repository = Repository(ConnectorDatabase(
        host='localhost',
        password='root',
        user='root',
        database='gri',
        port=int(3308)
    ))

    print(repository.add_user(Student(nombre='Paquito')))
    result = repository.get_student_by_id(Student(id=1))

    print(result.id, result.nombre)

