from flask import Flask, jsonify, request
from model import Employs
from model import db

# Instancia de Flask
# __name__ es el nombre del modulo actual
app = Flask(__name__)
# Configuracion de la base de datos
# dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3308/import_sql'
# db.init_app(app) inicializa la base de datos y usa la configuracion de la app
# Instancia de SQLAlchemy
db.init_app(app)


# @ es un decorador
# Un decorador es una funcion que recibe como parametro otra funcion
# y extiende su funcionalidad sin modificarla
@app.route('/employ/<id>', methods=['GET'])
def get_employ(id):
    # db.session.query(Employs) es el equivalente a SELECT * FROM employs
    # filter_by(id=id) es el equivalente a WHERE id = id

    # session es una coleccion de objetos cargados de la base de datos
    # para realizar operaciones sobre ellos
    # employ es un objeto de tipo Employs

    employ = db.session.query(Employs).filter_by(id=id).first()

    if employ is None:
        return jsonify('Employ not found'), 404

    return jsonify({
        'id': employ.id,
        'name': employ.name,
        'department': employ.department,
        'salary': employ.salary
    }), 200


@app.route('/employ/<int:id>', methods=['DELETE'])
def delete_employ(id):
    try:
        db.session.query(Employs).filter_by(id=id).delete()
        db.session.commit()
        return jsonify('Employ delete successfully'), 200
    except Exception as e:
        return jsonify('Error...')


@app.route('/employ', methods=['POST'])
def add_employ():
    )


@app.route('/employ/<int:id>', methods=['PUT'])
def update_employ(id):



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
