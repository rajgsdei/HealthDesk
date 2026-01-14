from fastapi import APIRouter, HTTPException, status
from app.models.user import UserCreate, UserResponse, LoginRequest, LoginResponse
from app.core.database import get_database
from app.core.security import get_password_hash, verify_password
from bson import ObjectId
from datetime import datetime

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate):
    """Register a new user"""
    db = get_database()
    
    # Check if user already exists
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create user document
    user_dict = user.model_dump(exclude={"password"})
    user_dict["hashed_password"] = get_password_hash(user.password)
    user_dict["created_at"] = datetime.utcnow()
    user_dict["updated_at"] = None
    
    # Insert into database
    result = await db.users.insert_one(user_dict)
    created_user = await db.users.find_one({"_id": result.inserted_id})
    
    return UserResponse(
        id=str(created_user["_id"]),
        **{k: v for k, v in created_user.items() if k not in ["_id", "hashed_password"]}
    )


@router.post("/login", response_model=LoginResponse)
async def login(credentials: LoginRequest):
    """Login user and return user information"""
    db = get_database()
    
    # Find user by email
    user = await db.users.find_one({"email": credentials.email})
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    # Verify password
    if not verify_password(credentials.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    # Check if user is active
    if not user.get("is_active", True):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )
    
    # Return user information
    user_response = UserResponse(
        id=str(user["_id"]),
        **{k: v for k, v in user.items() if k not in ["_id", "hashed_password"]}
    )
    
    return LoginResponse(user=user_response)


@router.get("/users/me", response_model=UserResponse)
async def get_current_user(email: str):
    """Get current user by email (for session validation)"""
    db = get_database()
    
    user = await db.users.find_one({"email": email})
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return UserResponse(
        id=str(user["_id"]),
        **{k: v for k, v in user.items() if k not in ["_id", "hashed_password"]}
    )
