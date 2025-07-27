from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from app import models, schemas
from fastapi import HTTPException

def create_loan(db: Session, loan: schemas.LoanCreate):
    # Simple loan creation without external service calls
    # In a real system, you'd validate user_id and book_id exist
    db_loan = models.Loan(
        user_id=loan.user_id,
        book_id=loan.book_id,
        issue_date=datetime.now(timezone.utc),
        due_date=loan.due_date,
        status=models.LoanStatus.ACTIVE
    )
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan

def get_loans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Loan).offset(skip).limit(limit).all()

def get_loan_by_id(db: Session, loan_id: int):
    return db.query(models.Loan).filter(models.Loan.id == loan_id).first()

def update_loan(db: Session, loan_id: int, loan: schemas.LoanUpdate):
    db_loan = get_loan_by_id(db, loan_id)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
 
    update_data = loan.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_loan, key, value)
    
    db.commit()
    db.refresh(db_loan)
    return db_loan

def delete_loan(db: Session, loan_id: int):
    db_loan = get_loan_by_id(db, loan_id)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    
    db.delete(db_loan)
    db.commit()
    return {"message": "Loan deleted successfully"}