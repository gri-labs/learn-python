# Esta es la importación del modulo sqlalchemy:
# El módulo sqlalchemy es un ORM (Object Relational Mapper) que nos permite mapear
# las tablas de la base de datos a clases de Python.
# Importamos las funciones create_engine y sessionmaker del módulo sqlalchemy.
# Estas funciones se utilizan para crear una conexión a la base de datos y una sesión, respectivamente.
# Que es una sesión?
# Una sesión es un objeto que nos permite interactuar con la base de datos.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ConnectorDatabase:
    def __init__(self, host, user, password, database, port):
        # Creamos una conexión a la base de datos
        self.engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')
        # Creamos una sesión
        self.Session = sessionmaker(bind=self.engine)

    def execute_and_filter(self, model_data, filter_by=None):
        # Abrimos una sesión.
        # La sentencia with nos permite ejecutar una función al principio y al final de un bloque de código
        # de manera segura.
        with self.Session() as session:
            # Ejecutamos la consulta
            # La función filter_by nos permite filtrar los resultados de la consulta
            # La función first nos permite obtener el primer resultado de la consulta
            # **filter_by es una forma de pasar argumentos a una función
            # Ejemplo:
            # def my_function(**kwargs):
            #     print(kwargs)
            # my_function(name='Juan', age=20)
            # Resultado:
            # {'name': 'Juan', 'age': 20}
            # query es una función que nos permite ejecutar una consulta
            ####
            # model_data.__class__ es una forma de obtener la clase de un objeto
            result = session.query(model_data.__class__).filter_by(**filter_by).first()
            # Cerramos la sesión
            session.close()
            # Retornamos el resultado
            return result

    def add(self, model_data):
        with self.Session() as session:
            session.add(model_data)
            session.commit()
            session.close()

    def update(self, model_data):
        with self.Session() as session:
            session.merge(model_data)
            session.commit()
            session.close()

    def delete_by_id(self, model_data):
        # TODO implementar
        pass