# Importa a biblioteca tkinter para criação de interfaces gráficas
import tkinter as tk

# Importa submódulos do tkinter para uso de widgets avançados e caixas de mensagem
from tkinter import ttk, messagebox

# Importa DateEntry do módulo tkcalendar, que é um widget para seleção de datas
from tkcalendar import DateEntry

# Importa MongoClient de pymongo, que é usado para conectar 
        # com o banco de dados MongoDB
from pymongo import MongoClient

# Importa ObjectId de bson, usado para manipular os IDs do MongoDB
from bson.objectid import ObjectId

# Importa o módulo pandas, que é usado para manipulação e análise de dados
import pandas as pd

# Importa o módulo datetime para manipulação de datas e horários
import datetime

# Importa o módulo bcrypt, que é usado para hashing de senhas
import bcrypt

# Estabelece uma conexão com o servidor MongoDB local na 
        # porta 27017 (porta padrão do MongoDB)
cliente = MongoClient("mongodb://localhost:27017/")


# Seleciona o banco de dados chamado 'Controle_de_Estoque foi mudado para 'ControledeEstoque'
banco = cliente["ControledeEstoque"]

# Dentro do banco de dados, seleciona a coleção 'produtos'
colecao_produtos = banco["produtos"]

# Dentro do banco de dados, seleciona a coleção 'movimentacoes'
colecao_movimentacoes = banco["movimentacoes"]

# Dentro do banco de dados, seleciona a coleção 'usuarios'
colecao_usuarios = banco["usuarios"]


# Esta função tem como objetivo criar um usuário administrador
        # padrão no sistema caso ele ainda não exista.
def criar_usuario_admin():
    
    # Primeiro, verifica se já existe um usuário com o nome "admin" na base de dados.
    # O método `count_documents` conta quantos documentos na 
            # coleção 'usuarios' atendem ao critério especificado.
    # Aqui, o critério é que o campo "username" deve ser igual a "admin".
    if colecao_usuarios.count_documents({"username": "admin"}) == 0:
        
        # Se não existir nenhum usuário "admin", definimos uma senha para ele.
        # 'admin123' é a senha escolhida nesse exemplo.
        senha = "admin123"
        
        # Aqui usamos a biblioteca bcrypt para criar uma versão segura da senha.
        # `encode('utf-8')` converte a senha de texto para uma sequência 
                # de bytes, pois bcrypt trabalha com bytes.
        # `bcrypt.gensalt()` gera um "salt" aleatório que será usado para 
                # aumentar a segurança do hash.
        # O "salt" é um valor aleatório que é adicionado à senha antes do 
                # processo de hashing para prevenir ataques de dicionário.
        hashed = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        
        # Inserimos um novo documento na coleção 'usuarios' com três campos:
        # "username" que é o nome do usuário,
        # "password" que é a senha hasheada (versão segura da senha),
        # e "plain_password" que é a senha em texto plano.
        # Armazenar senhas em texto plano é uma prática insegura porque qualquer 
                # um com acesso ao banco de dados pode lê-las.
        colecao_usuarios.insert_one({
            "username": "admin",
            "password": hashed,
            "plain_password": senha  # Incluir a senha em texto plano é para fins educativos, mas não é recomendado em produção.
        })


# Esta função é responsável por verificar as credenciais
        # de login de um usuário.
def verificar_login():
    
    # Obtém o nome de usuário inserido no campo de entrada 'entrada_usuario'.
    username = entrada_usuario.get()
    
    # Obtém a senha inserida no campo de entrada 'entrada_senha'.
    senha = entrada_senha.get()

    # Verifica se os campos de nome de usuário e senha não estão vazios.
    if not username or not senha:
        
        # Exibe uma mensagem de erro se algum dos campos estiver vazio.
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
        
        # Encerra a função sem fazer mais nada se os campos estiverem vazios.
        return

    # Busca na coleção de usuários um documento onde o campo "username" 
            # corresponde ao nome de usuário inserido.
    usuario = colecao_usuarios.find_one({"username": username})

    # Verifica se um usuário foi encontrado e se a senha inserida, 
            # quando codificada e comparada,
            # corresponde à senha hasheada armazenada no banco de dados.
    if usuario and bcrypt.checkpw(senha.encode('utf-8'), usuario["password"]):
        
        # Se as credenciais estiverem corretas, exibe uma mensagem de boas-vindas.
        messagebox.showinfo("Sucesso", f"Bem-vindo, {username}!")
        
        # Destrói a janela de login para não ser mais acessível após o login.
        janela_login.destroy()
        
        # Chama a função para abrir a janela principal do sistema após o login.
        abrir_janela_principal()
        
    else:
        
        # Se as credenciais não estiverem corretas, exibe uma mensagem de erro.
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")



# Define uma função chamada 'adicionar_produto' que é responsável por
        # adicionar um novo produto ao estoque no banco de dados.
def adicionar_produto():
    
    """Adiciona um novo produto ao estoque."""
    
    # Obtém o texto inserido no campo de entrada para o nome do produto.
    nome = entrada_nome.get()
    
    # Obtém o texto inserido no campo de entrada para o preço do produto.
    preco = entrada_preco.get()
    
    # Obtém o texto inserido no campo de entrada para a 
            # quantidade do produto em estoque.
    quantidade = entrada_quantidade.get()
    
    # Obtém o texto inserido no campo de entrada para o 
            # fornecedor do produto.
    fornecedor = entrada_fornecedor.get()
    
    # Verifica se algum dos campos de entrada está vazio. Todos os 
            # campos são obrigatórios.
    if not nome or not preco or not quantidade or not fornecedor:
    
        # Se algum campo estiver vazio, mostra uma mensagem de erro ao usuário.
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        
        # Encerra a função e retorna sem adicionar o produto, 
                # pois há campos não preenchidos.
        return


    # Tenta converter o preço e a quantidade para os tipos 
            # numéricos apropriados.
    try:
    
        # Converte o preço para um número de ponto flutuante.
        preco = float(preco)
        
        # Converte a quantidade para um inteiro.
        quantidade = int(quantidade)
    
    except ValueError:
    
        # Se ocorrer um erro na conversão, exibe uma mensagem de 
                # erro indicando o problema.
        messagebox.showerror("Erro", "Preço deve ser um número e quantidade deve ser um inteiro!")
        
        # Encerra a função e retorna sem adicionar o produto 
                # ao banco de dados.
        return
    
    # Insere o novo produto na coleção 'produtos' no banco de dados.
    colecao_produtos.insert_one({
        "nome": nome,  # Nome do produto.
        "preco": preco,  # Preço do produto convertido para float.
        "quantidade": quantidade,  # Quantidade do produto convertida para int.
        "fornecedor": fornecedor  # Nome do fornecedor do produto.
    })
    
    # Registra a movimentação do novo produto como uma entrada no estoque.
    registrar_movimentacao(nome, "Entrada", quantidade)
    
    # Exibe uma mensagem de sucesso informando que o produto 
            # foi cadastrado com sucesso.
    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
    
    # Recarrega os dados da Treeview para atualizar a lista de 
            # produtos com o novo produto adicionado.
    carregar_dados()
    
    # Limpa os campos de entrada após o cadastro do produto para que o 
            # usuário possa inserir novos produtos sem ter que apagar manualmente.
    limpar_campos()


def registrar_movimentacao(produto, tipo, quantidade):
    
    """
    Registra uma movimentação de produto no banco de dados.
    
    Args:
        produto (str): Nome do produto que está sendo movimentado.
        tipo (str): Tipo de movimentação, como 'Entrada' ou 'Saída'.
        quantidade (int): Quantidade do produto movimentado.
    """
    
    # Obtém a data e hora atual do sistema e formata para uma string no 
            # formato ano-mês-dia hora:minuto:segundo.
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Insere um novo documento na coleção 'movimentacoes' no banco de 
            # dados com as informações da movimentação.
    # O documento contém:
    # - 'produto': nome do produto movimentado.
    # - 'tipo': tipo da movimentação ('Entrada' ou 'Saída').
    # - 'quantidade': quantidade de produto movimentado.
    # - 'data': data e hora exata da movimentação.
    colecao_movimentacoes.insert_one({
        "produto": produto,  # Nome do produto.
        "tipo": tipo,        # Tipo de movimentação.
        "quantidade": quantidade,  # Quantidade do produto movimentado.
        "data": data_atual   # Data e hora da movimentação.
    })    


def limpar_campos():
    
    """Limpa os campos de entrada."""
    
    # Remove todo o texto que está no campo de entrada "Nome".
    # 'entrada_nome.delete(0, tk.END)' significa que o conteúdo será apagado 
    # desde o primeiro caractere (índice 0) até o final do campo (tk.END).
    entrada_nome.delete(0, tk.END)
    
    # Remove todo o texto que está no campo de entrada "Preço".
    # O comportamento é o mesmo que no campo anterior: apaga todo o conteúdo.
    entrada_preco.delete(0, tk.END)
    
    # Remove todo o texto que está no campo de entrada "Quantidade".
    # Garante que o campo fique completamente limpo.
    entrada_quantidade.delete(0, tk.END)
    
    # Remove todo o texto que está no campo de entrada "Fornecedor".
    # Deixa o campo vazio, pronto para receber novos dados.
    entrada_fornecedor.delete(0, tk.END)
    

def dar_baixa_produto():
    
    """
    Dá baixa no estoque do produto selecionado, subtraindo a quantidade especificada
    do estoque atual do produto.
    """
    
    # Obtém o item selecionado na Treeview de produtos.
    selecionado = tree_produtos.selection()
    
    # Verifica se um produto foi realmente selecionado.
    if not selecionado:
    
        # Exibe uma mensagem de erro se nenhum produto for selecionado.
        messagebox.showerror("Erro", "Selecione um produto para dar baixa!")
        
        # Interrompe a função, pois um produto precisa ser 
                # selecionado para continuar.
        return

    # Obtém os dados do item selecionado na Treeview.
    item = tree_produtos.item(selecionado)
    
    # Extrai o ID do documento no banco de dados associado ao produto selecionado.
    doc_id = item["values"][4]
    
    # Extrai o nome do produto do item selecionado para uso em registros ou mensagens.
    nome_produto = item["values"][0]
    
    # Converte a quantidade atual do produto para um inteiro.
    quantidade_atual = int(item["values"][2])
    
    # Obtém a quantidade a ser dada baixa do campo de entrada e armazena como string.
    quantidade_baixa = entrada_quantidade.get()

    # Verifica se a quantidade para dar baixa foi inserida.
    if not quantidade_baixa:
        
        # Exibe uma mensagem de erro se a quantidade não for informada.
        messagebox.showerror("Erro", "Informe a quantidade para dar baixa!")
        
        # Interrompe a função, pois a quantidade é necessária para proceder.
        return


    # Tenta converter a quantidade para baixa, inserida pelo 
            # usuário, de string para inteiro.
    try:
        
        quantidade_baixa = int(quantidade_baixa)
        
    except ValueError:
        
        # Caso a conversão falhe porque o valor inserido não é um 
                # número inteiro válido, mostra uma mensagem de erro.
        messagebox.showerror("Erro", "Quantidade para dar baixa deve ser um número inteiro!")
        
        # Interrompe a função, pois a quantidade para baixa precisa 
                # ser um número inteiro para proceder.
        return

    # Verifica se a quantidade para baixa é maior que a 
            # quantidade atual no estoque.
    if quantidade_baixa > quantidade_atual:
        
        # Se a quantidade para baixa for maior que o estoque 
                # disponível, mostra uma mensagem de erro.
        messagebox.showerror("Erro", "Quantidade insuficiente no estoque!")
        
        # Interrompe a função, pois não é possível dar baixa em uma 
                # quantidade maior que o estoque.
        return


    # Calcula a nova quantidade de produtos no estoque após a baixa.
    # A nova quantidade é obtida subtraindo a quantidade 
            # para baixa da quantidade atual.
    nova_quantidade = quantidade_atual - quantidade_baixa

    # Atualiza o documento do produto no banco de dados com a nova quantidade.
    # A busca é feita pelo ID do documento ("_id"), garantindo 
            # que apenas o produto correto será atualizado.
    # O operador "$set" atualiza apenas o campo "quantidade" no documento.
    colecao_produtos.update_one({"_id": ObjectId(doc_id)}, {"$set": {"quantidade": nova_quantidade}})
    
    # Registra a movimentação de saída no banco de dados.
    # A função 'registrar_movimentacao' é chamada com:
    # - o nome do produto,
    # - o tipo de movimentação ("Saída"),
    # - e a quantidade dada baixa.
    registrar_movimentacao(nome_produto, "Saída", quantidade_baixa)
    
    # Exibe uma mensagem informando que a operação foi realizada com sucesso.
    # A mensagem inclui a quantidade de unidades baixadas 
            # para feedback ao usuário.
    messagebox.showinfo("Sucesso", f"Baixa de {quantidade_baixa} unidade(s) realizada com sucesso!")
    
    # Recarrega os dados da Treeview para atualizar a lista de 
            # produtos e refletir a nova quantidade no estoque.
    carregar_dados()
    
    # Limpa os campos de entrada para que o usuário possa realizar 
            # outra operação sem ter que limpar os campos manualmente.
    limpar_campos()



def exibir_movimentacoes():
    
    """Exibe o histórico de movimentações em uma nova janela."""
    
    # Cria uma nova janela (Toplevel) chamada 'janela_movimentacoes', 
            # que é independente da janela principal.
    # Esta janela será usada para exibir o histórico de movimentações.
    janela_movimentacoes = tk.Toplevel(janela_principal)
    
    # Define o título da nova janela como "Histórico de Movimentações".
    janela_movimentacoes.title("Histórico de Movimentações")
    
    # Define as dimensões iniciais da janela como 1000 pixels de 
            # largura por 600 pixels de altura.
    janela_movimentacoes.geometry("1000x600")
    
    # Impede que o usuário redimensione a janela manualmente.
    # 'False, False' significa que a largura e a altura não podem ser alteradas.
    janela_movimentacoes.resizable(False, False)

    # Centraliza a janela na tela para melhorar a experiência 
            # visual do usuário.
    # Atualiza as dimensões internas da janela para garantir que 
            # todos os widgets já carregados sejam considerados.
    janela_movimentacoes.update_idletasks()
    
    # Obtém a largura atual da janela (após todos os ajustes internos).
    width = janela_movimentacoes.winfo_width()
    
    # Obtém a altura atual da janela.
    height = janela_movimentacoes.winfo_height()
    
    # Calcula a posição X para centralizar a janela horizontalmente na tela.
    # A posição é obtida subtraindo metade da largura da 
            # janela da largura total da tela.
    x = (janela_movimentacoes.winfo_screenwidth() // 2) - (width // 2)
    
    # Calcula a posição Y para centralizar a janela verticalmente na tela.
    # A posição é obtida subtraindo metade da altura da 
            # janela da altura total da tela.
    y = (janela_movimentacoes.winfo_screenheight() // 2) - (height // 2)
    
    # Define a posição final da janela para que ela apareça centralizada na tela.
    # A posição é definida usando um formato especial de string: 
            # largura x altura + posição_x + posição_y.
    janela_movimentacoes.geometry(f"{width}x{height}+{x}+{y}")


    # Cria um frame (contêiner) dentro da janela de movimentações, 
            # que será usado para organizar os campos de filtro.
    # 'pady=10' adiciona um espaço vertical ao redor do frame, 
            # separando-o de outros elementos na interface.
    frame_filtros = tk.Frame(janela_movimentacoes, pady=10)
    
    # Empacota o frame de filtros dentro da janela de movimentações.
    # O método 'pack()' é usado para posicionar o frame no layout da janela.
    frame_filtros.pack()
    
    # Adiciona um rótulo (label) ao frame de filtros para indicar o 
            # propósito do campo de entrada (filtro por produto).
    # 'text="Produto:"' define o texto exibido no rótulo.
    # 'font=("Helvetica", 12)' define o estilo e tamanho da fonte 
            # usada no texto do rótulo.
    # 'grid(row=0, column=0, padx=5)' posiciona o rótulo na primeira 
            # linha (linha 0) e primeira coluna (coluna 0) do layout em grade.
    # 'padx=5' adiciona um espaço horizontal ao redor do rótulo, melhorando a estética.
    tk.Label(frame_filtros, text="Produto:", 
             font=("Helvetica", 12)).grid(row=0, column=0, padx=5)
    
    # Cria um campo de entrada (Entry) no frame de filtros, 
            # permitindo ao usuário digitar o nome de um produto para filtrar.
    # 'font=("Helvetica", 12)' define o estilo e tamanho do 
            # texto digitado no campo de entrada.
    entrada_filtro_produto = tk.Entry(frame_filtros, 
                                      font=("Helvetica", 12))
    
    # Posiciona o campo de entrada ao lado do rótulo no layout em grade.
    # 'grid(row=0, column=1, padx=5)' coloca o campo de entrada 
            # na primeira linha (linha 0) e segunda coluna (coluna 1).
    # 'padx=5' adiciona um espaço horizontal entre o campo de 
            # entrada e outros elementos, melhorando a disposição visual.
    entrada_filtro_produto.grid(row=0, column=1, padx=5)


    # Adiciona um rótulo (label) ao frame de filtros para indicar o
            # filtro pelo tipo de movimentação.
    # 'text="Tipo:"' especifica que o campo se refere ao tipo da
            # movimentação, como "Entrada" ou "Saída".
    # 'font=("Helvetica", 12)' define o estilo e tamanho do texto no rótulo.
    # 'grid(row=0, column=2, padx=5)' posiciona o rótulo na primeira 
            # linha (linha 0) e terceira coluna (coluna 2) do layout.
    # 'padx=5' adiciona espaçamento horizontal ao redor do rótulo
            # para melhorar a organização visual.
    tk.Label(frame_filtros, 
             text="Tipo:", 
             font=("Helvetica", 12)).grid(row=0, column=2, padx=5)
    
    # Cria um campo de entrada (Entry) para que o usuário 
            # digite o tipo de movimentação.
    # O tipo pode ser, por exemplo, "Entrada" ou "Saída".
    # 'font=("Helvetica", 12)' especifica o estilo e tamanho da
            # fonte para o texto digitado no campo.
    entrada_filtro_tipo = tk.Entry(frame_filtros, font=("Helvetica", 12))
    
    # Posiciona o campo de entrada no layout em grade, na 
            # primeira linha e quarta coluna (coluna 3).
    # 'grid(row=0, column=3, padx=5)' coloca o campo ao lado do rótulo "Tipo:".
    # 'padx=5' adiciona espaçamento horizontal entre o campo 
            # de entrada e outros elementos.
    entrada_filtro_tipo.grid(row=0, column=3, padx=5)
    
    # Adiciona um rótulo (label) ao frame de filtros para 
            # indicar o filtro por data inicial.
    # 'text="Data Inicial:"' informa que o campo abaixo é para 
            # selecionar uma data inicial no filtro.
    # 'font=("Helvetica", 12)' define o estilo e tamanho do texto no rótulo.
    # 'grid(row=1, column=0, padx=5)' posiciona o rótulo na
            # segunda linha (linha 1) e primeira coluna (coluna 0).
    # 'padx=5' adiciona espaçamento horizontal ao redor do rótulo.
    tk.Label(frame_filtros, 
             text="Data Inicial:", 
             font=("Helvetica", 12)).grid(row=1, column=0, padx=5)
    
    # Cria um campo de entrada de data com um seletor de calendário.
    # 'DateEntry' é um widget que permite ao usuário selecionar 
            # uma data em um formato específico.
    # 'font=("Helvetica", 12)' define o estilo e tamanho da fonte no campo de entrada.
    # 'date_pattern="yyyy-MM-dd"' configura o formato da 
            # data para "ano-mês-dia".
    entrada_data_inicial = DateEntry(frame_filtros, 
                                     font=("Helvetica", 12), date_pattern='yyyy-MM-dd')
    
    # Posiciona o campo de entrada de data inicial no layout em 
            # grade, na segunda linha e segunda coluna (coluna 1).
    # 'grid(row=1, column=1, padx=5)' coloca o campo ao 
            # lado do rótulo "Data Inicial:".
    # 'padx=5' adiciona espaçamento horizontal para manter 
            # uma organização visual consistente.
    entrada_data_inicial.grid(row=1, column=1, padx=5)


    # Adiciona um rótulo (label) ao frame de filtros para 
            # indicar o filtro pela data final.
    # 'text="Data Final:"' informa que o campo ao lado é para 
            # selecionar a data final do filtro.
    # 'font=("Helvetica", 12)' define o estilo e tamanho da fonte usada no texto do rótulo.
    # 'grid(row=1, column=2, padx=5)' posiciona o rótulo na segunda 
            # linha (linha 1) e terceira coluna (coluna 2) do layout em grade.
    # 'padx=5' adiciona espaçamento horizontal ao redor do rótulo, 
            # melhorando o alinhamento visual.
    tk.Label(frame_filtros, 
             text="Data Final:", 
             font=("Helvetica", 12)).grid(row=1, column=2, padx=5)
    
    # Cria um campo de entrada de data com seletor de calendário para a data final.
    # 'DateEntry' permite que o usuário selecione uma data no 
            # formato "ano-mês-dia" ('yyyy-MM-dd').
    # 'font=("Helvetica", 12)' define o estilo e tamanho do 
            # texto exibido no campo de entrada.
    entrada_data_final = DateEntry(frame_filtros, 
                                   font=("Helvetica", 12), 
                                   date_pattern='yyyy-MM-dd')
    
    # Posiciona o campo de entrada de data final no layout em grade.
    # 'grid(row=1, column=3, padx=5)' coloca o campo de entrada 
            # ao lado do rótulo "Data Final:".
    # 'padx=5' adiciona espaçamento horizontal para manter a consistência visual.
    entrada_data_final.grid(row=1, column=3, padx=5)
    
    # Cria um botão que permite aplicar os filtros configurados pelo usuário.
    # 'text="Aplicar Filtro"' define o texto exibido no botão.
    # 'command=lambda: carregar_movimentacoes()' vincula o 
            # botão à função 'carregar_movimentacoes', 
            # que será chamada quando o botão for clicado. O uso de `lambda` 
            # permite passar filtros posteriormente.
    # 'bg="#2a9d8f"' define a cor de fundo do botão como um tom de verde-azulado.
    # 'fg="white"' define a cor do texto do botão como branco.
    # 'font=("Helvetica", 12)' define o estilo e tamanho da 
            # fonte usada no texto do botão.
    btn_aplicar_filtro = tk.Button(frame_filtros, 
                                   text="Aplicar Filtro", 
                                   command=lambda: carregar_movimentacoes(), 
                                   bg="#2a9d8f", 
                                   fg="white", 
                                   font=("Helvetica", 12))
    
    # Posiciona o botão "Aplicar Filtro" no layout em grade.
    # 'grid(row=0, column=4, rowspan=2, padx=5, pady=5)' coloca o 
            # botão na primeira linha (linha 0) e quinta coluna (coluna 4),
            # e faz o botão ocupar duas linhas verticalmente (com 'rowspan=2').
    # 'padx=5' e 'pady=5' adicionam espaçamento horizontal e vertical 
            # ao redor do botão para melhorar sua aparência.
    btn_aplicar_filtro.grid(row=0, 
                            column=4, 
                            rowspan=2, 
                            padx=5, 
                            pady=5)


    # Cria um frame (contêiner) dentro da janela de movimentações 
            # para organizar o contador de registros e o botão de exportar.
    # 'pady=10' adiciona um espaçamento vertical ao redor do 
            # frame, separando-o de outros elementos da interface.
    frame_utilitarios = tk.Frame(janela_movimentacoes, pady=10)
    
    # Empacota o frame de utilitários dentro da janela de movimentações.
    # 'pack()' organiza o frame no layout da janela.
    frame_utilitarios.pack()
    
    # Cria um rótulo (label) dentro do frame para exibir o 
            # total de registros de movimentações.
    # 'text="Total de registros: 0"' inicializa o rótulo com a 
            # mensagem padrão indicando que o total de registros é zero.
    # 'font=("Helvetica", 12)' define o estilo e tamanho da 
            # fonte do texto exibido no rótulo.
    lbl_total_registros = tk.Label(frame_utilitarios, 
                                   text="Total de registros: 0", 
                                   font=("Helvetica", 12))
    
    # Empacota o rótulo dentro do frame de utilitários.
    # 'side="left"' posiciona o rótulo no lado esquerdo do frame.
    # 'padx=10' adiciona um espaçamento horizontal de 10 pixels ao redor do rótulo.
    lbl_total_registros.pack(side="left", padx=10)
    
    # Cria um botão dentro do frame para exportar os dados das 
            # movimentações para um arquivo Excel.
    # 'text="Exportar para Excel"' define o texto exibido no botão.
    # 'command=lambda: exportar_movimentacoes()' vincula o botão à 
            # função 'exportar_movimentacoes',
            # que será chamada quando o botão for clicado.
    # 'bg="#6a994e"' define a cor de fundo do botão como um tom de verde.
    # 'fg="white"' define a cor do texto do botão como branco.
    # 'font=("Helvetica", 12)' define o estilo e tamanho do texto no botão.
    btn_exportar = tk.Button(frame_utilitarios, 
                             text="Exportar para Excel", 
                             command=lambda: exportar_movimentacoes(), 
                             bg="#6a994e", 
                             fg="white", 
                             font=("Helvetica", 12))
    
    # Empacota o botão dentro do frame de utilitários.
    # 'side="right"' posiciona o botão no lado direito do frame.
    # 'padx=10' adiciona um espaçamento horizontal de 10 pixels ao redor do botão.
    btn_exportar.pack(side="right", padx=10)


    # Cria uma árvore de visualização (Treeview) dentro da janela de movimentações.
    # 'janela_movimentacoes' é o contêiner pai onde a Treeview será exibida.
    # 'columns=("Produto", "Tipo", "Quantidade", "Data")' define as colunas 
            # que serão exibidas, com os identificadores "Produto", "Tipo", "Quantidade" e "Data".
    # 'show="headings"' exibe apenas os cabeçalhos das colunas, 
            # sem a coluna de índice padrão.
    tree_mov = ttk.Treeview(janela_movimentacoes, 
                            columns=("Produto", "Tipo", "Quantidade", "Data"), 
                            show="headings")
    
    # Configura o cabeçalho e o título da coluna "Produto".
    # 'text="Produto"' define o texto do cabeçalho para a coluna "Produto".
    tree_mov.heading("Produto", text="Produto")
    
    # Configura o cabeçalho e o título da coluna "Tipo".
    # 'text="Tipo"' define o texto do cabeçalho para a coluna "Tipo".
    tree_mov.heading("Tipo", text="Tipo")
    
    # Configura o cabeçalho e o título da coluna "Quantidade".
    # 'text="Quantidade"' define o texto do cabeçalho para a coluna "Quantidade".
    tree_mov.heading("Quantidade", text="Quantidade")
    
    # Configura o cabeçalho e o título da coluna "Data".
    # 'text="Data"' define o texto do cabeçalho para a coluna "Data".
    tree_mov.heading("Data", text="Data")
    
    # Configura a largura e o alinhamento do conteúdo da coluna "Produto".
    # 'width=200' define a largura da coluna em 200 pixels.
    # 'anchor="w"' alinha o texto da coluna à esquerda ("west").
    tree_mov.column("Produto", width=200, anchor="w")
    
    # Configura a largura e o alinhamento do conteúdo da coluna "Tipo".
    # 'width=100' define a largura da coluna em 100 pixels.
    # 'anchor="center"' alinha o texto da coluna ao centro.
    tree_mov.column("Tipo", width=100, anchor="center")
    
    # Configura a largura e o alinhamento do conteúdo da coluna "Quantidade".
    # 'width=100' define a largura da coluna em 100 pixels.
    # 'anchor="center"' alinha o texto da coluna ao centro.
    tree_mov.column("Quantidade", width=100, anchor="center")
    
    # Configura a largura e o alinhamento do conteúdo da coluna "Data".
    # 'width=200' define a largura da coluna em 200 pixels.
    # 'anchor="center"' alinha o texto da coluna ao centro.
    tree_mov.column("Data", width=200, anchor="center")
    
    # Empacota a Treeview dentro da janela de movimentações.
    # 'fill="both"' faz com que a Treeview se expanda para preencher 
            # todo o espaço disponível horizontal e verticalmente.
    # 'expand=True' permite que a Treeview ocupe qualquer espaço 
            # adicional na janela, ajustando-se dinamicamente.
    tree_mov.pack(fill="both", expand=True)

    
    # Define a função para carregar as movimentações na Treeview, 
            # aplicando filtros se necessário.
    def carregar_movimentacoes():
        
        # Remove todos os itens da Treeview para garantir que os 
                # novos dados não sejam adicionados em duplicidade.
        for item in tree_mov.get_children():
            tree_mov.delete(item)
    
        # Inicializa um dicionário vazio para armazenar os filtros de busca.
        filtro = {}
        
        # Obtém o texto inserido no campo de filtro de produto e 
                # remove espaços em branco desnecessários.
        produto = entrada_filtro_produto.get().strip()
        
        # Obtém o texto inserido no campo de filtro de tipo e remove 
                # espaços em branco desnecessários.
        tipo = entrada_filtro_tipo.get().strip()
        
        # Obtém a data inicial selecionada no campo de data inicial.
        data_inicial = entrada_data_inicial.get_date()
        
        # Obtém a data final selecionada no campo de data final.
        data_final = entrada_data_final.get_date()
    
        # Adiciona um filtro para o nome do produto se o usuário 
                # digitou algo no campo.
        # "$regex" permite buscar produtos que contenham o texto inserido, 
                # ignorando maiúsculas e minúsculas.
        if produto:
            filtro["produto"] = {"$regex": produto, "$options": "i"}
        
        # Adiciona um filtro para o tipo de movimentação se o usuário digitou algo no campo.
        # "$regex" faz uma busca flexível com o texto inserido, ignorando 
                # diferenças de maiúsculas e minúsculas.
        if tipo:
            filtro["tipo"] = {"$regex": tipo, "$options": "i"}
        
        # Adiciona um filtro para a data se o usuário selecionou uma 
                # data inicial ou final.
        if data_inicial or data_final:
            
            # Inicializa um filtro para o campo "data" no dicionário de filtros.
            filtro["data"] = {}
            
            # Adiciona a data inicial ao filtro, garantindo que as 
                    # movimentações ocorridas após ou no dia da data 
                    # inicial sejam incluídas.
            if data_inicial:
                filtro["data"]["$gte"] = data_inicial.strftime("%Y-%m-%d")
            
            # Adiciona a data final ao filtro, garantindo que as 
                    # movimentações ocorridas antes ou no dia da 
                    # data final sejam incluídas.
            if data_final:
                filtro["data"]["$lte"] = data_final.strftime("%Y-%m-%d") + " 23:59:59"
    
        # Busca os registros no banco de dados MongoDB usando os filtros configurados.
        # '.sort("data", 1)' ordena os registros pela data em ordem crescente.
        registros = colecao_movimentacoes.find(filtro).sort("data", 1)
        
        # Inicializa um contador para rastrear o total de registros encontrados.
        total = 0
        
        # Itera sobre os registros retornados pela busca no banco de dados.
        for doc in registros:
            
            # Insere cada registro na Treeview com os valores das 
                    # colunas correspondentes.
            tree_mov.insert("", "end", values=(doc["produto"], doc["tipo"], doc["quantidade"], doc["data"]))
            
            # Incrementa o contador de registros.
            total += 1
    
        # Atualiza o rótulo (label) que exibe o total de registros encontrados.
        lbl_total_registros.config(text=f"Total de registros: {total}")

            

    # Define a função para exportar as movimentações filtradas 
            # para um arquivo Excel.
    def exportar_movimentacoes():
        
        # Inicializa um dicionário vazio para armazenar os filtros aplicados.
        filtro = {}
        
        # Obtém o texto inserido no campo de filtro de produto e 
                # remove espaços desnecessários.
        # Isso é usado para buscar movimentações associadas a 
                # um produto específico.
        produto = entrada_filtro_produto.get().strip()
        
        # Obtém o texto inserido no campo de filtro de tipo de 
                # movimentação e remove espaços desnecessários.
        # Isso filtra movimentações pelo tipo, como "Entrada" ou "Saída".
        tipo = entrada_filtro_tipo.get().strip()
        
        # Obtém a data inicial selecionada no campo de filtro de data inicial.
        # Serve para definir o início de um intervalo de datas.
        data_inicial = entrada_data_inicial.get_date()
        
        # Obtém a data final selecionada no campo de filtro de data final.
        # Serve para definir o final de um intervalo de datas.
        data_final = entrada_data_final.get_date()
    
        # Verifica se o usuário inseriu um valor no filtro de produto.
        if produto:
            
            # Adiciona um filtro que busca movimentações cujo nome do 
                    # produto contenha o texto fornecido.
            # "$regex" realiza uma busca parcial ignorando maiúsculas e minúsculas.
            filtro["produto"] = {"$regex": produto, "$options": "i"}
        
        # Verifica se o usuário inseriu um valor no filtro de tipo.
        if tipo:
            
            # Adiciona um filtro que busca movimentações cujo tipo
                    # contenha o texto fornecido.
            filtro["tipo"] = {"$regex": tipo, "$options": "i"}
        
        # Verifica se o usuário selecionou uma data inicial ou final.
        if data_inicial or data_final:
            
            # Inicializa um filtro de data vazio para adicionar condições.
            filtro["data"] = {}
            
            # Se o usuário selecionou uma data inicial, adiciona 
                    # uma condição para incluir
                    # movimentações a partir dessa data.
            if data_inicial:
                filtro["data"]["$gte"] = data_inicial.strftime("%Y-%m-%d")
            
            # Se o usuário selecionou uma data final, adiciona uma
                    # condição para incluir movimentações até essa 
                    # data, incluindo o final do dia.
            if data_final:
                filtro["data"]["$lte"] = data_final.strftime("%Y-%m-%d") + " 23:59:59"


        # Converte os resultados da busca no MongoDB para uma lista de registros.
        # 'colecao_movimentacoes.find(filtro)' aplica os filtros configurados anteriormente.
        # 'list()' transforma os resultados da consulta em uma lista de documentos.
        registros = list(colecao_movimentacoes.find(filtro))
        
        # Verifica se a lista de registros está vazia, ou seja, não
                # foram encontrados dados para os critérios fornecidos.
        if not registros:
            
            # Exibe uma mensagem informando que não há registros para exportar.
            messagebox.showinfo("Exportar", "Não há registros para exportar!")
            
            # Retorna, encerrando a execução da função, já que
                    # não há dados para exportar.
            return
        
        # Converte os registros retornados em um DataFrame do pandas.
        # Isso facilita a manipulação e exportação dos dados para formatos como Excel.
        df = pd.DataFrame(registros)
        
        # Remove a coluna '_id' do DataFrame, que é automaticamente
                # adicionada pelo MongoDB e não é relevante para a exportação.
        # 'inplace=True' modifica o DataFrame original diretamente,
                # sem criar uma cópia.
        df.drop(columns=['_id'], inplace=True)
        
        # Define o nome do arquivo Excel para onde os dados serão exportados.
        # Neste caso, o arquivo será salvo na pasta atual com o 
                # nome 'movimentacoes_filtradas.xlsx'.
        arquivo = "movimentacoes_filtradas.xlsx"
        
        # Exporta o DataFrame para um arquivo Excel.
        # 'index=False' significa que os índices das linhas do 
                # DataFrame não serão exportados.
        df.to_excel(arquivo, index=False)
        
        # Exibe uma mensagem de sucesso ao usuário, indicando que
                # os dados foram exportados com sucesso.
        # Inclui o nome do arquivo na mensagem para informar 
                # onde os dados foram salvos.
        messagebox.showinfo("Exportar", f"Dados exportados com sucesso para {arquivo}!")


    # Carregar movimentações ao abrir a janela
    carregar_movimentacoes()



# Esta função é responsável por abrir a janela de gerenciamento de usuários.
def abrir_tela_usuarios():

    # Cria uma nova janela de nível superior que será usada 
            # para gerenciar usuários.
    # `tk.Toplevel()` cria uma nova janela que é filha da janela 
            # principal da aplicação.
    janela_usuarios = tk.Toplevel()

    # Define o título da janela.
    janela_usuarios.title("Gerenciar Usuários")

    # Define a geometria da janela, que é a largura e altura em pixels.
    # "800x600" define a janela com 800 pixels de largura e 600 pixels de altura.
    janela_usuarios.geometry("800x600")

    # Desabilita a capacidade de redimensionar a janela, tanto na
            # largura quanto na altura.
    janela_usuarios.resizable(False, False)

    # Prepara a janela para modificações, garantindo que as 
            # próximas operações que
    # dependam do tamanho e da posição da janela possam ser
            # calculadas corretamente.
    janela_usuarios.update_idletasks()

    # Obtém a largura atual da janela.
    width = janela_usuarios.winfo_width()
    
    # Obtém a altura atual da janela.
    height = janela_usuarios.winfo_height()

    # Calcula a posição x para centralizar a janela.
    # `winfo_screenwidth()` retorna a largura da tela do dispositivo.
    # `(width // 2)` calcula metade da largura da janela para ajustar ao centro.
    x = (janela_usuarios.winfo_screenwidth() // 2) - (width // 2)

    # Calcula a posição y para centralizar a janela.
    # `winfo_screenheight()` retorna a altura da tela do dispositivo.
    # `(height // 2)` calcula metade da altura da janela para ajustar ao centro.
    y = (janela_usuarios.winfo_screenheight() // 2) - (height // 2)

    # Aplica a geometria calculada para centralizar a janela na tela do usuário.
    # `f"{width}x{height}+{x}+{y}"` define a largura, altura e 
            # posicionamento da janela.
    janela_usuarios.geometry(f"{width}x{height}+{x}+{y}")

    
    # Esta função é responsável por carregar e exibir os usuários da 
            # coleção 'usuarios' do MongoDB na interface gráfica.
    def carregar_usuarios():
        
        # Itera sobre todos os itens atualmente presentes na árvore de 
                # visualização 'tree_usuarios'.
        # 'get_children()' obtém todos os itens (linhas) que estão 
                # atualmente na árvore de visualização.
        for item in tree_usuarios.get_children():
            
            # Remove cada item individual da árvore de visualização.
            # Isso limpa a árvore para que possamos recarregar os 
                    # dados sem duplicação.
            tree_usuarios.delete(item)
    
        # Busca todos os documentos presentes na coleção 'usuarios' no banco de dados.
        # 'find()' sem parâmetros retorna todos os documentos da coleção.
        registros = colecao_usuarios.find()
    
        # Itera sobre cada documento retornado pela consulta ao banco de dados.
        for doc in registros:
            
            # Insere um novo item na árvore de visualização 'tree_usuarios'.
            # "" indica que o item é adicionado na raiz da árvore.
            # "end" indica que o novo item será adicionado no final da lista de itens.
            # 'values' define os valores que serão mostrados nas colunas da
                    # árvore para este item específico.
            # 'str(doc["_id"])' converte o ObjectId do MongoDB para string, para exibição.
            # 'doc["username"]' acessa o nome de usuário armazenado no documento.
            # 'doc.get("plain_password", "")' tenta obter a senha em texto plano; 
                    # se não estiver presente, usa uma string vazia.
            tree_usuarios.insert(
                "", "end",
                values=(str(doc["_id"]), doc["username"], doc.get("plain_password", ""))
            )


    # Função para adicionar um novo usuário
    def adicionar_usuario():
        
        # Obtém o nome de usuário do campo de entrada correspondente
                # na interface gráfica.
        username = entrada_novo_usuario.get()
        
        # Obtém a senha do campo de entrada correspondente na
                # interface gráfica.
        senha = entrada_nova_senha.get()
    
        # Verifica se algum dos campos está vazio.
        if not username or not senha:
            
            # Exibe uma mensagem de erro se algum dos campos estiver vazio.
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            
            # Interrompe a função para não continuar com o cadastro.
            return
    
        # Verifica se já existe um usuário com o mesmo nome no banco de dados.
        if colecao_usuarios.find_one({"username": username}):
            
            # Se o usuário já existir, exibe uma mensagem de erro.
            messagebox.showerror("Erro", "Usuário já existe!")
            
            # Interrompe a função para não tentar inserir um usuário duplicado.
            return
    
        # Codifica a senha fornecida usando bcrypt para armazenamento seguro.
        # `encode('utf-8')` converte a senha de string para bytes para
                # ser processada pelo bcrypt.
        # `bcrypt.gensalt()` gera um salt aleatório que é usado na criação do hash.
        hashed = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        
        # Insere o novo usuário na coleção 'usuarios' no banco de dados.
        # O documento contém o nome de usuário, a senha hash e a senha em texto plano.
        colecao_usuarios.insert_one({
            "username": username,
            "password": hashed,
            "plain_password": senha
        })
        
        # Exibe uma mensagem informando que o usuário foi cadastrado com sucesso.
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")

        # Limpa os campos de entrada para que novos dados possam ser inseridos.
        entrada_novo_usuario.delete(0, tk.END)
        entrada_nova_senha.delete(0, tk.END)
        
        # Atualiza a lista de usuários exibida na interface gráfica 
                # para incluir o novo usuário.
        carregar_usuarios()

        # Fecha a tela
        janela_usuarios.destroy()

        

    # Define uma função que permite editar as informações de
                # um usuário existente.
    def editar_usuario():
        
        # Obtém o item selecionado na árvore de visualização 'tree_usuarios'.
        selecionado = tree_usuarios.selection()
    
        # Verifica se algum item foi realmente selecionado.
        if not selecionado:
            
            # Exibe uma mensagem de erro se nenhum usuário foi selecionado para edição.
            messagebox.showerror("Erro", "Selecione um usuário para editar!")
            
            # Encerra a função e não continua se nenhum usuário foi selecionado.
            return
    
        # Obtém as informações do item selecionado na árvore de visualização.
        item = tree_usuarios.item(selecionado)
        
        # Extrai o ID do documento MongoDB do usuário a partir do 
                # primeiro valor armazenado no item.
        doc_id = item["values"][0]
        
        # Obtém o novo nome de usuário inserido no campo de 
                # entrada 'entrada_novo_usuario'.
        username = entrada_novo_usuario.get()
        
        # Obtém a nova senha inserida no campo de entrada 'entrada_nova_senha'.
        nova_senha = entrada_nova_senha.get()
    
        # Verifica se os campos de novo nome de usuário e nova
                # senha estão preenchidos.
        if not username or not nova_senha:
            
            # Exibe uma mensagem de erro se algum dos campos 
                    # necessários estiver vazio.
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            
            # Encerra a função e não continua se algum campo estiver vazio.
            return
    
        # Codifica a nova senha usando bcrypt para armazenamento seguro.
        # O método 'encode' transforma a string em bytes, e 'bcrypt.gensalt()' 
                # gera um salt aleatório para o hash.
        hashed = bcrypt.hashpw(nova_senha.encode('utf-8'), bcrypt.gensalt())
    
        # Atualiza o documento do usuário no banco de dados com o novo 
                # nome de usuário e senha hasheada.
        colecao_usuarios.update_one(
            
            # Especifica o documento a ser atualizado pelo seu ID,
                    # convertendo o ID de string para ObjectId.
            {"_id": ObjectId(doc_id)},
            
            # Define os novos valores para o nome de usuário e senha.
            {"$set": {"username": username, "password": hashed, "plain_password": nova_senha}}
            
        )
    
        # Exibe uma mensagem de sucesso indicando que o usuário foi 
                # atualizado corretamente.
        messagebox.showinfo("Sucesso", f"Usuário '{username}' atualizado com sucesso!")
        
        # Limpa os campos de entrada após a atualização para evitar 
                # confusão ou duplicação de dados.
        entrada_novo_usuario.delete(0, tk.END)
        entrada_nova_senha.delete(0, tk.END)
        
        # Recarrega a lista de usuários na interface gráfica para 
                # refletir as mudanças feitas.
        carregar_usuarios()
        

    # Define uma função que permite excluir um usuário existente.
    def excluir_usuario():
        
        # Obtém o item (ou itens) selecionado na árvore de 
                # visualização 'tree_usuarios'.
        selecionado = tree_usuarios.selection()
    
        # Verifica se algum item foi realmente selecionado.
        if not selecionado:
            
            # Exibe uma mensagem de erro se nenhum usuário foi 
                    # selecionado para exclusão.
            messagebox.showerror("Erro", "Selecione um usuário para excluir!")
            
            # Encerra a função e não continua se nenhum usuário foi selecionado.
            return
    
        # Obtém as informações do item selecionado na árvore de visualização.
        item = tree_usuarios.item(selecionado)
        
        # Extrai o nome de usuário do segundo valor armazenado no item.
        username = item["values"][1]
        
        # Extrai o ID do documento MongoDB do usuário a partir do 
                # primeiro valor armazenado no item.
        doc_id = item["values"][0]
    
        # Pede confirmação ao usuário antes de excluir, mostrando o
                # nome do usuário a ser excluído.
        if messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o usuário '{username}'?"):
            
            # Se confirmado, executa a exclusão do documento do usuário 
                    # no banco de dados.
            colecao_usuarios.delete_one({"_id": ObjectId(doc_id)})
            
            # Exibe uma mensagem informando que o usuário foi excluído com sucesso.
            messagebox.showinfo("Sucesso", f"Usuário '{username}' excluído com sucesso!")
            
            # Recarrega a lista de usuários na interface gráfica para refletir a mudança.
            carregar_usuarios()


    # Define uma função que preenche automaticamente os campos de entrada
                    # com informações de um usuário selecionado.
    def preencher_campos_usuario(event):
     
        # Obtém a seleção atual na árvore de visualização 'tree_usuarios'.
        selecionado = tree_usuarios.selection()
    
        # Verifica se algum usuário foi selecionado na árvore de visualização.
        if selecionado:
        
            # Obtém o item selecionado, que contém os dados do usuário.
            item = tree_usuarios.item(selecionado)
            
            # Extrai os valores armazenados no item, que incluem o ID, 
                    # nome de usuário e senha.
            valores = item['values']
    
            # Limpa o campo de entrada onde o nome de usuário é inserido.
            entrada_novo_usuario.delete(0, tk.END)
            
            # Insere o nome de usuário extraído no campo de entrada correspondente.
            entrada_novo_usuario.insert(0, valores[1])  # Insere o nome de usuário.
    
            # Limpa o campo de entrada onde a senha é inserida.
            entrada_nova_senha.delete(0, tk.END)
            
            # Insere a senha extraída no campo de entrada correspondente.
            entrada_nova_senha.insert(0, valores[2])  # Insere a senha.


    # Configuração do layout da parte superior da janela de usuários.
    # Cria um frame (container) que será usado para conter outros 
                    # widgets na parte superior da janela.
    frame_topo = tk.Frame(janela_usuarios, pady=10)

    # Empacota o frame na janela. O frame irá se expandir para
            # acomodar o tamanho do conteúdo.
    # 'pack()' é um gerenciador de geometria que organiza os widgets em 
            # blocos antes de colocá-los na janela dos pais.
    frame_topo.pack()
    
    # Cria um widget de texto (Label) que serve como título na 
            # parte superior do frame.
    # 'text="Gerenciar Usuários"' define o texto a ser exibido no label.
    # 'font=("Helvetica", 16, "bold")' define o tipo, tamanho e 
            # estilo da fonte do texto.
    tk.Label(frame_topo, text="Gerenciar Usuários", font=("Helvetica", 16, "bold")).pack()
    
    # Cria um segundo frame para conter os formulários de 
            # entrada de dados dos usuários.
    # Este frame está posicionado abaixo do frame_topo na janela.
    frame_form = tk.Frame(janela_usuarios, padx=20, pady=10)

    # Empacota o frame_form na janela, utilizando também o método 'pack()' 
            # que adiciona o frame abaixo do frame_topo.
    frame_form.pack()


    # Cria um widget de texto (Label) que serve como uma etiqueta para o 
            # campo de entrada do nome de usuário.
    # 'text="Usuário:"' define o texto a ser exibido na etiqueta.
    # 'font=("Helvetica", 12)' especifica o tipo e o tamanho da fonte do texto.
    # 'grid(row=0, column=0, sticky="e")' organiza o widget na primeira linha, 
            # primeira coluna da grade do frame_form,
            # e o 'sticky="e"' faz o texto alinhar à direita (east) dentro
            # do espaço alocado para ele na grade.
    tk.Label(frame_form, text="Usuário:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="e")
    
    # Cria um campo de entrada (Entry) para que os usuários possam 
            # digitar seus nomes de usuário.
    # 'font=("Helvetica", 12)' define a fonte do texto digitado no campo.
    # Este widget é associado a 'frame_form'.
    entrada_novo_usuario = tk.Entry(frame_form, font=("Helvetica", 12))

    # 'grid(row=0, column=1, padx=10, pady=5)' posiciona o campo de 
            # entrada na primeira linha e segunda coluna.
    # 'padx=10' e 'pady=5' adicionam um espaço externo à esquerda/direita e 
            # acima/abaixo do widget, respectivamente.
    entrada_novo_usuario.grid(row=0, column=1, padx=10, pady=5)
    
    # Cria um widget de texto (Label) que serve como uma etiqueta 
            # para o campo de entrada da senha.
    # 'text="Senha:"' define o texto a ser exibido na etiqueta.
    # 'font=("Helvetica", 12)' especifica o tipo e o tamanho da fonte do texto.
    # 'grid(row=1, column=0, sticky="e")' organiza o widget na segunda
            # linha, primeira coluna da grade do frame_form,
            # e o 'sticky="e"' faz o texto alinhar à direita dentro do 
            # espaço alocado para ele na grade.
    tk.Label(frame_form, text="Senha:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="e")
    
    # Cria um campo de entrada (Entry) para que os usuários possam 
            # digitar suas senhas.
    # 'show="*"' faz com que qualquer texto digitado seja substituído 
            # por asteriscos, ocultando a senha.
    # 'font=("Helvetica", 12)' define a fonte do texto digitado no campo.
    entrada_nova_senha = tk.Entry(frame_form, 
                                  show="*", 
                                  font=("Helvetica", 12))

    # 'grid(row=1, column=1, padx=10, pady=5)' posiciona o campo de 
            # entrada na segunda linha e segunda coluna.
    entrada_nova_senha.grid(row=1, 
                            column=1, 
                            padx=10, 
                            pady=5)

    
    # Cria um frame para conter os botões que realizarão ações na 
            # janela de usuários.
    # 'pady=10' adiciona um espaçamento vertical ao redor do frame 
            # para separá-lo visualmente de outros elementos.
    frame_botoes = tk.Frame(janela_usuarios, pady=10)

    # Empacota o frame_botoes na janela, utilizando o gerenciador de layout 'pack',
            # que organiza os widgets em blocos antes de colocá-los na janela.
    frame_botoes.pack()
    
    # Cria um botão para adicionar novos usuários.
    # 'text="Adicionar Usuário"' define o texto a ser exibido no botão.
            # 'command=adicionar_usuario' vincula o botão à função 'adicionar_usuario' 
            # que será chamada quando o botão for clicado.
    # 'bg="#2a9d8f"' define a cor de fundo do botão como um tom de verde-azulado.
    # 'fg="white"' define a cor do texto do botão como branco.
    # 'font=("Helvetica", 12)' especifica a fonte e tamanho do texto.
    # 'width=15' define a largura do botão para garantir que o texto caiba adequadamente.
    btn_adicionar_usuario = tk.Button(frame_botoes, 
                                      text="Adicionar Usuário", 
                                      command=adicionar_usuario, 
                                      bg="#2a9d8f", 
                                      fg="white", 
                                      font=("Helvetica", 12), 
                                      width=15)
    
    # Empacota o botão no lado esquerdo do frame_botoes.
    # 'side="left"' coloca o botão à esquerda dentro do frame.
    # 'padx=5' adiciona um espaçamento horizontal de 5 pixels entre este 
            # botão e outros elementos ou bordas adjacentes.
    btn_adicionar_usuario.pack(side="left", padx=5)

    
    # Cria um botão para editar usuários existentes.
    # 'text="Editar Usuário"' define o texto a ser exibido no botão.
    # 'command=editar_usuario' vincula este botão à função 'editar_usuario' 
            # que será chamada quando o botão for clicado.
    # 'bg="#f4a261"' define a cor de fundo do botão como um tom de laranja.
    # 'fg="white"' define a cor do texto do botão como branco.
    # 'font=("Helvetica", 12)' especifica a fonte e tamanho do texto.
    # 'width=15' define a largura do botão para garantir que o texto caiba adequadamente.
    btn_editar_usuario = tk.Button(frame_botoes, 
                                   text="Editar Usuário", 
                                   command=editar_usuario, 
                                   bg="#f4a261", 
                                   fg="white", 
                                   font=("Helvetica", 12), 
                                   width=15)
    
    # Empacota o botão no lado esquerdo do frame_botoes, ao lado do botão de adicionar.
    # 'side="left"' coloca o botão à esquerda dentro do frame, próximo ao botão de adicionar.
    # 'padx=5' adiciona um espaçamento horizontal de 5 pixels entre 
            # este botão e outros elementos ou bordas adjacentes.
    btn_editar_usuario.pack(side="left", padx=5)


    # Cria um botão para excluir usuários existentes.
    # 'text="Excluir Usuário"' define o texto a ser exibido no botão.
    # 'command=excluir_usuario' vincula este botão à função 'excluir_usuario', 
            # que será chamada quando o botão for clicado.
    # 'bg="#e76f51"' define a cor de fundo do botão como um tom de coral.
    # 'fg="white"' define a cor do texto do botão como branco para contrastar com o fundo coral.
    # 'font=("Helvetica", 12)' especifica a fonte e o tamanho do texto no botão.
    # 'width=15' define a largura do botão para garantir que o texto caiba 
            # adequadamente e mantenha a consistência com outros botões.
    btn_excluir_usuario = tk.Button(frame_botoes, 
                                    text="Excluir Usuário", 
                                    command=excluir_usuario, 
                                    bg="#e76f51", 
                                    fg="white", 
                                    font=("Helvetica", 12), 
                                    width=15)
    
    # Empacota o botão no lado esquerdo do frame_botoes.
    # 'side="left"' coloca o botão à esquerda dentro do frame, alinhando-o ao 
            # lado dos outros botões já empacotados.
    # 'padx=5' adiciona um espaçamento horizontal de 5 pixels entre este 
            # botão e outros elementos ou bordas adjacentes.
    btn_excluir_usuario.pack(side="left", padx=5)
    
    # Cria um frame para conter a lista de usuários.
    # 'pady=10' adiciona um espaçamento vertical de 10 pixels acima e 
            # abaixo do frame para separá-lo visualmente de outros elementos.
    frame_lista = tk.Frame(janela_usuarios, pady=10)
    
    # Empacota o frame na janela. Configura o frame para preencher tanto 
            # horizontal quanto verticalmente o espaço disponível.
    # 'fill="both"' faz com que o frame se expanda tanto na horizontal quanto na vertical.
    # 'expand=True' permite que o frame expanda para preencher qualquer 
            # espaço adicional na janela, garantindo que ocupe todo o espaço disponível.
    frame_lista.pack(fill="both", expand=True)


    # Cria uma árvore de visualização dentro do 'frame_lista' para listar os usuários.
    # 'columns=("ID", "Username", "Password")' define as colunas da árvore 
            # de visualização com identificadores de coluna.
    # 'show="headings"' indica que apenas os cabeçalhos das colunas devem 
            # ser exibidos, sem a coluna de índice padrão à esquerda.
    tree_usuarios = ttk.Treeview(frame_lista, 
                                 columns=("ID", "Username", "Password"), 
                                 show="headings")
    
    # Configura o cabeçalho e a largura da coluna "ID".
    # 'text="ID"' define o texto do cabeçalho para a coluna "ID".
    tree_usuarios.heading("ID", text="ID")

    # 'width=100' define a largura da coluna "ID" em 100 pixels.
    # 'anchor="center"' alinha o texto da coluna ao centro.
    tree_usuarios.column("ID", width=100, anchor="center")
    
    # Configura o cabeçalho e a largura da coluna "Username".
    # 'text="Usuário"' define o texto do cabeçalho para a coluna "Username".
    tree_usuarios.heading("Username", text="Usuário")

    # 'width=200' define a largura da coluna "Username" em 200 pixels.
    tree_usuarios.column("Username", width=200, anchor="center")
    
    # Configura o cabeçalho e a largura da coluna "Password".
    # 'text="Senha"' define o texto do cabeçalho para a coluna "Password".
    tree_usuarios.heading("Password", text="Senha")

    # 'width=200' define a largura da coluna "Password" em 200 pixels.
    tree_usuarios.column("Password", width=200, anchor="center")
    
    # Empacota a árvore de visualização dentro do 'frame_lista'.
    # 'fill="both"' faz com que a árvore de visualização se expanda para 
            # preencher o espaço horizontal e vertical disponível.
    # 'expand=True' permite que a árvore de visualização expanda para 
            # preencher qualquer espaço adicional no layout.
    tree_usuarios.pack(fill="both", expand=True)
    
    # Associa um evento de seleção na árvore de visualização à 
            # função 'preencher_campos_usuario'.
    # '<<TreeviewSelect>>' é um evento que é acionado quando uma 
            # linha na árvore é selecionada.
    tree_usuarios.bind('<<TreeviewSelect>>', preencher_campos_usuario)
    
    # Chama a função 'carregar_usuarios' para carregar inicialmente os 
            # dados dos usuários na árvore de visualização.
    carregar_usuarios()

    
    
# Define uma função para filtrar produtos na Treeview baseada
        # em um termo de pesquisa.
def filtrar_produtos():
    
    # Obtém o termo de pesquisa do campo de entrada e remove espaços 
            # em branco desnecessários com .strip()
    termo = entrada_filtro.get().strip()

    # Verifica se o termo de pesquisa está vazio.
    if not termo:
        
        # Se estiver vazio, recarrega todos os dados para a Treeview, 
                # mostrando todos os produtos novamente.
        carregar_dados()
        
        # Sai da função sem fazer mais nada.
        return

    # Limpa todos os itens atuais da Treeview para evitar a duplicação 
            # de dados ao aplicar um novo filtro.
    for item in tree_produtos.get_children():
        tree_produtos.delete(item)

    # Cria um objeto de expressão regular (regex) para filtrar documentos.
    # "$regex": termo permite buscar documentos que contêm o termo de pesquisa.
    # "$options": "i" torna a busca insensível a maiúsculas e minúsculas.
    regex = {"$regex": termo, "$options": "i"}

    # Tenta converter o termo de pesquisa para valores numéricos 
            # para filtrar por preço ou quantidade.
    try:

        # Tenta converter o termo para um float para buscar por preço.
        preco_valor = float(termo)  

        # Tenta converter o termo para um int para buscar por quantidade.
        quantidade_valor = int(termo)  
        
    except ValueError:
        
        # Se a conversão falhar, significa que o termo de pesquisa não é um número.
        # Define preco_valor como None se o termo não puder ser convertido para float.
        preco_valor = None  

        # Define quantidade_valor como None se o termo não puder ser convertido para int.
        quantidade_valor = None  


    # Define uma consulta com operador "$or" que busca correspondências
            # em nome ou fornecedor.
    query = {"$or": [
        {"nome": regex},
        {"fornecedor": regex}
    ]}
    
    # Adiciona uma condição à consulta se o valor do preço não for None (se o 
            # termo de pesquisa for numérico e puder ser convertido para float).
    if preco_valor is not None:
        query["$or"].append({"preco": preco_valor})
    
    # Adiciona uma condição à consulta se o valor da quantidade não for None (se o 
            # termo de pesquisa for numérico e puder ser convertido para int).
    if quantidade_valor is not None:
        query["$or"].append({"quantidade": quantidade_valor})
    
    # Realiza a busca na coleção de produtos com a consulta configurada.
    registros = colecao_produtos.find(query)
    
    # Itera sobre cada documento encontrado na busca no banco de dados MongoDB.
    for doc in registros:
        
        # Extrai a quantidade do produto do documento atual. Esta informação é
                # utilizada para controle de estoque e exibição.
        quantidade = doc["quantidade"]
        
        # Insere um novo item na Treeview com os dados do documento atual.
        # O primeiro argumento "" indica que o item será adicionado na raiz da Treeview.
        # O segundo argumento "end" indica que o item será adicionado ao 
                # final da lista de itens existentes.
        # 'values' é uma tupla que contém os dados do produto que serão exibidos 
                # nas colunas correspondentes da Treeview.
        item_id = tree_produtos.insert(
            "", "end", 
            values=(doc["nome"], doc["preco"], quantidade, doc["fornecedor"], str(doc["_id"]))
        )
        
        # Verifica se a quantidade do produto é menor ou igual a 5.
        # Este é um critério comum para identificar produtos com estoque baixo.
        if quantidade <= 5:
            
            # Se a quantidade for menor ou igual a 5, aplica uma tag ao item na Treeview.
            # A tag "estoque_baixo" é usada para alterar a aparência do item e
                    # destacar que o estoque está baixo.
            tree_produtos.item(item_id, tags=("estoque_baixo",))
        
    # Configura a aparência dos itens na Treeview que têm a tag "estoque_baixo".
    # 'background="red"' define a cor de fundo dos itens com estoque baixo para vermelho.
    # 'foreground="white"' define a cor do texto desses itens para branco.
    # Essa configuração visual ajuda a chamar atenção para os 
            # produtos que precisam de reposição.
    tree_produtos.tag_configure("estoque_baixo", 
                                background="red", 
                                foreground="white")
    

# Define uma função para carregar dados dos produtos no banco de 
        # dados MongoDB para uma Treeview.
def carregar_dados():
    
    """Carrega os dados do MongoDB para a Treeview de produtos."""
    
    # Itera sobre cada item existente na Treeview de produtos 
            # para limpar itens antigos.
    for item in tree_produtos.get_children():
    
        # Deleta cada item individualmente para garantir que a Treeview 
                # está limpa antes de adicionar novos dados.
        tree_produtos.delete(item)

    # Busca todos os documentos na coleção 'produtos' no banco de dados MongoDB.
    registros = colecao_produtos.find()
    
    # Itera sobre cada documento retornado pelo MongoDB.
    for doc in registros:
        
        # Extrai a quantidade de produto do documento.
        quantidade = doc["quantidade"]
        
        # Insere um novo item na Treeview para cada produto encontrado.
        # "" indica que o item é adicionado na raiz da Treeview.
        # "end" significa que o item será adicionado no final da lista de itens.
        # 'values' são os dados que serão exibidos nas colunas da Treeview
                # para este item específico.
        item_id = tree_produtos.insert(
            "", "end", 
            values=(doc["nome"], doc["preco"], quantidade, doc["fornecedor"], str(doc["_id"]))
        )
        
        # Sinalizar estoque baixo se a quantidade de produto for menor ou igual a 5.
        if quantidade <= 5:
            
            # Aplica uma tag ao item na Treeview se o estoque estiver baixo.
            tree_produtos.item(item_id, tags=("estoque_baixo",))

    # Configura a tag 'estoque_baixo' para mudar a cor de fundo para 
            # vermelho e a cor do texto para branco.
    # Isso destaca visualmente os produtos com estoque baixo na Treeview.
    tree_produtos.tag_configure("estoque_baixo", background="red", foreground="white")


# Define a função para abrir a janela principal do sistema.
def abrir_janela_principal():
    
    """Abre a janela principal do sistema."""
    
    # Declara a variável `janela_principal` como global para que possa 
            # ser acessada em outras partes do programa.
    global janela_principal
    
    # Cria a janela principal do sistema usando o Tkinter.
    janela_principal = tk.Tk()
    
    # Define o título da janela como "Gerenciamento de Estoque".
    janela_principal.title("Gerenciamento de Estoque com MongoDB")
    
    # Maximiza a janela principal para ocupar toda a tela do monitor.
    # 'state("zoomed")' ajusta a janela para o modo de tela cheia.
    janela_principal.state('zoomed')
    
    # Permite que o usuário redimensione a janela manualmente,
            # tanto na largura quanto na altura.
    # 'resizable(True, True)' habilita o redimensionamento.
    janela_principal.resizable(True, True)

    # Layout da janela principal:
    # Cria um frame (contêiner) na parte superior da janela principal.
    # 'bg="#2a9d8f"' define a cor de fundo do frame como um tom de verde-azulado.
    # 'height=50' especifica que a altura do frame será de 50 pixels.
    frame_topo = tk.Frame(janela_principal, bg="#2a9d8f", height=50)
    
    # Posiciona o frame no topo da janela principal.
    # 'fill="x"' faz com que o frame ocupe toda a largura da janela.
    frame_topo.pack(fill="x")

    # Adiciona um rótulo (label) dentro do frame superior 
            # para exibir o título do sistema.
    # 'text="Sistema de Gerenciamento de Estoque - Completo"' 
            # define o texto exibido no rótulo.
    # 'bg="#2a9d8f"' e 'fg="white"' ajustam o fundo do rótulo para 
            # combinar com o frame e o texto para branco.
    # 'font=("Helvetica", 16, "bold")' configura a fonte para 
            # ser Helvetica, tamanho 16 e em negrito.
    lbl_titulo = tk.Label(frame_topo, 
                          text="Sistema de Gerenciamento de Estoque - Completo", 
                          bg="#2a9d8f", 
                          fg="white", 
                          font=("Helvetica", 16, "bold"))
    
    # Posiciona o rótulo dentro do frame superior.
    # 'pady=10' adiciona um espaçamento vertical ao redor do
            # rótulo para melhorar a estética.
    lbl_titulo.pack(pady=10)


    # Cria um frame (contêiner) para organizar os campos de entrada de dados.
    # 'janela_principal' é a janela onde o frame será adicionado.
    # 'padx=20' adiciona espaçamento horizontal em torno do frame.
    # 'pady=10' adiciona espaçamento vertical em torno do frame.
    frame_dados = tk.Frame(janela_principal, padx=20, pady=10)
    
    # Posiciona o frame dentro da janela principal.
    # 'fill="x"' faz com que o frame se expanda horizontalmente 
            # para preencher toda a largura da janela.
    frame_dados.pack(fill="x")
    
    # Adiciona um rótulo (label) ao frame para identificar o 
            # campo de entrada "Nome".
    # 'text="Nome:"' define o texto exibido no rótulo.
    # 'font=("Helvetica", 12)' configura a fonte para ser Helvetica, tamanho 12.
    # 'grid(row=0, column=0, sticky="e")' posiciona o rótulo na 
            # primeira linha (linha 0) e primeira coluna (coluna 0),
            # alinhando-o à direita com 'sticky="e"' (east - leste).
    tk.Label(frame_dados, 
             text="Nome:", 
             font=("Helvetica", 12)).grid(row=0, column=0, sticky="e")
    
    # Declara a variável 'entrada_nome' como global para
            # que possa ser acessada em outras funções.
    global entrada_nome
    
    # Cria um campo de entrada (Entry) para o usuário digitar o nome do produto.
    # 'font=("Helvetica", 12)' define o estilo e tamanho do texto digitado no campo.
    entrada_nome = tk.Entry(frame_dados, font=("Helvetica", 12))
    
    # Posiciona o campo de entrada no layout em grade.
    # 'row=0, column=1' posiciona o campo na primeira 
            # linha (linha 0) e na segunda coluna (coluna 1).
    # 'padx=10' adiciona espaçamento horizontal ao redor do campo.
    # 'pady=5' adiciona espaçamento vertical ao redor do campo.
    entrada_nome.grid(row=0, column=1, padx=10, pady=5)


    # Adiciona um rótulo (label) ao frame para identificar o 
            # campo de entrada "Preço".
    # 'text="Preço:"' define o texto exibido no rótulo.
    # 'font=("Helvetica", 12)' configura a fonte para ser Helvetica, tamanho 12.
    # 'grid(row=1, column=0, sticky="e")' posiciona o rótulo na
            # segunda linha (linha 1) e na primeira coluna (coluna 0),
            # alinhando-o à direita com 'sticky="e"' (east - leste).
    tk.Label(frame_dados, 
             text="Preço:", 
             font=("Helvetica", 12)).grid(row=1, column=0, sticky="e")
    
    # Declara a variável 'entrada_preco' como global para que 
            # possa ser acessada em outras funções.
    global entrada_preco
    
    # Cria um campo de entrada (Entry) para o usuário digitar o preço do produto.
    # 'font=("Helvetica", 12)' define o estilo e tamanho do texto digitado no campo.
    entrada_preco = tk.Entry(frame_dados, font=("Helvetica", 12))
    
    # Posiciona o campo de entrada "Preço" no layout em grade.
    # 'row=1, column=1' posiciona o campo na segunda linha (linha 1) e 
            # na segunda coluna (coluna 1).
    # 'padx=10' adiciona espaçamento horizontal ao redor do campo.
    # 'pady=5' adiciona espaçamento vertical ao redor do campo.
    entrada_preco.grid(row=1, column=1, padx=10, pady=5)
    
    # Adiciona um rótulo (label) ao frame para identificar o 
            # campo de entrada "Quantidade".
    # 'text="Quantidade:"' define o texto exibido no rótulo.
    # 'font=("Helvetica", 12)' configura a fonte para ser Helvetica, tamanho 12.
    # 'grid(row=2, column=0, sticky="e")' posiciona o rótulo na 
            # terceira linha (linha 2) e na primeira coluna (coluna 0),
            # alinhando-o à direita com 'sticky="e"' (east - leste).
    tk.Label(frame_dados, 
             text="Quantidade:", 
             font=("Helvetica", 12)).grid(row=2, column=0, sticky="e")
    
    # Declara a variável 'entrada_quantidade' como global para 
            # que possa ser acessada em outras funções.
    global entrada_quantidade
    
    # Cria um campo de entrada (Entry) para o usuário digitar a quantidade do produto.
    # 'font=("Helvetica", 12)' define o estilo e tamanho do texto digitado no campo.
    entrada_quantidade = tk.Entry(frame_dados, font=("Helvetica", 12))
    
    # Posiciona o campo de entrada "Quantidade" no layout em grade.
    # 'row=2, column=1' posiciona o campo na terceira linha (linha 2) e
            # na segunda coluna (coluna 1).
    # 'padx=10' adiciona espaçamento horizontal ao redor do campo.
    # 'pady=5' adiciona espaçamento vertical ao redor do campo.
    entrada_quantidade.grid(row=2, column=1, padx=10, pady=5)


    # Adiciona um rótulo (label) ao frame para identificar o
            # campo de entrada "Fornecedor".
    # 'text="Fornecedor:"' define o texto exibido no rótulo.
    # 'font=("Helvetica", 12)' configura a fonte para ser Helvetica, tamanho 12.
    # 'grid(row=3, column=0, sticky="e")' posiciona o rótulo na quarta 
            # linha (linha 3) e na primeira coluna (coluna 0),
            # alinhando-o à direita com 'sticky="e"' (east - leste).
    tk.Label(frame_dados, text="Fornecedor:", 
             font=("Helvetica", 12)).grid(row=3, column=0, sticky="e")
    
    # Declara a variável 'entrada_fornecedor' como global para que
            # possa ser acessada em outras funções.
    global entrada_fornecedor
    
    # Cria um campo de entrada (Entry) para o usuário digitar o
            # nome do fornecedor do produto.
    # 'font=("Helvetica", 12)' define o estilo e tamanho do
            # texto digitado no campo.
    entrada_fornecedor = tk.Entry(frame_dados, 
                                  font=("Helvetica", 12))
    
    # Posiciona o campo de entrada "Fornecedor" no layout em grade.
    # 'row=3, column=1' posiciona o campo na quarta linha (linha 3) e na segunda coluna (coluna 1).
    # 'padx=10' adiciona espaçamento horizontal ao redor do campo.
    # 'pady=5' adiciona espaçamento vertical ao redor do campo.
    entrada_fornecedor.grid(row=3, column=1, padx=10, pady=5)
    
    # Cria um novo frame para organizar os botões de ações.
    # Este frame será usado para adicionar botões como "Adicionar Produto", "Dar Baixa", etc.
    # 'pady=10' adiciona espaçamento vertical ao redor do frame, 
            # separando-o dos outros elementos da interface.
    frame_botoes = tk.Frame(janela_principal, pady=10)
    
    # Posiciona o frame de botões dentro da janela principal.
    # 'fill="x"' faz com que o frame ocupe toda a largura da janela principal.
    frame_botoes.pack(fill="x")


    # Cria um botão no frame de botões para adicionar produtos.
    # 'frame_botoes' é o contêiner onde o botão será posicionado.
    # 'text="Adicionar Produto"' define o texto exibido no botão.
    # 'command=adicionar_produto' vincula o botão à função 'adicionar_produto', 
            # que será executada quando o botão for clicado.
    # 'bg="#2a9d8f"' define a cor de fundo do botão como um tom de verde-azulado.
    # 'fg="white"' define a cor do texto no botão como branco.
    # 'font=("Helvetica", 12)' configura a fonte do texto para Helvetica, tamanho 12.
    # 'width=15' define a largura do botão, garantindo consistência visual.
    btn_adicionar = tk.Button(frame_botoes, 
                              text="Adicionar Produto", 
                              command=adicionar_produto, 
                              bg="#2a9d8f", 
                              fg="white", 
                              font=("Helvetica", 12), 
                              width=15)
    
    # Posiciona o botão "Adicionar Produto" no frame de botões.
    # 'side="left"' posiciona o botão à esquerda dentro do frame.
    # 'padx=10' adiciona espaçamento horizontal ao redor do botão,
            # separando-o de outros elementos.
    btn_adicionar.pack(side="left", padx=10)
    
    # Cria um botão no frame de botões para dar baixa no estoque de produtos.
    # 'frame_botoes' é o contêiner onde o botão será posicionado.
    # 'text="Dar Baixa"' define o texto exibido no botão.
    # 'command=dar_baixa_produto' vincula o botão à função 'dar_baixa_produto',
            # que será executada quando o botão for clicado.
    # 'bg="#e76f51"' define a cor de fundo do botão como um tom de vermelho.
    # 'fg="white"' define a cor do texto no botão como branco.
    # 'font=("Helvetica", 12)' configura a fonte do texto para Helvetica, tamanho 12.
    # 'width=15' define a largura do botão, garantindo consistência visual.
    btn_baixa = tk.Button(frame_botoes, 
                          text="Dar Baixa", 
                          command=dar_baixa_produto, 
                          bg="#e76f51", 
                          fg="white", 
                          font=("Helvetica", 12), 
                          width=15)
    
    # Posiciona o botão "Dar Baixa" no frame de botões.
    # 'side="left"' posiciona o botão à esquerda, ao lado do botão anterior.
    # 'padx=10' adiciona espaçamento horizontal ao redor do botão, 
            # separando-o de outros elementos.
    btn_baixa.pack(side="left", padx=10)


    # Cria um botão no frame de botões para exibir o histórico de movimentações.
    # 'frame_botoes' é o contêiner onde o botão será posicionado.
    # 'text="Histórico de Movimentações"' define o texto exibido no botão.
    # 'command=exibir_movimentacoes' vincula o botão à função 'exibir_movimentacoes', 
            # que será executada ao clicar no botão.
    # 'bg="#264653"' define a cor de fundo do botão como um tom de azul escuro.
    # 'fg="white"' define a cor do texto no botão como branco.
    # 'font=("Helvetica", 12)' configura a fonte do texto como Helvetica, tamanho 12.
    # 'width=20' especifica a largura do botão, deixando-o mais largo 
            # para destacar sua importância.
    btn_movimentacoes = tk.Button(frame_botoes, 
                                  text="Histórico de Movimentações", 
                                  command=exibir_movimentacoes, 
                                  bg="#264653", 
                                  fg="white", 
                                  font=("Helvetica", 12), 
                                  width=20)
    
    # Posiciona o botão "Histórico de Movimentações" no frame de botões.
    # 'side="left"' posiciona o botão à esquerda dentro do frame.
    # 'padx=10' adiciona espaçamento horizontal ao redor do 
            # botão, separando-o de outros elementos.
    btn_movimentacoes.pack(side="left", padx=10)
    
    # Cria um botão no frame de botões para abrir a tela de 
            # gerenciamento de usuários.
    # 'text="Gerenciar Usuários"' define o texto exibido no botão.
    # 'command=abrir_tela_usuarios' vincula o botão à função 'abrir_tela_usuarios', 
            # que será executada ao clicar no botão.
    # 'bg="#6a994e"' define a cor de fundo do botão como um tom de verde.
    # 'fg="white"' define a cor do texto no botão como branco.
    # 'font=("Helvetica", 12)' configura a fonte do texto como Helvetica, tamanho 12.
    # 'width=15' define a largura do botão, mantendo consistência com os outros botões.
    btn_gerenciar_usuarios = tk.Button(frame_botoes, 
                                       text="Gerenciar Usuários", 
                                       command=abrir_tela_usuarios, 
                                       bg="#6a994e", 
                                       fg="white", 
                                       font=("Helvetica", 12), 
                                       width=15)
    
    # Posiciona o botão "Gerenciar Usuários" no frame de botões.
    # 'side="left"' posiciona o botão à esquerda dentro do frame, ao 
            # lado do botão "Histórico de Movimentações".
    # 'padx=10' adiciona espaçamento horizontal ao redor do botão.
    btn_gerenciar_usuarios.pack(side="left", padx=10)
    
    # Cria um novo frame para organizar o campo de filtro.
    # Este frame será usado para adicionar elementos que permitem 
            # buscar produtos específicos na lista.
    # 'pady=10' adiciona espaçamento vertical em torno do frame, 
            # separando-o visualmente de outros elementos.
    frame_filtro = tk.Frame(janela_principal, pady=10)
    
    # Posiciona o frame de filtro dentro da janela principal.
    # 'fill="x"' faz com que o frame se expanda horizontalmente 
            # para preencher toda a largura da janela.
    frame_filtro.pack(fill="x")


    # Adiciona um rótulo ao frame de filtro para identificar a
            # funcionalidade de filtragem de produtos.
    # 'text="Filtrar Produtos:"' define o texto exibido no rótulo.
    # 'font=("Helvetica", 12)' configura a fonte para ser Helvetica, tamanho 12.
    # 'pack(side="left", padx=10)' posiciona o rótulo à esquerda no 
            # frame e adiciona espaçamento horizontal ao redor.
    tk.Label(frame_filtro, 
             text="Filtrar Produtos:", 
             font=("Helvetica", 12)).pack(side="left", padx=10)
    
    # Declara a variável 'entrada_filtro' como global para 
            # que possa ser acessada em outras funções.
    global entrada_filtro
    
    # Cria um campo de entrada (Entry) para o usuário digitar o termo a ser filtrado.
    # 'font=("Helvetica", 12)' configura o estilo e tamanho do texto digitado no campo.
    # 'width=50' define a largura do campo, permitindo que o usuário visualize termos mais longos.
    entrada_filtro = tk.Entry(frame_filtro, font=("Helvetica", 12), width=50)
    
    # Posiciona o campo de entrada no frame de filtro.
    # 'side="left"' alinha o campo à esquerda, ao lado do rótulo.
    # 'padx=10' adiciona espaçamento horizontal entre o campo e os outros elementos.
    entrada_filtro.pack(side="left", padx=10)
    
    # Cria um botão no frame de filtro para aplicar o filtro aos produtos.
    # 'text="Aplicar Filtro"' define o texto exibido no botão.
    # 'command=filtrar_produtos' vincula o botão à função 'filtrar_produtos', 
            # que será executada ao clicar no botão.
    # 'bg="#2a9d8f"' define a cor de fundo do botão como um tom de verde-azulado.
    # 'fg="white"' define a cor do texto no botão como branco.
    # 'font=("Helvetica", 12)' configura a fonte do texto como Helvetica, tamanho 12.
    btn_filtrar = tk.Button(frame_filtro, 
                            text="Aplicar Filtro", 
                            command=filtrar_produtos, 
                            bg="#2a9d8f", 
                            fg="white", 
                            font=("Helvetica", 12))
    
    # Posiciona o botão "Aplicar Filtro" no frame de filtro.
    # 'side="left"' alinha o botão à esquerda, ao lado do campo de entrada.
    # 'padx=10' adiciona espaçamento horizontal entre o botão e os outros elementos.
    btn_filtrar.pack(side="left", padx=10)
    
    # Cria um botão no frame de filtro para limpar o filtro aplicado.
    # 'text="Limpar Filtro"' define o texto exibido no botão.
    # 'command=lambda: [entrada_filtro.delete(0, tk.END), carregar_dados()]' 
            # define o comando a ser executado:
    # - Limpa o campo de entrada do filtro com 'entrada_filtro.delete(0, tk.END)'.
    # - Recarrega todos os dados na lista com 'carregar_dados()'.
    # 'bg="#e76f51"' define a cor de fundo do botão como um tom de vermelho.
    # 'fg="white"' define a cor do texto no botão como branco.
    # 'font=("Helvetica", 12)' configura a fonte do texto como Helvetica, tamanho 12.
    btn_limpar_filtro = tk.Button(frame_filtro, 
                                  text="Limpar Filtro", 
                                  command=lambda: [entrada_filtro.delete(0, tk.END), carregar_dados()], 
                                  bg="#e76f51", 
                                  fg="white", 
                                  font=("Helvetica", 12))
    
    # Posiciona o botão "Limpar Filtro" no frame de filtro.
    # 'side="left"' alinha o botão à esquerda, ao lado do botão "Aplicar Filtro".
    # 'padx=10' adiciona espaçamento horizontal entre o botão e os outros elementos.
    btn_limpar_filtro.pack(side="left", padx=10)
    
    # Cria um frame para exibir a lista de produtos ou outros
            # elementos em formato de tabela.
    # 'pady=20' adiciona espaçamento vertical em torno do frame, 
            # separando-o de outros elementos da interface.
    frame_lista = tk.Frame(janela_principal, pady=20)
    
    # Posiciona o frame de lista dentro da janela principal.
    # 'fill="both"' faz com que o frame ocupe toda a largura e
            # altura disponíveis.
    # 'expand=True' permite que o frame se expanda proporcionalmente
            # ao redimensionar a janela.
    frame_lista.pack(fill="both", expand=True)


    # Declara a variável 'tree_produtos' como global para que 
            # possa ser acessada em outras funções.
    global tree_produtos
    
    # Cria uma Treeview para exibir os dados dos produtos em formato de tabela.
    # 'frame_lista' é o contêiner onde a Treeview será adicionada.
    # 'columns=("Nome", "Preço", "Quantidade", "Fornecedor", "ID")' 
            # define as colunas da tabela.
    # Cada coluna representa uma propriedade do produto.
    # 'show="headings"' faz com que apenas os cabeçalhos das colunas 
            # sejam exibidos, sem uma coluna extra à esquerda.
    tree_produtos = ttk.Treeview(frame_lista, 
                                 columns=("Nome", "Preço", "Quantidade", "Fornecedor", "ID"), 
                                 show="headings")
    
    # Cria uma barra de rolagem vertical associada à Treeview.
    # 'frame_lista' é o contêiner onde a barra de rolagem será adicionada.
    # 'orient="vertical"' indica que a barra será vertical.
    # 'command=tree_produtos.yview' associa o movimento da barra à exibição vertical da Treeview.
    scroll_y = ttk.Scrollbar(frame_lista, orient="vertical", command=tree_produtos.yview)
    
    # Configura a Treeview para que ela utilize a barra de rolagem vertical.
    # 'yscrollcommand=scroll_y.set' sincroniza o movimento da
            # barra de rolagem com a Treeview.
    tree_produtos.configure(yscrollcommand=scroll_y.set)
    
    # Posiciona a barra de rolagem vertical à direita do frame.
    # 'side="right"' alinha a barra à borda direita do frame.
    # 'fill="y"' faz com que a barra de rolagem preencha toda a altura do frame.
    scroll_y.pack(side="right", fill="y")
    
    # Posiciona a Treeview dentro do frame.
    # 'fill="both"' faz com que a Treeview ocupe toda a largura e
            # altura disponíveis no frame.
    # 'expand=True' permite que a Treeview se expanda 
            # proporcionalmente ao redimensionar a janela.
    tree_produtos.pack(fill="both", expand=True)


    # Configura o cabeçalho da coluna "Nome" na Treeview.
    # 'text="Nome"' define o texto exibido no cabeçalho.
    tree_produtos.heading("Nome", text="Nome")
    
    # Configura o cabeçalho da coluna "Preço" na Treeview.
    # 'text="Preço"' define o texto exibido no cabeçalho.
    tree_produtos.heading("Preço", text="Preço")
    
    # Configura o cabeçalho da coluna "Quantidade" na Treeview.
    # 'text="Quantidade"' define o texto exibido no cabeçalho.
    tree_produtos.heading("Quantidade", text="Quantidade")
    
    # Configura o cabeçalho da coluna "Fornecedor" na Treeview.
    # 'text="Fornecedor"' define o texto exibido no cabeçalho.
    tree_produtos.heading("Fornecedor", text="Fornecedor")
    
    # Configura o cabeçalho da coluna "ID" na Treeview.
    # 'text="ID"' define o texto exibido no cabeçalho.
    tree_produtos.heading("ID", text="ID")
    
    # Define as propriedades visuais da coluna "Nome".
    # 'width=200' define a largura da coluna como 200 pixels.
    # 'anchor="w"' alinha o texto à esquerda dentro da coluna.
    tree_produtos.column("Nome", width=200, anchor="w")
    
    # Define as propriedades visuais da coluna "Preço".
    # 'width=100' define a largura da coluna como 100 pixels.
    # 'anchor="center"' alinha o texto ao centro dentro da coluna.
    tree_produtos.column("Preço", width=100, anchor="center")
    
    # Define as propriedades visuais da coluna "Quantidade".
    # 'width=100' define a largura da coluna como 100 pixels.
    # 'anchor="center"' alinha o texto ao centro dentro da coluna.
    tree_produtos.column("Quantidade", width=100, anchor="center")
    
    # Define as propriedades visuais da coluna "Fornecedor".
    # 'width=150' define a largura da coluna como 150 pixels.
    # 'anchor="w"' alinha o texto à esquerda dentro da coluna.
    tree_produtos.column("Fornecedor", width=150, anchor="w")
    
    # Define as propriedades visuais da coluna "ID".
    # 'width=100' define a largura da coluna como 100 pixels.
    # 'anchor="center"' alinha o texto ao centro dentro da coluna.
    tree_produtos.column("ID", width=100, anchor="center")
    
    # Vincula um evento à Treeview para capturar a seleção do usuário.
    # '<<TreeviewSelect>>' é o evento disparado quando o usuário seleciona um item.
    # 'preencher_campos_produto' é a função chamada para preencher
            # os campos com os dados do item selecionado.
    tree_produtos.bind('<<TreeviewSelect>>', preencher_campos_produto)
    
    # Chama a função 'carregar_dados' para preencher a
            # Treeview com os dados iniciais.
    # Esta função recupera os dados do banco de dados e 
            # os exibe na Treeview.
    carregar_dados()
    
    # Inicia o loop principal da interface gráfica.
    # 'mainloop()' mantém a janela principal aberta e ativa,
            # aguardando interações do usuário.
    janela_principal.mainloop()



# Define a função para preencher automaticamente os campos de entrada
    # quando um produto for selecionado na Treeview.
def preencher_campos_produto(event):
    
    # Obtém a seleção atual na Treeview que exibe os produtos.
    # 'tree_produtos.selection()' retorna uma lista com os
            # identificadores dos itens selecionados.
    selecionado = tree_produtos.selection()
    
    # Verifica se há um item selecionado na Treeview.
    # Caso nenhum item tenha sido selecionado, a função não faz nada.
    if selecionado:
        
        # Obtém os detalhes do item selecionado na Treeview.
        # 'tree_produtos.item(selecionado)' retorna um dicionário
                # com informações do item.
        item = tree_produtos.item(selecionado)
        
        # Extrai os valores das colunas do item selecionado.
        # 'item['values']' contém uma lista com os dados do produto, 
                # como nome, preço, quantidade e fornecedor.
        valores = item['values']
        
        # Limpa o campo de entrada "Nome" para garantir que não 
                # contenha dados antigos.
        entrada_nome.delete(0, tk.END)
        
        # Insere o nome do produto (primeiro valor em 'valores') no
                # campo de entrada "Nome".
        entrada_nome.insert(0, valores[0])
        
        # Limpa o campo de entrada "Preço".
        entrada_preco.delete(0, tk.END)
        
        # Insere o preço do produto (segundo valor em 'valores') no campo de entrada "Preço".
        entrada_preco.insert(0, valores[1])
        
        # Limpa o campo de entrada "Quantidade".
        entrada_quantidade.delete(0, tk.END)
        
        # Insere a quantidade do produto (terceiro valor em 'valores') 
                # no campo de entrada "Quantidade".
        entrada_quantidade.insert(0, valores[2])
        
        # Limpa o campo de entrada "Fornecedor".
        entrada_fornecedor.delete(0, tk.END)
        
        # Insere o nome do fornecedor (quarto valor em 'valores') no
                # campo de entrada "Fornecedor".
        entrada_fornecedor.insert(0, valores[3])
        
        # Define o foco no campo de "Quantidade".
        # Isso facilita a edição da quantidade pelo usuário, caso necessário.
        entrada_quantidade.focus_set()
        



# Cria a janela principal para a tela de login.
# 'tk.Tk()' inicializa a interface gráfica principal.
janela_login = tk.Tk()

# Define o título da janela.
# 'title("Login - Sistema de Estoque")' especifica o 
        # texto exibido na barra de título da janela.
janela_login.title("Login - Sistema de Estoque")

# Define o estado inicial da janela como maximizado.
# 'state('zoomed')' faz com que a janela ocupe toda a 
        # tela ao ser iniciada.
janela_login.state('zoomed')

# Permite que a janela seja redimensionada pelo usuário.
# 'resizable(True, True)' habilita a alteração de 
        # tamanho na horizontal e vertical.
janela_login.resizable(True, True)

# ------------------------------------------

# Cria um frame para organizar os elementos da tela de login.
# Este frame funciona como um contêiner para agrupar widgets 
        # como campos de entrada e botões.
# 'padx=20' adiciona um espaçamento horizontal ao redor do frame.
# 'pady=20' adiciona um espaçamento vertical ao redor do frame.
frame_login = tk.Frame(janela_login, 
                       padx=20, 
                       pady=20)

# Posiciona o frame de login no centro da janela principal.
# 'relx=0.5, rely=0.5' define as coordenadas relativas ao 
        # tamanho da janela, colocando o frame no meio.
# 'anchor="center"' ancora o frame ao seu centro, 
        # garantindo alinhamento exato.
frame_login.place(relx=0.5, 
                  rely=0.5, 
                  anchor='center')

# Cria um rótulo (label) para o título da tela de login.
# 'frame_login' é o contêiner onde o rótulo será adicionado.
# 'text="Bem-vindo ao Sistema de Estoque"' define o 
        # texto exibido no rótulo.
# 'font=("Helvetica", 20, "bold")' configura a fonte como 
        # Helvetica, tamanho 20, em negrito.
lbl_titulo_login = tk.Label(frame_login, 
                            text="Bem-vindo ao Sistema de Estoque", 
                            font=("Helvetica", 20, "bold"))

# Posiciona o rótulo do título no layout em grade.
# 'row=0, column=0' posiciona o rótulo na primeira 
        # linha (linha 0) e primeira coluna (coluna 0).
# 'columnspan=2' faz com que o rótulo ocupe duas colunas, 
        # centralizando-o no frame.
# 'pady=20' adiciona espaçamento vertical acima e abaixo 
        # do rótulo, melhorando a estética.
lbl_titulo_login.grid(row=0, 
                      column=0, 
                      columnspan=2, 
                      pady=20)

# Cria um rótulo (label) para identificar o campo de entrada "Usuário".
# 'frame_login' é o contêiner onde o rótulo será adicionado.
# 'text="Usuário:"' define o texto exibido no rótulo.
# 'font=("Helvetica", 14)' configura a fonte como Helvetica, tamanho 14.
# 'grid(row=1, column=0)' posiciona o rótulo na segunda 
        # linha (linha 1) e primeira coluna (coluna 0).
# 'pady=10' adiciona espaçamento vertical ao redor do rótulo.
# 'sticky="e"' alinha o rótulo à direita dentro da 
        # célula da grade (east - leste).
tk.Label(frame_login, 
         text="Usuário:", 
         font=("Helvetica", 14)).grid(row=1, column=0, pady=10, sticky='e')

# Cria um campo de entrada (Entry) para o usuário digitar o nome de usuário.
# 'frame_login' é o contêiner onde o campo será adicionado.
# 'font=("Helvetica", 14)' configura o estilo e 
        # tamanho do texto digitado no campo.
entrada_usuario = tk.Entry(frame_login, 
                           font=("Helvetica", 14))

# Posiciona o campo de entrada "Usuário" no layout em grade.
# 'row=1, column=1' posiciona o campo na segunda 
        # linha (linha 1) e segunda coluna (coluna 1).
# 'pady=10' adiciona espaçamento vertical ao redor do campo.
entrada_usuario.grid(row=1, 
                     column=1, 
                     pady=10)

# Cria um rótulo (label) para identificar o campo de entrada "Senha".
# 'frame_login' é o contêiner onde o rótulo será adicionado.
# 'text="Senha:"' define o texto exibido no rótulo.
# 'font=("Helvetica", 14)' configura a fonte como 
        # Helvetica, tamanho 14.
# 'grid(row=2, column=0)' posiciona o rótulo na terceira
        # linha (linha 2) e primeira coluna (coluna 0).
# 'pady=10' adiciona espaçamento vertical ao redor do rótulo.
# 'sticky="e"' alinha o rótulo à direita dentro da 
        # célula da grade (east - leste).
tk.Label(frame_login, 
         text="Senha:", 
         font=("Helvetica", 14)).grid(row=2, column=0, pady=10, sticky='e')

# Cria um campo de entrada (Entry) para o usuário digitar sua senha.
# 'frame_login' é o contêiner onde o campo será adicionado.
# 'show="*"' oculta os caracteres digitados, exibindo 
        # asteriscos (*) para proteger a senha.
# 'font=("Helvetica", 14)' configura o estilo e tamanho 
        # do texto digitado no campo.
entrada_senha = tk.Entry(frame_login, 
                         show="*", 
                         font=("Helvetica", 14))

# Posiciona o campo de entrada "Senha" no layout em grade.
# 'row=2, column=1' posiciona o campo na terceira
        # linha (linha 2) e segunda coluna (coluna 1).
# 'pady=10' adiciona espaçamento vertical ao redor do campo.
entrada_senha.grid(row=2, column=1, pady=10)

# Cria um botão para realizar o login.
# 'frame_login' é o contêiner onde o botão será adicionado.
# 'text="Login"' define o texto exibido no botão.
# 'command=verificar_login' vincula o botão à função 'verificar_login', 
        # que será executada ao clicar no botão.
# 'bg="#2a9d8f"' define a cor de fundo do botão como um tom de verde-azulado.
# 'fg="white"' define a cor do texto no botão como branco.
# 'font=("Helvetica", 14)' configura a fonte do texto 
        # como Helvetica, tamanho 14.
# 'width=10' define a largura do botão, tornando-o 
        # suficientemente largo para o texto.
btn_login = tk.Button(frame_login, 
                      text="Login", 
                      command=verificar_login, 
                      bg="#2a9d8f", 
                      fg="white", 
                      font=("Helvetica", 14), width=10)

# Posiciona o botão "Login" no layout em grade.
# 'row=3, column=0' posiciona o botão na quarta linha (linha 3) e
        # na primeira coluna (coluna 0).
# 'columnspan=2' faz com que o botão ocupe duas colunas, 
        # centralizando-o abaixo dos campos de entrada.
# 'pady=20' adiciona espaçamento vertical ao redor do 
        # botão, separando-o dos campos acima.
btn_login.grid(row=3, column=0, columnspan=2, pady=20)


# Cria um botão para permitir que o usuário acesse a 
        # tela de cadastro de um novo usuário.
# 'frame_login' é o contêiner onde o botão será adicionado.
# 'text="Cadastrar Usuário"' define o texto exibido no botão.
# 'command=abrir_tela_usuarios' vincula o botão à 
        # função 'abrir_tela_usuarios', que será executada ao clicar no botão.
# 'bg="#6a994e"' define a cor de fundo do botão como um tom de verde.
# 'fg="white"' define a cor do texto no botão como branco.
# 'font=("Helvetica", 14)' configura a fonte do texto 
        # como Helvetica, tamanho 14.
# 'width=15' define a largura do botão para 15 unidades, 
        # garantindo consistência com os outros botões.
btn_cadastrar_usuario = tk.Button(frame_login, 
                                  text="Cadastrar Usuário", 
                                  command=abrir_tela_usuarios, 
                                  bg="#6a994e", 
                                  fg="white", 
                                  font=("Helvetica", 14), 
                                  width=15)

# Posiciona o botão "Cadastrar Usuário" no layout em grade.
# 'row=4, column=0' posiciona o botão na quinta linha (linha 4) e 
        # primeira coluna (coluna 0).
# 'columnspan=2' faz com que o botão ocupe duas colunas, 
        # centralizando-o abaixo dos outros elementos.
# 'pady=10' adiciona espaçamento vertical ao redor do 
        # botão, separando-o dos elementos acima.
btn_cadastrar_usuario.grid(row=4, 
                           column=0, 
                           columnspan=2, 
                           pady=10)

# Chama a função 'criar_usuario_admin' para garantir que
        # um usuário admin padrão seja criado no banco de dados,
# caso ele ainda não exista. Esta função é executada 
        # uma vez ao iniciar a tela de login.
criar_usuario_admin()

# Inicia o loop principal da interface gráfica.
# 'mainloop()' mantém a janela de login aberta e aguarda 
        # interações do usuário, como clicar em botões.
janela_login.mainloop()