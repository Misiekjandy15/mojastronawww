# 📊 Baza Danych Użytkowników - Kompleksowy System

## 🎯 Przegląd Projektu

Kompletny system **rejestracji i logowania** z bazą danych SQLite. Projekt zawiera:

- ✅ Backend Flask z REST API
- ✅ Frontend HTML/CSS/JavaScript
- ✅ Baza danych SQLite
- ✅ Zarządzanie użytkownikami
- ✅ Haszowanie hasła SHA256
- ✅ Testy API
- ✅ Pełna dokumentacja

---

## 🚀 Szybki Start (5 minut)

### 1. Zainstaluj pakiety
```bash
pip install -r requirements.txt
```

### 2. Uruchom serwer
```bash
python app.py
```

### 3. Otwórz w przeglądarce
```
baza_danych_index.html
```

### 4. Zarejestruj się i zaloguj!

**Gotowe!** 🎉

---

## 📁 Struktura Plików

### 🔧 Backend
- **app.py** - Serwer Flask z API endpoints
- **requirements.txt** - Wymagane pakiety Python
- **test_api.py** - Testy API
- **manage_db.py** - Zarządzanie bazą CLI

### 🎨 Frontend
- **baza_danych_index.html** - Główna strona (START TUTAJ!)
- **loginpanel.html** - Panel logowania
- **przyciskrejstracji.html** - Panel rejestracji
- **panel_bazy_danych.html** - Admin panel

### 📚 Dokumentacja
- **SZYBKI_START.md** - Start w 5 minut
- **INSTRUKCJA.md** - Pełna dokumentacja
- **README_BAZA_DANYCH.md** - FAQ
- **PODSUMOWANIE.md** - Podsumowanie funkcji
- **schema.sql** - Schemat bazy danych

### ⚙️ Konfiguracja
- **konfiguracja.bat** - Setup (Windows)
- **uruchom_serwer.bat** - Run server (Windows)

### 📊 Baza Danych
- **users.db** - Plik bazy (tworzy się automatycznie)

---

## 📋 Tabela Bazy Danych

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL (SHA256),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Kolumny:**
- `id` - Unikalny identyfikator
- `username` - Nazwa użytkownika (unikalna)
- `password` - Hasło haszowane SHA256
- `created_at` - Data rejestracji

---

## 🌐 API Endpoints

| Metoda | Endpoint | Opis |
|--------|----------|------|
| POST | `/api/register` | Rejestracja nowego użytkownika |
| POST | `/api/login` | Logowanie użytkownika |
| POST | `/api/logout` | Wylogowanie |
| GET | `/api/check-login` | Sprawdzenie statusu |

---

## 🛠️ Zarządzanie Bazą Danych

### Wyświetl użytkowników
```bash
python manage_db.py list
```

### Dodaj użytkownika
```bash
python manage_db.py add username password
```

### Usuń użytkownika
```bash
python manage_db.py delete username
```

### Policz użytkowników
```bash
python manage_db.py count
```

### Resetuj bazę (⚠️ usuwa wszystko!)
```bash
python manage_db.py reset
```

---

## 🧪 Testowanie API

```bash
python test_api.py
```

Wyświetli testy dla:
- Rejestracji
- Logowania
- Walidacji
- Błędów

---

## 🔐 Bezpieczeństwo

- ✅ Hasła haszowane SHA256
- ✅ Nazwy unikalne
- ✅ Walidacja na backendu
- ✅ CORS skonfigurowany
- ✅ Session management

**Dla produkcji dodaj:**
- bcrypt/argon2 zamiast SHA256
- HTTPS/SSL
- Rate limiting
- Audit logs

---

## 📖 Dokumentacja

| Plik | Opis |
|------|------|
| SZYBKI_START.md | 5-minutowy przewodnik |
| INSTRUKCJA.md | Pełna dokumentacja |
| README_BAZA_DANYCH.md | Pytania i odpowiedzi |
| PODSUMOWANIE.md | Przegląd funkcji |
| schema.sql | Zapytania SQL |

---

## ❓ Problemy?

### "Błąd podczas logowania"
1. Sprawdź czy serwer jest uruchomiony (`python app.py`)
2. Sprawdź czy port 5000 jest dostępny
3. Przeczytaj INSTRUKCJA.md sekcję Troubleshooting

### "Port 5000 jest zajęty"
```bash
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Więcej pomocy
- Przeczytaj README_BAZA_DANYCH.md
- Przeczytaj INSTRUKCJA.md
- Uruchom `python test_api.py`

---

## 📊 Architektura

```
┌─────────────────────────────────────────┐
│          PRZEGLĄDARKA                   │
├─────────────────────────────────────────┤
│   loginpanel.html                       │
│   przyciskrejstracji.html               │
│   panel_bazy_danych.html                │
└─────────────────┬───────────────────────┘
                  │ HTTP JSON
                  │ (CORS)
                  ▼
┌─────────────────────────────────────────┐
│          BACKEND FLASK                  │
├─────────────────────────────────────────┤
│   app.py                                │
│   /api/register                         │
│   /api/login                            │
│   /api/logout                           │
│   /api/check-login                      │
└─────────────────┬───────────────────────┘
                  │ SQL
                  │
                  ▼
┌─────────────────────────────────────────┐
│       BAZA DANYCH (SQLite)              │
├─────────────────────────────────────────┤
│   users.db                              │
│   ├─ users table                        │
│   │  ├─ id (INTEGER, PK)                │
│   │  ├─ username (TEXT, UNIQUE)         │
│   │  ├─ password (TEXT, SHA256)         │
│   │  └─ created_at (TIMESTAMP)          │
│   └─ indeks na username                 │
└─────────────────────────────────────────┘
```

---

## 🎓 Technologia

- **Backend**: Python 3.7+, Flask, SQLite3
- **Frontend**: HTML5, CSS3, JavaScript ES6
- **API**: RESTful, JSON
- **Database**: SQLite3
- **Haszowanie**: SHA256

---

## 📦 Wymagania

- Python 3.7+
- Flask 2.3.2+
- Flask-CORS 4.0.0+
- SQLite3 (wbudowany w Python)

---

## 🎯 Następne Kroki

### Dla Nauki
- [ ] Zapoznaj się z INSTRUKCJA.md
- [ ] Uruchom test_api.py
- [ ] Przeanalizuj kod w app.py
- [ ] Spróbuj dodać nowe pole do bazy

### Dla Produkcji
- [ ] Zmień haszowanie na bcrypt
- [ ] Dodaj HTTPS
- [ ] Migraj na PostgreSQL
- [ ] Dodaj rate limiting
- [ ] Dodaj audit logs
- [ ] Wdróż na serwer

---

## 📞 Support

1. Przeczytaj dokumentację
2. Uruchom testy: `python test_api.py`
3. Sprawdź konsolę przeglądarki (F12)
4. Przeczytaj error logs w terminalu

---

## 📄 Licencja

Projekt edukacyjny.

---

## 🎉 Gotowy do Pracy!

**Zacznij tutaj:** Otwórz `baza_danych_index.html` 🚀

---

**Powodzenia!** ⭐

Jeśli projekt Ci się podoba, poświęć chwilę na zapoznanie się z dokumentacją aby w pełni zrozumieć architekturę systemu.
