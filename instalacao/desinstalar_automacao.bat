@echo off
REM Este script remove o Lancar_Painel.bat da pasta de inicializacao do Windows

echo Desinstalando o 'Painel da Clinica' da inicializacao...
echo.

SET STARTUP_FOLDER="%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

SET FILENAME="Lancar_Painel.bat"

REM Deleta o arquivo da pasta de inicialização
del %STARTUP_FOLDER%\%FILENAME%

echo.
echo SUCESSO!
echo O 'Painel da Clinica' foi removido da inicializacao.
echo.
pause