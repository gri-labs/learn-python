from repository import Repository
from connector_database import ConnectorDatabase


if __name__ == '__main__':
    # TODO: Arranca el docker-compose para tener tu base de datos
    # TODO: Crea o chequea que exista una base de datos para poder trabajar
    # TODO: Implementa correctamente el repositorio y el conector
    # TODO: Instancia el repositorio con el conector y tu classe para printar datos
    connector = ConnectorDatabase(
        host='localhost',
        user='root',
        password='root',
        database='gri',
        port=3307
    )

    repository = Repository(connector)
    # TODO: Adapta el repositorio al nombre de la base de datos
    # TODO: Inserta datos en la base de datos
    repository.insert_student('Paquito')
    # TODO: Obten el registro que has añadido y muestralo
    datos = repository.get_student_by_id(2)
    for i in datos:
        print(i)
    # TODO: Obten todos los usuarios
    datos = repository.get_students()
    for i in datos:
        for j in i:
            print(j)
    # TODO: Actualiza un usuario y muestra ese usuario
    repository.update_student(1,'Alex')
    datos = repository.get_student_by_id(3)
    for i in datos:
        print(i)
    # TODO: Borra un usuario
    repository.delete_student(1)
    # TODO: Muestra un usuario por ID


