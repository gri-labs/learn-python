from flask import jsonify, request
from pattern.student.application.response import StudentResponse


class RoutesStudent:
    def __init__(self, service, app):
        self.service = service
        self.app = app

        @self.app.route('/v1/student/<int:student_id>', methods=['GET'])
        def get_student_id(student_id):
            try:
                student = self.service.get_student_by_id(student_id)

                return jsonify(StudentResponse(student.id, student.name).to_json()), 200
            except ValueError as e:
                return jsonify(str(e)), 404

        # Add user
        @self.app.route('/v1/user', methods=['POST'])
        def add_student():
            try:
                data = request.get_json()

                required_fields = ['name', 'last_name', 'age', 'dni']

                for field in required_fields:
                    if field not in data:
                        raise ValueError(f'{field} is required')

                self.service.add_student()

                return jsonify('Student added'), 200
            except ValueError as e:
                return jsonify(str(e)), 404
