from sqlalchemy.orm import Session
from .models import Decision
from .schemas import DecisionCreate

def create_decision(db: Session, decision: DecisionCreate):
    db_decision = Decision(**decision.dict())
    db.add(db_decision)
    db.commit()
    db.refresh(db_decision)
    return db_decision

def get_decisions(db: Session):
    return db.query(Decision).all()
