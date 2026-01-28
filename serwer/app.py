# Import głównych komponentów Flask
from flask import Flask, request, jsonify, session
# Import obsługi CORS dla komunikacji między domenami
from flask_cors import CORS
# Import biblioteki do obsługi bazy danych SQLite
import sqlite3
# Import biblioteki do haszowania haseł
import hashlib
# Import biblioteki systemowej do operacji na plikach
import os
# Import do obsługi dat i czasu
from datetime import datetime

# Tworzenie instancji aplikacji Flask
app = Flask(__name__)
# Klucz sesji - powinien być zmieniony w produkcji
app.secret_key = 'your_secret_key_change_this'
# Konfiguracja CORS dla wszystkich endpointów
CORS(app, resources={r"/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})

# Ścieżka do bazy danych
DATABASE = 'users.db'

# Inicjalizacja bazy danych
def init_db():
    # Sprawdź czy plik bazy nie istnieje
    if not os.path.exists(DATABASE):
        # Połącz się z bazą danych
        conn = sqlite3.connect(DATABASE)
        # Utwórz kursor do wykonywania poleceń SQL
        c = conn.cursor()
        # Utwórz tabelę użytkowników
        c.execute('''CREATE TABLE users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,  # Auto-inkrementujące ID
                      username TEXT UNIQUE NOT NULL,  # Unikalna nazwa użytkownika
                      password TEXT NOT NULL,  # Hasło (zahaszowane)
                      role TEXT DEFAULT 'user',  # Rola użytkownika (domyślnie 'user')
                      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')  # Czas utworzenia
        # Zatwierdź zmiany w bazie
        conn.commit()
        # Zamknij połączenie z bazą
        conn.close()
        # Informacja o utworzeniu bazy
        print("Baza danych została utworzona!")

# Funkcja do haszowania hasła
def hash_password(password):
    # Zahashuj hasło algorytmem SHA256
    return hashlib.sha256(password.encode()).hexdigest()

# Funkcja do połączenia z bazą danych
def get_db():
    # Połącz z bazą danych
    conn = sqlite3.connect(DATABASE)
    # Ustaw fabrykę wierszy dla łatwiejszego dostępu do kolumn
    conn.row_factory = sqlite3.Row
    # Zwróć połączenie
    return conn

# Endpoint do rejestracji
@app.route('/api/register', methods=['POST'])  # Definicja trasy API dla rejestracji
def register():
    # Pobierz dane JSON z żądania
    data = request.get_json()
    # Wyodrębnij nazwę użytkownika
    username = data.get('username')
    # Wyodrębnij hasło
    password = data.get('password')
    # Wyodrębnij potwierdzenie hasła
    confirm_password = data.get('confirmPassword')

    # Walidacja
    # Sprawdź czy pola nie są puste
    if not username or not password:
        # Zwróć błąd 400
        return jsonify({'success': False, 'message': 'Nazwa użytkownika i hasło są wymagane'}), 400
    
    # Sprawdź czy hasła się zgadzają
    if password != confirm_password:
        # Zwróć błąd 400
        return jsonify({'success': False, 'message': 'Hasła nie pasują do siebie'}), 400
    
    # Sprawdź długość hasła
    if len(password) < 6:
        # Zwróć błąd 400
        return jsonify({'success': False, 'message': 'Hasło musi mieć co najmniej 6 znaków'}), 400

    # Próbuj wykonać operację bazodanową
    try:
        # Połącz z bazą danych
        conn = get_db()
        # Utwórz kursor
        c = conn.cursor()
        # Zahashuj hasło
        hashed_password = hash_password(password)
        # Wstaw nowego użytkownika
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                  (username, hashed_password))  # Parametry zapytania
        # Zatwierdź zmiany
        conn.commit()
        # Zamknij połączenie
        conn.close()
        # Sukces 201
        return jsonify({'success': True, 'message': 'Konto zostało założone! Możesz się teraz zalogować.'}), 201
    # Obsługa błędu unikalności nazwy
    except sqlite3.IntegrityError:
        # Błąd 400
        return jsonify({'success': False, 'message': 'Ta nazwa użytkownika już istnieje'}), 400
    # Obsługa innych błędów
    except Exception as e:
        # Błąd serwera 500
        return jsonify({'success': False, 'message': f'Błąd: {str(e)}'}), 500

# Endpoint do logowania
@app.route('/api/login', methods=['POST'])  # Definicja trasy API dla logowania
def login():
    # Pobierz dane JSON z żądania
    data = request.get_json()
    # Wyodrębnij nazwę użytkownika
    username = data.get('username')
    # Wyodrębnij hasło
    password = data.get('password')

    # Sprawdź czy pola nie są puste
    if not username or not password:
        # Błąd 400
        return jsonify({'success': False, 'message': 'Nazwa użytkownika i hasło są wymagane'}), 400

    # Próbuj wykonać operację logowania
    try:
        # Połącz z bazą danych
        conn = get_db()
        # Utwórz kursor
        c = conn.cursor()
        # Zahashuj hasło do porównania
        hashed_password = hash_password(password)
        # Znajdź użytkownika
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', 
                  (username, hashed_password))  # Parametry zapytania
        # Pobierz wynik
        user = c.fetchone()
        # Zamknij połączenie
        conn.close()

        # Jeśli użytkownik znaleziony
        if user:
            # Zapisz ID w sesji
            session['user_id'] = user['id']
            # Zapisz nazwę w sesji
            session['username'] = user['username']
            # Zapisz rolę w sesji
            session['role'] = user['role']
            # Sukces 200 z rolą użytkownika
            return jsonify({'success': True, 'message': 'Zalogowano pomyślnie', 'role': user['role']}), 200
        else:  # Jeśli użytkownik nie znaleziony
            # Błąd autoryzacji 401
            return jsonify({'success': False, 'message': 'Nieprawidłowa nazwa użytkownika lub hasło'}), 401
    # Obsługa błędów
    except Exception as e:
        # Błąd serwera 500
        return jsonify({'success': False, 'message': f'Błąd: {str(e)}'}), 500

# Endpoint do wylogowania
@app.route('/api/logout', methods=['POST'])  # Definicja trasy API dla wylogowania
def logout():
    # Wyczyść wszystkie dane sesji
    session.clear()
    # Sukces 200
    return jsonify({'success': True, 'message': 'Wylogowano pomyślnie'}), 200

# Endpoint do sprawdzenia statusu logowania
@app.route('/api/check-login', methods=['GET'])  # Definicja trasy API dla sprawdzania statusu
def check_login():
    # Sprawdź czy użytkownik jest zalogowany
    if 'user_id' in session:
        # Zalogowany - zwróć dane użytkownika
        return jsonify({
            'loggedIn': True, 
            'username': session['username'],
            'role': session.get('role', 'user')  # Domyślnie 'user' jeśli nie ma roli
        }), 200
    # Niezalogowany
    return jsonify({'loggedIn': False}), 200

# Endpoint do pobrania wszystkich użytkowników
@app.route('/api/users', methods=['GET'])  # Definicja trasy API dla pobierania użytkowników
def get_users():
    # Próbuj pobrać użytkowników
    try:
        # Połącz z bazą danych
        conn = get_db()
        # Utwórz kursor
        c = conn.cursor()
        # Pobierz wszystkich użytkowników
        c.execute('SELECT id, username, password, role, created_at FROM users ORDER BY created_at DESC')
        # Pobierz wyniki
        users = c.fetchall()
        # Zamknij połączenie
        conn.close()
        
        # Utwórz listę użytkowników
        users_list = []
        # Przetwarzaj każdego użytkownika
        for user in users:
            # Dodaj użytkownika do listy
            users_list.append({
                'id': user['id'],  # ID użytkownika
                'username': user['username'],  # Nazwa użytkownika
                'password': user['password'],  # Zahaszowane hasło
                'role': user['role'],  # Rola użytkownika
                'created_at': user['created_at']  # Czas utworzenia
            })
        
        # Zwróć listę użytkowników
        return jsonify({'success': True, 'users': users_list, 'count': len(users_list)}), 200
    # Obsługa błędów
    except Exception as e:
        # Błąd serwera 500
        return jsonify({'success': False, 'message': f'Błąd: {str(e)}'}), 500

# Endpoint do usuwania użytkownika
@app.route('/api/users/<int:user_id>', methods=['DELETE'])  # Definicja trasy API z parametrem ID
def delete_user(user_id):  # Funkcja przyjmuje ID użytkownika
    # Próbuj usunąć użytkownika
    try:
        # Połącz z bazą danych
        conn = get_db()
        # Utwórz kursor
        c = conn.cursor()
        
        # Sprawdź czy użytkownik istnieje
        c.execute('SELECT username FROM users WHERE id = ?', (user_id,))  # Znajdź użytkownika po ID
        # Pobierz wynik
        user = c.fetchone()
        
        # Jeśli użytkownik nie istnieje
        if not user:
            # Zamknij połączenie
            conn.close()
            # Błąd 404
            return jsonify({'success': False, 'message': 'Użytkownik nie istnieje'}), 404
        
        # Usuń użytkownika
        c.execute('DELETE FROM users WHERE id = ?', (user_id,))  # Usuń użytkownika
        # Zatwierdź zmiany
        conn.commit()
        # Zamknij połączenie
        conn.close()
        
        # Sukces 200
        return jsonify({'success': True, 'message': f'Użytkownik {user["username"]} został usunięty'}), 200
    # Obsługa błędów
    except Exception as e:
        # Błąd serwera 500
        return jsonify({'success': False, 'message': f'Błąd: {str(e)}'}), 500

# Uruchomienie aplikacji
if __name__ == '__main__':  # Jeśli skrypt uruchomiony bezpośrednio
    # Zainicjalizuj bazę danych
    init_db()
    # Uruchom aplikację Flask na porcie 5000 z debugowaniem
    app.run(debug=True, port=5000)
