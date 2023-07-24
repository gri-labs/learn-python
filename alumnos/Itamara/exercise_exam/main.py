from flask import Flask, jsonify
from repository import Repository
from connector_database import ConnectorDatabase

app = Flask(__name__)
repository = Repository()
connector = ConnectorDatabase()


@app.route('/create/user/<int:user_id>/<string:user_name>', methods=['POST'], endpoint='insert_user')
def insert_user(user_id, user_name):

    return jsonify('User created'), 201


@app.route('/user/<int:user_id>', methods=['GET'], endpoint='get_student')
def get_user(user_id):
    return jsonify(""), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
