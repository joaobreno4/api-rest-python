from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import UsuarioDB, Base

# Cria as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API REST com Banco de Dados")

# Dependency para DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Schema Pydantic
class Usuario(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True


@app.get("/")
def home():
    return {"mensagem": "API com banco está rodando"}


@app.post("/usuarios", status_code=201)
def criar_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_db = UsuarioDB(**usuario.dict())

    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)

    return usuario_db


@app.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioDB).all()


@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(UsuarioDB.id == usuario_id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return usuario


@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(UsuarioDB.id == usuario_id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db.delete(usuario)
    db.commit()

    return {"mensagem": "Usuário removido com sucesso"}
