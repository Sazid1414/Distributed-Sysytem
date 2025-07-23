@echo off
echo ========================================
echo SIMPLE SERVICE TEST
echo ========================================

cd /d "d:\OneDrive\Documents\Distributed-Sysytem\Phase3"
call venv\Scripts\activate

echo.
echo Testing User Service startup...
cd user-service
echo Current directory: %CD%
echo Starting User Service...
python -m uvicorn app.main:app --host 127.0.0.1 --port 8080 --timeout-graceful-shutdown 1
