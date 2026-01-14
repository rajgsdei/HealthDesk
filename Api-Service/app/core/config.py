from pydantic_settings import BaseSettings
from typing import List
import json


class Settings(BaseSettings):
    PROJECT_NAME: str = "HealthDesk API"
    VERSION: str = "0.1.0"
    
    # MongoDB settings
    MONGODB_URL: str = "mongodb://localhost:27017"
    MONGODB_DB_NAME: str = "healthdesk"
    
    # CORS settings - will accept both JSON string or Python list
    ALLOWED_ORIGINS: str = "*"
    
    class Config:
        env_file = ".env"
        case_sensitive = True
    
    def get_allowed_origins(self) -> List[str]:
        """Parse ALLOWED_ORIGINS from env"""
        if self.ALLOWED_ORIGINS == "*":
            return ["*"]
        try:
            # Try to parse as JSON list
            return json.loads(self.ALLOWED_ORIGINS)
        except:
            # Fall back to comma-separated string
            return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]


settings = Settings()
