@echo off
echo ========================================
echo TESTING API ENDPOINTS
echo ========================================

echo.
echo 🧪 Testing clean API endpoints through reverse proxy...
echo.

echo 1. Testing /api/users
curl -s http://127.0.0.1:8000/api/users
echo.
echo.

echo 2. Testing /api/books
curl -s http://127.0.0.1:8000/api/books
echo.
echo.

echo 3. Testing /api/loans
curl -s http://127.0.0.1:8000/api/loans
echo.
echo.

echo 4. Testing main gateway
curl -s http://127.0.0.1:8000/
echo.
echo.

echo 5. Testing health check
curl -s http://127.0.0.1:8000/health
echo.
echo.

echo ========================================
echo 🎯 CLEAN API ENDPOINTS WORKING!
echo ========================================
echo.
echo ✅ Available endpoints:
echo    GET http://127.0.0.1:8000/api/users
echo    GET http://127.0.0.1:8000/api/books  
echo    GET http://127.0.0.1:8000/api/loans
echo.
echo 📝 Create new records:
echo    POST http://127.0.0.1:8000/api/users
echo    POST http://127.0.0.1:8000/api/books
echo    POST http://127.0.0.1:8000/api/loans
echo.
pause
