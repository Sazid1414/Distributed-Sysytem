@echo off
echo ========================================
echo STOPPING DOCKER SERVICES
echo ========================================

echo Stopping all containers...
docker stop user-service book-service loan-service api-gateway

echo Removing all containers...
docker rm user-service book-service loan-service api-gateway

echo Removing network...
docker network rm library-network

echo.
echo ========================================
echo ALL SERVICES STOPPED AND CLEANED UP
echo ========================================
