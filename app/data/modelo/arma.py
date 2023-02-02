from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.data.modelo import Base


class Arma(Base):
    __tablename__ = "armas"

    id = Column(Integer, primary_key=True)
    NombreArma = Column(String)
    precio = Column(String)
    arma_mas_utilizada= relationship("Usuario")

