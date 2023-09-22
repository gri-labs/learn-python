from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Numeric

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3308/import_sql'
db = SQLAlchemy(app)


class Employs(db.Model):
    __tablename__ = "employs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    department = Column(String, index=True)
    salary = Column(Numeric(precision=10, scale=2))


@app.route('/employ/<id>', methods=['GET'])
def get_student(id):
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
