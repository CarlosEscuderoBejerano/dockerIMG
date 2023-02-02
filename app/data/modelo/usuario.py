from sqlalchemy import Column, ForeignKey,Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.data.modelo import Base
from app.data.modelo.personaje import Personaje
from app.data.modelo.arma import Arma


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    personaje_mas_utilizado = Column(Integer,ForeignKey("personajes.id"))
    arma_mas_utilizada = Column(Integer,ForeignKey("armas.id"))
    personaje  = relationship("Personaje",back_populates="personaje_mas_utilizado")
    arma = relationship("Arma",back_populates="arma_mas_utilizada")

    

    
    