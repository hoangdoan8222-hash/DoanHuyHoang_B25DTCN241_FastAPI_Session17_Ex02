from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from schelies import PatientCreate, PatientResponse
from servies import (
    get_all_patients,
    get_patient,
    create_patient
)

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hospital Management API"
    }


@app.get("/patients")
def list_patients(db: Session = Depends(get_db)):
    return get_all_patients(db)


@app.get("/patients/{id}", response_model=PatientResponse)
def detail_patient(id: int, db: Session = Depends(get_db)):
    patient = get_patient(id, db)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


@app.post("/patients", response_model=PatientResponse)
def add_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    return create_patient(patient, db)