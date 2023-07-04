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


# def connection_database():


# def execute_query():


# Se define una ruta para la aplicación
# La ruta es la raíz de la aplicación

def connection_database(database_name):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        port=int(3307),
        database=database_name,
    )
    connection.connect()
    return connection


@app.route('/', methods=['GET'])
def get_data():
    connection_db = connection_database('MyNewDb')
    cursor_db = connection_db.cursor()
    get_all_sql = f"""
    SELECT * FROM NewEstudiantes
    """
    exec(cursor_db, get_all_sql)
    rows = cursor_db.fetchall()
    return rows


def exec_and_commit(cursor, connection, query):
    cursor.execute(query)
    connection.commit()


def exec(cursor, query):
    cursor.execute(query)


if __name__ == '__main__':
    # Se configura el log
    logging.basicConfig(filename='request.log', level=logging.DEBUG)
    app.run(host='0.0.0.0', port=8080)
