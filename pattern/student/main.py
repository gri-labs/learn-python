from pattern.student.infrastructure.connector import ConnectorDatabase
from pattern.student.infrastructure.repository import Repository
from pattern.student.application.service import Service
from pattern.student.app.routes import RoutesStudent

if __name__ == '__main__':
    repository = Repository(ConnectorDatabase(
        host='localhost',
        password='root',
        user='root',
        database='school',
        port=int(3308)
    ))

    service = Service(repository)

    routes = RoutesStudent(service)
    routes.app.run(host='0.0.0.0', port=6000, debug=True)





