from flask import jsonify, request
from flask import Flask
from applications.employ.v2.model import Employee
from applications.employ.v2.connector_database import ConnectorDatabase
from applications.employ.v2.config import config_database


class Routes:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = config_database()['SQLALCHEMY_DATABASE_URI']
        self.connector_database = ConnectorDatabase(self.app)

    def configure_routes(self):
        @self.app.route('/v1/user/<id>', methods=['GET'])
        def get_employee_id(id):
            employ = self.connector_database.get_by_filter(id, Employee)
            if employ is None:
                return jsonify('Employ not found'), 404
            return jsonify({
                'id': employ.id,
                'name': employ.name,
                'department': employ.department,
                'salary': employ.salary
            }), 200

        @self.app.route('/v1/login', methods=['POST'])
        def add_employee():
            requests = request.get_json()
            try:
                self.connector_database.add(Employee(
                    name=requests['name'],
                    department=requests['department'],
                    salary=requests['salary']
                ))
                return jsonify('Employ created successfully'), 201
            except Exception as e:
                return jsonify('Error...')

        @self.app.route('/employ/<id>', methods=['PUT'])
        def update_employee(id):
            requests = request.get_json()
            try:
                self.connector_database.update(Employee(
                    id=id,
                    name=requests['name'],
                    department=requests['department'],
                    salary=requests['salary']
                ))
                return jsonify('Employ updated successfully'), 200
            except Exception as e:
                return jsonify('Error...')

        @self.app.route('/employ/<id>', methods=['DELETE'])
        def delete_employee(id):
            employ = Employee(
                id=id
            )

            try:
                self.connector_database.get_by_filter(id, employ)
                if employ is None:
                    return jsonify('Employ not found'), 404

                self.connector_database.delete(Employee(
                    id=id
                ))

                return jsonify('Employ delete successfully'), 200
            except Exception as e:
                return jsonify('Error...')
