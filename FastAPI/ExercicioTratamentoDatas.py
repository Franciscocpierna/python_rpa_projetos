# Importa o módulo tkinter para criação de interface gráfica.
import tkinter as tk

# Importa o módulo messagebox do tkinter para exibir
        # mensagens de erro e alertas.
from tkinter import messagebox

# Importa o módulo ttk do tkinter para uso de widgets que
        # seguem o tema do sistema operacional.
from tkinter import ttk

# Importa o módulo scrolledtext do tkinter para criar uma área de
        # texto com barras de rolagem integradas.
from tkinter import scrolledtext

# Importa o módulo requests para fazer requisições HTTP.
import requests

# Define a URL base da API para facilitar as requisições futuras.
API_URL = "http://127.0.0.1:8000"


# Define a função testar_conexao que verifica a acessibilidade da API.
def testar_conexao():

    try:

        # Tenta obter uma resposta da API acessando o endpoint de documentação.
        resposta = requests.get(f"{API_URL}/docs")

        # Verifica o código de status da resposta, se 200, a conexão é bem-sucedida.
        if resposta.status_code == 200:

            messagebox.showinfo("Conexão", "Conexão com a API bem-sucedida!")

        else:

            # Se o código de status não for 200, informa uma falha na conexão.
            messagebox.showerror("Conexão", "Falha na conexão com a API.")

    except requests.exceptions.RequestException as e:

        # Captura exceções relacionadas à requisição e exibe uma mensagem de erro.
        messagebox.showerror("Erro", f"Erro ao se conectar à API:\n{e}")


# Define a função calcular_idade para calcular a idade de uma
# pessoa a partir da sua data de nascimento.
def calcular_idade():

    # Obtém o valor do campo de entrada para data de nascimento.
    data_nascimento = entrada_data_nascimento.get()

    # Verifica se o campo de data de nascimento está vazio.
    if not data_nascimento:

        # Mostra uma mensagem de erro se o campo estiver vazio.
        messagebox.showerror("Erro", "Por favor, insira a data de nascimento no formato DD/MM/AAAA.")

        # Sai da função para evitar mais execução.
        return

    try:

        # Faz uma requisição POST para a API para calcular a idade,
        # enviando a data de nascimento como JSON.
        resposta = requests.post(f"{API_URL}/calcular-idade/", json={

            # A data inserida pelo usuário.
            "data_nascimento": data_nascimento,

            # O formato esperado pela API.
            "formato": "%d/%m/%Y"

        })

        # Verifica se a requisição foi bem-sucedida. Se houver erro, gera uma exceção.
        resposta.raise_for_status()

        # Converte a resposta JSON da API em um dicionário Python.
        dados = resposta.json()

        # Configura a área de texto para mostrar a idade para permitir edição.
        area_resultado_idade.config(state="normal")

        # Limpa a área de texto onde a idade será mostrada.
        area_resultado_idade.delete("1.0", tk.END)

        # Insere a idade calculada na área de texto.
        area_resultado_idade.insert(tk.END, f"Idade: {dados['idade']} anos")

        # Desabilita a área de texto após inserir a idade para evitar edições.
        area_resultado_idade.config(state="disabled")

    except requests.exceptions.RequestException as e:

        # Se houver problemas na conexão com a API,
        # mostra uma mensagem de erro.
        messagebox.showerror("Erro", f"Erro ao se conectar à API:\n{e}")


# Define a função diferenca_datas para calcular a
# diferença entre duas datas.
def diferenca_datas():

    # Obtém as datas de início e fim a partir dos campos de
    # entrada na interface gráfica.
    data_inicio = entrada_data_inicio.get()
    data_fim = entrada_data_fim.get()

    # Verifica se algum dos campos está vazio.
    if not data_inicio or not data_fim:

        # Mostra uma mensagem de erro caso uma ou ambas as
        # datas não sejam inseridas.
        messagebox.showerror("Erro", "Por favor, insira ambas as datas no formato DD/MM/AAAA.")

        # Encerra a execução da função se as datas não forem fornecidas.
        return

    try:

        # Realiza uma requisição POST para a API, enviando as datas de início e fim.
        resposta = requests.post(f"{API_URL}/diferenca-entre-datas/", json={

            "data_inicio": data_inicio,  # Data de início inserida pelo usuário.
            "data_fim": data_fim,  # Data de fim inserida pelo usuário.
            "formato": "%d/%m/%Y"  # Formato das datas conforme esperado pela API.

        })

        # Verifica se houve algum erro na requisição HTTP.
        resposta.raise_for_status()

        # Converte a resposta JSON da API em um dicionário Python.
        dados = resposta.json()

        # Extrai a diferença entre as datas do dicionário de resposta.
        diferenca = dados["diferenca"]

        # Configura a área de texto para mostrar a diferença para permitir edição.
        area_resultado_diferenca.config(state="normal")

        # Limpa qualquer conteúdo anterior na área de texto.
        area_resultado_diferenca.delete("1.0", tk.END)

        # Insere a diferença calculada na área de texto.
        area_resultado_diferenca.insert(
            tk.END,
            f"Diferença: {diferenca['dias']} dias, {diferenca['meses']} meses, {diferenca['anos']} anos"
        )

        # Desabilita a área de texto para prevenir edições após inserir o resultado.
        area_resultado_diferenca.config(state="disabled")

    except requests.exceptions.RequestException as e:

        # Se houver um erro de conexão com a API, mostra uma
        # mensagem de erro ao usuário.
        messagebox.showerror("Erro", f"Erro ao se conectar à API:\n{e}")


# Define a função data_por_extenso que é responsável por converter uma
# data em formato numérico para o formato por extenso.
def data_por_extenso():

    # Obtém a data inserida pelo usuário no campo de entrada
    # específico na interface gráfica.
    data = entrada_data_extenso.get()

    # Verifica se o campo de entrada está vazio.
    if not data:

        # Mostra uma mensagem de erro caso o usuário não tenha inserido a data.
        messagebox.showerror("Erro", "Por favor, insira a data no formato DD/MM/AAAA.")

        # Encerra a execução da função se a data não for inserida.
        return

    try:

        # Realiza uma requisição POST para a API para converter a
        # data em formato extenso.
        resposta = requests.post(f"{API_URL}/data-por-extenso/", json={

            "data": data,  # Data inserida pelo usuário.
            "formato": "%d/%m/%Y"  # Especifica o formato da data esperado pela API.

        })

        # Verifica se houve algum erro na requisição HTTP.
        # Caso exista, uma exceção será lançada.
        resposta.raise_for_status()

        # Converte a resposta da API de JSON para um dicionário
        # Python para facilitar o acesso aos dados.
        dados = resposta.json()

        # Traduzindo para português
        dia_semana = {
            "Monday": "Segunda-feira", "Tuesday": "Terça-feira", "Wednesday": "Quarta-feira",
            "Thursday": "Quinta-feira", "Friday": "Sexta-feira", "Saturday": "Sábado", "Sunday": "Domingo"
        }
        mes_extenso = {
            "January": "janeiro", "February": "fevereiro", "March": "março",
            "April": "abril", "May": "maio", "June": "junho",
            "July": "julho", "August": "agosto", "September": "setembro",
            "October": "outubro", "November": "novembro", "December": "dezembro"
        }

        # Armazena o texto da data por extenso que foi retornado pela API.
        texto_extenso = dados["data_por_extenso"]

        # Substitui os nomes dos dias da semana em inglês pelos
        # correspondentes em português.
        for ingles, portugues in dia_semana.items():
            texto_extenso = texto_extenso.replace(ingles, portugues)

        # Substitui os nomes dos meses em inglês pelos
        # correspondentes em português.
        for ingles, portugues in mes_extenso.items():
            texto_extenso = texto_extenso.replace(ingles, portugues)

        # Configura a área de texto de resultado para ser editável temporariamente.
        area_resultado_extenso.config(state="normal")

        # Limpa o texto anteriormente exibido na área de texto.
        area_resultado_extenso.delete("1.0", tk.END)

        # Insere o novo texto da data por extenso já traduzido para o português.
        area_resultado_extenso.insert(tk.END, texto_extenso)

        # Retorna a configuração da área de texto para
        # desabilitada, impedindo edição.
        area_resultado_extenso.config(state="disabled")

    # Bloco que captura e trata exceções lançadas durante as requisições HTTP.
    except requests.exceptions.RequestException as e:

        # A função `showerror` do módulo `messagebox` é usada para
        # exibir uma janela de mensagem de erro.
        # "Erro" é o título da janela de mensagem, que informa ao usuário
        # que ocorreu um erro.
        # `f"Erro ao se conectar à API:\n{e}"` é a mensagem mostrada ao usuário.
        # Esta mensagem é formatada para incluir
        # uma descrição mais detalhada do erro que ocorreu durante a
        # tentativa de comunicação com a API.
        # `{e}` captura e exibe a mensagem de erro específica retornada pela
        # exceção, que pode ajudar no diagnóstico do problema.
        messagebox.showerror("Erro", f"Erro ao se conectar à API:\n{e}")


# Definição da função verificar_bissexto, que não recebe parâmetros e é
# acionada pelo evento de um botão na interface gráfica.
def verificar_bissexto():

    # A variável 'ano' recebe o valor digitado pelo usuário no
    # campo de entrada 'entrada_ano_bissexto'.
    # O método .get() é usado para extrair o texto atual do
    # campo de entrada.
    ano = entrada_ano_bissexto.get()

    # Condicional que verifica se o texto inserido é composto apenas
    # por dígitos, ou seja, é um número.
    # O método .isdigit() retorna True se a string contém
    # apenas dígitos e não está vazia.
    if not ano.isdigit():

        # Caso 'ano' não seja um dígito (ou seja, não é um ano válido), uma
        # janela de mensagem de erro é mostrada.
        # 'showerror' é uma função do módulo 'messagebox' que cria
        # uma janela de diálogo de erro.
        # O primeiro argumento é o título da janela, e o segundo é a
        # mensagem exibida ao usuário.
        messagebox.showerror("Erro", "Por favor, insira um ano válido.")

        # A instrução 'return' encerra a execução da função caso o
        # input não seja válido,
        # evitando que o restante do código seja executado e possíveis
        # erros ou comportamentos indesejados ocorram.
        return

    # Bloco try-except para lidar com a possibilidade de
    # erros na requisição HTTP.
    try:

        # Realiza uma requisição GET à API usando a URL formatada com o
        # ano informado pelo usuário.
        # A URL é construída concatenando a URL base da API, o
        # endpoint específico e o ano fornecido.
        resposta = requests.get(f"{API_URL}/ano-bissexto/{ano}")

        # .raise_for_status() levanta uma exceção HTTPError se a
        # resposta da requisição não for bem-sucedida.
        # Isto é, se o código de status não for entre 200 e 400.
        resposta.raise_for_status()

        # Converte a resposta da API de JSON para um dicionário Python usando .json().
        dados = resposta.json()

        # Configura o widget de texto para poder modificar seu conteúdo.
        area_resultado_bissexto.config(state="normal")

        # Limpa o conteúdo atual do widget de texto para exibir a nova informação.
        area_resultado_bissexto.delete("1.0", tk.END)

        # Insere a resposta da API no widget de texto. Exibe o ano
        # consultado e se ele é bissexto ou não.
        # A expressão condicional ('É bissexto' if dados['bissexto'] else
        # 'Não é bissexto') decide o texto baseado no valor booleano.
        area_resultado_bissexto.insert(
            tk.END,
            f"Ano: {dados['ano']} - {'É bissexto' if dados['bissexto'] else 'Não é bissexto'}"
        )

        # Retorna o widget de texto ao estado 'disabled' para
        # prevenir a edição do conteúdo pelo usuário.
        area_resultado_bissexto.config(state="disabled")

    # Bloco except para capturar exceções específicas que
    # podem ocorrer durante a requisição.
    except requests.exceptions.RequestException as e:

        # Se ocorrer algum erro durante a conexão ou processamento da
        # requisição, uma mensagem de erro é exibida.
        # O erro pode ser qualquer exceção lançada pela biblioteca requests,
        # incluindo problemas de conexão ou timeouts.
        messagebox.showerror("Erro", f"Erro ao se conectar à API:\n{e}")


# Cria a janela principal para a aplicação utilizando a biblioteca tkinter.
janela = tk.Tk()

# Define o título da janela, que aparece na barra de título da janela.
janela.title("Tratamento de Datas")

# Define as dimensões da janela principal (largura x altura),
        # que determina o tamanho da janela ao ser exibida.
janela.geometry("600x500")

# Configura a cor de fundo da janela, utilizando um código de
        # cor hexadecimal para um cinza claro.
janela.configure(bg="#f0f0f0")

# Cria um botão na janela principal. Este botão será usado
        # para testar a conexão com a API.
# O botão é configurado com várias propriedades estilísticas e funcionais:
# 'text' define o texto que aparece no botão.
# 'font' define o tipo e tamanho da fonte usada no texto do botão.
# 'command' vincula uma função que será executada quando o botão for
        # pressionado. Neste caso, a função testar_conexao.
# 'bg' (background) define a cor de fundo do botão, um verde que sugere ação positiva.
# 'fg' (foreground) define a cor do texto, branco para alto
        # contraste com o fundo verde.
# 'pack' é um gerenciador de geometria do tkinter que organiza widgets em
        # blocos antes de colocá-los na janela.
# 'pady' dá um espaçamento vertical entre o botão e outros elementos na
        # janela, melhorando a estética e separação visual.
tk.Button(janela,
          text="Testar Conexão com a API",
          font=("Arial", 12),
          command=testar_conexao,
          bg="#4caf50",
          fg="white").pack(pady=10)

# Cria um 'Notebook' (um container para abas) no objeto 'janela'.
        # O 'ttk.Notebook' é um widget que permite a organização
        # de interfaces em abas separadas.
abas = ttk.Notebook(janela)

# Adiciona o widget 'abas' à janela, configurando para preencher o
        # espaço disponível ('fill="both"') e expandir se há espaço extra ('expand=True').
# Isso assegura que as abas ocupem todo o espaço disponível
        # na janela principal.
abas.pack(fill="both", expand=True)

# Cria uma 'Frame' para a primeira aba do notebook, que será usada
        # para calcular a idade. 'ttk.Frame' é um container
        # para outros widgets.
aba_idade = ttk.Frame(abas)

# Adiciona a 'Frame' recém-criada ao 'Notebook', especificando o
        # texto da aba como "Calcular Idade".
abas.add(aba_idade, text="Calcular Idade")

# Cria e adiciona um rótulo à 'Frame' da aba de idade, instruindo o
        # usuário sobre como deve ser inserida a data de nascimento.
# O rótulo usa a fonte Arial tamanho 12.
tk.Label(aba_idade,
         text="Data de nascimento (DD/MM/AAAA):",
         font=("Arial", 12)).pack(pady=10)

# Cria um campo de entrada ('Entry') para que o usuário digite a
        # data de nascimento. O campo tem uma largura definida para 30
        # caracteres e usa a fonte Arial tamanho 12.
entrada_data_nascimento = tk.Entry(aba_idade, font=("Arial", 12), width=30)

# Adiciona o campo de entrada à 'Frame' da aba de idade, com um
        # espaçamento vertical ('pady=5') para separá-lo de outros
        # elementos na interface, melhorando a organização visual.
entrada_data_nascimento.pack(pady=5)

# Cria um botão na aba 'aba_idade' com o texto "Calcular Idade".
# Este botão é ligado à função 'calcular_idade',
# que será executada quando o botão for clicado. O botão utiliza a
        # fonte Arial tamanho 12, com um fundo verde (#4caf50)
# e texto em branco (fg="white") para destacar a ação que ele representa.
tk.Button(aba_idade,
          text="Calcular Idade",
          command=calcular_idade,
          font=("Arial", 12),
          bg="#4caf50",
          fg="white").pack(pady=10)

# Cria uma área de texto 'ScrolledText' dentro da aba 'aba_idade'.
        # 'ScrolledText' é uma versão do widget 'Text'
        # que inclui uma barra de rolagem integrada, o que é
        # útil para exibir múltiplas linhas de texto.
# Configurações incluem:
# - font=("Arial", 12): Define a fonte do texto.
# - width=50: Define a largura da área de texto para
        # acomodar 50 caracteres por linha.
# - height=5: Define a altura da área de texto, suficiente
        # para mostrar 5 linhas de texto.
# - state="disabled": Inicialmente desabilita a edição do texto,
        # assim o usuário não pode alterar o conteúdo manualmente.
# - bg="#e8f5e9": Define uma cor de fundo suave para a área de texto,
        # melhorando a estética e a legibilidade.
area_resultado_idade = scrolledtext.ScrolledText(aba_idade,
                                                 font=("Arial", 12),
                                                 width=50,
                                                 height=5,
                                                 state="disabled",
                                                 bg="#e8f5e9")

# Adiciona a área de texto à aba 'aba_idade' usando o método 'pack',
        # que a posiciona dentro da interface.
# O parâmetro 'pady=10' adiciona um espaçamento vertical de 10
        # pixels acima e abaixo da área de texto,
        # ajudando a separá-la visualmente de outros elementos na interface.
area_resultado_idade.pack(pady=10)


# Cria uma nova aba no widget 'Notebook' chamada 'aba_diferenca'.
# 'ttk.Frame' é usado para criar um contêiner para todos os widgets
        # que serão adicionados nesta aba, permitindo organizar
        # visualmente os componentes de interface.
aba_diferenca = ttk.Frame(abas)

# Adiciona a 'aba_diferenca' ao widget 'Notebook' chamado 'abas'.
        # A aba é rotulada como "Diferença entre Datas",
        # oferecendo ao usuário uma indicação clara do
        # propósito desta seção da interface.
abas.add(aba_diferenca, text="Diferença entre Datas")

# Cria um rótulo dentro de 'aba_diferenca' para instruir o usuário
        # sobre como preencher a informação esperada.
# O texto "Data inicial (DD/MM/AAAA):" orienta o usuário a inserir a
        # data no formato específico de dia, mês e ano.
# A fonte Arial tamanho 12 é utilizada para garantir
        # que o texto seja legível.
tk.Label(aba_diferenca,
         text="Data inicial (DD/MM/AAAA):",
         font=("Arial", 12)).pack(pady=10)

# Cria um campo de entrada 'Entry' dentro da 'aba_diferenca'
        # onde os usuários podem digitar a data inicial.
# A fonte Arial tamanho 12 e largura 30 são especificadas para
        # manter a consistência visual e assegurar
        # que haja espaço suficiente para digitar a
        # data completa no formato especificado.
entrada_data_inicio = tk.Entry(aba_diferenca,
                               font=("Arial", 12),
                               width=30)

# Adiciona o campo de entrada 'entrada_data_inicio' à interface,
        # usando o método 'pack' que o posiciona
        # na tela e adiciona um pequeno espaço vertical (pady=5)
        # para separá-lo visualmente de outros elementos na interface.
entrada_data_inicio.pack(pady=5)

# Cria um rótulo dentro de 'aba_diferenca' que instrui o
        # usuário a inserir a data final.
# Este rótulo ajuda a esclarecer o que deve ser inserido no campo associado.
# O texto "Data final (DD/MM/AAAA):" orienta especificamente o
        # usuário a inserir a data no formato de dia, mês e ano.
# A fonte Arial tamanho 12 é escolhida para manter a consistência
        # visual com outros elementos de texto na interface.
tk.Label(aba_diferenca,
         text="Data final (DD/MM/AAAA):",
         font=("Arial", 12)).pack(pady=10)

# Cria um campo de entrada 'Entry' para a data final dentro da 'aba_diferenca'.
# Este campo permite ao usuário inserir a data final para o cálculo da diferença.
# A largura do campo é definida como 30, que é suficiente para
        # inserir a data no formato especificado sem cortes.
# A fonte Arial tamanho 12 é usada para garantir a legibilidade e
        # a uniformidade visual com outros campos de entrada.
entrada_data_fim = tk.Entry(aba_diferenca,
                            font=("Arial", 12),
                            width=30)

# Adiciona o campo de entrada 'entrada_data_fim' à interface gráfica.
# O método 'pack' é usado para organizar o campo na tela, com um
        # pequeno espaço vertical (pady=5) para separação
        # estética e funcional de outros elementos na interface.
# Isso ajuda a evitar que os elementos visuais fiquem demasiadamente agrupados.
entrada_data_fim.pack(pady=5)

# Cria um botão dentro da 'aba_diferenca' que, ao ser clicado,
        # aciona a função 'diferenca_datas'.
# O botão é rotulado como "Calcular Diferença", indicando sua
        # função claramente ao usuário.
# O estilo visual do botão é definido com a fonte Arial tamanho 12,
        # um fundo verde (#4caf50), e texto em branco,
# proporcionando uma boa visibilidade e um design atraente.
# O comando associado ao botão ('command=diferenca_datas') conecta o
        # botão à função que calcula a diferença entre datas.
# O método 'pack' é usado para adicionar o botão ao layout da aba,
        # com um espaçamento vertical de 10 pixels ('pady=10'),
        # ajudando a separar visualmente este botão de outros
        # controles na interface.
tk.Button(aba_diferenca,
          text="Calcular Diferença",
          command=diferenca_datas,
          font=("Arial", 12),
          bg="#4caf50",
          fg="white").pack(pady=10)

# Cria uma área de texto rolável 'ScrolledText' para exibir os
        # resultados do cálculo de diferença entre datas.
# Esta área é inicialmente desabilitada ('state="disabled"') para
        # impedir a edição direta pelo usuário, garantindo que
# só exiba os resultados gerados pelo sistema e mantendo a
        # integridade dos dados exibidos.
# A fonte Arial tamanho 12 é escolhida para a legibilidade, e a
        # largura de 50 caracteres com 5 linhas de altura
# oferece espaço suficiente para apresentar as informações de
        # diferença entre as datas.
# O fundo da área de texto é um verde claro ('#e8f5e9'), que é
        # suave para os olhos e combina com o esquema de cores do botão.
# O método 'pack' é novamente usado para adicionar a área de texto
        # ao layout, com um espaçamento vertical de 10 pixels ('pady=10'),
        # proporcionando uma separação adequada de outros elementos na aba.
area_resultado_diferenca = scrolledtext.ScrolledText(aba_diferenca,
                                                     font=("Arial", 12),
                                                     width=50,
                                                     height=5,
                                                     state="disabled",
                                                     bg="#e8f5e9")
area_resultado_diferenca.pack(pady=10)


# Cria um objeto de frame 'Frame' da biblioteca ttk (parte do tkinter)
        # que serve como um contêiner para outros widgets.
# Este frame é adicionado ao objeto 'Notebook' chamado 'abas',
        # que gerencia múltiplas abas na interface do usuário.
# O frame é especificamente para a funcionalidade de converter
        # datas para o formato por extenso.
aba_extenso = ttk.Frame(abas)

# Adiciona o frame 'aba_extenso' ao objeto 'Notebook' 'abas'.
# O texto "Data por Extenso" é usado como título desta aba,
        # explicando claramente sua função ao usuário.
abas.add(aba_extenso, text="Data por Extenso")

# Cria e configura um rótulo (Label) dentro da 'aba_extenso'
        # que orienta os usuários onde inserir a data.
# O texto "Data (DD/MM/AAAA):" informa o formato esperado da
        # data, ajudando a prevenir erros de entrada.
# A fonte Arial tamanho 12 é usada para garantir que o
        # texto seja facilmente legível.
tk.Label(aba_extenso,
         text="Data (DD/MM/AAAA):",
         font=("Arial", 12)).pack(pady=10)

# Cria uma entrada (Entry) para que os usuários possam digitar a data.
# Este campo de entrada está configurado para aceitar texto
        # com a fonte Arial tamanho 12 e largura de 30 caracteres,
        # oferecendo espaço suficiente para a maioria dos formatos de data.
entrada_data_extenso = tk.Entry(aba_extenso, font=("Arial", 12), width=30)

# Posiciona o campo de entrada na interface gráfica usando o método 'pack'.
# Um espaçamento vertical (pady) de 5 pixels é adicionado
        # acima e abaixo do campo de entrada para separá-lo visualmente
        # dos outros elementos na aba, facilitando a organização da interface.
entrada_data_extenso.pack(pady=5)

# Cria um botão na aba 'aba_extenso' que, quando clicado,
        # executará a função 'data_por_extenso'.
# O texto no botão é "Converter para Extenso", indicando claramente sua função.
# A fonte é definida como Arial tamanho 12, proporcionando uma leitura clara.
# A cor de fundo do botão é verde (#4caf50) e o texto é branco,
        # criando um contraste alto para fácil identificação.
# O botão é posicionado na interface usando o método 'pack', com
        # um espaçamento vertical de 10 pixels para separação dos demais elementos.
tk.Button(aba_extenso,
          text="Converter para Extenso",
          command=data_por_extenso,
          font=("Arial", 12),
          bg="#4caf50",
          fg="white").pack(pady=10)

# Cria uma área de texto deslizante usando a classe 'ScrolledText' da biblioteca 'tkinter'.
# Esta área é usada para exibir a data formatada por extenso após a conversão.
# Define-se a fonte como Arial tamanho 12, a largura em 50 caracteres e a altura em 5 linhas,
# garantindo espaço suficiente para exibir datas completas.
# O estado inicial é "disabled" para prevenir que o usuário edite o texto diretamente,
# e a cor de fundo é um verde claro (#e8f5e9) para destacar a área de resultado.
# A área de texto é adicionada à interface na aba 'aba_extenso' usando o método 'pack',
# com um espaçamento vertical de 10 pixels para uma boa separação visual entre os elementos.
area_resultado_extenso = scrolledtext.ScrolledText(aba_extenso,
                                                   font=("Arial", 12),
                                                   width=50, height=5,
                                                   state="disabled",
                                                   bg="#e8f5e9")

area_resultado_extenso.pack(pady=10)


# Cria uma nova aba no 'Notebook' chamado 'abas', que é um
        # widget para gerenciar abas múltiplas na interface.
# 'aba_bissexto' é o nome da variável que representa esta aba específica.
# Adiciona esta nova aba ao 'Notebook' com o rótulo "Ano Bissexto",
        # que descreve a funcionalidade da aba.
aba_bissexto = ttk.Frame(abas)
abas.add(aba_bissexto, text="Ano Bissexto")

# Cria e exibe um rótulo na aba 'aba_bissexto'.
# O texto "Ano:" serve para indicar ao usuário que ele deve inserir um ano nesta entrada.
# A fonte é Arial tamanho 12, garantindo que o texto seja legível.
# O rótulo é posicionado usando o método 'pack', com um espaçamento
        # vertical de 10 pixels para separação clara dos outros elementos da interface.
tk.Label(aba_bissexto,
         text="Ano:",
         font=("Arial", 12)).pack(pady=10)

# Cria uma caixa de entrada para que o usuário insira o ano
        # que deseja verificar se é bissexto.
# A entrada permite textos, então será necessário validar para
        # garantir que apenas números sejam considerados.
# Configurada com a fonte Arial tamanho 12 e largura suficiente (30 caracteres)
        # para acomodar a maioria dos tamanhos de entrada de ano.
# O widget é adicionado à interface da aba 'aba_bissexto' usando o
        # método 'pack', com um espaçamento vertical de 5 pixels para um layout organizado.
entrada_ano_bissexto = tk.Entry(aba_bissexto,
                                font=("Arial", 12),
                                width=30)

entrada_ano_bissexto.pack(pady=5)

# Cria um botão na interface gráfica, especificamente na aba 'aba_bissexto'.
# O texto "Verificar Ano Bissexto" no botão informa claramente a
        # função do botão.
# 'command=verificar_bissexto' conecta este botão à função 'verificar_bissexto'
        # que será chamada quando o botão for clicado.
# O botão usa a fonte Arial tamanho 12 para manter a consistência visual
        # com outros textos na interface.
# 'bg="#4caf50"' define a cor de fundo do botão como um verde vivo, e 'fg="white"'
        # define a cor do texto para branco, melhorando a legibilidade.
# O botão é adicionado à interface usando o método 'pack', com um
        # espaçamento vertical de 10 pixels acima e abaixo
        # para separá-lo de outros elementos.
tk.Button(aba_bissexto,
          text="Verificar Ano Bissexto",
          command=verificar_bissexto,
          font=("Arial", 12),
          bg="#4caf50",
          fg="white").pack(pady=10)

# Cria uma área de texto com barra de rolagem na aba 'aba_bissexto'.
# Configurada com a fonte Arial tamanho 12, largura suficiente
        # para 50 caracteres e altura para 5 linhas, proporcionando
        # espaço adequado para mostrar resultados.
# 'state="disabled"' impede que o usuário edite o conteúdo da área de
        # texto diretamente, mantendo a integridade dos resultados exibidos.
# 'bg="#e8f5e9"' define a cor de fundo da área de texto para um
        # verde claro suave, oferecendo um contraste suave com o
        # texto e um visual agradável.
# A área de texto é também adicionada usando o método 'pack', com
        # espaçamento vertical de 10 pixels, assegurando uma boa
        # separação visual dentro da aba.
area_resultado_bissexto = scrolledtext.ScrolledText(aba_bissexto,
                                                    font=("Arial", 12),
                                                    width=50, height=5,
                                                    state="disabled",
                                                    bg="#e8f5e9")

area_resultado_bissexto.pack(pady=10)


# Inicia o loop da interface gráfica
janela.mainloop()