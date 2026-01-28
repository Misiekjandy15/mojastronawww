# Struktura Projektu

## 📁 Organizacja Folderów

Projekt został zorganizowany w logiczne foldery z polskimi nazwami dla lepszej maintainability i czytelności kodu.

```
mojastronawww-main/
├── 🐍 serwer/                  # Serwer Flask (Python)
│   ├── app.py                 # Główna aplikacja Flask z API
│   └── requirements.txt        # Zależności Python
├── 🎨 strona/                  # Strony i style HTML/CSS
│   ├── strony_html/           # Pliki HTML stron
│   │   ├── index.html         # Strona główna
│   │   ├── pobierz.html       # Strona pobierania
│   │   ├── baza_danych_index.html # Indeks bazy danych
│   │   └── instrukcja.html     # Strona instrukcji
│   ├── style_css/             # Pliki CSS
│   │   └── style.css          # Główne style strony
│   └── zasoby/                # Zasoby (obrazy, ikony)
├── 🔐 logowanie/               # System autentykacji
│   ├── loginpanel.html         # Panel logowania
│   ├── loginpanel.css          # Style panelu logowania
│   ├── przyciskrejstracji.html # Panel rejestracji
│   └── przyciskrejstracji.css  # Style panelu rejestracji
├── 👨‍💼 panel_admina/            # Panel administracyjny
│   └── panel_bazy_danych.html  # Panel zarządzania użytkownikami
├── 📝 artykuly/                 # Artykuły o AI
│   ├── 5-zastosowan-ai-ktore-zmienia-twoje-zycie.html
│   ├── 5-zastosowan-ai-ktore-zmienia-twoje-zycie.css
│   ├── jak-ai-rewolucjonizuje-opieke-zdrowotna.html
│   ├── jak-ai-rewolucjonizuje-opieke-zdrowotna.css
│   ├── czy-ai-jest-zagrozeniem-dla-ludzkosci.html
│   └── czy-ai-jest-zagrozeniem-dla-ludzkosci.css
├── 📚 dokumentacja/            # Dokumentacja projektu
│   ├── README.md               # Główna dokumentacja
│   ├── README_BAZA_DANYCH.md   # Dokumentacja bazy danych
│   ├── SZYBKI_START.md         # Szybki start
│   ├── PODSUMOWANIE.md         # Podsumowanie projektu
│   ├── INSTRUKCJA.md            # Instrukcja obsługi
│   ├── PLIKI_PROJEKTU.txt      # Lista plików projektu
│   └── STRUKTURA_PROJEKTU.md   # Ta dokumentacja
├── 🧪 testy/                   # Pliki testowe
│   ├── test_role_system.html   # Test systemu ról
│   └── test_api.py              # Test API
├── ⚙️ skrypty/                 # Skrypty pomocnicze
│   ├── konfiguracja.bat        # Skrypt konfiguracyjny
│   ├── uruchom_serwer.bat      # Skrypt uruchamiający serwer
│   └── manage_db.py             # Zarządzanie bazą danych
├── 💾 baza_danych/             # Pliki bazy danych
│   ├── users.db                # Baza danych SQLite
│   └── schema.sql              # Schemat bazy danych
└── .git/                       # Kontrola wersji Git
```

## 🔗 Ścieżki i Linki

### Relatywne ścieżki w plikach HTML:

- **Strona główna** (`strona/strony_html/index.html`):
  - CSS: `../style_css/style.css`
  - Logowanie: `../logowanie/loginpanel.html`
  - Panel admina: `../panel_admina/panel_bazy_danych.html`
  - Artykuły: `../artykuly/nazwa-artykulu.html`

- **Panel logowania** (`logowanie/loginpanel.html`):
  - CSS: `loginpanel.css` (w tym samym folderze)
  - Rejestracja: `przyciskrejstracji.html` (w tym samym folderze)
  - Strona główna: `../strona/strony_html/index.html`

- **Panel rejestracji** (`logowanie/przyciskrejstracji.html`):
  - CSS: `loginpanel.css` (w tym samym folderze)
  - Logowanie: `loginpanel.html` (w tym samym folderze)

## 🎯 Zasady Organizacji

### 1. **Serwer** (`serwer/`)
- Wszystkie pliki Python/Flask
- Konfiguracja serwera
- Zależności projektu

### 2. **Strona** (`strona/`)
- **strony_html/**: Wszystkie pliki HTML
- **style_css/**: Wszystkie pliki CSS
- **zasoby/**: Obrazy, ikony, fonty

### 3. **Logowanie** (`logowanie/`)
- Wszystkie pliki związane z logowaniem i rejestracją
- Style dla paneli autentykacji

### 4. **Panel Admina** (`panel_admina/`)
- Panel administracyjny
- Zarządzanie użytkownikami

### 5. **Artykuły** (`artykuly/`)
- Wszystkie artykuły o AI
- Style dla artykułów

### 6. **Dokumentacja** (`dokumentacja/`)
- Wszystkie pliki dokumentacji
- Instrukcje i przewodniki

### 7. **Testy** (`testy/`)
- Pliki testowe
- Testy API i UI

### 8. **Skrypty** (`skrypty/`)
- Skrypty pomocnicze
- Automatyzacja

### 9. **Baza Danych** (`baza_danych/`)
- Pliki bazy danych
- Schematy i migracje

## 🔄 Przepływ Danych

1. **Użytkownik** → `logowanie/loginpanel.html` → `serwer/app.py` → `strona/strony_html/index.html`
2. **Admin** → `panel_admina/panel_bazy_danych.html` → `serwer/app.py` → Baza danych
3. **Artykuły** → `strona/strony_html/index.html` → `artykuly/*.html`

## 🚀 Uruchomienie

1. **Backend**: `cd serwer && python app.py`
2. **Frontend**: Otwórz `strona/strony_html/index.html` w przeglądarce
3. **Testy**: Otwórz `testy/test_role_system.html`

## 📝 Korzyści

- ✅ **Czytelność**: Łatwe znalezienie odpowiednich plików
- ✅ **Utrzymanie**: Logiczne grupowanie funkcjonalności
- ✅ **Skalowalność**: Łatwe dodawanie nowych funkcji
- ✅ **Teamwork**: Jasna struktura dla wielu deweloperów
- ✅ **Debugowanie**: Szybkie lokalizowanie problemów

## 🔧 Wskazówki

- Przy dodawaniu nowej funkcji, umieść pliki w odpowiednim folderze
- Utrzymuj spójność w nazewnictwie plików
- Aktualizuj dokumentację przy zmianach struktury
- Testuj ścieżki po przenoszeniu plików
