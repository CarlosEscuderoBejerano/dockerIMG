from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.data.modelo import Base


class Personaje(Base):
    __tablename__ = "personajes"

    id = Column(Integer, primary_key=True)
    nombrePersonaje = Column(String)
    habilidadQ = Column(String)
    habilidadE = Column(String)
    habilidadC = Column(String)
    habilidadX = Column(String)
    clase = Column(String)
    personaje_mas_utilizado = relationship("Usuario")
    