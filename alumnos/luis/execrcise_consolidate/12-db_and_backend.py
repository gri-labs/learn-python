# Siguiendo el ejemplo del script app y el script full_db, crea un script que:
# tenga un endpoint que muestre todos los registros de la tabla estudiantes
# tenga un endpoint que muestre un registro de la tabla estudiantes
# tenga un endpoint que inserte un registro en la tabla estudiantes
# tenga un endpoint que elimine un registro de la tabla estudiantes
from flask import Flask
import mysql.connector
import logging

# Se crea una instancia de la clase flask llamada app
# app es una instancia de la clase Flask y un objeto de la clase Flask
app = Flask(__name__)


def connection_database(host, user, password, database, port):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(port),
    )
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    data = cursor.fetchall()
    return data


def show_data(data):
    for row in data:
        print(row)


# Se define una ruta para la aplicación
# La ruta es la raíz de la aplicación
@app.route('/', methods=['GET'], endpoint='get_estudiantes')
# Define una función llamada hell_world
# Nos ayuda a encapsular el código, mantener funcionalidades...
def get_estudiantes():
    connection = connection_database()
    query = "SELECT * FROM estudiantes;"
    result = execute_query(connection, query)
    return str(result)


@app.route('/', methods=['GET'], endpoint='get_estudiantes_byid')
def get_estudiantes_byid(connection):
    query = "SELECT id FROM estudiantes WHERE nombre ='luis';"
    execute_query(connection, query)
    return execute_query(connection, query)


def insert_estudiantes(connection):
    query = "INSERT INTO `estudiantes`.`estudiantes` (id, nombre) VALUES (1, 'luis');"
    execute_query(connection, query)


def delete_estudiantes(connection):
    query = "DELETE FROM `estudiantes`.`estudiantes` WHERE nombre = 'luis';"
    execute_query(connection, query)


def close_connect(connection):
    connection.close()


def run(connection):
    get_estudiantes(connection)
    get_estudiantes_byid(connection)
    insert_estudiantes(connection)
    show_data(data)
    data = get_estudiantes(connection)
    delete_estudiantes(connection)
    close_connect(connection)


if __name__ == '__main__':
    # Se configura el log
    logging.basicConfig(filename='request.log', level=logging.DEBUG)
    # Se ejecuta el servidor
    app.run(host='0.0.0.0', port=6000, debug=True)
