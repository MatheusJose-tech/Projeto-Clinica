@echo off
REM Muda o diretorio para a pasta onde o script esta
cd /d "%~dp0"

REM Executa o main.py (que está na pasta principal) 
pythonw.exe "%~dp0..\main.py"