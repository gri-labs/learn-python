from connector import ConnectorDatabase
from repository import Repository
from service import Service
from student import StudentEntity

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
