import flask from Flask
import mysql.connector
import logging


# Se crea una instancia de la clase flask llamada app
# app es una instancia de la clase Flask y un objeto de la clase Flask
app = Flask(__name__)


def connection_database():


def execute_query():


# Se define una ruta para la aplicación
# La ruta es la raíz de la aplicación
@app.route('/', methods=['GET'])
# Define una función llamada hell_world
# Nos ayuda a encapsular el código, mantener funcionalidades...
def get_estudiantes():


if __name__ == '__main__':
    # Se configura el log
    logging.basicConfig(filename='request.log', level=logging.DEBUG)
    app.run(host='0.0.0.0', port=6000)
