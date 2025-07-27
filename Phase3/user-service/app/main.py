from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Service")

@app.get("/health")
async def health_check():
    """Health check endpoint for Docker and monitoring"""
    return {"status": "healthy", "service": "user-service"}

app.include_router(router)