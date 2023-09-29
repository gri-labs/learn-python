from applications.employ.v2.connector_database import db


class Employee(db.Model):
    __tablename__ = "employs"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, index=True)
    department = db.Column(db.String, index=True)
    salary = db.Column(db.Numeric(precision=10, scale=2))
