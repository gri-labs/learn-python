from flask import jsonify


class Routes:
    def (self, app, ):
        self. =
        self.repository =

        @self.app.route('/v1/student/<int:student_id>', methods=['GET'])
        def get_student_id:
            :
                result = self..get_student_by_id()
                return jsonify(result), 200
            except Exception as e:
                print(e)
