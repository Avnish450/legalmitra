@echo off
REM ============================================
REM  LegalMitra - one click launcher (Windows)
REM ============================================
title LegalMitra Server
echo.
echo  Starting LegalMitra...
echo.
python -m pip install -r requirements.txt --quiet
start "" http://127.0.0.1:5000
python app.py
pause
