from datetime import date
from pydantic import BaseModel, Field, field_validator

#Configura o modelo de dados para criar um evento, com validação de campos
class EventoCreate(BaseModel):
    titulo: str
    descricao: str | None = None
    data_evento: date
    capacidade: int = Field(gt=0)

#Cria uma regra de validação para o campo data_evento, que não pode ser uma data passada
    @field_validator("data_evento")
    @classmethod
    def nao_pode_ser_passada(cls, v):
        if v < date.today():
            raise ValueError("Data do evento não pode ser passada")
        return v

class EventoOut(EventoCreate):
    id: int
    status: str
    model_config = {"from_attributes": True}