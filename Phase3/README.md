# 🐳 Distributed System with Nginx Reverse Proxy

A microservices-based distributed system using Docker containers with Nginx as a reverse proxy.

## 🏗️ Architecture

```
Client → Nginx Reverse Proxy (Port 80) → Docker Containers
                                          ├── User Service (Port 8080)
                                          ├── Book Service (Port 8082)
                                          └── Loan Service (Port 8081)
```

## 🚀 Quick Start

### Start the entire system:
```cmd
docker-compose up --build
```

### Access the system:
- **Main Gateway**: http://localhost
- **Health Check**: http://localhost/health

### API Endpoints:
- **Users**: http://localhost/api/users
- **Books**: http://localhost/api/books
- **Loans**: http://localhost/api/loans

### Service Documentation:
- **Users**: http://localhost/docs/users
- **Books**: http://localhost/docs/books
- **Loans**: http://localhost/docs/loans

## 🛑 Stop the system:
```cmd
docker-compose down
```

## 🔧 Useful Commands

```cmd
# View logs
docker-compose logs -f

# View specific service logs
docker-compose logs nginx
docker-compose logs user-service

# Check container status
docker-compose ps

# Restart services
docker-compose restart
```

## 📁 Project Structure
```
Phase3/
├── docker-compose.yml      # Container orchestration
├── nginx.conf             # Nginx reverse proxy config
├── user-service/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
├── book-service/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
└── loan-service/
    ├── Dockerfile
    ├── requirements.txt
    └── app/
```

## 🔄 Technology Stack

- **Reverse Proxy**: Nginx (in Docker container)
- **Framework**: FastAPI
- **Database**: SQLite
- **Containerization**: Docker & Docker Compose
- **Architecture**: Microservices
