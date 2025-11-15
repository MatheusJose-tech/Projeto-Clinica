@echo off
REM %~dp0 é o caminho para a pasta 'instalação'
REM %~dp0.. é o caminho para a pasta principal (um nível acima)

REM Executa o main.py (que está na pasta principal) silenciosamente
pythonw.exe "%~dp0..\main.py"