# ⚡ SZYBKI START - 5 MINUT

## 1️⃣ Zainstaluj (1 min)

```bash
konfiguracja.bat
```

lub

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Uruchom Serwer (1 min)

```bash
uruchom_serwer.bat
```

lub

```bash
python app.py
```

**Powinieneś zobaczyć:**
```
Running on http://127.0.0.1:5000
```

---

## 3️⃣ Otwórz w Przeglądarce (1 min)

Otwórz plik: `loginpanel.html`

---

## 4️⃣ Zarejestruj się (1 min)

1. Kliknij "Zarejestruj się"
2. Wpisz:
   - Username: `michal`
   - Password: `haslo123`
   - Confirm: `haslo123`
3. Kliknij "Zarejestruj się"

---

## 5️⃣ Zaloguj się (1 min)

1. Wpisz dane:
   - Username: `michal`
   - Password: `haslo123`
2. Kliknij "Zaloguj się"
3. **GOTOWE!** 🎉

---

## 📊 Sprawdź Bazę Danych

```bash
python manage_db.py list
```

Zobaczysz:
```
=== WSZYSCY UŻYTKOWNICY ===

┌────┬──────────┬─────────────────────┐
│ ID │ Username │ Data rejestracji    │
├────┼──────────┼─────────────────────┤
│ 1  │ michal   │ 2026-01-26 10:30:00 │
└────┴──────────┴─────────────────────┘
```

---

## 🆘 Problemy?

### "Nie mogę się zalogować"
- Czy serwer jest uruchomiony? (`python app.py`)
- Czy port 5000 jest dostępny?
- Czy hasło jest prawidłowe?

### "Błąd podczas rejestracji"
- Nazwa użytkownika musi być unikalna
- Hasło min 6 znaków
- Hasła muszą się zgadzać

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

---

## 📚 Więcej Informacji

- `INSTRUKCJA.md` - Pełna dokumentacja
- `README_BAZA_DANYCH.md` - FAQ
- `schema.sql` - Schemat bazy danych
- `PODSUMOWANIE.md` - Podsumowanie

---

**Wszystko gotowe!** Zabawy z bazą danych! 🚀
