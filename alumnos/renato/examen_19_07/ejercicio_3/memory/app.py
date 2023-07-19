
from flask import Flask

from repository import Repository

app = Flask(__name__)


repo = Repository()


@app.route('/create/user/<int:user_id>/<string:name>/<int:age>', methods=['POST'])
def create_user(user_id, name, age):
    repo.add_user(user_id, name, age)
    return 'Usuario creado'


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = repo.get_user(user_id)
    if user:
        return f"Usuario: {user['name']}, Edad: {user['age']}", 200
    else:
        return 'Usuario no encontrado', 404


if __name__ == '__main__':
    app.run()
