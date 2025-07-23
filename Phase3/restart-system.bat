@echo off
echo ========================================
echo RESTARTING DISTRIBUTED SYSTEM
echo ========================================

cd /d "d:\OneDrive\Documents\Distributed-Sysytem\Phase3"

echo.
echo 🛑 Stopping any existing services...
taskkill /f /im python.exe 2>nul
taskkill /f /im uvicorn.exe 2>nul

echo Waiting 3 seconds for processes to stop...
timeout /t 3 /nobreak > nul

echo.
echo 🔄 Activating virtual environment...
call venv\Scripts\activate

echo.
echo 🚀 Starting User Service (Port 8080)...
cd user-service
start "User Service" cmd /k "call ..\venv\Scripts\activate && python -m uvicorn app.main:app --host 127.0.0.1 --port 8080 --reload"
cd ..

echo Waiting 4 seconds for User Service...
timeout /t 4 /nobreak > nul

echo.
echo 📚 Starting Book Service (Port 8082)...
cd book-service  
start "Book Service" cmd /k "call ..\venv\Scripts\activate && python -m uvicorn app.main:app --host 127.0.0.1 --port 8082 --reload"
cd ..

echo Waiting 4 seconds for Book Service...
timeout /t 4 /nobreak > nul

echo.
echo 📖 Starting Loan Service (Port 8081)...
cd loan-service
start "Loan Service" cmd /k "call ..\venv\Scripts\activate && python -m uvicorn app.main:app --host 127.0.0.1 --port 8081 --reload"
cd ..

echo.
echo Waiting 5 seconds for all services to fully start...
timeout /t 5 /nobreak > nul

echo.
echo 🔍 Checking service status...
netstat -an | findstr ":8080" && echo ✅ User Service running on 8080
netstat -an | findstr ":8081" && echo ✅ Loan Service running on 8081  
netstat -an | findstr ":8082" && echo ✅ Book Service running on 8082

echo.
echo 🌐 Starting API Gateway (Port 8000)...
echo.
echo ========================================
echo 🎯 CLEAN ENDPOINTS READY!
echo ========================================
echo.
echo 📍 Test these endpoints:
echo    http://localhost:8000/api/users
echo    http://localhost:8000/api/books
echo    http://localhost:8000/api/loans
echo    http://localhost:8000/health
echo.
echo 🚀 Starting API Gateway now...
python api_gateway.py
