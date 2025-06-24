@echo off
title Sinuca Delicia - Launcher

echo Iniciando Sinuca Delicia...
echo.

REM Verificar se Python esta instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python nao encontrado. Tentando python3...
    python3 --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo Erro: Python nao esta instalado no sistema.
        echo Por favor, instale Python para jogar Sinuca Delicia.
        echo Voce pode baixar em: https://www.python.org/downloads/
        pause
        exit /b 1
    ) else (
        set PYTHON_CMD=python3
    )
) else (
    set PYTHON_CMD=python
)

REM Verificar se pygame esta instalado
%PYTHON_CMD% -c "import pygame" >nul 2>&1
if %errorlevel% neq 0 (
    echo Pygame nao encontrado. Tentando instalar...
    pip install pygame
    if %errorlevel% neq 0 (
        echo Erro ao instalar pygame.
        echo Por favor, instale pygame manualmente: pip install pygame
        pause
        exit /b 1
    )
)

REM Navegar para o diretorio do jogo
cd /d "%~dp0"

REM Verificar se o arquivo do jogo existe
if not exist "em movimento sinuca.py" (
    echo Erro: Arquivo do jogo nao encontrado: em movimento sinuca.py
    pause
    exit /b 1
)

echo Executando o jogo...
echo Diretorio: %CD%
echo Comando: %PYTHON_CMD% "em movimento sinuca.py"
echo.

REM Executar o jogo
%PYTHON_CMD% "em movimento sinuca.py"

REM Verificar se o jogo foi executado com sucesso
if %errorlevel% equ 0 (
    echo.
    echo Jogo finalizado com sucesso!
) else (
    echo.
    echo Erro ao executar o jogo. Codigo de saida: %errorlevel%
    echo Verifique se todas as dependencias estao instaladas.
)

pause

