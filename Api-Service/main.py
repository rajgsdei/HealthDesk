from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.config import settings
from app.core.database import connect_to_mongo, close_mongo_connection, get_database
from app.core.security import get_password_hash
from app.api.routes import health, enquiries, auth
from datetime import datetime


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    
    # Create default admin user if it doesn't exist
    await create_default_admin()
    
    yield
    # Shutdown
    await close_mongo_connection()


async def create_default_admin():
    """Create default admin user on startup if it doesn't exist"""
    db = get_database()
    
    admin_email = "admin@healthdesk.com"
    
    # Check if admin user exists
    existing_admin = await db.users.find_one({"email": admin_email})
    
    if not existing_admin:
        # Create default admin user
        admin_user = {
            "email": admin_email,
            "full_name": "Admin User",
            "role": "admin",
            "is_active": True,
            "hashed_password": get_password_hash("admin123"),
            "created_at": datetime.utcnow(),
            "updated_at": None
        }
        
        await db.users.insert_one(admin_user)
        print(f"✓ Created default admin user: {admin_email} / admin123")
    else:
        print(f"ℹ Admin user already exists: {admin_email}")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/api", tags=["Health"])
app.include_router(enquiries.router, prefix="/api/enquiries", tags=["Enquiries"])
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])


@app.get("/api/")
async def root():
    return {"message": "HealthDesk API is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
