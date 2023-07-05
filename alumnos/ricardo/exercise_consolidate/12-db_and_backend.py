# Siguiendo el ejemplo del script app y el script full_db, crea un script que:
# tenga un endpoint que muestre todos los registros de la tabla estudiantes
# tenga un endpoint que muestre un registro de la tabla estudiantes
# tenga un endpoint que inserte un registro en la tabla estudiantes
# tenga un endpoint que elimine un registro de la tabla estudiantes
from flask import Flask
import mysql.connector
import logging

app = Flask(__name__)


def connection_database():


def execute_query(connection, query):


@app.route('/', methods=['GET'], endpoint='get_all_students')
def get_all_students():
    query = "SELECT * FROM estudiantes;"
    connection = connection_database()


if __name__ == '__main__':
    # Se configura el log
    logging.basicConfig(filename='request.log', level=logging.DEBUG)
    app.run(host='0.0.0.0', port=6000)
