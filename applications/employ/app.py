from flask import Flask, jsonify
from model import db, Employs

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3308/import_sql'
db.init_app(app)


@app.route('/employ/<id>', methods=['GET'])
def get_employ(id):
    employ = Employs.query.filter_by(id=id).first()

    if employ is None:
        return jsonify('Employ not found'), 404

    return jsonify({
        'id': employ.id,
        'name': employ.name,
        'department': employ.department,
        'salary': employ.salary
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
