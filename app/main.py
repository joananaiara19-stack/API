from fastapi import FastAPI
from app.database import Base, engine
from app.models import evento  # importante: registra a tabela
from app.api.v1.routers import eventos

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Eventos Acadêmicos", version="1.0.0")
app.include_router(eventos.router, prefix="/api/v1")

@app.get("/")
def home():
    return {"status": "API online", "docs": "Acesse /docs para ver os endpoints"}