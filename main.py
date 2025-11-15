import logging
import os
import sys
import threading
import database
import relogio
import interface

# CRIANDO LOG

# Define o formato do log
log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
date_format = "%d/%m/%Y %H:%M:%S"

# Pega o diretorio atual para criar a clinica.log
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(diretorio_atual, "logs", "clinica.log")

logging.basicConfig(
    level=logging.INFO,             
    format=log_format,             
    datefmt=date_format,            
    handlers=[
        logging.FileHandler(log_file_path), # Escreve no arquivo 'clinica.log'
        # logging.StreamHandler(sys.stdout)   # Console
    ]
)

logging.info("Logging configurado.")

# Main 
if __name__ == "__main__":
    
    logging.info("Aplicação da Clínica iniciada.")

    try:
        logging.info("Configurando o Banco de dados...")
        database.iniciar_banco()
        logging.info("Banco de dados está operante!")
        logging.info("Iniciando a verificação das máquinas em segundo plano...")
        
        tarefa_relogio = threading.Thread(
            target=relogio.iniciar_loop_relogio,
            daemon=True
        )
        tarefa_relogio.start()
        
        logging.info("Iniciando o aplicativo...")
        interface.iniciar_aplicativo()
        
    except Exception as e:
        logging.critical(f"Falha crítica ao iniciar a aplicação: {e}", exc_info=True)
    os.system("cls")
    logging.info("Interface fechada. Encerrando a aplicação.")