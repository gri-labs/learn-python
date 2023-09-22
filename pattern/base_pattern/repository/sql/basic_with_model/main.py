from connector import ConnectorDatabaseBasicModel
from repository import RepositoryBasicModel
from student import StudentEntityBasicModel

if __name__ == '__main__':
    repository = RepositoryBasicModel(ConnectorDatabaseBasicModel(
        host='localhost',
        password='root',
        user='root',
        database='gri',
        port=int(3308)
    ))

    # Add employ
    repository.add_student(
        StudentEntityBasicModel(
            nombre='Juan',
        ))

    # Get employ by id
    student = repository.get_student_by_id(500)
    print(student.name)

    # TODO: Usa los métodos del repositorio para crear, actualizar y borrar un estudiante
