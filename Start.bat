@echo off
cd /d C:\Users\Desk-032\tts_project

echo Iniciando IA...
start cmd /k ollama run mistral

timeout /t 3 > nul

call tts_env\Scripts\activate.bat
tts_env\Scripts\python.exe IA_Companheira.py

pause