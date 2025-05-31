
# Library Management System - Microservices Architecture

## Overview

This project implements a comprehensive Library Management System using a microservices architecture. The system consists of three core services that work together to provide a complete library management solution:

- **User Service**: Manages user accounts, authentication, and profile information
- **Book Service**: Handles book inventory, metadata, and availability tracking
- **Loan Service**: Orchestrates book borrowing and returns between users and books

The system enables library patrons to register accounts, browse the catalog, borrow and return books, and view their loan history. Librarians can manage the book inventory, track loans, and maintain the library system.

## Architecture

The application follows a microservices architecture pattern with the following components:

- **Nginx**: Acts as an API Gateway, providing a unified entry point and routing requests to appropriate services
- **User Service** (Port 8081): Dedicated to user management operations
- **Book Service** (Port 8082): Handles all book-related functionality
- **Loan Service** (Port 8083): Manages the relationships between users and books during lending processes

Each service has its own database and communicates with other services via HTTP when necessary.

## Technologies Used

- **FastAPI**: Modern, high-performance web framework for building APIs with Python
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library
- **Pydantic**: Data validation and settings management using Python type annotations
- **HTTPX**: Fully featured async HTTP client for service-to-service communication
- **Tenacity**: Retry library for implementing resilient inter-service communications
- **Nginx**: Reverse proxy and API gateway
- **PostgreSQL/SQLite**: Database options for data persistence

## Directory Structure

```
/Phase2
├── user-service/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py         # FastAPI application
│   │   ├── models.py       # SQLAlchemy models
│   │   ├── schemas.py      # Pydantic schemas
│   │   ├── crud.py         # Database operations
│   │   └── routers.py      # API endpoints
│   └── requirements.txt
├── book-service/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   └── routers.py
│   └── requirements.txt
├── loan-service/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   └── routers.py
│   └── requirements.txt
├── nginx/
│   └── library-services    # Nginx configuration
├── start_services.sh       # Service startup script
└── Readme.md               # This file
```

## Getting Started

### Prerequisites

- Python 3.10+
- Nginx
- PostgreSQL or SQLite

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/library-management.git
   cd library-management
   ```

2. Set up virtual environments and install dependencies for each service:
   ```bash
   # User Service
   cd user-service
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   deactivate
   
   # Book Service
   cd ../book-service
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   deactivate
   
   # Loan Service
   cd ../loan-service
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   deactivate
   ```

3. Install and configure Nginx:
   ```bash
   sudo apt update
   sudo apt install nginx
   ```

4. Create an Nginx configuration:
   ```bash
   sudo nano /etc/nginx/sites-available/library-services
   ```

5. Add the following configuration:
   ```nginx
   server {
       listen 80;
       server_name localhost;

       # User Service
       location /api/users {
           proxy_pass http://localhost:8081;
           proxy_http_version 1.1;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           
           # CORS headers
           add_header Access-Control-Allow-Origin '*';
           add_header Access-Control-Allow-Methods 'GET, POST, PUT, DELETE, PATCH, OPTIONS';
           add_header Access-Control-Allow-Headers 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization';
       }
       
       # Book Service
       location /api/books {
           proxy_pass http://localhost:8082;
           proxy_http_version 1.1;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           
           # CORS headers
           add_header Access-Control-Allow-Origin '*';
           add_header Access-Control-Allow-Methods 'GET, POST, PUT, DELETE, PATCH, OPTIONS';
           add_header Access-Control-Allow-Headers 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization';
       }
       
       # Loan Service
       location /api/loans {
           proxy_pass http://localhost:8083;
           proxy_http_version 1.1;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           
           # CORS headers
           add_header Access-Control-Allow-Origin '*';
           add_header Access-Control-Allow-Methods 'GET, POST, PUT, DELETE, PATCH, OPTIONS';
           add_header Access-Control-Allow-Headers 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization';
       }
       
       # API Documentation
       location /docs/users {
           proxy_pass http://localhost:8081/docs;
           proxy_http_version 1.1;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
       
       location /docs/books {
           proxy_pass http://localhost:8082/docs;
           proxy_http_version 1.1;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
       
       location /docs/loans {
           proxy_pass http://localhost:8083/docs;
           proxy_http_version 1.1;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
       
       # Health check endpoint
       location /health {
           return 200 'OK';
           add_header Content-Type text/plain;
       }
   }
   ```

6. Enable the configuration:
   ```bash
   sudo ln -s /etc/nginx/sites-available/library-services /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

## Running the Application

Create a startup script (`start_services.sh`) to run all three services:

```bash
#!/bin/bash

echo "Starting Library Management System..."

# Start User Service
cd user-service
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8081 &
deactivate
cd ..

# Start Book Service
cd book-service
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8082 &
deactivate
cd ..

# Start Loan Service
cd loan-service
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8083 &
deactivate

echo "All services started successfully!"
echo "API Gateway: http://localhost/"
echo ""
echo "API Documentation:"
echo "- User Service: http://localhost/docs/users"
echo "- Book Service: http://localhost/docs/books"
echo "- Loan Service: http://localhost/docs/loans"

wait
```

Make the script executable and run it:
```bash
chmod +x start_services.sh
./start_services.sh
```

## API Documentation

When the services are running, access the Swagger UI documentation at:

- **User Service**: http://localhost/docs/users
- **Book Service**: http://localhost/docs/books
- **Loan Service**: http://localhost/docs/loans

## Service Details

### User Service

Manages library patrons and staff accounts.

**Endpoints:**
- `POST /api/users/`: Register a new user
- `GET /api/users/{user_id}`: Get user details
- `PUT /api/users/{user_id}`: Update user details

**User Model:**
- `id`: Unique identifier
- `name`: User's full name
- `email`: User's email address (unique)
- `password_hash`: Hashed password for security
- `role`: User role (patron, librarian, admin)

### Book Service

Manages the library's book inventory.

**Endpoints:**
- `POST /api/books/`: Add a new book
- `GET /api/books/{book_id}`: Get book details
- `GET /api/books/`: Search books with filters
- `PUT /api/books/{book_id}`: Update book details
- `PATCH /api/books/{book_id}/availability`: Update book availability
- `DELETE /api/books/{book_id}`: Remove a book

**Book Model:**
- `id`: Unique identifier
- `title`: Book title
- `author`: Book author
- `isbn`: ISBN number
- `published_year`: Year of publication
- `genre`: Book genre
- `description`: Book description
- `total_copies`: Total copies owned by the library
- `available_copies`: Currently available copies

### Loan Service

Orchestrates book borrowing and returns.

**Endpoints:**
- `POST /api/loans/`: Issue a book to a user
- `POST /api/loans/returns/`: Process a book return
- `GET /api/loans/{loan_id}`: Get loan details
- `GET /api/loans/user/{user_id}`: Get user's loan history
- `PUT /api/loans/{loan_id}/extend`: Extend a loan's due date

**Loan Model:**
- `id`: Unique identifier
- `user_id`: User who borrowed the book
- `book_id`: Book that was borrowed
- `issue_date`: Date when the book was borrowed
- `due_date`: Date when the book should be returned
- `return_date`: Date when the book was actually returned (null if not returned)
- `status`: Current status (ACTIVE, RETURNED, OVERDUE)
- `extensions_count`: Number of times the loan has been extended

## Error Handling and Resilience

The system implements several resilience patterns:

1. **Retry Pattern**: Service-to-service communications use the Tenacity library to automatically retry failed requests, handling transient failures gracefully.

2. **Circuit Breaker**: The system detects when a service is failing and prevents cascading failures by failing fast.

3. **Timeout Handling**: All inter-service requests have appropriate timeouts to prevent blocking operations.

4. **Graceful Degradation**: If a non-critical service is unavailable, the system continues to function with reduced capabilities.

Example of resilience pattern implementation:
```python
@retry(stop=stop_after_attempt(3), wait=wait_fixed(1), retry=retry_if_exception_type(httpx.RequestError))
async def get_user(client: httpx.AsyncClient, user_id: int):
    try:
        response = await client.get(f"{USER_SERVICE_URL}/api/users/{user_id}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail="User not found")
        raise HTTPException(status_code=503, detail="User Service unavailable")
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="User Service unavailable")
```

## Future Enhancements

1. **Authentication & Authorization**: Implement JWT-based authentication
2. **Message Queue**: Replace direct HTTP calls with message queues for asynchronous communication
3. **Containerization**: Package each service as a Docker container
4. **Kubernetes Deployment**: Orchestrate services using Kubernetes
5. **Monitoring & Logging**: Implement ELK stack or Prometheus/Grafana
6. **CI/CD Pipeline**: Implement automated testing and deployment
7. **Notification Service**: Add email/SMS notifications for due dates, overdue books, etc.

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request


