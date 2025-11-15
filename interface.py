import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database
import datetime
from dateutil.relativedelta import relativedelta


def iniciar_aplicativo():
    janela = tk.Tk()
    janela.title("Controle de Trocas - Diasafe (Clínica IRRA)")
    janela.geometry("600x600")

    '''estilo = ttk.Style(janela)
    estilo.theme_use("clam")'''

    atualizar = ttk.Frame(janela)
    atualizar.pack(pady = 10, fill="x", padx= 10)
    
    def clique():
        escolha_maquina = lista_das_maquinas.get()
        if not escolha_maquina:
            messagebox.showwarning("Atenção", "Por favor, selecione uma máquina.")
            return

        data_manual = atualizar_data_manual.get()
        data_manual_confirmacao = f"Você confirma a troca para a {escolha_maquina}?"
        data_padrao = datetime.date.today()
        
        if data_manual:
            if len(data_manual) != 10 or data_manual[4] != '-' or data_manual[7] != '-':
                messagebox.showerror("Erro", "Formato de data inválido. Use AAAA-MM-DD.")
                return
            mensagem_confirmacao = f"Você confirma a troca para a {escolha_maquina} na data {data_manual}?"
        else:
            mensagem_confirmacao = f"Você confirma a troca para a {escolha_maquina} na data {data_padrao}?"
        
        confirmar = messagebox.askyesno("Confirmação", mensagem_confirmacao)

        if confirmar:
            if data_manual:
                sucesso = database.trocar_data_maquina(escolha_maquina, data_manual)
            else:
                sucesso = database.trocar_data_maquina(escolha_maquina)
            
            
            if sucesso:
                janela_status.config(text=f"{escolha_maquina} atualizada!", foreground="green")
                atualizar_aplicativo(janela_mestra_box)
                atualizar_data_manual.delete(0, tk.END)
            else:
                janela_status.config(text="Erro ao atualizar.", foreground="red")
        else:
            janela_status.config(text="Atualização cancelada.", foreground="orange")
    
    aviso = ttk.Label(atualizar, text="Selecione a máquina para confirmar a troca:")
    aviso.pack(fill="x")

    lista_do_combobox = database.listar_para_a_interface()
    lista_das_maquinas = ttk.Combobox(atualizar, values=lista_do_combobox,state="readonly", width=40)
    lista_das_maquinas.pack(pady=5, side=tk.LEFT,fill="x", expand= True)

    botao_para_atualizar = ttk.Button(atualizar,text="Confirmar Troca",command=clique)
    botao_para_atualizar.pack(pady=5, side=tk.RIGHT, padx=5)

    janela_status = ttk.Label(janela, text="")
    janela_status.pack(pady=5)

    janela_painel = ttk.Label(janela, text="Status de todas as máquinas:")
    janela_painel.pack(pady=(10, 0))

    atualizar_painel = ttk.Frame(janela)
    atualizar_painel.pack(fill="both",expand=True,padx=10,pady=10)


    janela_data_manual = ttk.Label(atualizar, text= "Data (opcional, AAAA-MM-DD):")
    janela_data_manual.pack(pady=5, side=tk.LEFT, padx=5)

    atualizar_data_manual = ttk.Entry(atualizar, width=15)
    atualizar_data_manual.pack(pady=5, side=tk.LEFT,padx=5)


    rolar = ttk.Scrollbar(atualizar_painel, orient=tk.VERTICAL)

    janela_mestra_box = tk.Listbox(atualizar_painel,yscrollcommand=rolar.set, font=("Courier", 10))
    rolar.config(command=janela_mestra_box.yview)

    rolar.pack(side=tk.RIGHT, fill=tk.Y)
    janela_mestra_box.pack(side=tk.LEFT, fill="both",expand=True)
    
    atualizar_aplicativo(janela_mestra_box)
    janela.mainloop()


def atualizar_aplicativo(janela_mestre):
    janela_mestre.delete(0, tk.END)

    data_hoje = datetime.date.today()

    lista_maquinas = database.listar_todas_as_maquinas()

    for (id_maquina, data_de_troca) in lista_maquinas:
        
        try:
            data_ultima_troca = datetime.datetime.strptime(data_de_troca, "%Y-%m-%d").date()
            data_vencimento = data_ultima_troca + relativedelta(months=+6)
            data_venc_formatado = data_vencimento.strftime("%d/%m/%Y")
             data_ultima_troca_formatada = data_ultima_troca.strftime("%d/%m/%Y")
    
            
            dias_restantes = (data_vencimento - data_hoje).days

            informacoes_maquina = f"{id_maquina}  |  Última Troca: {data_ultima_troca_formatada}  |  Vencimento: {data_venc_formatado}"

            janela_mestre.insert(tk.END, informacoes_maquina)

            if dias_restantes <= 0:
                # VENCIDO (Vermelho)
                janela_mestre.itemconfig(tk.END, {'bg':'#FFCCCC'}) 
            elif dias_restantes <= 30:
                # ALERTA (Amarelo)
                janela_mestre.itemconfig(tk.END, {'bg':'#FFFFCC'})
            else:
                # OK (Verde)
                janela_mestre.itemconfig(tk.END, {'bg':'#CCFFCC'})

        except Exception as e:
         janela_mestre.insert(tk.END, f"Erro ao processar {id_maquina}: {e}")
         janela_mestre.itemconfig(tk.END, {'bg':'#AAAAAA'})

