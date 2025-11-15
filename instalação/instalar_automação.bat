@echo off
REM Este script copia o lançador lançar Painel.bat
REM para a pasta de inicialização do Windows

echo Instalando o 'Painel da Clinica' na inicialização...
echo.

REM Caminho da pasta de inicialização
SET STARTUP_FOLDER="%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

copy "%~dp0Lançar_Painel.bat" %STARTUP_FOLDER%

echo.
echo SUCESSO!
echo O 'Painel da Clinica' foi instalado.
echo.
echo Ele vai iniciar automaticamente da próxima vez que o computador ligar.
echo.
pause