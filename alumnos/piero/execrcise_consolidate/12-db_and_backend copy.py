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
        database='estudiantes'
)
    return connection

def execute_query(query, connection):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

# tenga un endpoint que muestre todos los registros de la tabla estudiantes
# Se define una ruta para la aplicación
# La ruta es la raíz de la aplicación
@app.route('/estudiantes', methods=['GET'])
# Define una función llamada hell_world
# Nos ayuda a encapsular el código, mantener funcionalidades...
def get_all_estudiantes():
    connection = connection_database()
    query = "SELECT * FROM estudiantes"
    result = execute_query(query, connection)
    connection.close()
    return str(result)

# tenga un endpoint que muestre un registro de la tabla estudiantes
@app.route('/estudiantes/<int:estudiante_id>', methods=['GET'])
def get_estudiantes(estudiante_id):
    connection = connection_database()
    query = f"SELECT * FROM estudiantes WHERE id = {estudiante_id}"
    result = execute_query(query, connection)
    connection.close()
    return str(result)

# tenga un endpoint que inserte un registro en la tabla estudiantes
@app.route('/estudiantes/post', methods=['POST'])
def post_estudiantes():
    connection = connection_database
    query = "INSERT INTO estudiantes (id, nombre, carrera) VALUES (2, Ricardo, Master)"
    execute_query(query, connection)
    connection.commit()
    connection.close()
    response = {'message': 'Estudiante insertado correctamente.'} 
    return response

# tenga un endpoint que elimine un registro de la tabla estudiantes
@app.route('/estudiantes/<int:delete_estudiante_id>', methods=['DELETE'])
def delete_estudiantes(delete_estudiante_id):
    connection = connection_database
    query = f"DELETE FROM estudiantes WHERE id = {delete_estudiante_id}"
    execute_query(query, connection)
    connection.commit()
    connection.close()
    response = {'message': 'Estudiante eliminado correctamente.'} 
    return response
   

if __name__ == '__main__':
    # Se configura el log
    logging.basicConfig(filename='request.log', level=logging.DEBUG)
    app.run(host='localhost', port=8080)