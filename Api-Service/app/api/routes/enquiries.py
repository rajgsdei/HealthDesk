from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.enquiry import Enquiry, EnquiryCreate, EnquiryResponse
from app.core.database import get_database
from bson import ObjectId
from datetime import datetime

router = APIRouter()


@router.post("/", response_model=EnquiryResponse, status_code=status.HTTP_201_CREATED)
async def create_enquiry(enquiry: EnquiryCreate):
    """Create a new patient enquiry"""
    db = get_database()
    enquiry_dict = enquiry.model_dump()
    enquiry_dict["created_at"] = datetime.utcnow()
    enquiry_dict["status"] = "pending"
    
    result = await db.enquiries.insert_one(enquiry_dict)
    created_enquiry = await db.enquiries.find_one({"_id": result.inserted_id})
    
    return EnquiryResponse(
        id=str(created_enquiry["_id"]),
        **{k: v for k, v in created_enquiry.items() if k != "_id"}
    )


@router.get("/", response_model=List[EnquiryResponse])
async def get_all_enquiries():
    """Get all enquiries"""
    db = get_database()
    enquiries = []
    
    async for enquiry in db.enquiries.find():
        enquiries.append(
            EnquiryResponse(
                id=str(enquiry["_id"]),
                **{k: v for k, v in enquiry.items() if k != "_id"}
            )
        )
    
    return enquiries


@router.get("/{enquiry_id}", response_model=EnquiryResponse)
async def get_enquiry(enquiry_id: str):
    """Get a specific enquiry by ID"""
    db = get_database()
    
    try:
        enquiry = await db.enquiries.find_one({"_id": ObjectId(enquiry_id)})
    except:
        raise HTTPException(status_code=400, detail="Invalid enquiry ID format")
    
    if not enquiry:
        raise HTTPException(status_code=404, detail="Enquiry not found")
    
    return EnquiryResponse(
        id=str(enquiry["_id"]),
        **{k: v for k, v in enquiry.items() if k != "_id"}
    )
