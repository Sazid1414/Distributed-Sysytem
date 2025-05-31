# Library Management System

## Overview
This project is a Library Management System, structured with both monolithic and microservices architectures:

- **Phase 1**: A monolithic application built with FastAPI.
---

## Phase 1: Monolithic Architecture

The monolithic version consists of a single FastAPI application with the following components:

### Directory Structure
```
Phase1/
├── .env                   # Environment variables
├── readme.md              # Documentation
├── requirements.txt       # Project dependencies
├── smart_library.db       # SQLite database
├── app/
│   ├── database.py        # Database connection and session management
│   ├── main.py            # Main FastAPI application entry point
│   ├── models.py          # SQLAlchemy ORM models
│   ├── schemas.py         # Pydantic schemas for request/response validation
│   ├── crud/              # Database CRUD operations
│   │   ├── books.py       # Book-related database operations
│   │   ├── loans.py       # Loan-related database operations
│   │   └── users.py       # User-related database operations
│   └── routers/           # API route definitions
│       ├── books.py       # Book-related endpoints
│       ├── loans.py       # Loan-related endpoints
│       ├── stats.py       # Statistics endpoints
│       └── users.py       # User-related endpoints
```

---

### API Endpoints

#### Users: `/api/users`
- **GET /** - List all users
- **GET /{user_id}** - Get user details
- **POST /** - Create a new user

#### Books: `/api/books`
- **GET /** - List/search books
- **GET /{book_id}** - Get book details
- **POST /** - Add a new book
- **PUT /{book_id}** - Update a book
- **DELETE /{book_id}** - Remove a book

#### Loans: `/api/loans`
- **POST /** - Issue a loan
- **POST /returns/** - Return a book

---

### Setting Up Phase 1

1. **Create a virtual environment**:
    ```bash
    python -m venv fastapi-env
    ```

2. **Activate the virtual environment**:
    - On Windows:
      ```bash
      fastapi-env\Scripts\activate
      ```
    - On Linux/macOS:
      ```bash
      source fastapi-env/bin/activate
      ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    uvicorn app.main:app --reload
    ```

5. **Access the API documentation**:
    - Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

---