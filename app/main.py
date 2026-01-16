from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from . import crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Engineering Decision Log API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def health_check():
    return {"status": "Decision Log API running"}

@app.post("/decisions", response_model=schemas.DecisionResponse)
def create_decision(decision: schemas.DecisionCreate, db: Session = Depends(get_db)):
    return crud.create_decision(db, decision)

@app.get("/decisions", response_model=list[schemas.DecisionResponse])
def list_decisions(db: Session = Depends(get_db)):
    return crud.get_decisions(db)
