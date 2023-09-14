from flask import Flask
from repository import Repository
from connector import ConnectorDatabase
from controller import Routes

if __name__ == '__main__':
    app = Flask(__name__)

    connector_database = ConnectorDatabase(
        host='localhost',

    )

    repository = Repository(connector_database)
    routes = Routes(app, repository)

    app.run(host='0.0.0.0', port=6000, debug=True)





