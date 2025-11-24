# Importa o módulo tkinter e o renomeia como 'tk', facilitando referências no código.
# O 'ttk' é importado do 'tkinter' para usar widgets que têm um estilo melhorado.
# O 'messagebox' é usado para mostrar caixas de diálogo de erro.
import tkinter as tk
from tkinter import ttk, messagebox

# Importa o módulo 'requests', que permite enviar requisições HTTP
# de maneira fácil e intuitiva em Python.
import requests

# A variável 'URL_BASE' armazena a URL base da API, que é usada para
# construir as URLs completas das requisições.
# A URL indica que a API está sendo executada localmente no
# computador na porta 8000.
URL_BASE = "http://127.0.0.1:8000"


# Define a função 'consumir_operacao' que é responsável por
# fazer as requisições à API.
# A função aceita três argumentos: 'operacao', 'numero1' e 'numero2'.
# 'operacao' é uma string que indica a operação matemática a
# ser realizada (ex: 'soma').
# 'numero1' e 'numero2' são os números sobre os quais a
# operação será realizada.
def consumir_operacao(operacao, numero1, numero2):

    # Constrói a URL completa para acessar a API usando a
    # operação especificada.
    # A URL é formada pela URL base e o nome da operação, por
    # exemplo, "http://127.0.0.1:8000/soma".
    url = f"{URL_BASE}/{operacao}"

    # Cria um dicionário 'parametros' que contém os parâmetros 'numero1' e 'numero2'.
    # Estes parâmetros serão passados na URL da requisição.
    parametros = {"numero1": numero1, "numero2": numero2}

    # Tenta executar a requisição HTTP GET usando a função 'requests.get'.
    # A URL e os parâmetros são passados como argumentos para a função.
    try:

        resposta = requests.get(url, params=parametros)

        # Checa o código de status da resposta HTTP.
        # Se o código de status for 200, a requisição foi bem-sucedida.
        if resposta.status_code == 200:

            # Extrai o 'resultado' do JSON retornado pela API e o retorna.
            return resposta.json()["resultado"]

        else:

            # Se o código de status não for 200, levanta uma exceção com detalhes do erro,
            # que são extraídos do JSON da resposta
            # usando 'resposta.json()["detail"]'.
            raise Exception(resposta.json()["detail"])

    except Exception as e:

        # Se ocorrer qualquer exceção durante a requisição ou processamento da
        # resposta, retorna uma string contendo a mensagem de erro.
        return f"Erro: {e}"


# Define a função 'calcular', que é chamada quando o usuário interage com a
# interface gráfica para realizar uma operação matemática.
def calcular():

    try:

        # Tenta converter o texto inserido pelo usuário nos campos de
        # entrada 'entrada_numero1' e 'entrada_numero2' para floats.
        # 'entrada_numero1.get()' e 'entrada_numero2.get()' recuperam o
        # texto desses campos de entrada.
        numero1 = float(entrada_numero1.get())
        numero2 = float(entrada_numero2.get())

        # Recupera a operação matemática selecionada pelo usuário
        # no 'combobox' da interface gráfica.
        # 'operacao_selecionada.get()' retorna o valor atual
        # selecionado no combobox 'operacao_selecionada'.
        operacao = operacao_selecionada.get()

        # Chama a função 'consumir_operacao' definida anteriormente,
        # passando a operação e os dois números.
        # Esta função realiza a requisição à API e retorna o resultado.
        resultado = consumir_operacao(operacao, numero1, numero2)

        # Atualiza o texto do 'resultado_label' com o resultado obtido.
        # 'resultado_label["text"]' define o texto do rótulo 'resultado_label'
        # para mostrar o resultado.
        resultado_label["text"] = f"Resultado: {resultado}"

    except ValueError:

        # Caso ocorra um ValueError durante a conversão dos números, isso
        # significa que o usuário não inseriu valores válidos.
        # Mostra uma mensagem de erro usando uma caixa de diálogo de erro.
        messagebox.showerror("Erro", "Por favor, insira números válidos!")

    except Exception as e:

        # Captura qualquer outra exceção que possa ocorrer durante a execução
        # da função 'consumir_operacao' ou qualquer outra parte do bloco try.
        # Mostra uma mensagem de erro usando uma caixa de diálogo de erro,
        # com a mensagem da exceção convertida para string.
        messagebox.showerror("Erro", str(e))


# Cria a janela principal do aplicativo usando a biblioteca tkinter.
# 'tk.Tk()' inicializa uma nova janela (ou instancia a
# janela principal do aplicativo tkinter).
janela = tk.Tk()

# Define o título da janela que aparece na barra de título da janela.
# 'janela.title("Calculadora com API")' coloca o
# título "Calculadora com API" na janela criada.
janela.title("Calculadora com API")

# Configura as dimensões da janela principal.
# 'janela.geometry("400x300")' define a largura da janela
# para 400 pixels e a altura para 300 pixels.
janela.geometry("400x300")

# Cria um rótulo (label) que será exibido dentro da janela principal.
# 'tk.Label(janela, text="Número 1:")' cria um rótulo com o texto "Número 1:".
# Este rótulo serve para indicar ao usuário onde ele deve inserir o
# primeiro número para a operação matemática.
# 'pack(pady=5)' organiza o rótulo dentro da janela e adiciona um
# preenchimento vertical (pady) de 5 pixels para separá-lo
# de outros elementos.
tk.Label(janela, text="Número 1:").pack(pady=5)

# Cria um campo de entrada (Entry) onde o usuário pode digitar o primeiro número.
# 'tk.Entry(janela, width=20)' cria uma caixa de entrada com
# largura suficiente para 20 caracteres.
# 'entrada_numero1' é a variável que armazena a referência a este campo de
# entrada, permitindo que seu valor seja acessado ou
# modificado posteriormente.
entrada_numero1 = tk.Entry(janela, width=20)

# Organiza o campo de entrada dentro da janela usando o método 'pack'.
# 'pack()' é um gerenciador de geometria em tkinter que posiciona o widget na janela.
# Sem parâmetros adicionais aqui, ele simplesmente adiciona o campo de
# entrada abaixo do último widget adicionado, neste caso, o rótulo "Número 1:".
entrada_numero1.pack()

# Cria um rótulo (Label) para o segundo número da operação matemática.
# 'tk.Label(janela, text="Número 2:")' cria um rótulo com o
# texto "Número 2:", que será exibido na janela.
# 'pack(pady=5)' organiza este rótulo dentro da janela, adicionando um
# espaçamento vertical (pady) de 5 pixels acima e abaixo dele
# para separação dos outros elementos.
tk.Label(janela, text="Número 2:").pack(pady=5)

# Cria um campo de entrada (Entry) para o usuário inserir o segundo número.
# 'tk.Entry(janela, width=20)' cria o campo com uma largura definida
# para acomodar 20 caracteres.
# 'entrada_numero2' é a variável que armazena este campo de entrada,
# permitindo acessar ou modificar seu conteúdo mais tarde.
entrada_numero2 = tk.Entry(janela, width=20)

# Organiza o campo de entrada na janela usando o método 'pack'.
# 'pack()' adiciona o campo de entrada logo abaixo do rótulo "Número 2:".
entrada_numero2.pack()

# Cria um rótulo para indicar onde o usuário deve selecionar a
# operação matemática desejada.
# 'tk.Label(janela, text="Selecione a operação:")' define o texto do
# rótulo como "Selecione a operação:".
# Este rótulo é usado para orientar o usuário sobre onde e como
# selecionar a operação matemática que deseja executar.
tk.Label(janela, text="Selecione a operação:").pack(pady=5)

# Cria um Combobox usando 'ttk.Combobox' que permite ao usuário escolher
# entre várias opções em uma lista dropdown.
# 'values=["soma", "subtracao", "multiplicacao", "divisao"]' define as
# operações disponíveis para seleção.
# 'state="readonly"' torna o combobox apenas para leitura, impedindo que o
# usuário digite um valor; ele pode apenas selecionar da lista.
operacao_selecionada = ttk.Combobox(janela, values=["soma", "subtracao", "multiplicacao", "divisao"], state="readonly")

# Define o valor inicial do combobox como "soma", que será a opção mostrada
# por padrão quando a janela for aberta.
operacao_selecionada.set("soma")

# Organiza o combobox na janela usando o método 'pack'.
# 'pack()' adiciona o combobox abaixo do último rótulo adicionado, com um
# espaçamento vertical conforme definido anteriormente.
operacao_selecionada.pack()

# Cria um botão para executar a operação matemática.
# 'tk.Button(janela, text="Calcular", command=calcular)' cria um botão
# na 'janela' com o texto "Calcular".
# O argumento 'command=calcular' define que, quando o botão for
# pressionado, a função 'calcular' será chamada.
# Esta função é responsável por coletar os valores dos campos de
# entrada, enviar esses valores para a API e exibir o resultado.
botao_calcular = tk.Button(janela, text="Calcular", command=calcular)

# Organiza o botão dentro da janela usando o método 'pack'.
# 'pady=10' adiciona um preenchimento vertical de 10 pixels acima e abaixo do
# botão, ajudando a separá-lo visualmente de outros elementos na interface.
botao_calcular.pack(pady=10)

# Cria um rótulo (label) para exibir o resultado da operação matemática.
# 'tk.Label(janela, text="Resultado: ", font=("Arial", 14))' cria um rótulo
# com o texto inicial "Resultado: ".
# O parâmetro 'font=("Arial", 14)' define que o texto do rótulo usará a
# fonte Arial tamanho 14, o que torna o texto maior e mais legível.
resultado_label = tk.Label(janela, text="Resultado: ", font=("Arial", 14))

# Organiza o rótulo de resultado dentro da janela usando o método 'pack'.
# 'pady=20' adiciona um preenchimento vertical de 20 pixels
# acima e abaixo do rótulo.
# Isso garante que haja um espaçamento adequado entre o rótulo de
# resultado e outros elementos da interface, melhorando a apresentação visual.
resultado_label.pack(pady=20)

# Inicia o loop da interface
janela.mainloop()