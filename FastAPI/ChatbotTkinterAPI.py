# Importa o módulo tkinter, que é uma biblioteca padrão do Python 
# usada para criar interfaces gráficas de usuário.
import tkinter as tk

# Importa a função 'messagebox' do módulo tkinter, que é usada para exibir 
# caixas de mensagem, como alertas de erro ou informações para o usuário.
from tkinter import messagebox

# Importa a biblioteca 'requests', que permite fazer requisições HTTP 
# para interagir com APIs.
import requests

# URL da API
# Define a URL base da API que será consumida. Neste caso, é o
# endpoint "/perguntar" do servidor local.
# A API deve estar em execução no endereço especificado (http://127.0.0.1:8000) 
# para que este código funcione.
URL_API = "http://127.0.0.1:8000/perguntar"


# Função para enviar a pergunta para a API
def enviar_pergunta():

    """
    Envia a pergunta para a API e exibe a resposta na interface.
    """

    # Obtém o texto da pergunta digitado pelo usuário.
    # 'entrada_pergunta.get()' captura o conteúdo do campo de entrada de texto.
    # 'strip()' remove espaços extras no início e no final da string
    # para evitar erros com entradas mal formatadas.
    pergunta = entrada_pergunta.get().strip()

    # Verifica se o usuário digitou algo no campo de entrada.
    # Caso o campo esteja vazio, exibe uma mensagem de erro
    # utilizando 'messagebox.showerror'.
    # O código retorna imediatamente para evitar 
    # processar uma entrada inválida.
    if not pergunta:

        # Exibe a mensagem de erro.
        messagebox.showerror("Erro", "Por favor, digite uma pergunta.")

        # Encerra a execução da função.
        return

    try:

        # Faz uma requisição POST para a API, enviando a pergunta do usuário.
        # O endpoint da API está definido em 'URL_API', e 
        # os dados são enviados no formato JSON.
        # A chave "texto" contém o conteúdo da pergunta digitada pelo usuário.
        resposta = requests.post(URL_API, json={"texto": pergunta})

        # Verifica se a requisição foi bem-sucedida (status HTTP 200).
        # Caso contrário, levanta uma exceção que será capturada pelo bloco 'except'.
        resposta.raise_for_status()

        # Converte o conteúdo JSON retornado pela API em um dicionário Python.
        # 'resposta.json()' transforma a resposta do servidor em 
        # um formato acessível pelo código.
        # Exemplo de resposta: {"resposta": "A capital do Brasil é Brasília."}
        dados = resposta.json()

        # Exibe a resposta da API na interface gráfica.

        # Habilita a edição do widget 'texto_resposta' para que o
        # conteúdo possa ser atualizado.
        # Por padrão, o widget está desabilitado para evitar edição manual.
        texto_resposta.config(state="normal")

        # Remove todo o texto presente no widget 'texto_resposta'.
        # O índice "1.0" representa o início do texto, e 'tk.END' indica o final.
        texto_resposta.delete("1.0", tk.END)

        # Insere a resposta retornada pela API no widget 'texto_resposta'.
        # A chave "resposta" do dicionário 'dados' contém o texto retornado pela API.
        texto_resposta.insert(tk.END, dados["resposta"])

        # Desabilita novamente o widget 'texto_resposta' para 
        # evitar edições manuais após a atualização.
        texto_resposta.config(state="disabled")

    # Captura exceções relacionadas a problemas na conexão ou requisição HTTP.
    except requests.exceptions.RequestException as e:

        # Exibe uma mensagem de erro ao usuário caso haja falha 
        # na comunicação com a API.
        # A mensagem inclui detalhes sobre o erro para ajudar
        # na identificação do problema.
        messagebox.showerror("Erro", f"Erro ao se conectar à API:\n{e}")

    # Captura exceções relacionadas à ausência de chaves no
    # dicionário retornado pela API.
    except KeyError:

        # Exibe uma mensagem de erro caso o dicionário retornado 
        # pela API não contenha a chave esperada "resposta".
        # Isso pode indicar um problema na resposta da API ou na
        # lógica de processamento.
        messagebox.showerror("Erro", "Erro ao processar a resposta da API.")


# Criação da janela principal
# Cria uma instância da janela principal da aplicação gráfica usando o Tkinter.
# 'tk.Tk()' é a classe que representa a janela da aplicação, 
# onde todos os componentes da interface serão adicionados.
janela = tk.Tk()

# Define o título da janela
# A função 'title()' define o texto que será exibido na
# barra de título da janela.
# Isso ajuda a identificar a funcionalidade da 
# aplicação para o usuário.
janela.title("Chatbot com Tkinter e API")

# Define as dimensões da janela
# A função 'geometry()' define o tamanho da janela em pixels.
# Neste caso, a janela terá 500 pixels de largura e 400 pixels de altura.
# Isso cria uma janela de tamanho fixo e controlado para a aplicação.
janela.geometry("500x400")

# Impede que o usuário redimensione a janela
# 'resizable(False, False)' impede a alteração do tamanho da
# janela, tanto na direção horizontal quanto vertical.
# Isso ajuda a manter o layout da interface consistente e evita
# problemas de adaptação com a interface.
janela.resizable(False, False)

# Rótulo para o campo de pergunta
# Cria um rótulo (Label) que será exibido na interface gráfica.
# O rótulo é um widget de texto simples.
# 'text="Digite sua pergunta:"' é o texto que será exibido no rótulo.
# 'font=("Arial", 12)' define a fonte e o tamanho do texto. 
# A fonte Arial é usada com tamanho 12 para legibilidade.
rotulo_pergunta = tk.Label(janela,
                           text="Digite sua pergunta:",
                           font=("Arial", 12))

# Posiciona o rótulo na janela
# 'pack()' é usado para posicionar o widget na janela. 
# Ele organiza o layout automaticamente.
# O parâmetro 'pady=10' adiciona um espaçamento de 10 pixels 
# acima e abaixo do rótulo, para garantir que o
# layout não fique sobrecarregado.
rotulo_pergunta.pack(pady=10)

# Campo de entrada para a pergunta
# Cria um campo de entrada (Entry) onde o usuário pode
# digitar a pergunta que deseja fazer.
# 'font=("Arial", 12)' define a fonte do texto dentro do campo de entrada.
# O tamanho da fonte é 12, o que torna o texto legível.
# 'width=50' define a largura do campo de entrada para acomodar um 
# número maior de caracteres, nesse caso, até 50 caracteres visíveis na tela.
entrada_pergunta = tk.Entry(janela,
                            font=("Arial", 12),
                            width=50)

# Posiciona o campo de entrada na janela usando 'pack()'.
# 'pady=5' adiciona um espaçamento vertical de 5 pixels
# acima e abaixo do campo de entrada.
# Isso ajuda a manter o layout organizado e evita que o
# campo fique muito próximo de outros elementos.
entrada_pergunta.pack(pady=5)

# Botão para enviar a pergunta
# Cria um botão (Button) que o usuário pode clicar para
# enviar a pergunta para a API.
# O texto do botão é "Enviar", que indica a ação que será
# realizada ao clicar nele.
# 'font=("Arial", 12)' define a fonte do texto no botão, 
# com tamanho 12 para legibilidade.
# O parâmetro 'command=enviar_pergunta' vincula a função 'enviar_pergunta' 
# ao evento de clique do botão.
# Quando o botão for clicado, a função 'enviar_pergunta' será 
# chamada para processar a pergunta e mostrar a resposta.
botao_enviar = tk.Button(janela,
                         text="Enviar",
                         font=("Arial", 12),
                         command=enviar_pergunta)

# Posiciona o botão na janela usando 'pack()'.
# 'pady=10' adiciona um espaçamento vertical de 10 pixels ao 
# redor do botão, para dar mais destaque e separar o botão de outros elementos.
botao_enviar.pack(pady=10)

# Rótulo para o campo de resposta
# Cria um rótulo (Label) que informa ao usuário que a área
# abaixo será a resposta da API.
# O texto exibido no rótulo é "Resposta:", o que instrui o usuário
# sobre onde será exibido o conteúdo retornado.
# 'font=("Arial", 12)' define a fonte do texto do rótulo como Arial, 
# com tamanho 12, para garantir legibilidade.
rotulo_resposta = tk.Label(janela,
                           text="Resposta:",
                           font=("Arial", 12))

# Posiciona o rótulo na janela utilizando o método 'pack()'.
# 'pady=10' adiciona 10 pixels de espaçamento vertical antes e
# depois do rótulo, garantindo que ele não fique
# muito perto de outros elementos.
rotulo_resposta.pack(pady=10)

# Campo de texto para exibir a resposta
# Cria uma área de texto (Text) onde a resposta da API será exibida.
# 'font=("Arial", 12)' define a fonte do texto exibido como Arial, tamanho 12,
# para garantir que a resposta seja legível.
# 'height=10' e 'width=50' definem a altura e a largura do campo de texto. 
# Com esses valores, o campo pode exibir até 10 linhas de
# texto e 50 caracteres por linha.
# 'state="disabled"' impede que o usuário edite diretamente o campo de texto.
# A ideia é que a área de resposta seja somente para visualização.
# 'wrap="word"' garante que o texto na área de texto seja quebrado 
# automaticamente nas palavras (não cortando palavras
# no meio), facilitando a leitura.
texto_resposta = tk.Text(janela,
                         font=("Arial", 12),
                         height=10,
                         width=50,
                         state="disabled",
                         wrap="word")

# Posiciona o campo de texto na janela utilizando o método 'pack()'.
# 'pady=5' adiciona 5 pixels de espaçamento vertical antes e
# depois da área de texto, ajudando a organizar o layout visualmente.
texto_resposta.pack(pady=5)

# Inicia o loop principal da interface
janela.mainloop()