# Importa o módulo tkinter com o alias tk, usado para
# criar interfaces gráficas.
import tkinter as tk

# Importa o módulo ttk do tkinter para usar widgets
# com um estilo aprimorado.
from tkinter import ttk

# Importa o módulo messagebox do tkinter para mostrar
# mensagens de erro em caixas de diálogo.
from tkinter import messagebox
from tokenize import endpats

# Importa o módulo requests para fazer requisições HTTP.
import requests

# Define a URL base da API como uma variável constante
# para fácil referência e modificação.
URL_BASE = "http://127.0.0.1:8000"


# Define uma função chamada 'consumir_api' para
# interagir com uma API externa.
def consumir_api(endpoint, dados):

    # Tenta executar o bloco de código dentro do try.
    try:

        # Constrói a URL completa para a requisição combinando a
        # URL base com o endpoint específico.
        url = f"{URL_BASE}/{endpoint}"

        # Faz uma requisição POST para a URL construída,
        # enviando 'dados' como JSON.
        resposta = requests.post(url, json=dados)

        # Verifica se o código de status da resposta é 200 (sucesso).
        if resposta.status_code == 200:

            # Se for bem-sucedida, retorna os dados da resposta
            # convertidos de JSON para um dicionário Python.
            return resposta.json()

        else:

            # Se o status code não for 200, retorna um dicionário
            # com informações sobre o erro.
            return {"erro": resposta.status_code, "mensagem": resposta.text}

    # Captura qualquer exceção que ocorra durante a tentativa de
    # fazer a requisição ou processar a resposta.
    except Exception as e:

        # Retorna um dicionário com um erro genérico de conexão e
        # a mensagem de erro associada.
        return {"erro": "Conexão", "mensagem": str(e)}


# Define a função 'executar_operacao' que não recebe parâmetros e
# é chamada quando o usuário clica no botão 'Executar'.
def executar_operacao():

    # Obtém o texto da área de texto 'entrada_texto'. "1.0" refere-se à primeira
    # linha e primeiro caractere, e 'tk.END' refere-se ao fim do texto.
    # O método 'strip()' é usado para remover espaços em
    # branco extras no início e no final do texto.
    texto = entrada_texto.get("1.0", tk.END).strip()

    # Verifica se nenhum texto foi inserido.
    if not texto:

        # Exibe uma mensagem de erro usando uma caixa de
        # diálogo se o texto estiver vazio.
        messagebox.showerror("Erro", "Por favor, insira um texto para processar.")

        # Interrompe a execução da função sem
        # retornar qualquer valor.
        return

    # Obtém a operação selecionada pelo usuário no
    # combobox 'operacao_selecionada'.
    operacao = operacao_selecionada.get()

    # Cria um dicionário para armazenar os dados que serão
    # enviados para a API. Inicialmente contém apenas o texto.
    dados = {"texto": texto}

    # Verifica se a operação selecionada é "Substituir Palavra".
    if operacao == "Substituir Palavra":

        # Obtém a palavra antiga da entrada correspondente e
        # remove espaços extras.
        palavra_antiga = entrada_palavra_antiga.get().strip()

        # Obtém a palavra nova da entrada correspondente e
        # remove espaços extras.
        palavra_nova = entrada_palavra_nova.get().strip()

        # Verifica se ambas as palavras (antiga e nova) foram fornecidas.
        if not palavra_antiga or not palavra_nova:

            # Exibe uma mensagem de erro se uma das
            # palavras não foi preenchida.
            messagebox.showerror("Erro", "Preencha as palavras antiga e nova para substituição.")

            # Interrompe a execução da função sem retornar qualquer valor.
            return

        # Adiciona as palavras antiga e nova ao dicionário 'dados'.
        dados["palavra_antiga"] = palavra_antiga
        dados["palavra_nova"] = palavra_nova

    # Define um dicionário chamado 'endpoints' que mapeia as operações
    # disponíveis na interface gráfica para os respectivos endpoints da API.
    # Cada chave no dicionário é o nome da operação exibido no combobox da GUI, e o
    # valor associado é o nome do endpoint correspondente na API.
    endpoints = {
        "Contar Elementos": "contar",  # Mapeia "Contar Elementos" para o endpoint "/contar".
        "Texto em Maiúsculas": "maiusculas",  # Mapeia "Texto em Maiúsculas" para o endpoint "/maiusculas".
        "Texto em Minúsculas": "minusculas",  # Mapeia "Texto em Minúsculas" para o endpoint "/minusculas".
        "Remover Espaços Extras": "remover_espacos", # Mapeia "Remover Espaços Extras" para o endpoint "/remover_espacos".
        "Inverter Texto": "inverter",  # Mapeia "Inverter Texto" para o endpoint "/inverter".
        "Substituir Palavra": "substituir",  # Mapeia "Substituir Palavra" para o endpoint "/substituir".
        "Extrair Primeiro Nome": "primeiro_nome",  # Mapeia "Extrair Primeiro Nome" para o endpoint "/primeiro_nome".
        "Extrair Último Nome": "ultimo_nome",  # Mapeia "Extrair Último Nome" para o endpoint "/ultimo_nome".
        "Maior Palavra e Tamanho": "tamanho_palavra", # Mapeia "Maior Palavra e Tamanho" para o endpoint "/tamanho_palavra".
        "Texto Capitalizado": "capitalizar",  # Mapeia "Texto Capitalizado" para o endpoint "/capitalizar".
    }

    # Chama a função 'consumir_api', passando o endpoint correspondente à
    # operação selecionada e os dados preparados.
    # 'endpoints[operacao]' pega o endpoint correto do dicionário baseado
    # na operação escolhida pelo usuário no combobox.
    # 'dados' é o dicionário contendo as informações necessárias para
    # realizar a operação (por exemplo, o texto e palavras adicionais).
    resultado = consumir_api(endpoints[operacao], dados)

    # Verifica se o dicionário 'resultado' retornado
    # pela API contém a chave "erro".
    if "erro" in resultado:

        # Se a chave "erro" estiver presente, significa que ocorreu um erro.
        # Uma mensagem de erro é exibida ao usuário usando uma caixa de diálogo.
        # O valor associado à chave "mensagem" no
        # dicionário 'resultado' é mostrado na mensagem de erro.
        messagebox.showerror("Erro", resultado["mensagem"])

    else:

        # Se não houver erro, o resultado da operação é exibido
        # na interface gráfica.
        # O método 'set' é usado para atualizar o valor da
        # variável 'resultado_texto', que é vinculada a um rótulo na GUI.
        # 'str(resultado)' converte o dicionário retornado
        # pela API em uma string para exibição.
        resultado_texto.set(str(resultado))


# Cria a janela principal do aplicativo utilizando a biblioteca Tkinter.
# 'tk.Tk()' inicializa a instância principal da interface gráfica.
janela = tk.Tk()

# Define o título da janela que será exibido na barra de título do aplicativo.
# 'title()' altera o título da janela para "Consumir API
        # de Tratamento de Texto".
janela.title("Consumir API de Tratamento de Texto")

# Configura o tamanho da janela principal do aplicativo.
# 'geometry()' define as dimensões da janela como 600 pixels
        # de largura e 500 pixels de altura.
janela.geometry("600x500")

# Adiciona um rótulo (Label) à janela para orientar o
        # usuário sobre onde inserir o texto.
# 'tk.Label()' cria um rótulo com o texto "Insira o texto:".
# O parâmetro 'font=("Arial", 12)' define a fonte usada no
        # rótulo como Arial, tamanho 12.
# 'pack(pady=5)' organiza o rótulo na janela com um
        # espaçamento vertical (padding) de 5 pixels.
tk.Label(janela,
         text="Insira o texto:",
         font=("Arial", 12)).pack(pady=5)

# Cria uma caixa de texto (Text) onde o usuário pode
        # inserir múltiplas linhas de texto.
# 'tk.Text()' cria o widget com uma altura de 5 linhas e
        # uma largura de 60 caracteres.
entrada_texto = tk.Text(janela,
                        height=5,
                        width=60)

# Posiciona a caixa de texto na janela utilizando o método 'pack()'.
# 'pack(pady=5)' adiciona um espaçamento vertical (padding)
        # de 5 pixels acima e abaixo da caixa de texto.
entrada_texto.pack(pady=5)

# Adiciona um rótulo (Label) à interface para orientar o usuário.
# O texto "Selecione a operação:" indica que o usuário
        # deve escolher uma operação.
# 'font=("Arial", 12)' define a fonte usada no rótulo como Arial, tamanho 12.
# 'pack(pady=5)' posiciona o rótulo na interface com um
        # espaçamento vertical (padding) de 5 pixels acima e abaixo.
tk.Label(janela,
         text="Selecione a operação:",
         font=("Arial", 12)).pack(pady=5)

# Cria um combobox (menu suspenso) para o usuário
        # selecionar a operação desejada.
# 'ttk.Combobox()' é usado em vez de 'tk' para
        # criar um widget com estilo moderno.
# 'janela' é o contêiner onde o combobox será exibido.
# 'values=[]' define a lista de opções disponíveis no menu suspenso.
operacao_selecionada = ttk.Combobox(
    janela,
    values=[
        "Contar Elementos",           # Conta caracteres, palavras e frases no texto.
        "Texto em Maiúsculas",        # Converte o texto para letras maiúsculas.
        "Texto em Minúsculas",        # Converte o texto para letras minúsculas.
        "Remover Espaços Extras",     # Remove espaços extras do texto.
        "Inverter Texto",             # Inverte o texto.
        "Substituir Palavra",         # Substitui uma palavra antiga por uma nova no texto.
        "Extrair Primeiro Nome",      # Extrai o primeiro nome do texto.
        "Extrair Último Nome",        # Extrai o último nome do texto.
        "Maior Palavra e Tamanho",    # Encontra a maior palavra e seu comprimento.
        "Texto Capitalizado",         # Capitaliza cada palavra no texto.
    ],
    state="readonly",  # Define o combobox como somente leitura; o usuário só pode selecionar, não digitar.
    width=40,          # Define a largura do combobox para acomodar as opções mais longas.
)

# Define a operação padrão selecionada no combobox.
# 'set("Contar Elementos")' faz com que "Contar Elementos"
        # seja a opção exibida por padrão.
operacao_selecionada.set("Contar Elementos")

# Posiciona o combobox na interface usando o método 'pack()'.
# 'pady=5' adiciona um espaçamento vertical de 5 pixels
        # acima e abaixo do widget.
operacao_selecionada.pack(pady=5)


# Cria um contêiner chamado 'frame_substituir' dentro
        # da janela principal.
# Um frame é um widget usado para agrupar elementos relacionados,
        # permitindo organizar melhor a interface gráfica.
frame_substituir = tk.Frame(janela)

# Adiciona um rótulo ao frame para o campo "Palavra antiga".
# O texto "Palavra antiga:" indica que o usuário deve inserir a
        # palavra que será substituída.
# A fonte do texto é configurada como Arial, tamanho 10,
        # para boa legibilidade.
# 'grid(row=0, column=0)' posiciona este rótulo na primeira
        # linha e primeira coluna do frame.
# 'padx=5' adiciona um espaçamento horizontal (padding)
        # de 5 pixels entre o rótulo e outros elementos.
tk.Label(frame_substituir,
         text="Palavra antiga:",
         font=("Arial", 10)).grid(row=0, column=0, padx=5)

# Cria um campo de entrada (Entry) para o usuário
        # digitar a palavra antiga.
# 'width=20' define o campo com capacidade para
        # exibir até 20 caracteres visíveis.
# Este campo é armazenado na variável 'entrada_palavra_antiga'
        # para ser acessado posteriormente.
# 'grid(row=0, column=1)' posiciona este campo de entrada
        # na primeira linha e segunda coluna do frame.
entrada_palavra_antiga = tk.Entry(frame_substituir, width=20)
entrada_palavra_antiga.grid(row=0, column=1, padx=5)

# Adiciona um rótulo ao frame para o campo "Palavra nova".
# O texto "Palavra nova:" indica que o usuário deve inserir a
        # nova palavra que substituirá a antiga.
# Configura a fonte como Arial, tamanho 10, e posiciona o
        # rótulo na segunda linha e primeira coluna do frame.
# 'padx=5' adiciona espaçamento horizontal, semelhante ao rótulo anterior.
tk.Label(frame_substituir,
         text="Palavra nova:",
         font=("Arial", 10)).grid(row=1, column=0, padx=5)

# Cria um campo de entrada (Entry) para o usuário digitar a nova palavra.
# 'width=20' especifica o tamanho do campo de entrada.
# Este campo é armazenado na variável 'entrada_palavra_nova'
        # para ser acessado posteriormente.
# 'grid(row=1, column=1)' posiciona este campo na
        # segunda linha e segunda coluna do frame.
entrada_palavra_nova = tk.Entry(frame_substituir, width=20)
entrada_palavra_nova.grid(row=1, column=1, padx=5)

# Posiciona o frame na janela principal
        # utilizando o método 'pack()'.
# 'pady=10' adiciona um espaçamento vertical (padding)
        # de 10 pixels acima e abaixo do frame.
frame_substituir.pack(pady=10)


# Cria um botão para executar a operação selecionada pelo usuário.
# 'tk.Button()' cria um widget de botão na janela principal 'janela'.
# O texto exibido no botão é "Executar", e sua fonte é
        # configurada como Arial, tamanho 12.
# O parâmetro 'command=executar_operacao' define que, ao
        # clicar no botão, a função 'executar_operacao' será chamada.
botao_executar = tk.Button(janela,
                           text="Executar",
                           font=("Arial", 12),
                           command=executar_operacao)

# Posiciona o botão na janela usando o método 'pack()'.
# 'pady=10' adiciona um espaçamento vertical de 10 pixels
        # acima e abaixo do botão, garantindo um layout espaçado.
botao_executar.pack(pady=10)

# Adiciona um rótulo (Label) para indicar a área de
        # exibição do resultado ao usuário.
# O texto exibido é "Resultado:", e sua fonte é
        # configurada como Arial, tamanho 12.
# 'pack(pady=5)' posiciona o rótulo com um espaçamento
        # vertical de 5 pixels para separá-lo dos outros elementos.
tk.Label(janela,
         text="Resultado:",
         font=("Arial", 12)).pack(pady=5)

# Cria uma variável StringVar para armazenar e
        # manipular o texto do resultado dinamicamente.
# StringVar é uma classe do tkinter usada para vincular
        # variáveis a widgets de interface gráfica.
resultado_texto = tk.StringVar()

# Cria um rótulo (Label) para exibir o resultado da operação.
# 'textvariable=resultado_texto' vincula o texto do
        # rótulo à variável 'resultado_texto',
# permitindo que o texto seja atualizado dinamicamente pela aplicação.
# A fonte é Arial, tamanho 12, com um fundo branco ('bg="white"')
        # para destacar a área de resultado.
# 'relief="sunken"' cria um efeito visual de borda rebaixada no rótulo.
# 'width=70' define a largura do rótulo, enquanto 'height=5'
        # define a altura.
# 'wraplength=500' permite que o texto seja quebrado em
        # linhas se exceder 500 pixels de largura.
# 'anchor="nw"' alinha o texto no canto superior esquerdo do rótulo.
# 'justify="left"' alinha o texto à esquerda dentro do rótulo.
resultado_label = tk.Label(
    janela,
    textvariable=resultado_texto,
    font=("Arial", 12),
    bg="white",
    relief="sunken",
    width=70,
    height=5,
    wraplength=500,
    anchor="nw",
    justify="left"
)

# Posiciona o rótulo de resultado na janela principal
        # usando o método 'pack()'.
# 'pady=5' adiciona um espaçamento vertical de
        # 5 pixels acima e abaixo do rótulo.
resultado_label.pack(pady=5)

# Inicia o loop da interface
janela.mainloop()