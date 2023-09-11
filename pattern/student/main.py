from pattern.student.infrastructure.connector import ConnectorDatabase
from pattern.student.domain.repository import StudentRepository
from pattern.student.domain.service import StudentService
from pattern.student.application.controllers import RoutesStudent
from flask import Flask

if __name__ == '__main__':
    app = Flask(__name__)

    repository = StudentRepository(ConnectorDatabase(
        host='localhost',
        password='root',
        user='root',
        database='school',
        port=int(3308)
    ))

    service = StudentService(repository)

    routes = RoutesStudent(service, app)
    app.run(host='0.0.0.0', port=6000, debug=True)