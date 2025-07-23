# Phase 3: Distributed System

## 🚀 Quick Start
```cmd
start.bat
```
##Task Kill 
taskkill /f /im python.exe 2>nul
## 🌐 Access Points
- **API Gateway**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📂 Project Structure
```
Phase3/
├── api_gateway.py          # Python reverse proxy
├── start.bat              # Startup script
├── user-service/          # User management (Port 8080)
├── book-service/          # Book inventory (Port 8082)
├── loan-service/          # Loan management (Port 8081)
├── venv/                  # Virtual environment
└── README.md              # This file
```

## ✅ Phase 3 Complete
- 3 Independent microservices
- Python reverse proxy (replaces Nginx)
- Single entry point through API Gateway
- Clean API endpoints: `/api/users`, `/api/books`, `/api/loans`
