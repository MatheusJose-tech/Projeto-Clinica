from senhas import EMAIL, SENHA, DESTINATARIO
import smtplib
from email.message import EmailMessage
import datetime
import logging

logs = logging.getLogger(__name__)


def enviar_email(maquinas_vencidas):
    msg = EmailMessage()

    msg['Subject'] = "ALERTA: Manutenção de Máquinas Pendente"
    msg['From'] = EMAIL
    msg['To'] = DESTINATARIO
    corpo_email = f"Atenção Usuário!\n\nAs seguintes máquinas estão com a manutenção vencida e precisam de troca urgente do 'diasafe':\n\n"
    
    for (maquina, data) in maquinas_vencidas:
        data_vencimento = data.strftime("%d/%m/%Y")

        corpo_email += f"- {maquina}, próximo vencimento do diasafe: {data_vencimento}\n"
        
    corpo_email += "\nPor favor, realizar a manutenção e atualizar o sistema."

    msg.set_content(corpo_email)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL, SENHA)
            smtp.send_message(msg)
            logs.info("Email de Aviso enviado com sucesso!")
    except Exception as e:
        logs.error(f"ERRO: {e}", exc_info = True)
