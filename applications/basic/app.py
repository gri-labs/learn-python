# Importamos la clase Flask desde el paquete flask
from flask import Flask, request

# Creamos una instancia de Flask
# El objeto app es nuestra aplicación WSGI
# Que nos permite desplegar nuestra aplicación Web
# Se le pasa como parámetro el módulo actual (__name__)
# WSGI: Web Server Gateway Interface

app = Flask(__name__)


# EL decorador route nos permite filtrar las petició HTTP recibida
# de tal forma que cuando se haga una petición HTTP a la ruta
# especificada, se ejecutará la función hello_world
@app.route('/')
def inicio():
    return 'Página principal'


@app.route('/articulos/')
def articulos():
    return 'Lista de artículos'


@app.route('/acercade')
def acercade():
    return 'Página acerca de...', 200, {'Content-Type': 'text/plain'}


# Método post
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return 'Hemos accedido por POST'
    if request.method == 'GET':
        return 'Hemos accedido por GET'


@app.route('/info', methods=["GET", "POST"])
def info():
    cad = ""
    cad += "URL:" + request.url + "\n"
    cad += "Método:" + request.method + "\n"

    cad = cad + "header:\n"
    for item, value in request.headers.items():
        cad += "{}:{}\n".format(item, value)

    cad = cad + "información en formularios (POST):\n"
    for item, value in request.form.items():
        cad += "{}:{}\n".format(item, value)

    cad += "información en URL (GET):\n"
    for item, value in request.args.items():
        cad += "{}:{}\n".format(item, value)

    cad += "Ficheros:\n"
    for item, value in request.files.items():
        cad += "{}:{}\n".format(item, value)

    print(cad)

    return cad


if __name__ == '__main__':
    # Ejecutamos la aplicación
    # Por defecto, la aplicación se ejecuta en el puerto 5000
    # Podemos cambiar la dirección IP y el puerto que nuestro servidor responderá
    app.run(host='0.0.0.0', port=81, debug=True)
