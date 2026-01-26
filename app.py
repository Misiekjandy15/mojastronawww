from flask import Flask, request, jsonify, session
from flask_cors import CORS
import sqlite3
import hashlib
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_change_this'
CORS(app, resources={r"/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})

# Ścieżka do bazy danych
DATABASE = 'users.db'

# Inicjalizacja bazy danych
def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''CREATE TABLE users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT UNIQUE NOT NULL,
                      password TEXT NOT NULL,
                      role TEXT DEFAULT 'user',
                      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()
        print("Baza danych została utworzona!")

# Funkcja do haszowania hasła
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Funkcja do połączenia z bazą danych
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Endpoint do rejestracji
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')

    # Walidacja
    if not username or not password:
        return jsonify({'success': False, 'message': 'Nazwa użytkownika i hasło są wymagane'}), 400
    
    if password != confirm_password:
        return jsonify({'success': False, 'message': 'Hasła nie pasują do siebie'}), 400
    
    if len(password) < 6:
        return jsonify({'success': False, 'message': 'Hasło musi mieć co najmniej 6 znaków'}), 400

    try:
        conn = get_db()
        c = conn.cursor()
        hashed_password = hash_password(password)
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                  (username, hashed_password))
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': 'Konto zostało założone! Możesz się teraz zalogować.'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'success': False, 'message': 'Ta nazwa użytkownika już istnieje'}), 400
    except Exception as e:
        return jsonify({'success': False, 'message': f'Błąd: {str(e)}'}), 500

# Endpoint do logowania
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'success': False, 'message': 'Nazwa użytkownika i hasło są wymagane'}), 400

    try:
        conn = get_db()
        c = conn.cursor()
        hashed_password = hash_password(password)
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', 
                  (username, hashed_password))
        user = c.fetchone()
        conn.close()

        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            return jsonify({'success': True, 'message': 'Zalogowano pomyślnie'}), 200
        else:
            return jsonify({'success': False, 'message': 'Nieprawidłowa nazwa użytkownika lub hasło'}), 401
    except Exception as e:
        return jsonify({'success': False, 'message': f'Błąd: {str(e)}'}), 500

# Endpoint do wylogowania
@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True, 'message': 'Wylogowano pomyślnie'}), 200

# Endpoint do sprawdzenia statusu logowania
@app.route('/api/check-login', methods=['GET'])
def check_login():
    if 'user_id' in session:
        return jsonify({'loggedIn': True, 'username': session['username']}), 200
    return jsonify({'loggedIn': False}), 200

# Endpoint do pobrania wszystkich użytkowników
@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT id, username, password, role, created_at FROM users ORDER BY created_at DESC')
        users = c.fetchall()
        conn.close()
        
        users_list = []
        for user in users:
            users_list.append({
                'id': user['id'],
                'username': user['username'],
                'password': user['password'],
                'role': user['role'],
                'created_at': user['created_at']
            })
        
        return jsonify({'success': True, 'users': users_list, 'count': len(users_list)}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f'Błąd: {str(e)}'}), 500

# Endpoint do usuwania użytkownika
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        conn = get_db()
        c = conn.cursor()
        
        # Sprawdź czy użytkownik istnieje
        c.execute('SELECT username FROM users WHERE id = ?', (user_id,))
        user = c.fetchone()
        
        if not user:
            conn.close()
            return jsonify({'success': False, 'message': 'Użytkownik nie istnieje'}), 404
        
        # Usuń użytkownika
        c.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'message': f'Użytkownik {user["username"]} został usunięty'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f'Błąd: {str(e)}'}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
