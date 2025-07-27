from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db
from typing import List

router = APIRouter(prefix="/api/loans", tags=["Loans"])

@router.post("/", response_model=schemas.Loan, status_code=201)
def create_loan(loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    """Create a new loan"""
    return crud.create_loan(db, loan)

@router.get("/", response_model=List[schemas.Loan])
def get_loans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all loans"""
    return crud.get_loans(db, skip=skip, limit=limit)

# FIXED: Changed from /{loan_id} to /loan/{loan_id} to avoid conflict with /docs
@router.get("/loan/{loan_id}", response_model=schemas.Loan)
def get_loan(loan_id: int, db: Session = Depends(get_db)):
    """Get a specific loan by ID"""
    loan = crud.get_loan_by_id(db, loan_id)
    if loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan

# FIXED: Changed from /{loan_id} to /loan/{loan_id} to avoid conflict with /docs
@router.put("/loan/{loan_id}", response_model=schemas.Loan)
def update_loan(loan_id: int, loan: schemas.LoanUpdate, db: Session = Depends(get_db)):
    """Update a loan"""
    return crud.update_loan(db, loan_id, loan)

# FIXED: Changed from /{loan_id} to /loan/{loan_id} to avoid conflict with /docs
@router.delete("/loan/{loan_id}")
def delete_loan(loan_id: int, db: Session = Depends(get_db)):
    """Delete a loan"""
    return crud.delete_loan(db, loan_id)