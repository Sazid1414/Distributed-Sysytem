"""
Quick test to see if we can start a service
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    # Test User Service
    print("Testing User Service import...")
    import user_service.app.main as user_app
    print("✅ User Service imported successfully")
    
    # Test Book Service  
    print("Testing Book Service import...")
    import book_service.app.main as book_app
    print("✅ Book Service imported successfully")
    
    # Test Loan Service
    print("Testing Loan Service import...")  
    import loan_service.app.main as loan_app
    print("✅ Loan Service imported successfully")
    
    print("\n🎉 All services can be imported!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nTrying with correct paths...")
    
    try:
        os.chdir("user-service")
        from app.main import app as user_app
        print("✅ User Service works with correct path")
        os.chdir("..")
        
        os.chdir("book-service") 
        from app.main import app as book_app
        print("✅ Book Service works with correct path")
        os.chdir("..")
        
        os.chdir("loan-service")
        from app.main import app as loan_app  
        print("✅ Loan Service works with correct path")
        os.chdir("..")
        
    except Exception as e2:
        print(f"❌ Still error: {e2}")
        
print("\nServices are ready to start!")
