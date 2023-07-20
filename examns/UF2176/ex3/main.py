from flask import Flask, jsonify
from repository import InMemoryRepository

app = Flask(__name__)
in_memory_repository = InMemoryRepository()


@app.route('/create/user/<int:user_id>/<string:user_name>', methods=['POST'], endpoint='insert_user')
def insert_user(user_id, user_name):
    user = {
        'id': user_id,
        'name': user_name
    }

    in_memory_repository.add(user)
    return jsonify('User created'), 201


@app.route('/user/<int:user_id>', methods=['GET'], endpoint='get_student')
def get_user(user_id):
    user = in_memory_repository.get(user_id)
    if user is None:
        return jsonify('User not found'), 404

    return jsonify(user), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
