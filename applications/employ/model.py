from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Numeric

db = SQLAlchemy()


class Employs(db.Model):
    __tablename__ = "employs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    department = Column(String, index=True)
    salary = Column(Numeric(precision=10, scale=2))
