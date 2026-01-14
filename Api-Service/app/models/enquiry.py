from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class EnquiryBase(BaseModel):
    patient_name: str = Field(..., min_length=1, max_length=100)
    patient_email: EmailStr
    patient_phone: str = Field(..., min_length=10, max_length=15)
    subject: str = Field(..., min_length=1, max_length=200)
    message: str = Field(..., min_length=1)


class EnquiryCreate(EnquiryBase):
    pass


class Enquiry(EnquiryBase):
    status: str = "pending"  # pending, in-progress, completed
    created_at: datetime
    

class EnquiryResponse(Enquiry):
    id: str
    
    class Config:
        from_attributes = True
