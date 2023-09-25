from flask import
from flask import
from applications.employ.v2.model import
from applications.employ.v2.connector_database import
from applications.employ.v2.config import


class Routes:
    def __init__(self):
        self.app = Flask()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = config_database()['SQLALCHEMY_DATABASE_URI']
        self.connector_database = ConnectorDatabase()

    def configure_routes(self):
        self.app.route('/employ/<id>', methods=['GET'])
        def get_employee_id(id):
