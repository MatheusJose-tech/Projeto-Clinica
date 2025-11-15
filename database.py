import sqlite3
import datetime
import os
import logging

logs = logging.getLogger(__name__)

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
banco = os.path.join(diretorio_atual, "banco", "clinica.db")

def iniciar_banco():
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS maquinas(id_da_maquina TEXT PRIMARY KEY, data_ultima_troca TEXT)")

    cursor.execute("SELECT COUNT(*) FROM maquinas")
    contagem = cursor.fetchone()[0]

    if contagem == 0:
        logs.info("Realizando o processo de criar o Banco, por favor aguarde....")
        data_padrao = "2025-05-10"
        
        for i in range(1, 41):
            nome_maquina = f"Máquina {i:02d}"
            cursor.execute("INSERT INTO maquinas(id_da_maquina, data_ultima_troca) VALUES (?,?)", (nome_maquina, data_padrao))

        conexao.commit()
        logs.info("Banco gerado!")
    
    conexao.close()

def listar_todas_as_maquinas():
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()

    cursor.execute("SELECT id_da_maquina, data_ultima_troca FROM maquinas")

    maquinas = cursor.fetchall()
    conexao.close()
    return maquinas

def listar_para_a_interface():
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()

    cursor.execute("SELECT id_da_maquina FROM maquinas ORDER BY id_da_maquina")

    gui_id_maquina = cursor.fetchall()
    conexao.close()
    
    gui_id_maquina_limpa = [item[0] for item in gui_id_maquina]
    return gui_id_maquina_limpa

def trocar_data_maquina(maquina, data_especifica = None):
    
    if data_especifica:
        data_escolhida = data_especifica
        logs.info(f"Usando a data manual para a {maquina}")
    else:
        data_escolhida = datetime.date.today().strftime("%Y-%m-%d")
        logs.info(f"Usando a data de hoje para a {maquina}")

    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = "UPDATE maquinas SET data_ultima_troca = ? WHERE id_da_maquina = ?"

        cursor.execute(sql, (data_escolhida, maquina))
        conexao.commit()
        logs.info(f"Troca da data da Máquina {maquina} atualizada para data de {data_escolhida}")

        conexao.close()
        return True
    except Exception as e:
        logs.error(f"Erro na Máquina {maquina}: {e}", exc_info = True)
        return False

