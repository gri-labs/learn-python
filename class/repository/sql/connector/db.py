import mysql.connector


# ConnectorDatabase class
# Que es una clase?
# Es una estructura que define un objeto
class ConnectorDatabase:
    # Que es un constructor?
    # Es una funcion que se ejecuta al crear una instancia de la clase
    # Que es self?
    # Es una referencia al objeto que se esta creando
    # Que es __init__?
    # Es el constructor de la clase
    # la estructura de un constructor es:
    # def __init__(self, param1, param2, param3, ...):
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    # Que es un metodo?
    # Es una funcion que pertenece a una clase
    # al inicializar un metodo se debe pasar como primer parametro self
    # la estructura de un metodo es:
    # def method_name(self, param1, param2, param3, ...):
    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.,
            database=self.database,
            port=self.port
        )

        return self.connection

    def disconnect(self):
        self.connection.close()