from repository import Repository
from connector_database import ConnectorDatabase


if __name__ == '__main__':
    # TODO: Arranca el docker-compose para tener tu base de datos
    # TODO: Crea o chequea que exista una base de datos para poder trabajar
    # TODO: Implementa correctamente el repositorio y el conector
    # TODO: Instancia el repositorio con el conector y tu classe para printar datos
    repository = Repository(ConnectorDatabase(
        host='localhost',
        user='root',
        password='root',
        database='gri',
        port=3308
    ))

    # TODO: Adapta el repositorio al nombre de la base de datos
    # TODO: Inserta datos en la base de datos

    repository.insert_student('Pepe')

    # TODO: Obten el registro que has añadido y muestralo

    print(repository.get_students_by_name('Pepe'))
    # TODO: Obten todos los usuarios
    # TODO: Actualiza un usuario y muestra ese usuario
    repository.update_student(6466, 'Pepito')

    # TODO: Muestra un usuario por ID
    print(repository.get_student_by_id(6466))
    # TODO: Borra un usuario

    repository.delete_student(6466)

    # TODO: Muestra el usuario borrado
    print(repository.get_student_by_id(6466))

