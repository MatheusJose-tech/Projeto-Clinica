import os
from dotenv import load_dotenv

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# pegar as informações em  chave.env
chave = os.path.join(diretorio_atual, "segurança","chave.env")
load_dotenv(chave)

# Chaves de acesso para poder enviar os email
EMAIL = os.environ.get("EMAIL")
SENHA = os.environ.get("SENHA")
DESTINATARIO = os.environ.get("DESTINATARIO")