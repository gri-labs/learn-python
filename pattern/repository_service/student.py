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


# Modelo de negocio
# Entity
# Clase que representa el modelo de negocio
# No tiene ninguna dependencia de la base de datos
class StudentEntity():
    # Propiedades por defecto
    id = 0
    nombre = ""
    password = bytes()

    def __init__(self, id=0, nombre="", password=bytes()):
        self.id = id
        self.nombre = nombre
        self.password = password
