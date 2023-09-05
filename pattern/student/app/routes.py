from flask import Flask, jsonify


class RoutesStudent:
    def __init__(self, service):
        self.service = service
        self.app = Flask(__name__)
        self.app.route('/user/<int:user_id>', methods=['GET'], endpoint='get_student_id')
        self.app.route('/user/<string:user_name>', methods=['GET'], endpoint='get_student_by_name')

    def get_student_id(self, user_id):
        user = self.service.get_student_by_id(user_id)
        if user is None:
            return jsonify('User not found'), 404
        return jsonify(user), 200

    def get_student_by_name(self, user_name):
        self.service.get_student_by_name(user_name)
