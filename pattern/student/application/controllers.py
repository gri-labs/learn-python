from flask import jsonify
from pattern.student.application.response import StudentResponse


class RoutesStudent:
    def __init__(self, service, app):
        self.service = service
        self.app = app

        @self.app.route('/user/<int:user_id>', methods=['GET'])
        def get_student_id(user_id):
            try:
                student = self.service.get_student_by_id(user_id)

                student_response = StudentResponse(student.id, student.name)

                return jsonify(student_response.to_json()), 200
            except ValueError as e:
                return jsonify(str(e)), 404
