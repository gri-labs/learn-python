from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ConnectorDatabase:
    def __init__(self, host, user, password, database, port):
        self.engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')
        self.Session = sessionmaker(bind=self.engine)

    def execute_and_filter(self, model_object, filter_by=None):
        with self.Session() as session:
            result = session.query(model_object).filter_by(**filter_by).first()
            return result

    def execute_and_commit(self, model_object):
        with self.Session() as session:
            session.add(model_object)
            session.commit()
            session.close()

    def delete_and_commit(self, model_object):
        with self.Session() as session:
            session.delete(model_object)
            session.commit()
            session.close()