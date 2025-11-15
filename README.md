# ⚙️ Sistema de Monitoramento de Manutenção (Clínica IRRA)

Este projeto é um sistema de automação desenvolvido em Python para monitorar o ciclo de vida de equipamentos (diasafe) em 40 máquinas de hemodiálise. O sistema foi pensado para a **Clínica IRRA em Arapiraca-AL**.

O script roda em segundo plano, verificando continuamente as datas da última troca. Quando um equipamento vence (a cada 6 meses), o sistema envia automaticamente um e-mail de alerta consolidado para os responsáveis, garantindo que a manutenção ocorra no prazo.

## 🎯 Contexto do Projeto

Este software possui um duplo propósito:

1.  **Acadêmico:** Servir como um projeto de estudo e portfólio para o curso de Ciência da Computação na **Universidade Federal de Alagoas (UFAL)**.
2.  **Prático:** Ser uma ferramenta funcional para otimizar e automatizar o controle de manutenção na Clínica IRRA.

-----

## 📸 Visualização do Painel

A interface principal do aplicativo, onde o funcionário pode ver o status de todas as máquinas (com cores) e confirmar uma troca, podendo inserir uma data manual caso tenha esquecido de registrar no dia.

![Dashboard do Monitor da Clínica](painel.png)

-----

## ✨ Funcionalidades Principais

* **Automação em Background:** O script (`relogio.py`) roda em uma *thread* separada, monitorando as datas 24/7 sem interromper o usuário.
* **Dashboard de Status:** A interface (`interface.py`) funciona como um painel de controle, exibindo o status de todas as 40 máquinas com códigos de cores (vermelho, amarelo, verde).
* **Registro Manual de Data:** Permite ao usuário inserir uma data manualmente (formato AAAA-MM-DD) caso tenha esquecido de registrar a troca no dia exato.
* **Alertas por E-mail:** Envia um único e-mail consolidado (`correio.py`) com todas as máquinas vencidas e suas datas de vencimento.
* **Resiliência:** Se a verificação falhar (ex: internet cair), o robô tenta novamente em 1 hora, em vez de esperar 24h.
* **Logging:** Todas as ações (verificações, envios de e-mail, erros) são salvas em um arquivo `logs/clinica.log` para depuração.
* **Armazenamento Persistente:** Utiliza um banco de dados SQLite (`banco/clinica.db`) para armazenar o estado de todas as 40 máquinas.
* **Gerenciamento de Credenciais:** As senhas de e-mail são mantidas de forma segura fora do código, lendo um arquivo `chave.env` na pasta `segurança/`.

-----

## 🛠️ Ferramentas e Bibliotecas

* **Python 3.x**
* **Tkinter** (para a interface gráfica `interface.py`)
* **SQLite3** (para o banco de dados `database.py`)
* **smtplib** e `email.message` (para o envio dos e-mails)
* **threading** (para rodar a verificação e a GUI ao mesmo tempo)
* **python-dotenv** (para gerenciar as variáveis de ambiente)
* **python-dateutil** (para calcular facilmente os 6 meses de vencimento)
* **logging** (para o registro de eventos)

----

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos

Primeiro, clone este repositório para a sua máquina. 
```bash
git clone https://github.com/MatheusJose-tech/Projeto-Clinica.git
cd Projeto-Clinica
```

Em seguida, instale as dependências necessárias.

No arquivo `requirements.txt` terá as seguintes dependências para serem instaladas:
```txt
python-dotenv
python-dateutil
````

E rode no terminal:

```bash
pip install -r requirements.txt
```

### 2\. (MUITO IMPORTANTE) Configurando as Credenciais

Este projeto precisa de senhas para enviar e-mails. As credenciais são lidas da pasta `segurança/`.

**Passo 1:** Dentro de `segurança/`, crie um arquivo chamado `chave.env`.

**Passo 2:** Copie e cole o modelo abaixo dentro do seu `chave.env` e preencha com as suas credenciais:

```ini
# (Use o e-mail da sua prefêrencia para poder enviar os e-mails)
EMAIL="seu-email-bot@gmail.com"

# (Use a SENHA DE APP de 16 dígitos gerada pelo Google)
SENHA="suasenhadegesseisdigitos"

# (E-mail que vai RECEBER o alerta)
# (Se caso for mais de um E-mail é necessário colocar virgula após um E-mail digitado)
DESTINATARIO="email1@clinica.com, email2@clinica.com"
```

### 3\. Instalando a Automação (1 clique)

Para fazer o app iniciar sozinho junto com o Windows, basta dar um clique duplo no arquivo que estará dentro da pasta `instalacao/`:

`instalar_automacao.bat`

Isso irá copiar um atalho para a pasta de inicialização do Windows. O programa iniciará automaticamente na próxima vez que o computador ligar.

Caso não queira mais usar a automação, basta ir na mesma pasta `instalacao/` e clicar em: 
 
`desinstalar_automacao.bat`

Isso irá remover o atalho da pasta de inicialização do Windows.

### 4\. Rodando o Sistema Manualmente

Se não quiser instalar, você pode rodar o programa a qualquer momento.

**Não clique** no `main.py`. Em vez disso, clique no **`Lançar_Painel.bat`**.

Isso iniciará o `main.py` usando o `pythonw.exe` (modo silencioso), que irá abrir por momento um console preto, porém poderá fechar o console sem problemas.

-----

## 🛣️ Próximos Passos (Roadmap)

Embora o projeto esteja funcional, algumas melhorias futuras poderiam ser:

  * **Gerenciamento pela GUI:** Adicionar botões na interface para "Adicionar Nova Máquina" ou "Desativar Máquina".
  * **Gráficos Simples:** Criar uma nova aba na GUI que mostre um gráfico de quantas manutenções foram feitas por mês.
  * **Validação de Data:** Melhorar o campo de data manual para usar um "calendário" em vez de texto, evitando erros de digitação.

-----

## 📄 Licença

O código deste projeto está licenciado sob os termos do arquivo **[LICENSE.md](LICENSE)**.

-----

## 👥 Autores

  * **Matheus José**

      * Estudante de Ciência da Computação 2° Período
      * Universidade Federal de Alagoas (UFAL)

  * **Elias Custódio**

      * Colaborador do Projeto
      * Instituto Federal de Alagoas (IFAL)

<!-- end list -->

```
```
