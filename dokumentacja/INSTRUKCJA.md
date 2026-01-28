# 🎓 Kompletna Instrukcja - Baza Danych Użytkowników

## 📋 Spis Treści
1. [Szybki Start](#szybki-start)
2. [Struktura Bazy Danych](#struktura-bazy-danych)
3. [Instalacja](#instalacja)
4. [Uruchamianie](#uruchamianie)
5. [Zarządzanie Bazą](#zarządzanie-bazą)
6. [API Endpoints](#api-endpoints)
7. [Troubleshooting](#troubleshooting)

---

## 🚀 Szybki Start

### Dla niecierpliwych:

**1. Instalacja (raz)**
```bash
konfiguracja.bat
```
lub
```bash
pip install -r requirements.txt
```

**2. Uruchomienie serwera**
```bash
uruchom_serwer.bat
```
lub
```bash
python app.py
```

**3. Otwórz w przeglądarce**
```
loginpanel.html
```

**Gotowe!** 🎉

---

## 📊 Struktura Bazy Danych

### Diagram

```
┌─────────────────────────────────────┐
│          TABELA: users              │
├─────────────────────────────────────┤
│ id (INTEGER)                        │
│ ├─ PRIMARY KEY                      │
│ ├─ AUTO INCREMENT                   │
│ └─ Unikalna liczba dla każdego      │
│    użytkownika                      │
├─────────────────────────────────────┤
│ username (TEXT)                     │
│ ├─ UNIQUE                           │
│ ├─ NOT NULL                         │
│ └─ Nazwa użytkownika (login)        │
├─────────────────────────────────────┤
│ password (TEXT)                     │
│ ├─ NOT NULL                         │
│ ├─ SHA256 haszowane                 │
│ └─ Zazyfrowane hasło                │
├─────────────────────────────────────┤
│ created_at (TIMESTAMP)              │
│ ├─ DEFAULT: CURRENT_TIMESTAMP       │
│ └─ Data i czas rejestracji          │
└─────────────────────────────────────┘
```

### Przykładowe dane

```sql
┌────┬──────────────┬────────────────────────┬─────────────────────┐
│ id │   username   │       password         │     created_at      │
├────┼──────────────┼────────────────────────┼─────────────────────┤
│ 1  │ michal       │ 78a1c71d... (SHA256)   │ 2026-01-26 10:30:00 │
│ 2  │ anna         │ a1b2c3d4... (SHA256)   │ 2026-01-26 11:45:00 │
│ 3  │ tomasz       │ e5f6g7h8... (SHA256)   │ 2026-01-26 14:20:00 │
└────┴──────────────┴────────────────────────┴─────────────────────┘
```

---

## 💾 Instalacja

### Wymagania
- Python 3.7+
- Windows/Mac/Linux
- Git (opcjonalnie)

### Krok 1: Zainstaluj Python

1. Pobierz z: https://www.python.org/downloads/
2. Uruchom instalator
3. **WAŻNE**: Zaznacz "Add Python to PATH"
4. Kliknij "Install Now"

**Weryfikacja:**
```bash
python --version
```

### Krok 2: Zainstaluj pakiety

**Opcja A - Automatycznie (Windows):**
```bash
konfiguracja.bat
```

**Opcja B - Ręcznie:**
```bash
pip install -r requirements.txt
```

Weryfikacja:
```bash
pip list
```

---

## ⚙️ Uruchamianie

### Metoda 1: Dwuklik (Windows)
1. Otwórz folder projektu
2. Kliknij dwa razy `uruchom_serwer.bat`

### Metoda 2: Terminal
```bash
python app.py
```

### Oczekiwany output:
```
WARNING in app.runserver:
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Dostęp do aplikacji
- **Panel logowania**: `http://localhost/loginpanel.html` lub `file:///.../loginpanel.html`
- **Rejestracja**: Kliknij "Zarejestruj się"
- **Panel administracji**: `panel_bazy_danych.html`

---

## 🛠️ Zarządzanie Bazą

### Wyświetl użytkowników

```bash
python manage_db.py list
```

**Output:**
```
=== WSZYSCY UŻYTKOWNICY ===

╒════╤════════════════╤════════════════════════╕
│ ID │ Nazwa użytkownika │ Data rejestracji      │
╞════╪════════════════╪════════════════════════╡
│ 1  │ michal         │ 2026-01-26 10:30:00    │
│ 2  │ anna           │ 2026-01-26 11:45:00    │
╘════╧════════════════╧════════════════════════╛
```

### Dodaj użytkownika

```bash
python manage_db.py add michal haslo123
```

**Wymogi**:
- Nazwa: min 3 znaki
- Hasło: min 6 znaków
- Nazwa musi być unikalna

### Usuń użytkownika

```bash
python manage_db.py delete michal
```

### Policz użytkowników

```bash
python manage_db.py count
```

### Resetuj bazę (⚠️ NIEBEZPIECZNE!)

```bash
python manage_db.py reset
```

**To usunie WSZYSTKIE dane!**

---

## 🌐 API Endpoints

### Base URL
```
http://localhost:5000
```

### 1. Rejestracja

**POST** `/api/register`

**Request:**
```json
{
  "username": "michal",
  "password": "haslo123",
  "confirmPassword": "haslo123"
}
```

**Success Response (201):**
```json
{
  "success": true,
  "message": "Konto zostało założone! Możesz się teraz zalogować."
}
```

**Error Response (400):**
```json
{
  "success": false,
  "message": "Ta nazwa użytkownika już istnieje"
}
```

**Walidacja:**
- Nazwa użytkownika: wymagana, unikalna
- Hasła: muszą się zgadzać, min 6 znaków

---

### 2. Logowanie

**POST** `/api/login`

**Request:**
```json
{
  "username": "michal",
  "password": "haslo123"
}
```

**Success Response (200):**
```json
{
  "success": true,
  "message": "Zalogowano pomyślnie"
}
```

**Error Response (401):**
```json
{
  "success": false,
  "message": "Nieprawidłowa nazwa użytkownika lub hasło"
}
```

---

### 3. Wylogowanie

**POST** `/api/logout`

**Response (200):**
```json
{
  "success": true,
  "message": "Wylogowano pomyślnie"
}
```

---

### 4. Sprawdzenie Statusu

**GET** `/api/check-login`

**Zalogowany (200):**
```json
{
  "loggedIn": true,
  "username": "michal"
}
```

**Niezalogowany (200):**
```json
{
  "loggedIn": false
}
```

---

## 🧪 Testowanie

### Zainstaluj requests

```bash
pip install requests
```

### Uruchom testy

```bash
python test_api.py
```

**Przykład output:**
```
═════════════════════════════════════════════
     TESTY API BACKENDU UŻYTKOWNIKÓW
═════════════════════════════════════════════

=== TEST REJESTRACJI ===
Status: 201
Odpowiedź: {'success': True, 'message': '...'}

=== TEST LOGOWANIA - SUKCES ===
Status: 200
Odpowiedź: {'success': True, 'message': '...'}
```

---

## 🔐 Bezpieczeństwo

### Haszowanie Hasła

- **Algorytm**: SHA256
- **Salt**: Nie dodawany (wersja simple)
- **Przykład**:

```
Hasło: "haslo123"
SHA256: 3b78...8c42 (64 znaki hex)
```

**UWAGA**: Do produkcji użyj `bcrypt` lub `argon2`!

### Best Practices

- ✅ Hasła zawsze haszowane
- ✅ Nazwy unikalne
- ✅ Walidacja na backendu
- ✅ CORS security
- ✅ Session management

### Producja (TODO)

```python
# Zamiast SHA256:
from werkzeug.security import generate_password_hash, check_password_hash

# Hash
hashed = generate_password_hash('password')

# Verify
check_password_hash(hashed, 'password')
```

---

## 📁 Pliki Projektu

```
├── app.py                    ← Backend (Flask API)
├── loginpanel.html           ← Panel logowania
├── przyciskrejstracji.html   ← Panel rejestracji
├── panel_bazy_danych.html    ← Admin panel
├── manage_db.py              ← CLI do zarządzania
├── test_api.py               ← Testy
├── requirements.txt          ← Zależności
├── konfiguracja.bat          ← Setup (Windows)
├── uruchom_serwer.bat        ← Run server (Windows)
├── schema.sql                ← Schemat bazy
├── users.db                  ← Baza (auto-created)
├── README_BAZA_DANYCH.md     ← Dokumentacja
└── PODSUMOWANIE.md           ← Podsumowanie
```

---

## ❓ Troubleshooting

### Problem: "Błąd podczas logowania. Serwer backend nie jest uruchomiony"

**Rozwiązanie:**
1. Otwórz nowy terminal
2. Uruchom: `python app.py`
3. Sprawdź czy serwer działa na `http://localhost:5000`

### Problem: "ModuleNotFoundError: No module named 'flask'"

**Rozwiązanie:**
```bash
pip install -r requirements.txt
```

### Problem: "Port 5000 jest już w użyciu"

**Rozwiązanie (Windows PowerShell):**
```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Problem: "CORS error w przeglądarce"

**Rozwiązanie:**
- Upewnij się że `Flask-CORS` jest zainstalowany
- Sprawdź czy serwer na porcie 5000 jest włączony
- Otwórz konsolę przeglądarki (F12) i sprawdź błędy

### Problem: "Baza danych nie istnieje"

**Rozwiązanie:**
- Baza `users.db` jest tworzona automatycznie
- Jeśli problem: usuń `users.db` i uruchom `python app.py` ponownie

### Problem: "Hasło nieprawidłowe dla известного użytkownika"

**Rozwiązanie:**
- Hasła są wrażliwe na wielkość liter
- Sprawdź czy CapsLock nie jest włączony
- Zresetuj hasło usuwając użytkownika i rejestrując go ponownie

---

## 🎯 Następne Kroki

### Dla Produkcji

1. **Lepsze haszowanie hasła**
   ```bash
   pip install bcrypt
   ```

2. **SSL/HTTPS**
   ```bash
   pip install pyopenssl
   ```

3. **Baza danych**
   - Zmienić z SQLite na PostgreSQL/MySQL
   - Dodać backupy

4. **Security**
   - Dodać rate limiting
   - CSRF protection
   - SQL injection prevention

### Dodatkowe Funkcjonalności

- [ ] Reset hasła
- [ ] 2FA (Two Factor Auth)
- [ ] Email verification
- [ ] User profiles
- [ ] Admin panel
- [ ] Audit logs
- [ ] API keys

---

## 📞 Support

Jeśli masz problemy:

1. Sprawdź [Troubleshooting](#troubleshooting)
2. Przeczytaj error logs w terminalu
3. Otwórz DevTools w przeglądarce (F12)
4. Uruchom: `python test_api.py`

---

## 📄 Licencja

Projekt domowy do nauki.

---

**Powodzenia!** 🚀
