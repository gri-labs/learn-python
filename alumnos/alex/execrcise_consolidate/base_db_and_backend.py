# Siguiendo el ejemplo del script app y el script full_db, crea un script que:
# tenga un endpoint que muestre todos los registros de la tabla estudiantes
# tenga un endpoint que muestre un registro de la tabla estudiantes
# tenga un endpoint que inserte un registro en la tabla estudiantes
# tenga un endpoint que elimine un registro de la tabla estudiantes
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


def connection_database():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='estudiantes',
        port=int(3307),
    )

    return connection
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result
def execute_query_and_commit(connection, query):
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
    connect = connection_database()
    query = "SELECT * FROM estudiantes;"
    result = execute_query(connect, query)
    connect.close()
    return str(result)


# curl http://localhost:6000/student/1
# Usar el --head para ver la respuesta del servidor
# Método GET con parámetros en la URL
# Es útil para obtener información de un registro en concreto
# Que significa el <int:student_id>?
# Es un parámetro que se pasa en la URL y que se puede usar en el método
# En este caso se llama student_id y es un entero
@app.route('/student/<int:student_id>', methods=['GET'], endpoint='get_student')
def get_student(student_id):
    connect = connection_database()
    query = "SELECT * FROM estudiantes WHERE id = %s;" % student_id
    result = execute_query(connect, query)
    return str(result)


# curl -X POST http://localhost:6000/student/1/Ricardo
# En este método POST se envía la información en la URL con dos parametros /1/Ricardo
# Es útil para insertar poca información
@app.route('/student/<int:student_id>/<string:student_name>', methods=['POST'], endpoint='insert_student')
def insert_student(student_id, student_name):
    connect = connection_database()
    query = "INSERT INTO estudiantes (id, nombre) VALUES (%s, '%s');" % (student_id, student_name)
    try:
        execute_query_and_commit(connect, query)
        return jsonify("OK")
    except Exception as e:
        return jsonify("Error")


# curl -X POST "http://localhost:6000/student/headers?student_id=1&student_name=ricardo"
# Método POST con parámetros en la URL
# Es útil para insertar información
@app.route('/student/headers', methods=['POST'], endpoint='insert_student_headers')
def insert_student_headers():
    connect = connection_database()
    student_id = request.args.get('student_id')
    student_name = request.args.get('student_name')
    query = "INSERT INTO estudiantes (id, nombre) VALUES (%s, '%s');" % (student_id, student_name)
    try:
        execute_query_and_commit(connect, query)
        return jsonify('OK')
    except Exception as e:
        return jsonify("Error")



# curl -X DELETE http://localhost:6000/student/1
# Metodo DELETE
# Es útil para eliminar información
@app.route('/student/<int:student_id>', methods=['DELETE'], endpoint='delete_student')
def delete_student(student_id):
    connect = connection_database()
    query = "DELETE FROM `estudiantes`.`estudiantes` WHERE id=%s;" % (student_id)
    try:
        execute_query_and_commit(connect, query)
        return jsonify('TODO implementar')
    except Exception as e:
        return jsonify("Error")


# curl -X PUT http://localhost:6000/student/1/pepe
# Metodo PUT
# Es útil para actualizar información
@app.route('/student/<int:student_id>/<string:student_name>git pu', methods=['PUT'], endpoint='update_student')
def update_student(student_id, student_name):
    connect = connection_database()
    query = "UPDATE estudiantes SET nombre = '%s' WHERE id=%s;" % (student_name, student_id)
    try:
        execute_query_and_commit(connect, query)
        return jsonify('TODO implementar')
    except Exception as e:
        return jsonify("Error")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)