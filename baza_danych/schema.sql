-- Baza danych użytkowników - Schemat SQL
-- SQLite

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indeks dla szybszego wyszukiwania po username
CREATE INDEX idx_username ON users(username);

-- Przykładowe zapytania

-- 1. Pobierz wszystkich użytkowników
SELECT id, username, created_at FROM users;

-- 2. Pobierz użytkownika po nazwie
SELECT * FROM users WHERE username = 'michal';

-- 3. Sprawdź czy użytkownik istnieje i hasło się zgadza
SELECT * FROM users WHERE username = 'michal' AND password = 'sha256_hash_hasla';

-- 4. Dodaj nowego użytkownika
INSERT INTO users (username, password) VALUES ('michal', 'sha256_hash_hasla');

-- 5. Usuń użytkownika
DELETE FROM users WHERE username = 'michal';

-- 6. Policz wszystkich użytkowników
SELECT COUNT(*) as liczba_uzytkownikow FROM users;

-- 7. Wyświetl ostatnio zarejestrowanych użytkowników
SELECT * FROM users ORDER BY created_at DESC LIMIT 10;

-- 8. Wyświetl użytkowników zarejestrowanych w ostatniej dobie
SELECT * FROM users WHERE created_at > datetime('now', '-1 day');

-- 9. Zmień hasło użytkownika
UPDATE users SET password = 'nowe_sha256_haslo' WHERE username = 'michal';

-- 10. Wyświetl statystykę rejestracji
SELECT 
    DATE(created_at) as dzien,
    COUNT(*) as liczba_rejestracji
FROM users 
GROUP BY DATE(created_at)
ORDER BY dzien DESC;
