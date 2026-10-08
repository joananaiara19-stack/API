from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.evento import Evento
from app.schemas.evento import EventoCreate, EventoOut

router = APIRouter(prefix="/eventos", tags=["Eventos"])

@router.post("", response_model=EventoOut, status_code=status.HTTP_201_CREATED)
def criar(dados: EventoCreate, db: Session = Depends(get_db)):
    evento = Evento(**dados.model_dump())
    db.add(evento)
    db.commit()
    db.refresh(evento)
    return evento

@router.get("", response_model=list[EventoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Evento).all()

@router.get("/{evento_id}", response_model=EventoOut)
def buscar(evento_id: int, db: Session = Depends(get_db)):
    evento = db.get(Evento, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado.")
    return evento

@router.put("/{evento_id}", response_model=EventoOut)
def atualizar(evento_id: int, dados: EventoCreate, db: Session = Depends(get_db)):
    evento = db.get(Evento, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado.")
    for campo, valor in dados.model_dump().items():
        setattr(evento, campo, valor)
    db.commit()
    db.refresh(evento)
    return evento

@router.delete("/{evento_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir(evento_id: int, db: Session = Depends(get_db)):
    evento = db.get(Evento, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado.")
    db.delete(evento)
    db.commit()