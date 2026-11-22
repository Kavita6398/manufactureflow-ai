
from datetime import datetime, timezone

from fastapi import FastAPI

from app.core.config import settings


# Create the FastAPI application using centralized settings
app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered CRM and Manufacturing Operations Management System",
    version="0.1.0",
    debug=settings.DEBUG
)


# Root endpoint
@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "project": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "status": "running"
    }


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
