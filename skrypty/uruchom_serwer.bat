@echo off
REM Skrypt do uruchomienia serwera backendu

echo ========================================
echo Uruchamianie serwera backendu...
echo ========================================
echo.
echo Serwer bedzie dostepny na: http://localhost:5000
echo.
echo Aby zatrzymac serwer, nacisnij CTRL+C
echo.

cd ..\serwer
python app.py

pause
