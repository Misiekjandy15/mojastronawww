"""
Testy API backendu
Uruchom: python test_api.py
"""

import requests
import json

API_URL = 'http://localhost:5000'

def test_register():
    """Test rejestracji nowego użytkownika"""
    print("\n=== TEST REJESTRACJI ===")
    
    data = {
        'username': 'testuser',
        'password': 'testpass123',
        'confirmPassword': 'testpass123'
    }
    
    response = requests.post(f'{API_URL}/api/register', json=data)
    print(f"Status: {response.status_code}")
    print(f"Odpowiedź: {response.json()}")

def test_register_duplicate():
    """Test rejestracji zduplikowanej nazwy"""
    print("\n=== TEST REJESTRACJI - DUPLIKAT ===")
    
    data = {
        'username': 'testuser',
        'password': 'testpass123',
        'confirmPassword': 'testpass123'
    }
    
    response = requests.post(f'{API_URL}/api/register', json=data)
    print(f"Status: {response.status_code}")
    print(f"Odpowiedź: {response.json()}")

def test_register_mismatched_password():
    """Test rejestracji z niezgodnym hasłem"""
    print("\n=== TEST REJESTRACJI - NIEZGODNE HASŁA ===")
    
    data = {
        'username': 'anotheruser',
        'password': 'pass123',
        'confirmPassword': 'pass456'
    }
    
    response = requests.post(f'{API_URL}/api/register', json=data)
    print(f"Status: {response.status_code}")
    print(f"Odpowiedź: {response.json()}")

def test_register_short_password():
    """Test rejestracji z krótkim hasłem"""
    print("\n=== TEST REJESTRACJI - KRÓTKIE HASŁO ===")
    
    data = {
        'username': 'shortpass',
        'password': '123',
        'confirmPassword': '123'
    }
    
    response = requests.post(f'{API_URL}/api/register', json=data)
    print(f"Status: {response.status_code}")
    print(f"Odpowiedź: {response.json()}")

def test_login_success():
    """Test zalogowania - sukces"""
    print("\n=== TEST LOGOWANIA - SUKCES ===")
    
    # Najpierw zarejestruj użytkownika
    register_data = {
        'username': 'logintest',
        'password': 'loginpass123',
        'confirmPassword': 'loginpass123'
    }
    requests.post(f'{API_URL}/api/register', json=register_data)
    
    # Teraz zaloguj się
    login_data = {
        'username': 'logintest',
        'password': 'loginpass123'
    }
    
    response = requests.post(f'{API_URL}/api/login', json=login_data)
    print(f"Status: {response.status_code}")
    print(f"Odpowiedź: {response.json()}")

def test_login_wrong_password():
    """Test zalogowania - błędne hasło"""
    print("\n=== TEST LOGOWANIA - BŁĘDNE HASŁO ===")
    
    login_data = {
        'username': 'testuser',
        'password': 'wrongpassword'
    }
    
    response = requests.post(f'{API_URL}/api/login', json=login_data)
    print(f"Status: {response.status_code}")
    print(f"Odpowiedź: {response.json()}")

def test_login_nonexistent_user():
    """Test zalogowania - użytkownik nie istnieje"""
    print("\n=== TEST LOGOWANIA - UŻYTKOWNIK NIE ISTNIEJE ===")
    
    login_data = {
        'username': 'nonexistent',
        'password': 'anypassword'
    }
    
    response = requests.post(f'{API_URL}/api/login', json=login_data)
    print(f"Status: {response.status_code}")
    print(f"Odpowiedź: {response.json()}")

def test_check_login():
    """Test sprawdzenia statusu logowania"""
    print("\n=== TEST SPRAWDZENIA LOGOWANIA ===")
    
    session = requests.Session()
    
    # Zaloguj się
    login_data = {
        'username': 'testuser',
        'password': 'testpass123'
    }
    session.post(f'{API_URL}/api/login', json=login_data)
    
    # Sprawdź status
    response = session.get(f'{API_URL}/api/check-login')
    print(f"Status: {response.status_code}")
    print(f"Odpowiedź: {response.json()}")

def main():
    print("╔══════════════════════════════════════════════╗")
    print("║     TESTY API BACKENDU UŻYTKOWNIKÓW         ║")
    print("╚══════════════════════════════════════════════╝")
    print(f"\nAdres API: {API_URL}")
    print("\nUpewnij się że serwer Flask jest uruchomiony!")
    
    try:
        # Test połączenia
        response = requests.get(f'{API_URL}/', timeout=2)
    except requests.ConnectionError:
        print("\n❌ BŁĄD: Nie można połączyć się z serwerem!")
        print(f"Serwer powinien być dostępny na {API_URL}")
        print("Uruchom: python app.py")
        return
    except Exception as e:
        print(f"\n⚠️ Ostrzeżenie: {e}")
    
    # Uruchom testy
    test_register()
    test_register_duplicate()
    test_register_mismatched_password()
    test_register_short_password()
    test_login_success()
    test_login_wrong_password()
    test_login_nonexistent_user()
    test_check_login()
    
    print("\n" + "="*50)
    print("Testy zakończone!")
    print("="*50)

if __name__ == '__main__':
    main()
