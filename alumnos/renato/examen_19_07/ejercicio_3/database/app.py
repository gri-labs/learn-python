from flask import Flask

from repositoryDB import RepositoryDB

app = Flask(__name__)

repo = RepositoryDB()


def print_data(to_print):
    for result in to_print:
        print(result)
    return


@app.route('/create/user/<int:user_id>/<string:name>/<int:age>', methods=['POST'])
def create_user(user_id, name, age):
    connection_db = repo.connection_database('localhost', 'root', 'root', 3307, 'mysql')
    repo.insert_data(connection_db, "examen", "users", user_id, name, age)
    repo.close_connection(connection_db)
    return 'Usuario creado', 200


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    connection_db = repo.connection_database('localhost', 'root', 'root', 3307, 'mysql')
    data_by_id = repo.get_data_by_id(connection_db, "examen", "users", user_id)
    repo.close_connection(connection_db)
    print_data(data_by_id)
    return "OK", 200


if __name__ == '__main__':
    connection_db = repo.connection_database('localhost', 'root', 'root', 3307, 'mysql')
    repo.create_db(connection_db, "examen")
    repo.create_table(connection_db, "examen", "users")

    app.run()
