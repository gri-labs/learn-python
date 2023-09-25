from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Numeric

db = SQLAlchemy()


# Modelo de persistencia
# db.Model es el encargado de la comunicacion con la base de datos
# contiene los metodos necesarios para realizar las operaciones CRUD
class Employs(db.Model):
    __tablename__ = "employs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    department = Column(String, index=True)
    salary = Column(Numeric(precision=10, scale=2))
