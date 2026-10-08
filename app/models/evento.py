from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    data_evento = Column(Date, nullable=False)
    capacidade = Column(Integer, nullable=False)
    status = Column(String, default="ativo")