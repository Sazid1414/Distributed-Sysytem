"""
Simple Reverse Proxy Server for Distributed System
Replaces Nginx with a lightweight Python solution
"""
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse, Response
import httpx
import uvicorn
from typing import Any, Dict
import asyncio
import os

app = FastAPI(
    title="API Gateway - Distributed System",
    description="Simple reverse proxy routing requests to microservices",
    version="1.0.0"
)

# Service URLs - Support both local and Docker environments
SERVICES = {
    "users": os.getenv("USER_SERVICE_URL", "http://127.0.0.1:8080"),
    "books": os.getenv("BOOK_SERVICE_URL", "http://127.0.0.1:8082"), 
    "loans": os.getenv("LOAN_SERVICE_URL", "http://127.0.0.1:8081")
}

async def proxy_request(service_url: str, path: str, request: Request):
    """Forward request to the appropriate service"""
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            # Build the target URL
            target_url = f"{service_url}{path}"
            
            # Get request body if it exists
            body = await request.body()
            
            # Forward the request
            response = await client.request(
                method=request.method,
                url=target_url,
                headers=dict(request.headers),
                content=body,
                params=request.query_params
            )
            
            return response
            
        except httpx.RequestError as e:
            raise HTTPException(status_code=503, detail=f"Service unavailable: {str(e)}")

@app.get("/")
async def root():
    """API Gateway Home - Overview of available services"""
    return {
        "message": "🚀 API Gateway - Distributed System",
        "architecture": "Microservices with Python Reverse Proxy",
        "services": {
            "User Service": f"{SERVICES['users']}/docs",
            "Book Service": f"{SERVICES['books']}/docs", 
            "Loan Service": f"{SERVICES['loans']}/docs"
        },
        "routing": {
            "/api/users/*": "→ User Service",
            "/api/books/*": "→ Book Service", 
            "/api/loans/*": "→ Loan Service"
        },
        "status": "✅ Online"
    }

@app.get("/health")
async def health_check():
    """System Health Check - Monitor microservices status"""
    health_status = {}
    
    async with httpx.AsyncClient(timeout=5.0) as client:
        for service_name, service_url in SERVICES.items():
            try:
                response = await client.get(f"{service_url}/health", timeout=3.0)
                health_status[service_name] = "✅ Online" if response.status_code == 200 else "❌ Error"
            except:
                health_status[service_name] = "❌ Offline"
    
    return {
        "gateway": "✅ Online",
        "services": health_status,
        "timestamp": "2025-07-22"
    }

# Generic route handlers - True reverse proxy pattern
@app.api_route("/api/users/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@app.api_route("/api/users", methods=["GET", "POST", "PUT", "DELETE", "PATCH"]) 
async def proxy_users(request: Request, path: str = ""):
    """Route all /api/users requests to User Service"""
    target_path = f"/api/users/{path}" if path else "/api/users/"
    response = await proxy_request(SERVICES["users"], target_path, request)
    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers)
    )

@app.api_route("/api/books/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@app.api_route("/api/books", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_books(request: Request, path: str = ""):
    """Route all /api/books requests to Book Service"""
    target_path = f"/api/books/{path}" if path else "/api/books/"
    response = await proxy_request(SERVICES["books"], target_path, request)
    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers)
    )

@app.api_route("/api/loans/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@app.api_route("/api/loans", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_loans(request: Request, path: str = ""):
    """Route all /api/loans requests to Loan Service"""
    target_path = f"/api/loans/{path}" if path else "/api/loans/"
    response = await proxy_request(SERVICES["loans"], target_path, request)
    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers)
    )

# Documentation redirects
@app.get("/docs/users")
async def users_docs():
    """Redirect to User Service documentation"""
    return RedirectResponse(url=f"{SERVICES['users']}/docs")

@app.get("/docs/books") 
async def books_docs():
    """Redirect to Book Service documentation"""
    return RedirectResponse(url=f"{SERVICES['books']}/docs")

@app.get("/docs/loans")
async def loans_docs():
    """Redirect to Loan Service documentation"""
    return RedirectResponse(url=f"{SERVICES['loans']}/docs")

if __name__ == "__main__":
    print("🚀 Starting API Gateway (Reverse Proxy)...")
    print("📍 Gateway URL: http://127.0.0.1:8000")
    print("📖 API Docs: http://127.0.0.1:8000/docs")
    print("🏥 Health Check: http://127.0.0.1:8000/health")
    print("🔗 Service Docs:")
    print(f"   👥 Users: http://127.0.0.1:8000/docs/users")
    print(f"   📚 Books: http://127.0.0.1:8000/docs/books") 
    print(f"   📖 Loans: http://127.0.0.1:8000/docs/loans")
    
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
