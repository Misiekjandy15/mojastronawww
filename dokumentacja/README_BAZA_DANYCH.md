# Baza danych - Instrukcja uruchamiania

## Konfiguracja

### 1. Zainstaluj Python (jeśli nie masz)
- Pobierz z: https://www.python.org/downloads/
- Zaznacz "Add Python to PATH" podczas instalacji

### 2. Zainstaluj wymagane pakiety
Otwórz terminal w folderze projektu i uruchom:

```bash
pip install -r requirements.txt
```

### 3. Uruchom serwer backend
```bash
python app.py
```

Serwer powinien uruchomić się na http://localhost:5000

### 4. Otwórz stronę w przeglądarce
```
http://localhost/loginpanel.html  (lub otwórz plik lokalnie)
```

## Struktura bazy danych

Baza danych SQLite zawiera tabelę `users` z następującymi polami:

- **id** - unikalny identyfikator (INTEGER, PRIMARY KEY, AUTO INCREMENT)
- **username** - nazwa użytkownika (TEXT, UNIQUE, NOT NULL)
- **password** - hasło (TEXT, NOT NULL, zahaszowane SHA256)
- **created_at** - data utworzenia konta (TIMESTAMP)

## Funkcjonalności

### Rejestracja
- Użytkownik wprowadza nazwę użytkownika, hasło i potwierdzenie hasła
- Walidacja: hasła muszą się zgadzać, minimalna długość 6 znaków
- Nazwa użytkownika musi być unikalna
- Hasło jest zahaszowane za pomocą SHA256

### Logowanie
- Użytkownik wprowadza nazwę użytkownika i hasło
- System sprawdza w bazie danych czy taki użytkownik istnieje
- Hasło jest sprawdzane przy użyciu haszowania

### Bezpieczeństwo
- Hasła są zahaszowane (SHA256)
- Nazwy użytkownika muszą być unikalne
- CORS jest skonfigurowany
- Sesja przechowuje dane zalogowanego użytkownika

## Pliki projektu

- `app.py` - Backend Flask z API
- `loginpanel.html` - Strona logowania
- `przyciskrejstracji.html` - Strona rejestracji
- `users.db` - Baza danych SQLite (tworzona automatycznie)
- `requirements.txt` - Wymagane pakiety Python

## Troubleshooting

### Błąd: "Błąd podczas logowania. Upewnij się, że serwer backend jest uruchomiony"
- Sprawdź czy serwer Flask jest uruchomiony na http://localhost:5000
- Uruchom `python app.py` w terminalu

### Błąd CORS
- Upewnij się że Flask-CORS jest zainstalowany: `pip install Flask-CORS`
- Sprawdź czy serwer jest uruchomiony na porcie 5000

### Baza danych nie istnieje
- Baza danych `users.db` jest tworzona automatycznie przy pierwszym uruchomieniu
- Jeśli chcesz ją zresetować, usuń plik `users.db` i uruchom ponownie serwer
