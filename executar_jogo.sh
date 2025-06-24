#!/bin/bash

# Script para executar o jogo Sinuca Delícia
# Este script será chamado pelo site quando o usuário clicar em "Jogar Agora"

echo "Iniciando Sinuca Delícia..."

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Python3 não encontrado. Tentando python..."
    if ! command -v python &> /dev/null; then
        echo "Erro: Python não está instalado no sistema."
        echo "Por favor, instale Python para jogar Sinuca Delícia."
        read -p "Pressione Enter para continuar..."
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

# Verificar se pygame está instalado
$PYTHON_CMD -c "import pygame" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Pygame não encontrado. Tentando instalar..."
    pip install pygame
    if [ $? -ne 0 ]; then
        echo "Erro ao instalar pygame. Tentando com pip3..."
        pip3 install pygame
        if [ $? -ne 0 ]; then
            echo "Erro: Não foi possível instalar pygame."
            echo "Por favor, instale pygame manualmente: pip install pygame"
            read -p "Pressione Enter para continuar..."
            exit 1
        fi
    fi
fi

# Navegar para o diretório do jogo
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GAME_DIR="$SCRIPT_DIR/jogo"

if [ ! -d "$GAME_DIR" ]; then
    echo "Erro: Diretório do jogo não encontrado: $GAME_DIR"
    read -p "Pressione Enter para continuar..."
    exit 1
fi

cd "$GAME_DIR"

# Verificar se o arquivo do jogo existe
GAME_FILE="em movimento sinuca.py"
if [ ! -f "$GAME_FILE" ]; then
    echo "Erro: Arquivo do jogo não encontrado: $GAME_FILE"
    read -p "Pressione Enter para continuar..."
    exit 1
fi

echo "Executando o jogo..."
echo "Diretório: $GAME_DIR"
echo "Comando: $PYTHON_CMD \"$GAME_FILE\""

# Executar o jogo
$PYTHON_CMD "$GAME_FILE"

# Verificar se o jogo foi executado com sucesso
if [ $? -eq 0 ]; then
    echo "Jogo finalizado com sucesso!"
else
    echo "Erro ao executar o jogo. Código de saída: $?"
    echo "Verifique se todas as dependências estão instaladas."
fi

read -p "Pressione Enter para fechar..."

