# Distributed System - Phase 3

A microservices-based library management system with Python reverse proxy instead of Nginx.

## Architecture

- **API Gateway**: Python reverse proxy (port 8000)
- **User Service**: User management (port 8080)
- **Book Service**: Book catalog (port 8082)
- **Loan Service**: Book lending (port 8081)

## Quick Start

1. **Run the system**:
   ```bash
   start.bat
   ```

2. **Access the system**:
   - API Gateway: http://localhost:8000/docs
   - User Service: http://localhost:8080/docs
   - Book Service: http://localhost:8082/docs
   - Loan Service: http://localhost:8081/docs

## Features

✅ **True Reverse Proxy**: Pattern-based routing like Nginx  
✅ **Microservices**: Independent services with their own models  
✅ **No Code Duplication**: Each service maintains its own logic  
✅ **Clean Architecture**: Gateway only does routing  

## API Endpoints

- `GET/POST/PUT/DELETE /api/users/*` → User Service
- `GET/POST/PUT/DELETE /api/books/*` → Book Service
- `GET/POST/PUT/DELETE /api/loans/*` → Loan Service

## Technology Stack

- **FastAPI** - Web framework
- **SQLite** - Database (per service)
- **Uvicorn** - ASGI server
- **httpx** - HTTP client for proxy
- **Pydantic** - Data validation
