@echo off
echo ========================================
echo STARTING COMPLETE SYSTEM
echo ========================================

echo.
echo 1. Activating virtual environment...
call venv\Scripts\activate

echo.
echo 2. Starting all services in background...
echo Starting User Service (Port 8080)...
start "User Service" cmd /k "venv\Scripts\activate && python -m uvicorn user-service.app.main:app --host 127.0.0.1 --port 8080"

timeout /t 2 > nul

echo Starting Book Service (Port 8082)...
start "Book Service" cmd /k "venv\Scripts\activate && python -m uvicorn book-service.app.main:app --host 127.0.0.1 --port 8082"

timeout /t 2 > nul

echo Starting Loan Service (Port 8081)...
start "Loan Service" cmd /k "venv\Scripts\activate && python -m uvicorn loan-service.app.main:app --host 127.0.0.1 --port 8081"

timeout /t 3 > nul

echo.
echo 3. Starting Python API Gateway (Reverse Proxy)...
echo This will be your single entry point on port 8000!
echo.
python api_gateway.py
