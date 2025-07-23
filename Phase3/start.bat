@echo off
echo ========================================
echo PHASE 3: DISTRIBUTED SYSTEM
echo ========================================

cd /d "d:\OneDrive\Documents\Distributed-Sysytem\Phase3"
call venv\Scripts\activate

echo.
echo 🛑 Stopping any existing services...
taskkill /f /im python.exe 2>nul
timeout /t 2 /nobreak > nul

echo.
echo 🚀 Starting services...

echo Starting User Service (Port 8080)...
cd user-service
start "User Service" cmd /k "call ..\venv\Scripts\activate && python -m uvicorn app.main:app --host 127.0.0.1 --port 8080"
cd ..

timeout /t 3 /nobreak > nul

echo Starting Book Service (Port 8082)...
cd book-service
start "Book Service" cmd /k "call ..\venv\Scripts\activate && python -m uvicorn app.main:app --host 127.0.0.1 --port 8082"
cd ..

timeout /t 3 /nobreak > nul

echo Starting Loan Service (Port 8081)...
cd loan-service
start "Loan Service" cmd /k "call ..\venv\Scripts\activate && python -m uvicorn app.main:app --host 127.0.0.1 --port 8081"
cd ..

timeout /t 5 /nobreak > nul

echo.
echo 🌐 Starting API Gateway (Port 8000)...
echo.
echo ✅ Access your system at: http://localhost:8000/docs
echo.
python api_gateway.py