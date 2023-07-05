# Importa la clase flask del modulo flask
# Flask es una clase que nos permite crear una aplicación web
# Flask es un framework
# Un framework es un conjunto de herramientas que nos permite desarrollar aplicaciones
from flask import Flask
# Importa el modulo logging
import logging

# Se crea una instancia de la clase flask llamada app
# app es un objeto instanciado de la clase Flask
app = Flask(__name__)

# Se define una ruta para la aplicación
# La ruta es la raíz de la aplicación
@app.route('/', methods=['GET'])
# Define una función llamada hello_world
# Nos ayuda a encapsular que se ejecuta cuando se hace una petición a la ruta /
def hello_world():
    return 'Hello World!'


# Arranque del servidor o inicio del programa
if __name__ == '__main__':
    # Se configura el log
    logging.basicConfig(filename='request.log', level=logging.DEBUG)
    # Se ejecuta el servidor
    app.run(host='0.0.0.0', port=8080)