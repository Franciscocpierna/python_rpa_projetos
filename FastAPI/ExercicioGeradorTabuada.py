# Importa tkinter para criar a interface gráfica.
import tkinter as tk

# Importa messagebox para exibir mensagens de erro e
        # scrolledtext para criar uma área de texto com barra de rolagem.
from tkinter import messagebox, scrolledtext

# Importa requests para fazer requisições HTTP à API.
import requests

# Define a URL base da API para gerar a tabuada.
URL_API = "http://127.0.0.1:8000/tabuada/"


# Define a função 'gerar_tabuada' que será chamada quando o
# botão "Gerar Tabuada" for pressionado.
def gerar_tabuada():

    """
    Consome a API de tabuada e exibe o resultado.
    Esta função coleta os valores inseridos pelo usuário na interface gráfica,
    valida-os e envia uma requisição HTTP à API para gerar a tabuada.
    """

    # Obtém o valor do número digitado pelo usuário no campo de entrada.
    # O método 'get()' recupera o texto do widget Entry.
    # 'strip()' remove quaisquer espaços em branco no início e no final do texto.
    numero = entrada_numero.get().strip()

    # Obtém o valor do limite digitado pelo usuário no campo de entrada.
    # Este campo é opcional, mas o valor, se fornecido, é
    # tratado de forma semelhante ao campo de número.
    limite = entrada_limite.get().strip()

    # Validações básicas
    # Verifica se o número fornecido é válido.
    # A função 'isdigit()' retorna True se a string contém apenas
    # caracteres numéricos e não está vazia.
    # Caso contrário, exibe uma mensagem de erro ao usuário
    # indicando que o número não é válido.
    if not numero.isdigit():

        messagebox.showerror("Erro", "Por favor, insira um número válido.")

        # Encerra a execução da função para evitar
        # processar um número inválido.
        return

    # Verifica se o limite fornecido é válido, caso tenha sido preenchido.
    # O limite é opcional, mas se fornecido, deve conter apenas números inteiros positivos.
    # Caso o limite não seja um número válido, exibe uma mensagem de erro ao usuário.
    if limite and not limite.isdigit():

        messagebox.showerror("Erro", "O limite deve ser um número inteiro positivo.")

        # Encerra a execução da função para evitar processar um limite inválido.
        return

    try:

        # Monta a URL da requisição para a API.
        # Se o limite foi fornecido, inclui o parâmetro 'ate' com o valor do limite na URL.
        # Caso o limite não tenha sido preenchido, a URL não incluirá parâmetros adicionais.
        params = f"?ate={limite}" if limite else ""
        url = f"{URL_API}{numero}{params}"

        # Faz uma requisição HTTP do tipo GET para a URL gerada.
        # A função 'requests.get()' envia a requisição para o servidor da API.
        resposta = requests.get(url)

        # Verifica se a resposta HTTP indica sucesso (código de status 200).
        # Caso o código de status indique erro (4xx ou 5xx), a
        # função 'raise_for_status()' levanta uma exceção.
        resposta.raise_for_status()

        # Processa a resposta da API.
        # Converte o conteúdo JSON da resposta HTTP para um dicionário Python.
        dados = resposta.json()

        # Obtém a tabuada retornada pela API a partir do dicionário 'dados'.
        # Usa o método 'get()' para buscar a chave "tabuada".
        # Se a chave não existir, retorna um dicionário vazio.
        tabuada = dados.get("tabuada", {})

        # Converte os dados da tabuada em uma string formatada para exibição.
        # Para cada item no dicionário 'tabuada', gera uma
        # linha no formato "chave = valor".
        # 'f"{chave} = {valor}"' cria a linha, e '\n'.join() une
        # todas as linhas com quebras de linha.
        texto_resultado = "\n".join([f"{chave} = {valor}" for chave, valor in tabuada.items()])

        # Exibe o resultado na área de texto da interface gráfica.
        # Primeiro, habilita a área de texto para que seja possível modificá-la.
        area_resultado.config(state="normal")

        # Limpa qualquer conteúdo pré-existente na área de texto.
        area_resultado.delete("1.0", tk.END)

        # Insere o texto formatado da tabuada na área de texto.
        area_resultado.insert(tk.END, texto_resultado)

        # Desabilita a área de texto para evitar que o usuário
        # modifique manualmente os resultados.
        area_resultado.config(state="disabled")

    except requests.exceptions.RequestException as e:

        # Trata exceções relacionadas à requisição HTTP.
        # Caso ocorra um erro ao se conectar à API (como
        # falha de conexão ou resposta inválida),
        # exibe uma mensagem de erro ao usuário
        # com detalhes sobre a exceção.
        messagebox.showerror("Erro", f"Erro ao se conectar à API:\n{e}")


# Configuração da interface gráfica

# Inicializa a janela principal da aplicação gráfica
        # usando a biblioteca tkinter.
# 'tk.Tk()' cria uma instância da janela principal onde
        # todos os widgets serão adicionados.
janela = tk.Tk()

# Define o título da janela, que será exibido na
        # barra de título do aplicativo.
# Este título ajuda a identificar a funcionalidade
        # da aplicação para o usuário.
janela.title("Gerador de Tabuada")

# Define o tamanho fixo da janela principal como 400
        # pixels de largura por 400 pixels de altura.
# Essa configuração ajuda a garantir que todos os
        # elementos se encaixem adequadamente no layout.
janela.geometry("400x400")

# Impede que o usuário redimensione a janela tanto
        # horizontal quanto verticalmente.
# Isso garante que o layout permaneça consistente e
        # evita problemas visuais.
janela.resizable(False, False)

# Adiciona um rótulo (Label) para instruir o usuário sobre o que fazer.
# 'tk.Label()' cria um widget de texto simples exibido na janela principal 'janela'.
# O texto "Digite o número:" informa que o usuário deve inserir um número.
# A fonte usada é Arial com tamanho 12, garantindo boa legibilidade.
rotulo_numero = tk.Label(janela,
                         text="Digite o número:",
                         font=("Arial", 12))

# Posiciona o rótulo na janela principal usando o método 'pack()'.
# O parâmetro 'pady=5' adiciona um espaçamento
        # vertical de 5 pixels acima e abaixo do rótulo.
# Isso garante que o layout não fique apertado e
        # melhora a organização visual.
rotulo_numero.pack(pady=5)

# Cria um campo de entrada (Entry) para o usuário
        # inserir o número desejado.
# 'tk.Entry()' é usado para criar um campo onde o
        # texto pode ser digitado.
# O campo é adicionado à janela principal 'janela',
        # com fonte Arial e tamanho 12 para consistência visual.
# A largura do campo é definida como 20 caracteres
        # para acomodar números de vários dígitos.
entrada_numero = tk.Entry(janela,
                          font=("Arial", 12),
                          width=20)

# Posiciona o campo de entrada na janela principal
        # abaixo do rótulo.
# O método 'pack()' é utilizado novamente com 'pady=5'
        # para adicionar espaçamento vertical.
# Isso separa visualmente o campo de entrada dos
        # outros elementos da interface.
entrada_numero.pack(pady=5)

# Rótulo e entrada para o limite da tabuada

# Cria um rótulo (Label) para informar ao usuário que ele pode
        # inserir o limite da tabuada.
# O texto "Limite da tabuada (opcional):" indica que este
        # campo não é obrigatório.
# O rótulo utiliza a fonte Arial com tamanho 12 para manter a
        # consistência visual com os outros elementos.
rotulo_limite = tk.Label(janela,
                         text="Limite da tabuada (opcional):",
                         font=("Arial", 12))

# Posiciona o rótulo na interface gráfica usando o método 'pack()'.
# 'pady=5' adiciona um espaçamento vertical de 5 pixels
        # acima e abaixo do rótulo, melhorando a organização do layout.
rotulo_limite.pack(pady=5)

# Cria um campo de entrada (Entry) para o usuário
        # inserir o limite da tabuada.
# Este campo permite que o usuário digite o número
        # máximo até o qual a tabuada será gerada.
# O campo é estilizado com a fonte Arial, tamanho 12,
        # para consistência com os demais elementos visuais.
# A largura do campo é definida como 20 caracteres,
        # suficiente para números maiores.
entrada_limite = tk.Entry(janela,
                          font=("Arial", 12),
                          width=20)

# Posiciona o campo de entrada na interface logo abaixo do rótulo.
# O método 'pack()' é usado para alinhar o campo
        # centralmente e adicionar um espaçamento
        # vertical de 5 pixels ('pady=5').
entrada_limite.pack(pady=5)

# Botão para gerar a tabuada

# Cria um botão (Button) que, ao ser clicado, irá
        # executar a função 'gerar_tabuada'.
# O texto do botão é "Gerar Tabuada", indicando sua funcionalidade.
# A fonte usada no botão é Arial com tamanho 12, garantindo
        # uma boa legibilidade e mantendo o estilo visual da aplicação.
# O parâmetro 'command=gerar_tabuada' associa o clique
        # do botão à função 'gerar_tabuada',
        # que será responsável por consumir a API,
        # processar os dados e exibir o resultado.
botao_gerar = tk.Button(janela,
                        text="Gerar Tabuada",
                        font=("Arial", 12),
                        command=gerar_tabuada)

# Posiciona o botão na interface usando o método 'pack()'.
# 'pady=10' adiciona um espaçamento vertical de 10 pixels
        # acima e abaixo do botão, separando-o visualmente dos outros elementos.
botao_gerar.pack(pady=10)

# Área de texto para exibir o resultado

# Cria uma área de texto com barra de rolagem para exibir a tabuada gerada.
# 'scrolledtext.ScrolledText()' é usado para criar um widget
        # de texto com suporte embutido para rolagem vertical.
# O texto exibido usará a fonte Courier com tamanho 12,
        # ideal para exibição de dados tabulares, já que é uma fonte monoespaçada.
# A largura é definida como 30 caracteres e a altura como 10
        # linhas, proporcionando espaço suficiente para exibir a tabuada.
# 'state="disabled"' impede que o usuário edite manualmente a
        # área de texto; ela será habilitada temporariamente
        # quando os dados forem inseridos.
area_resultado = scrolledtext.ScrolledText(janela,
                                           font=("Courier", 12),
                                           width=30,
                                           height=10,
                                           state="disabled")

# Posiciona a área de texto na interface abaixo do botão.
# O método 'pack()' é usado para centralizar o widget na janela.
# 'pady=10' adiciona um espaçamento vertical de 10 pixels acima e
        # abaixo da área de texto, melhorando a organização do layout.
area_resultado.pack(pady=10)

# Rodando o loop principal da interface
janela.mainloop()