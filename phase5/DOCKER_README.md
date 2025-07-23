# Docker Deployment Guide

This guide explains how to build and run the Distributed Library System using Docker containers.

## Prerequisites

- Docker Desktop installed and running
- Git Bash or Command Prompt

## Project Structure

```
phase4/
├── api_gateway.py                 # API Gateway service
├── requirements.txt               # Python dependencies
├── Dockerfile                     # API Gateway Dockerfile
├── build-docker-images.bat        # Script to build all images
├── run-docker-services.bat        # Script to run all containers
├── stop-docker-services.bat       # Script to stop all containers
├── user-service/
│   ├── Dockerfile                 # User service Dockerfile
│   ├── requirements.txt           # Service dependencies
│   ├── .env                       # Environment variables
│   └── app/                       # Application code
├── book-service/
│   ├── Dockerfile                 # Book service Dockerfile
│   ├── requirements.txt           # Service dependencies
│   ├── .env                       # Environment variables
│   └── app/                       # Application code
└── loan-service/
    ├── Dockerfile                 # Loan service Dockerfile
    ├── requirements.txt           # Service dependencies
    ├── .env                       # Environment variables
    └── app/                       # Application code
```

## Quick Start

### 1. Build All Docker Images

```cmd
build-docker-images.bat
```

This will build Docker images for:
- User Service
- Book Service  
- Loan Service
- API Gateway

### 2. Run All Services

```cmd
run-docker-services.bat
```

This will:
- Create a Docker network for inter-service communication
- Start all services in the correct order
- Map ports for external access

### 3. Access the Services

- **API Gateway**: http://localhost:8000/docs
- **User Service**: http://localhost:8080/docs
- **Book Service**: http://localhost:8082/docs
- **Loan Service**: http://localhost:8081/docs

### 4. Stop All Services

```cmd
stop-docker-services.bat
```

## Manual Docker Commands

If you prefer to run Docker commands manually:

### Build Images

```cmd
# User Service
cd user-service
docker build -t user-service:latest .
cd ..

# Book Service
cd book-service
docker build -t book-service:latest .
cd ..

# Loan Service
cd loan-service
docker build -t loan-service:latest .
cd ..

# API Gateway
docker build -t api-gateway:latest .
```

### Create Network

```cmd
docker network create library-network
```

### Run Containers

```cmd
# User Service
docker run -d --name user-service --network library-network -p 8080:8080 user-service:latest

# Book Service
docker run -d --name book-service --network library-network -p 8082:8082 book-service:latest

# Loan Service
docker run -d --name loan-service --network library-network -p 8081:8081 loan-service:latest

# API Gateway
docker run -d --name api-gateway --network library-network -p 8000:8000 api-gateway:latest
```

## Useful Docker Commands

### View Running Containers
```cmd
docker ps
```

### View Container Logs
```cmd
docker logs user-service
docker logs book-service
docker logs loan-service
docker logs api-gateway
```

### Access Container Shell
```cmd
docker exec -it user-service bash
```

### Stop Individual Containers
```cmd
docker stop user-service
docker stop book-service
docker stop loan-service
docker stop api-gateway
```

### Remove Containers
```cmd
docker rm user-service book-service loan-service api-gateway
```

### Remove Images
```cmd
docker rmi user-service:latest book-service:latest loan-service:latest api-gateway:latest
```

## Troubleshooting

### Port Already in Use
If you get port binding errors, make sure no other services are running on ports 8000, 8080, 8081, or 8082.

### Container Won't Start
Check the logs using `docker logs [container-name]` to see error messages.

### Network Issues
Make sure all containers are on the same network (`library-network`) for inter-service communication.

### Database Issues
The SQLite databases are created automatically when the services start. They are stored inside the containers and will be reset when containers are removed.

## Service Architecture

- **API Gateway** (Port 8000): Routes requests to appropriate services
- **User Service** (Port 8080): Manages user data and authentication
- **Book Service** (Port 8082): Manages book inventory
- **Loan Service** (Port 8081): Manages book loans and returns

All services run independently and communicate through HTTP APIs.
