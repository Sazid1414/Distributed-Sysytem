import requests
import json

# Base URLs
USER_SERVICE = "http://127.0.0.1:8080"
BOOK_SERVICE = "http://127.0.0.1:8082" 
LOAN_SERVICE = "http://127.0.0.1:8081"

def test_services():
    print("🧪 Testing Distributed System Services...\n")
    
    # Test 1: Create a user
    print("1️⃣ Creating a user...")
    user_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "role": "student"
    }
    
    try:
        response = requests.post(f"{USER_SERVICE}/api/users/", json=user_data)
        if response.status_code == 201:
            user = response.json()
            print(f"✅ User created: {user['name']} (ID: {user['id']})")
            user_id = user['id']
        else:
            print(f"❌ Failed to create user: {response.status_code}")
            return
    except Exception as e:
        print(f"❌ Error creating user: {e}")
        return
    
    # Test 2: Create a book
    print("\n2️⃣ Creating a book...")
    book_data = {
        "title": "Python Programming",
        "author": "Test Author",
        "isbn": "1234567890123",
        "total_copies": 5
    }
    
    try:
        response = requests.post(f"{BOOK_SERVICE}/api/books/", json=book_data)
        if response.status_code == 201:
            book = response.json()
            print(f"✅ Book created: {book['title']} (ID: {book['id']})")
            book_id = book['id']
        else:
            print(f"❌ Failed to create book: {response.status_code}")
            return
    except Exception as e:
        print(f"❌ Error creating book: {e}")
        return
    
    # Test 3: Create a loan
    print("\n3️⃣ Creating a loan...")
    loan_data = {
        "user_id": user_id,
        "book_id": book_id,
        "due_date": "2026-07-22T14:02:57.791Z"
    }
    
    try:
        response = requests.post(f"{LOAN_SERVICE}/api/loans/", json=loan_data)
        if response.status_code == 201:
            loan = response.json()
            print(f"✅ Loan created: User {loan['user_id']} borrowed Book {loan['book_id']}")
            print(f"   Loan ID: {loan['id']}, Due: {loan['due_date']}")
        else:
            print(f"❌ Failed to create loan: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Error creating loan: {e}")
    
    print("\n🎉 Test complete!")

if __name__ == "__main__":
    test_services()
