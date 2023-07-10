# Siguiendo el ejemplo del script app y el script full_db, crea un script que:
# tenga un endpoint que muestre todos los registros de la tabla estudiantes
# tenga un endpoint que muestre un registro de la tabla estudiantes
# tenga un endpoint que inserte un registro en la tabla estudiantes
# tenga un endpoint que elimine un registro de la tabla estudiantes
from flask import Flask, request, jsonify
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
    return connection


@app.route('/', methods=['GET'])
def get_data():
    get_all_sql = f"""
    SELECT * FROM estudiantes
    """
    rows = execute_query_select(get_all_sql)
    if len(rows) > 0:
        return jsonify(rows), 200
    else:
        return jsonify("NO HAY ESTUDIANTES"), 204


@app.route('/<int:row_id>', methods=['GET'])
def get_data_by_id(row_id=0):
    sql_code = f"""
    SELECT * FROM estudiantes.estudiantes WHERE id = {row_id}
    """
    rows = execute_query_select(sql_code)
    if len(rows) > 0:
        return jsonify(rows), 200
    else:
        return jsonify("NO ENCUENTRO EL ESTUDIANTE"), 404


@app.route('/insert', methods=['POST'])
def insert_data():
    row_id = request.json.get('id')
    name = request.json.get('nombre')
    career = request.json.get('carrera')
    sql_code = f"""
    INSERT INTO estudiantes.estudiantes (id, nombre, carrera)
    VALUES ('{row_id}', '{name}', '{career}')
    """
    exec_and_commit(sql_code)
    return


@app.route('/delete', methods=['DELETE'])
def remove_data():
    name = request.json.get('nombre')
    sql_code = f"""
    DELETE FROM estudiantes.estudiantes WHERE nombre='{name}';
    """
    exec_and_commit(sql_code)


def exec_and_commit(query):
    cursor = connection_db.cursor()
    cursor.execute(query)
    connection_db.commit()
    cursor.close()

def execute_query_select(query):
    cursor = connection_db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


if __name__ == '__main__':
    # Se configura el log
    logging.basicConfig(filename='request.log', level=logging.DEBUG)
    connection_db = connection_database('estudiantes')
    cursor_db = connection_db.cursor()
    app.run(host='0.0.0.0', port=8080)
