from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ConnectorDatabase:
    def __init__(self, app=None):
        if app is not None:
            self.db = db
            self.db.init_app(app)

    def get_by_filter(self, id, model_data):
        employ = self.db.session.query(model_data).filter_by(id=id).first()
        return employ

    def get_employs(self, model_data):
        employs = self.db.session.query(model_data).all()
        return employs

    def add(self, model_data):
        self.db.session.add(model_data)
        self.db.session.commit()

    def update(self, model_data):
        self.db.session.merge(model_data)
        self.db.session.commit()

    def delete(self, model_data):
        self.db.session.delete(model_data)
        self.db.session.commit()
