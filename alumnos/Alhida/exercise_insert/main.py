import mysql.connector
import random
def connection_database(host, user, password, database, port):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(port),
    )
    return connection
def commit_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
def execute_query_select(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    rows_result = cursor.fetchall()
    cursor.close()
    return rows_result
def insertar_datos(connection):
    cursor = connection.cursor()
    for i in range(100000):
        nombre = "maria" + str(i)
        apellido = "gonzales" + str(i)
        edad = random.randint(18, 99)
        email = "maria" + str(i) + "@email.com"
        query = f"INSERT INTO alumnos (nombre, apellido, edad, email) VALUES ('{nombre}', '{apellido}', {edad}, '{email}')"
        cursor.execute(query)
        if i % 1000 == 0:
            print(f"Insertados {i+1} datos")
    connection.commit()
    cursor.close()
def eliminarDatos(connection):
    query = "DELETE FROM alumnos"
    commit_query(connection, query)
    print("Datos eliminados")
def datos_id(connection, num_id):
    query = "SELECT * FROM estudiantes WHERE id = %s;" % num_id
    result = execute_query_select(connection, query)
    return result
def datos_edad(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM alumnos WHERE edad = %s"
    cursor.execute(query, (18,))
    rows_result = cursor.fetchall()
    if len(rows_result) > 0:
        print(rows_result)
    cursor.close()


if __name__ == '__main__':
    connection = connection_database("localhost", "root", "root", "estudiantes", "3307")

    while True:
        respuesta = input("¿Qué quieres hacer? (insertar, eliminar, datos_id, datos_edad, salir): ")

        if respuesta == "insertar":
            insertar_datos(connection)
        elif respuesta == "eliminar":
            eliminarDatos(connection)
        elif respuesta == "datos_id":
            num_id = input("numero de id: ")
            print(datos_id(connection, num_id))
        elif respuesta == "datos_edad":
            datos_edad(connection)
        elif respuesta == "salir":
            break
        else:
            print("respuesta equivocada")

    connection.close()
