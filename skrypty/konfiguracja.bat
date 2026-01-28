@echo off
REM Instrukcja konfiguracji - Windows

cls
color 0A

echo.
echo ========================================
echo  KONFIGURACJA BAZY DANYCH UZYTKOWNIKOW
echo ========================================
echo.

REM Sprawdź czy Python jest zainstalowany
python --version >nul 2>&1
if errorlevel 1 (
    echo [BLAD] Python nie jest zainstalowany lub nie jest w PATH!
    echo Pobierz Python z: https://www.python.org/downloads/
    echo Podczas instalacji zaznacz: "Add Python to PATH"
    pause
    exit /b 1
)

echo [OK] Python znaleziony
python --version

echo.
echo Instalowanie pakietów wymaganych...
echo.

pip install -r requirements.txt

if errorlevel 1 (
    echo [BLAD] Instalacja pakietów nieudana!
    pause
    exit /b 1
)

echo.
echo [OK] Pakiety zainstalowane pomyslnie!
echo.
echo ========================================
echo  KONFIGURACJA GOTOWA!
echo ========================================
echo.
echo Aby uruchomic serwer, wykonaj:
echo   python app.py
echo.
echo Lub kliknij dwa razy: uruchom_serwer.bat
echo.
pause
