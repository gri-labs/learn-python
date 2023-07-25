from flask import Flask, jsonify
from repository import Repository
from print_data import PrintData
from connector_database import ConnectorDatabase

app = Flask(__name__)
connector = ConnectorDatabase('localhost', 'root', 'root', 'gri', 3307)
repository = Repository(connector)
print_data = PrintData


@app.route('/create/student/<string:name>', methods=['POST'], endpoint='insert_student')
def insert_student(name):
    repository.insert_student(name)
    return jsonify('User created'), 201


@app.route('/student/<int:student_id>', methods=['GET'], endpoint='get_student')
def get_student(student_id):
    datos = repository.get_student_by_id(student_id)
    print_data.print_data(datos)
    return jsonify(""), 200

@app.route('/students', methods=['GET'], endpoint='get_students')
def get_students():
    datos = repository.get_students()
    print_data.print_data(datos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
