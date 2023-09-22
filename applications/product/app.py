from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from model import Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:contraseña@localhost/nombre_de_la_base_de_datos'
db = SQLAlchemy(app)


@app.route('/products', methods=['GET'])
def get_products():
    from model import Product
    products = Product.query.all()
    return products


@app.route('/product/<id>', methods=['GET'])
def get_product():
    from model import Product
    product = Product.query.filter_by(id=id).first()
    return product.name


# Add product
@app.route('/product', methods=['POST'])
def add_product():
    nombre = request.form['nombre']
    producto = Product(nombre=nombre)
    db.session.add(producto)
    db.session.commit()
    return 'Producto agregado'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
