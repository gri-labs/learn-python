# Siguiendo el ejemplo del script app y el script full_db, crea un script que:
# tenga un endpoint que muestre todos los registros de la tabla estudiantes
# tenga un endpoint que muestre un registro de la tabla estudiantes
# tenga un endpoint que inserte un registro en la tabla estudiantes
# tenga un endpoint que elimine un registro de la tabla estudiantes
from flask import Flask, request, jsonify
import mysql.connector
# Se crea una instancia de la clase flask llamada app
# app es una instancia de la clase Flask y un objeto de la clase Flask
app = Flask(__name__)


def connection_database():
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
# Define una función llamada hell_world
# Nos ayuda a encapsular el código, mantener funcionalidades...
@app.route('/estudiante', methods=['GET'])
def get_all_estudiantes():
    connection = connection_database()
    query = "SELECT * FROM estudiante"
    result = execute_query(query, connection)
    connection.close()
    return str(result)

# tenga un endpoint que muestre un registro de la tabla estudiantes
@app.route('/estudiante/<int:estudiante_id>', methods=['GET'])
def get_estudiantes(estudiante_id):
    connection = connection_database()
    query = f"SELECT * FROM estudiante WHERE id = {estudiante_id}"
    result = execute_query(query, connection)
    connection.close()
    return str(result)


# tenga un endpoint que inserte un registro en la tabla estudiantes
@app.route('/estudiante/post', methods=['POST'])
def post_estudiantes():
    try:
        connection = connection_database()
        query = "INSERT INTO estudiante (id, nombre, carrera) VALUES (%s, %s, %s)"
        values = (request.json['id'], request.json['nombre'], request.json['carrera'])
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        connection.close()
        return jsonify({'mensaje': 'Estudiante insertado correctamente'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

# tenga un endpoint que elimine un registro de la tabla estudiantes
@app.route('/estudiante/delete/<int:delete_estudiante_id>', methods=['DELETE'])
def delete_estudiantes(delete_estudiante_id):
    try:
        connection = connection_database()
        query = f"DELETE FROM estudiante WHERE id = {delete_estudiante_id}"
        execute_query(query, connection)
        connection.commit()
        connection.close()
        return jsonify({'mensaje': 'Estudiante eliminado correctamente'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error al eliminar estudiante'})

if __name__ == '__main__':
    # Se configura el log
    app.run(host='0.0.0.0', port=8080, debug=True)
