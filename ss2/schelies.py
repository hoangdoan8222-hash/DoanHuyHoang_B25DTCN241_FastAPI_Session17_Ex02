from pydantic import BaseModel


class PatientCreate(BaseModel):
    patient_code: str
    doctor_id: int


class PatientResponse(BaseModel):
    id: int
    patient_code: str
    doctor_id: int

    class Config:
        from_attributes = True