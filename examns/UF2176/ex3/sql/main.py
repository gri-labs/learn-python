from flask import Flask, jsonify
from connector_database import ConnectorDatabase
from repository import Repository

app = Flask(__name__)
repository = Repository(ConnectorDatabase(
    host='localhost',
    user='root',
    password='root',
    database='examen',
    port=3308
))


@app.route('/create/user/<string:user_name>', methods=['POST'], endpoint='insert_user')
def insert_user(user_name):
    repository.insert_student(user_name)
    return jsonify('User created'), 201


@app.route('/user/<int:user_id>', methods=['GET'], endpoint='get_student')
def get_user(user_id):
    user = repository.get_student_by_id(user_id)
    if user is None:
        return jsonify('User not found'), 404
    return jsonify(user), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
