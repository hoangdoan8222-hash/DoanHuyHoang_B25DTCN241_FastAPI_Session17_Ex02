from sqlalchemy.orm import Session
from models import Patient
from schelies import PatientCreate


def get_all_patients(db: Session):
    return db.query(Patient).all()


def get_patient(id: int, db: Session):
    return db.query(Patient).filter(Patient.id == id).first()


def create_patient(patient: PatientCreate, db: Session):
    new_patient = Patient(
        patient_code=patient.patient_code,
        doctor_id=patient.doctor_id
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient