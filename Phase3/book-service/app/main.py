from fastapi import FastAPI
from app.routers import router
from app.database import engine, Base
import uvicorn

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Book Service",
    description="Book Service API for Library Management System",
    version="1.0.0"
)

@app.get("/health")
async def health_check():
    """Health check endpoint for Docker and monitoring"""
    return {"status": "healthy", "service": "book-service"}

# Include router
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8082, reload=True)