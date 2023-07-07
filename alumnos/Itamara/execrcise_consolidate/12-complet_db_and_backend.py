# Siguiendo el ejemplo del script app y el script full_db, crea un script que:
# tenga un endpoint que muestre todos los registros de la tabla estudiantes
# tenga un endpoint que muestre un registro de la tabla estudiantes
# tenga un endpoint que inserte un registro en la tabla estudiantes
# tenga un endpoint que elimine un registro de la tabla estudiantes
import Flask from flask, request, jasonfy
import mysql.connector



app = Flask(__name__)


def connection_database():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='gri',
        port=int(3307),
    )

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


# curl http://localhost:6000/students
# Metodo GET
# Es útil para obtener información
@app.route('/students', methods=['GET'], endpoint='get_all_students')
def get_all_students():
    query = "SELECT * FROM estudiantes;"
    connection = connection_database()
    result = execute_query(connection, query)
    connection.close()

    if len(result) == 0:
        # devolver un 404
        return jsonify('No se ha encontrado el estudiante'), 404

    return jsonfy(result)


# curl http://localhost:6000/student/1
# Metodo GET con parametros en la URL
# Es útil para obtener información de un registro en concreto
@app.route('/student/<int:student_id>', methods=['GET'], endpoint='get_student')
def get_student(student_id):
    query = "SELECT * FROM estudiantes WHERE id = %s;" % student_id
    connection = connection_database()
    result = execute_query(connection, query)
    if len(result) == 0:
        # devolver un 404
        return jsonify('No se ha encontrado el estudiante'), 404
    connection.close()

    return str(result)


# curl -X POST http://localhost:6000/student/1/Ricardo
# Metodo POST con parametros en la URL
@app.route('/student/<int:student_id>/<string:student_name>', methods=['POST'], endpoint='insert_student')
def insert_student(student_id, student_name):
    query = "INSERT INTO estudiantes (id, nombre) VALUES (%s, '%s');" % (student_id, student_name)
    connection = connection_database()
    result = execute_query(connection, query)
    connection.close()
    return str(result)


# curl -X POST http://localhost:6000/student/headers -H 'student_id: 1' -H 'student_name: Ricardo'
# Metodo POST con headers
# Que son los headers?
# Es información que se envía en la cabecera de la petición
# forma parte del protocolo HTTP
# Se envían en el formato clave: valor
# Es útil para enviar información que no se quiere que se vea en la URL
# Es útil para enviar mucha información
@app.route('/student/headers', methods=['POST'], endpoint='insert_student_headers')
def insert_student_headers():
    student_id = request.headers.get('student_id')
    student_name = request.headers.get('student_name')
    query = "INSERT INTO estudiantes (id, nombre) VALUES (%s, '%s');" % (student_id, student_name)
    connection = connection_database()
    result = execute_query(connection, query)
    connection.close()
    return str(result)

# curl -X DELETE http://localhost:6000/student/1
# Metodo DELETE
# Es útil para eliminar información
@app.route('/student/<int:student_id>', methods=['DELETE'], endpoint='delete_student')
def delete_student(student_id):
    query = "DELETE FROM estudiantes WHERE id %s;" % student_id
    connection = connection_database()
    result = execute_query(connection, query)
    connection.close()
    return str(result)

# curl -X PUT http://localhost:6000/student/1/Ricardo
# Metodo PUT
# Es útil para actualizar información
@app.route('/student/<int:student_id>/<string:student_name>', methods=['PUT'], endpoint='update_student')
def update_student(student_id, student_name):
    query = "UPDATE estudiantes SET nombre = '%s' WHERE id = %s;" % (student_name, student_id)
    connection = connection_database()
    result = execute_query(connection, query)
    connection.close()
    return str(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
