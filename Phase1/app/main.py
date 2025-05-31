from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import traceback
from app.routers import users, books, loans, stats
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Library System")

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": f"Internal Server Error: {str(exc)}", 
                 "traceback": traceback.format_exc()}
    )

@app.get("/")
async def root():
    return {"message": "Welcome to Smart Library System API", 
            "documentation": "/docs"}

app.include_router(users.router)
app.include_router(books.router)
app.include_router(loans.router)
app.include_router(stats.router)
