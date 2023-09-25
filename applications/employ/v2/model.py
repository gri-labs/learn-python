from applications.employ.v2.connector_database import db


class Employee(db.):
    __tablename__ = ""
     = db.(db., primary_key=True, index=True)
    name = db.Column(db., index=True)
     = db.(db., index=True)
    salary = db.Column(db.(precision=10, scale=2))
