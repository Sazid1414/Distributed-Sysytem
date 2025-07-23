@echo off
echo ========================================
echo BUILDING DOCKER IMAGES
echo ========================================

echo Building User Service Docker Image...
cd user-service
docker build -t user-service:latest .
cd ..

echo Building Book Service Docker Image...
cd book-service
docker build -t book-service:latest .
cd ..

echo Building Loan Service Docker Image...
cd loan-service
docker build -t loan-service:latest .
cd ..

echo Building API Gateway Docker Image...
docker build -t api-gateway:latest .

echo.
echo ========================================
echo ALL IMAGES BUILT SUCCESSFULLY
echo ========================================
echo.
echo To run the services, use the run-docker-services.bat script
