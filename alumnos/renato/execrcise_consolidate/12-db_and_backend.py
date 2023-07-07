# Siguiendo el ejemplo del script app y el script full_db, crea un script que:
# tenga un endpoint que muestre todos los registros de la tabla estudiantes
# tenga un endpoint que muestre un registro de la tabla estudiantes
# tenga un endpoint que inserte un registro en la tabla estudiantes
# tenga un endpoint que elimine un registro de la tabla estudiantes
from flask import Flask, request
import mysql.connector

app = Flask(__name__)


def connection_database(database_name):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        port=int(3307),
        database=database_name,
    )
    return connection


@app.route('/students', methods=['GET'])
def get_data():
    get_all_sql = f"""
    SELECT * FROM NewEstudiantes
    """
    rows = execute_query_select(get_all_sql)
    return rows


@app.route('/student/<int:row_id>', methods=['GET'])
def get_data_by_id(row_id):
    sql_code = f"""
    SELECT * FROM myNewDb.NewEstudiantes WHERE id = {row_id}
    """
    results = execute_query_select(sql_code)
    return results


@app.route('/student/headers', methods=['POST'])
def insert_data():
    row_id = request.json.get('id')
    name = request.json.get('nombre')
    career = request.json.get('carrera')
    sql_code = f"""
    INSERT INTO myNewDb.NewEstudiantes (id, nombre, carrera)
    VALUES ('{row_id}', '{name}', '{career}')
    """
    results = execute_query_select(sql_code)
    return results


@app.route('/student/<int:student_id>/<string:student_name>/<string:student_carrera>', methods=['POST'])
def insert_student(student_id,student_name,student_carrera):
    sql_code = f"""
    INSERT INTO myNewDb.NewEstudiantes (id, nombre, carrera)
    VALUES ('{student_id}', '{student_name}', '{student_carrera}')
    """
    results = execute_query_select(sql_code)
    return results


@app.route('/delete', methods=['DELETE'])
def remove_data():
    name = request.json.get('nombre')
    sql_code = f"""
    DELETE FROM myNewDb.NewEstudiantes WHERE nombre='{name}';
    """
    results = execute_query_select(sql_code)
    return results


def exec_and_commit(cursor, connection, query):
    cursor.execute(query)
    connection.commit()


def execute_query_select(query):
    cursor = connection_db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


if __name__ == '__main__':
    connection_db = connection_database('myNewDb')
    cursor_db = connection_db.cursor()
    app.run(host='0.0.0.0', port=8080)
