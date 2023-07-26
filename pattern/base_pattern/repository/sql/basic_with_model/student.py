# Create model for student
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Modelo de persistencia
# DTO (Data Transfer Object)
class StudentDTO(Base):
    __tablename__ = 'estudiantes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))


# Una entidad es?
# Una entidad es una clase que representa un modelo de negocio
# No tiene ninguna dependencia de la base de datos
class StudentEntity():
    # Propiedades por defecto
    # Las entidades siempre deben tener un id
    id = 0
    nombre = ""

    def __init__(self, id=0, nombre=""):
        self.id = id
        self.nombre = nombre
