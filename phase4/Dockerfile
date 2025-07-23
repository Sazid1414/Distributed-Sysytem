# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API Gateway code
COPY api_gateway.py .

# Set environment variables for Docker networking
ENV USER_SERVICE_URL=http://user-service:8080
ENV BOOK_SERVICE_URL=http://book-service:8082
ENV LOAN_SERVICE_URL=http://loan-service:8081

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "api_gateway:app", "--host", "0.0.0.0", "--port", "8000"]
