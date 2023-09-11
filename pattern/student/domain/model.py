from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Modelo de persistencia
# DTO (Data Transfer Object)
class StudentDTORepositoryService(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)
    dni = Column(String(255))
