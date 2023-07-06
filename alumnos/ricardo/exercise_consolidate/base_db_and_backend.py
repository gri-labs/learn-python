# Siguiendo el ejemplo del script app y el script full_db, crea un script que:
# tenga un endpoint que muestre todos los registros de la tabla estudiantes
# tenga un endpoint que muestre un registro de la tabla estudiantes
# tenga un endpoint que inserte un registro en la tabla estudiantes
# tenga un endpoint que elimine un registro de la tabla estudiantes
from flask import Flask, request, jsonify
import mysql.connector
import logging

app = Flask(__name__)


def connection_database():
    return jsonify('TODO implementar')


def execute_query(connection, query):
    return jsonify('TODO implementar')


def execute_query_with_commit(connection, query):
    return jsonify('TODO implementar')


def connection_close(connection):
    connection.close()


# curl http://localhost:6000/students
# Usar el --head para ver la respuesta del servidor
# Metodo GET
# Es útil para obtener información
@app.route('/students', methods=['GET'], endpoint='get_all_students')
def get_all_students():
    return jsonify('TODO implementar')


# curl http://localhost:6000/student/1
# Usar el --head para ver la respuesta del servidor
# Método GET con parámetros en la URL
# Es útil para obtener información de un registro en concreto
@app.route('/student/<int:student_id>', methods=['GET'], endpoint='get_student')
def get_student(student_id):
    query = "SELECT * FROM estudiantes WHERE id=%s;" % student_id
    return jsonify('TODO implementar')


# curl -X POST http://localhost:6000/student/1/Ricardo
# En este método POST se envía la información en la URL con dos parametros /1/Ricardo
# Es útil para insertar poca información
@app.route('/student/<int:student_id>/<string:student_name>', methods=['POST'], endpoint='insert_student')
def insert_student(student_id, student_name):
    return jsonify('TODO implementar')


# curl -X POST "http://localhost:6000/student/headers?student_id=1&student_name=ricardo"
# Método POST con parámetros en la URL
# Es útil para insertar información
@app.route('/student/headers', methods=['POST'], endpoint='insert_student_headers')
def insert_student_headers():
    student_id = request.args.get('student_id')
    student_name = request.args.get('student_name')
    return jsonify('TODO implementar')


# curl -X DELETE http://localhost:6000/student/1
# Metodo DELETE
# Es útil para eliminar información
@app.route('/student/<int:student_id>', methods=['DELETE'], endpoint='delete_student')
def delete_student(student_id):
    return jsonify('TODO implementar')


# curl -X PUT http://localhost:6000/student/1/pepe
# Metodo PUT
# Es útil para actualizar información
@app.route('/student/<int:student_id>/<string:student_name>', methods=['PUT'], endpoint='update_student')
def update_student(student_id, student_name):
    query = "UPDATE estudiantes SET nombre = '%s' WHERE id=%s;" % (student_name, student_id)


if __name__ == '__main__':
    # Se configura el log
    logging.basicConfig(filename='request.log', level=logging.DEBUG)
    app.run(host='0.0.0.0', port=6000)