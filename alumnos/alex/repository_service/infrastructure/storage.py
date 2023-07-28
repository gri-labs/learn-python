from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Modelo de persistencia
# DTO (Data Transfer Object)
class StudentDTO(Base):
    __tablename__ = 'estudiantes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    apellido = Column(String(255))
    edad = Column(Integer)
    password = Column(String(255))