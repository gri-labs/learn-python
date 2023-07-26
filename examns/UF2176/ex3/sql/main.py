from flask import Flask, jsonify
from repository import Repository
from connector_database import ConnectorDatabase

app = Flask(__name__)

connector = ConnectorDatabase(
        host='localhost',
        user='root',
        password='root',
        database='users',
        port=3307
)

repository = Repository(connector)

@app.route('/create/user/<int:user_id>/<string:user_name>/<int:user_age>', methods=['POST'], endpoint='insert_user')
def insert_user(user_id, user_name, user_age):
    try:
        repository.insert_user(user_id, user_name, user_age)
        return jsonify('User created'), 201
    except Exception as err:
        return jsonify('error', err)
    

@app.route('/user/<int:user_id>', methods=['GET'], endpoint='get_user')
def get_user(user_id):
    try:
        user = repository.get_user_by_id(user_id)
        if user is None:
            return jsonify('User not found'), 404
        else:
            return jsonify(user), 200
    except:
        return jsonify('error'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)