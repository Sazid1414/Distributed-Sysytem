@echo off
cd /d "d:\OneDrive\Documents\Distributed-Sysytem\Phase3"
call venv\Scripts\activate

echo ========================================
echo TESTING PHASE 3 DISTRIBUTED SYSTEM
echo ========================================

echo.
echo 1. Starting User Service (Port 8080)...
start "User Service" cmd /k "call venv\Scripts\activate && python -m uvicorn user-service.app.main:app --host 127.0.0.1 --port 8080"

echo Waiting 3 seconds for User Service to start...
timeout /t 3 /nobreak > nul

echo.
echo 2. Starting Book Service (Port 8082)...
start "Book Service" cmd /k "call venv\Scripts\activate && python -m uvicorn book-service.app.main:app --host 127.0.0.1 --port 8082"

echo Waiting 3 seconds for Book Service to start...
timeout /t 3 /nobreak > nul

echo.
echo 3. Starting Loan Service (Port 8081)...
start "Loan Service" cmd /k "call venv\Scripts\activate && python -m uvicorn loan-service.app.main:app --host 127.0.0.1 --port 8081"

echo Waiting 5 seconds for all services to start...
timeout /t 5 /nobreak > nul

echo.
echo 4. Checking if services are running...
netstat -an | findstr ":8080"
netstat -an | findstr ":8081"
netstat -an | findstr ":8082"

echo.
echo 5. Testing direct service access...
echo Testing User Service...
curl -s http://127.0.0.1:8080/api/users/ || echo "User Service not responding"

echo Testing Book Service...
curl -s http://127.0.0.1:8082/api/books/ || echo "Book Service not responding"

echo Testing Loan Service...
curl -s http://127.0.0.1:8081/api/loans/ || echo "Loan Service not responding"

echo.
echo 6. Starting API Gateway (Python Reverse Proxy)...
echo This will start on port 8000 - your single entry point!
echo.
echo API Gateway starting... Access at: http://localhost:8000/
python api_gateway.py
