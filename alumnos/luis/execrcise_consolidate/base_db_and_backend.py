# Siguiendo el ejemplo del script app y el script full_db, crea un script que:
# tenga un endpoint que muestre todos los registros de la tabla estudiantes
# tenga un endpoint que muestre un registro de la tabla estudiantes
# tenga un endpoint que inserte un registro en la tabla estudiantes
# tenga un endpoint que elimine un registro de la tabla estudiantes
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


def connection_database(host, user, password, database, port):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(port),
    )

    return jsonify(connection)


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)


def execute_query_with_commit(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def connection_close(connection):
    connection.close()


# curl http://localhost:6000/students
# Usar el --head para ver la respuesta del servidor
# Metodo GET
# Es útil para obtener información
@app.route('/students', methods=['GET'], endpoint='get_all_students')
def get_all_students():
    connection = connection_database()
    query = "SELECT * FROM estudiantes;"
    result = execute_query(connection, query)

    if len(result) == 0:
        return jsonify('No se ha encontrado al estudiante'), 404
    else:
        return jsonify('Todo ha ido ok'), 200


# curl http://localhost:6000/student/1
# Usar el --head para ver la respuesta del servidor
# Método GET con parámetros en la URL
# Es útil para obtener información de un registro en concreto
# Que significa el <int:student_id>?
# Es un parámetro que se pasa en la URL y que se puede usar en el método
# En este caso se llama student_id y es un entero
@app.route('/student/<int:student_id>', methods=['GET'], endpoint='get_student')
def get_student(student_id):
    connection = connection_database()
    query = "SELECT * FROM estudiantes WHERE id = 1;"
    result = execute_query(connection, query)

    if len(result) == 0:
        return jsonify('No se ha encontrado al estudiante'), 404
    else:
        return jsonify('Todo ha ido ok'), 202


# curl -X POST http://localhost:6000/student/1/Ricardo
# En este método POST se envía la información en la URL con dos parametros /1/Ricardo
# Es útil para insertar poca información
@app.route('/student/<int:student_id>/<string:student_name>', methods=['POST'], endpoint='insert_student')
def insert_student(student_id, student_name):
    connection = connection_database()
    query = "INSERT INTO estudiantes (id, nombre) VALUES (%s, '%s');" % (student_id, student_name)
    execute_query_with_commit(connection, query)
    connection.close()
    try:
        execute_query_with_commit(connection, query)
        return jsonify('OK'), 200
    except Exception as e:
        return jsonify('ERROR'), 500


# curl -X POST "http://localhost:6000/student/headers?student_id=1&student_name=ricardo"
# Método POST con parámetros en la URL
# Es útil para insertar información
@app.route('/student/headers', methods=['POST'], endpoint='insert_student_headers')
def insert_student_headers(student_id, student_name):
    student_id = request.args.get('student_id')
    student_name = request.args.get('student_name')
    connection = connection_database()
    query = "INSERT INTO estudiantes (id, nombre) VALUES (%s, '%s');" % (student_id, student_name)
    connection.close()
    try:
        execute_query_with_commit(connection, query)
        return jsonify('OK'), 200
    except Exception as e:
        return jsonify('ERROR'), 500


# curl -X DELETE http://localhost:6000/student/1
# Metodo DELETE
# Es útil para eliminar información
@app.route('/student/<int:student_id>', methods=['DELETE'], endpoint='delete_student')
def delete_student(student_id):
    connection = connection_database()
    query = "DELETE * FROM `estudiantes` WHERE id = 1;"
    student_id = request.args.get('student_id')
    execute_query_with_commit(connection, query)
    try:
        execute_query_with_commit(connection, query)
        return jsonify('OK'), 200
    except Exception as e:
        return jsonify('ERROR'), 500


# curl -X PUT http://localhost:6000/student/1/pepe
# Metodo PUT
# Es útil para actualizar información
@app.route('/student/<int:student_id>/<string:student_name>', methods=['PUT'], endpoint='update_student')
def update_student(student_id, student_name):
    connection = connection_database()
    query = "UPDATE estudiantes SET nombre = '%s' WHERE id=%s;" % (student_name, student_id)
    execute_query_with_commit(connection, query)
    try:
        execute_query_with_commit(connection, query)
        return jsonify('OK'), 200
    except Exception as e:
        return jsonify('ERROR'), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)