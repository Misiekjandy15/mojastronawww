#!/usr/bin/env python3
"""
Skrypt zarządzania bazą danych użytkowników
"""

import sqlite3
import hashlib
from tabulate import tabulate
import os

DATABASE = 'users.db'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def get_all_users():
    """Wyświetl wszystkich użytkowników"""
    if not os.path.exists(DATABASE):
        print("Baza danych nie istnieje!")
        return
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT id, username, password, role, created_at FROM users')
    users = c.fetchall()
    conn.close()
    
    if users:
        print("\n=== WSZYSCY UŻYTKOWNICY ===\n")
        # Przygotuj dane do wyświetlenia
        data = []
        for user in users:
            user_id, username, password_hash, role, created_at = user
            # Pokaż tylko pierwszy 15 znaków haszu
            password_preview = password_hash[:15] + "..." if len(password_hash) > 15 else password_hash
            data.append([user_id, username, password_preview, role, created_at])
        
        headers = ['ID', 'Username', 'Hasło (SHA256)', 'Rola', 'Data rejestracji']
        print(tabulate(data, headers=headers, tablefmt='grid'))
    else:
        print("Brak użytkowników w bazie danych")

def delete_user(username):
    """Usuń użytkownika"""
    if not os.path.exists(DATABASE):
        print("Baza danych nie istnieje!")
        return
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE username = ?', (username,))
    
    if c.rowcount > 0:
        conn.commit()
        print(f"Użytkownik '{username}' został usunięty")
    else:
        print(f"Użytkownik '{username}' nie znaleziony")
    
    conn.close()

def add_user(username, password, role='user'):
    """Dodaj użytkownika ręcznie"""
    if not os.path.exists(DATABASE):
        print("Baza danych nie istnieje! Uruchom najpierw app.py")
        return
    
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        hashed_password = hash_password(password)
        c.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', 
                  (username, hashed_password, role))
        conn.commit()
        conn.close()
        print(f"Użytkownik '{username}' został dodany pomyślnie (Rola: {role})")
    except sqlite3.IntegrityError:
        print(f"Błąd: Użytkownik '{username}' już istnieje")

def reset_database():
    """Resetuj bazę danych"""
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
        print("Baza danych została usunięta")
    else:
        print("Baza danych nie istnieje")

def count_users():
    """Policz użytkowników"""
    if not os.path.exists(DATABASE):
        print("Baza danych nie istnieje!")
        return
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM users')
    count = c.fetchone()[0]
    conn.close()
    
    print(f"\nLiczba użytkowników w bazie: {count}")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("""
Zarządzanie bazą danych użytkowników
=====================================

Użycie:
  python manage_db.py list              - Wyświetl wszystkich użytkowników
  python manage_db.py add <user> <pass> [role] - Dodaj nowego użytkownika
  python manage_db.py delete <user>     - Usuń użytkownika
  python manage_db.py count             - Policz użytkowników
  python manage_db.py reset             - Resetuj bazę danych

Role: 'user' (domyślnie) lub 'admin'
        """)
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'list':
        get_all_users()
    elif command == 'count':
        count_users()
    elif command == 'add':
        if len(sys.argv) < 4:
            print("Błąd: Użycie: python manage_db.py add <username> <password> [role]")
            sys.exit(1)
        role = sys.argv[4] if len(sys.argv) > 4 else 'user'
        add_user(sys.argv[2], sys.argv[3], role)
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Błąd: Użycie: python manage_db.py delete <username>")
            sys.exit(1)
        delete_user(sys.argv[2])
    elif command == 'reset':
        confirm = input("Jesteś pewny? (yes/no): ")
        if confirm.lower() == 'yes':
            reset_database()
    else:
        print(f"Nieznane polecenie: {command}")
