from repository import RepositoryBasic
from connector_database import ConnectorDatabaseBasic


if __name__ == '__main__':
    # TODO: Arranca el docker-compose para tener tu base de datos
    # TODO: Crea o chequea que exista una base de datos para poder trabajar
    # TODO: Implementa correctamente el repositorio y el conector
    # TODO: Instancia el repositorio con el conector y tu classe para printar datos
    connector = ConnectorDatabaseBasic(
        host='localhost',
        user='root',
        password='root',
        database='gri',
        port=3308
    )

    repository = RepositoryBasic(connector)

    # TODO: Adapta el repositorio al nombre de la base de datos
    # TODO: Inserta datos en la base de datos

    repository.insert_student('Paquito')

    # TODO: Obten el registro que has añadido y muestralo

    print("Estudiante insertado: ")
    repository.get_students_by_name('Paquito')
    # TODO: Obten todos los usuarios
    # TODO: Actualiza un usuario y muestra ese usuario
    repository.update_student(1038575, 'Paquito2')

    # TODO: Muestra un usuario por ID
    print("Estudiante actualizado: ")
    print(repository.get_student_by_id(1038575))
    # TODO: Borra un usuario

    repository.delete_student(6466)

    # TODO: Muestra el usuario borrado
    print("Estudiante borrado: ")
    print(repository.get_student_by_id(6466))

