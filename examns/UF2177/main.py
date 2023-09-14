from flask import Flask
from controller import Routes
from repository import Repository
from connector import ConnectorDatabase

if __name__ == '__main__':
    app = Flask(__name__)

    connector_database = ConnectorDatabase(
        host='localhost',
        user='root',
        password='root',
        database='UF2177',
        port=3306
    )

    repository = Repository(connector_database)
    routes = Routes(app, repository)

    app.run(host='0.0.0.0', port=6000, debug=True)





