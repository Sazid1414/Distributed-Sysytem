@echo off
echo ========================================
echo STARTING PHASE 3 DISTRIBUTED SYSTEM
echo ========================================

cd /d "d:\OneDrive\Documents\Distributed-Sysytem\Phase3"
call venv\Scripts\activate

echo.
echo 🚀 Starting User Service (Port 8080)...
cd user-service
start "User Service" cmd /k "call ..\venv\Scripts\activate && python -m uvicorn app.main:app --host 127.0.0.1 --port 8080"
cd ..

echo Waiting 3 seconds...
timeout /t 3 /nobreak > nul

echo.
echo 📚 Starting Book Service (Port 8082)...
cd book-service
start "Book Service" cmd /k "call ..\venv\Scripts\activate && python -m uvicorn app.main:app --host 127.0.0.1 --port 8082"
cd ..

echo Waiting 3 seconds...
timeout /t 3 /nobreak > nul

echo.
echo 📖 Starting Loan Service (Port 8081)...
cd loan-service
start "Loan Service" cmd /k "call ..\venv\Scripts\activate && python -m uvicorn app.main:app --host 127.0.0.1 --port 8081"
cd ..

echo.
echo Waiting 5 seconds for all services to start...
timeout /t 5 /nobreak > nul

echo.
echo 🌐 Starting API Gateway (Python Reverse Proxy) on Port 8000...
echo.
echo ========================================
echo 🎯 YOUR DISTRIBUTED SYSTEM IS STARTING!
echo ========================================
echo.
echo 📍 Access points:
echo    Main Gateway: http://localhost:8000/
echo    Health Check: http://localhost:8000/health
echo    API Docs: http://localhost:8000/docs
echo.
echo 🔗 Direct Services (for testing):
echo    User Service: http://localhost:8080/docs
echo    Book Service: http://localhost:8082/docs  
echo    Loan Service: http://localhost:8081/docs
echo.
echo Starting API Gateway now...
python api_gateway.py
