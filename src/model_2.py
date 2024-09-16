#Representação do banco de dados. Não nessariamente o meu model tem que ter as mesma caracteristicas do meu schema (view)

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db_3 import Base

class Pokemon(Base):
    __tablename__ = 'pokemons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    created_at = Column(DateTime, default=func.now())  # Campo adicionado