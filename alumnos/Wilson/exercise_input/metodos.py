import mysql.connector
import random

diccionario_nombres = (
'Ricardo', 'Antonio', 'Alex', 'Piero', 'Renato', 'Itamara', 'Ariadna', 'Jesus', 'Luis', 'Wilson', 'Alhida', 'Adrian')
diccionario_emails = (
'ricky', 'toni', 'ale', 'pizza', 'reno', 'brasil', 'pp', 'gemela', 'lucho', 'chucho', 'colombo', 'fit')
diccionario_apellidos = (
'Forero', 'Giorgio', 'Acciardi', 'Cebrian', 'Olivera', 'Baquero', 'Diaz', 'Grande', 'Labrador', 'Montaner')


def connection_database(host, user, password, database, port):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(port),
    )
    return connection


def create_database(connection):
    query = "CREATE DATABASE IF NOT EXISTS gri;"
    execute_query_with_commit(connection, query)


def create_table(connection):
    query = "CREATE TABLE `edades_tabla` (id INT PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(50), apellido VARCHAR(50), edad INT, email VARCHAR(50));"
    execute_query_with_commit(connection, query)


def execute_query_with_commit(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    if query == "SELECT COUNT(*) FROM edades_tabla;":
        num = cursor.fetchall()
        return num[0][0]
    if query == "SELECT * FROM edades_tabla;":
        rows = cursor.fetchall()
        return rows
    if query == "SELECT id FROM edades_tabla;":
        rows = cursor.fetchall()
        return rows
    connection.commit()
    cursor.close()
    return "La query se ejecuto con exito"


def generate_information_table(connection, cardinality_table):
    for i in range(cardinality_table):
        query = f"INSERT INTO edades_tabla (id, nombre, apellido, edad, email) VALUES ('{i + 1}', '{random.choice(diccionario_nombres)}', '{random.choice(diccionario_apellidos)}', '{random.randint(18, 55)}', '{random.choice(diccionario_emails)}{random.randint(1, 99)}@gmail.com');"
        try:
            execute_query_with_commit(connection, query)
        except Exception as e:
            print("Error: %s" % e)
            print("Se inserto el registro %s" % i)

    return f"Se añadieron {cardinality_table} nombres aleatorios a la tabla"


def delete_information_table(connection, cardinality_delete):
    cardinality_table = execute_query_with_commit(connection, "SELECT COUNT(*) FROM edades_tabla;")
    for i in range(cardinality_delete):
        diccionario_id_to_delete = execute_query_with_commit(connexion, "SELECT id FROM edades_tabla;")
        if cardinality_table - i > 0:
            print(random.choice(diccionario_id_to_delete)[0])
            query = f"DELETE FROM `edades_tabla` WHERE `edades_tabla`.`id` = {random.choice(diccionario_id_to_delete)[0]};"
            try:
                execute_query_with_commit(connection, query)
            except Exception as e: \
                    print("Error: %s" % e)
        else:
            print("Ya se eliminaron todos los registros de la tabla")
            break


if __name__ == '__main__':
    connexion = connection_database('localhost', 'root', 'root', 'gri', 3308)
    # create_database(connexion)
    # create_table(connexion)
    print("Por favor indique si desea INSERTAR, ELIMINAR, SELECCIONAR, valores aleatorios en la tabla edades_tabla:")
    encendido = "off"
    while encendido == "off":
        decision = input("Que desea hacer:")
        match decision:
            case "INSERTAR":
                num_añadir = int(input("Cuantos datos aleatorios desea añadir:"))
                print(generate_information_table(connexion, num_añadir))
                encendido = "on"
            case "ELIMINAR":
                num_eliminar = int(input("Cuantos datos aleatorios desea eliminar:"))
                print(delete_information_table(connexion, num_eliminar))
                encendido = "on"
            case "SELECCIONAR":
                decision_select = input("Desea seleccionar todos los datos de la tabla? (SI o NO)")
                encendido = "on"
                if decision_select == "SI":
                    execute_query_with_commit(connexion, "SELECT * FROM edades_tabla;")
                else:
                    input("Cuantos datos aleatorios desea ver?")
                    rows = execute_query_with_commit(connexion, "SELECT id FROM edades_tabla;")
            case _:
                print("El comando no se reconoce, solo puede escribir INSERTAR, ELIMINAR, SELECCIONAR:")
