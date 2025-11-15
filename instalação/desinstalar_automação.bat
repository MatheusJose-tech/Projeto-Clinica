@echo off
REM Este script remove o Lançar_Painel.bat da pasta de inicialização do Windows

echo Desinstalando o 'Painel da Clinica' da inicialização...
echo.

REM Define o caminho da pasta de inicialização
SET STARTUP_FOLDER="%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

SET FILENAME="Lançar_Painel.bat"

REM Deleta o arquivo Lançar_Painel.bat da pasta de inicialização
del %STARTUP_FOLDER%\%FILENAME%

echo.
echo SUCESSO!
echo O 'Painel da Clinica' foi removido da inicialização.
echo.
echo.
pause