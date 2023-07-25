from connector import ConnectorDatabase
from repository import Repository
from student import StudentEntity

if __name__ == '__main__':
    repository = Repository(ConnectorDatabase(
        host='localhost',
        password='root',
        user='root',
        database='gri',
        port=int(3308)
    ))

    # Add student
    repository.add_student(
        StudentEntity(
            nombre='Juan',
        ))

    # Get student by id
    student = repository.get_student_by_id(500)
    print(student.nombre)

    # TODO: Usa los métodos del repositorio para crear, actualizar y borrar un estudiante
