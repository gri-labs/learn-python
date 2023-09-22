from sqlalchemy import Column
from sqlalchemy import Integer, String
from app import db


class Students(db.Model):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
