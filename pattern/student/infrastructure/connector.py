# Esta es la importación del modulo sqlalchemy:
# El módulo sqlalchemy es un ORM (Object Relational Mapper) que nos permite mapear
# las tablas de la base de datos a clases de Python.
# Importamos las funciones create_engine y sessionmaker del módulo sqlalchemy.
# Estas funciones se utilizan para crear una conexión a la base de datos y una sesión, respectivamente.
# Que es una sesión?
# Una sesión es un objeto que nos permite interactuar con la base de datos.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


class ConnectorDatabase:
    def __init__(self, host, user, password, database, port):
        # Creamos una conexión a la base de datos
        self.engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')
        # Creamos una sesión
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def get_by_id(self, model_data, id):
        try:
            # Ejecutamos la consulta
            return self.session.query(model_data.__class__).get(id)
        except SQLAlchemyError as e:
            print(e)
            return None

    def add(self, model_data):
        with self.Session() as session:
            session.add(model_data)
            session.commit()
            session.close()

    def update(self, model_data):
        with self.Session() as session:
            # Actualizamos el objeto en la sesión
            session.merge(model_data)

            # Committing the changes to the database
            session.commit()

            # Closing the session
            session.close()

    def delete(self, model_data):
        with self.Session() as session:
            # Deleting the object from the session
            session.delete(model_data)

            # Committing the changes to the database
            session.commit()

            # Closing the session
            session.close()
