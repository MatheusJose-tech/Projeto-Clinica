import database
import correio
import datetime
import time
from dateutil.relativedelta import relativedelta
import logging

logs = logging.getLogger(__name__)

def verificacao_maquinas():
    logs.info(f"Iniciando a verificação dos vencimentos das máquinas....")
    maquinas_vencidas = []
    data_de_hoje = datetime.date.today()

    lista_das_maquinas = database.listar_todas_as_maquinas()

    if not lista_das_maquinas:
        logs.info("Nenhuma máquina encontrada!")
        return
    
    for (id_maquina, data_de_troca) in lista_das_maquinas:
        try:
            data_ultima_troca = datetime.datetime.strptime(data_de_troca, "%Y-%m-%d").date()
            data_vencimento = data_ultima_troca + relativedelta(months=+6)

            if data_de_hoje >= data_vencimento:
                vencimento = (id_maquina, data_vencimento)
                maquinas_vencidas.append(vencimento)


        except Exception as e:
         logs.info(f"Erro em calcular a data da máquina {id_maquina}: {e}")
    
    if len(maquinas_vencidas) > 0:
        logs.info("ALERTA!")
        logs.info(f"Foram encontradas {len(maquinas_vencidas)} máquinas vencidas!")
        correio.enviar_email(maquinas_vencidas)
    else:
        logs.info("Nenhuma máquina vencida encontrada!")

def iniciar_loop_relogio():
    while True:
        try:
            verificacao_maquinas()
            desligar = 60*60*24
                 
        except Exception as e:
            logs.error(f"Erro inesperado no loop do relógio: {e}", exc_info = True)
            logs.error(f"iniciando os procedimentos de contenção....", exc_info = True)
            desligar = 60 * 60 # Verificação em 1h 


        logs.info(f"Verificação concluída. Próxima verificação em {desligar//3600} horas.")
        time.sleep(desligar)
