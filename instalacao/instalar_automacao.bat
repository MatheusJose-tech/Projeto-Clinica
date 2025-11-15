@echo off
REM ESTE SCRIPT DEVE SER EXECUTADO DE DENTRO DA PASTA INSTALACAO/

echo Instalando o 'Painel da Clinica' na inicialização...
echo.

REM 1. Define o caminho ABSOLUTO da pasta principal do projeto (um nível acima)
SET PROJECT_ROOT=%~dp0..

SET STARTUP_FOLDER="%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
SET TARGET_NAME=Lancar_Painel.bat
SET TARGET_PATH=%STARTUP_FOLDER%\%TARGET_NAME%

echo Escrevendo o arquivo de inicialização...

REM 2. Escreve a PRIMEIRA linha no arquivo final (cria o arquivo)
REM O comando CD /D força o prompt a mudar para a pasta do projeto
ECHO @echo off > %TARGET_PATH%
ECHO cd /d ""%PROJECT_ROOT%"" >> %TARGET_PATH%

REM 3. Escreve a SEGUNDA linha no arquivo final (executa o main.py)
ECHO pythonw.exe main.py >> %TARGET_PATH%

echo.
echo SUCESSO!
echo O "Painel da Clinica" foi instalado e será iniciado com o Windows.
echo.
pause