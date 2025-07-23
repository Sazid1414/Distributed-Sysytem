@echo off
echo ========================================
echo RUNNING DOCKER SERVICES
echo ========================================

echo Stopping any existing containers...
docker stop user-service book-service loan-service api-gateway 2>nul
docker rm user-service book-service loan-service api-gateway 2>nul

echo Creating Docker network for services...
docker network create library-network 2>nul

echo.
echo Starting User Service (Port 8080)...
docker run -d --name user-service --network library-network -p 8080:8080 user-service:latest

echo Starting Book Service (Port 8082)...
docker run -d --name book-service --network library-network -p 8082:8082 book-service:latest

echo Starting Loan Service (Port 8081)...
docker run -d --name loan-service --network library-network -p 8081:8081 loan-service:latest

timeout /t 5 /nobreak > nul

echo Starting API Gateway (Port 8000)...
docker run -d --name api-gateway --network library-network -p 8000:8000 api-gateway:latest

echo.
echo ========================================
echo ALL SERVICES STARTED
echo ========================================
echo.
echo ✅ Access your system at: http://localhost:8000
echo ✅ User Service: http://localhost:8080/docs
echo ✅ Book Service: http://localhost:8082/docs
echo ✅ Loan Service: http://localhost:8081/docs
echo ✅ API Gateway: http://localhost:8000/docs
echo.
echo To view logs: docker logs [container-name]
echo To stop all: docker stop user-service book-service loan-service api-gateway
