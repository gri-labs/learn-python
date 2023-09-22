from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:contraseña@localhost/nombre_de_la_base_de_datos'
db = SQLAlchemy(app)


@app.route('/student/<id>', methods=['POST'])
def get_student():
    from model import Students
    student = Students.query.filter_by(id=id).first()
    return student.name


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
