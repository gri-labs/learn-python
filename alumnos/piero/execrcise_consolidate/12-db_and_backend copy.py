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


def connection_database(host, user, password, database):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        port=int(3307),
        database='students'
)
    return connection

def execute_query(query, connection):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows



# Se define una ruta para la aplicación
# La ruta es la raíz de la aplicación
@app.route('/', methods=['GET'])
# Define una función llamada hell_world
# Nos ayuda a encapsular el código, mantener funcionalidades...
def get_estudiantes(query, connection):
    return execute_query(query, connection)


if __name__ == '__main__':
    # Se configura el log
    logging.basicConfig(filename='request.log', level=logging.DEBUG)
    app.run(host='0.0.0.0', port=6000)
    conn = connection_database("localhost", "root", "root", "gri")
    query = "SELECT * FROM users"
    results = get_estudiantes(query, conn)
    print(results)