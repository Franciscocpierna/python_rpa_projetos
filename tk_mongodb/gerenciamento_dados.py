# Importa a biblioteca tkinter para criar interfaces gráficas. 
# 'tk' é um alias para facilitar o acesso às funções da biblioteca.
import tkinter as tk

# Importa componentes específicos de tkinter: ttk para widgets 
        # com estilo aprimorado e messagebox para caixas de diálogo.
from tkinter import ttk, messagebox

# Importa o MongoClient de pymongo, que permite conectar ao 
        # servidor MongoDB e executar operações no banco de dados.
from pymongo import MongoClient

# Importa ObjectId de bson.objectid, utilizado para manipular os 
        # identificadores únicos do MongoDB.
from bson.objectid import ObjectId  # Importando ObjectId

# Importa a biblioteca pandas como 'pd', que é usada para manipulação e 
        # análise de dados, incluindo a exportação para Excel.
import pandas as pd

# Cria uma conexão ao MongoDB, especificando a URL do servidor 
        # local e a porta padrão (27017).
cliente = MongoClient("mongodb://localhost:27017")  # Atualize para seu endereço

# Acessa o banco de dados chamado 'CadastroDB' dentro do servidor MongoDB. 
banco = cliente["CadastroDB"]

# Acessa a coleção 'usuarios' dentro do banco de dados 'CadastroDB'.
# Uma coleção no MongoDB é similar a uma tabela em bancos de dados relacionais.
colecao = banco["usuarios"]


# Define a função 'carregar_dados', que pode receber um parâmetro 
        # opcional chamado 'filtros'.
# Esta função é crucial para a interação com o banco de dados MongoDB, 
        # carregando dados na interface gráfica baseada em critérios de 
        # filtro fornecidos pelo usuário.
def carregar_dados(filtros=None):
    
    """Carrega os dados do MongoDB para a Treeview com base nos filtros."""

    # Inicia iterando sobre todos os itens atualmente exibidos na Treeview.
    # A função 'get_children()' recupera uma lista de todos os itens (linhas).
    for item in tree.get_children():
        
        # Para cada item identificado pela 'get_children()', o 'delete(item)' é chamado.
        # Este comando remove cada item da Treeview para evitar duplicação 
                # de dados quando os novos dados forem carregados.
        # Isso assegura que a Treeview esteja limpa antes de 
                # carregar ou recarregar dados.
        tree.delete(item)
    
    # Cria uma variável 'consulta' que verificará se algum filtro foi fornecido.
    # Se 'filtros' não for None, usa o valor de 'filtros'; caso 
            # contrário, usa um dicionário vazio.
    # Um dicionário vazio em uma consulta MongoDB retorna todos os 
            # registros da coleção, porque não especifica condições de filtro.
    consulta = filtros if filtros else {}
    
    # Realiza uma consulta ao MongoDB usando a coleção 'colecao'.
    # O método 'find(consulta)' executa a busca na coleção 'colecao' 
            # do MongoDB com os critérios especificados em 'consulta'.
    # Se 'consulta' for um dicionário vazio, todos os documentos
            # na coleção serão retornados.
    registros = colecao.find(consulta)
    
    # Itera sobre cada documento retornado pela função 'find'.
    for doc in registros:
        
        # Cada documento (doc) é inserido como uma nova linha na Treeview.
        # O primeiro argumento "" em 'tree.insert' significa que o novo item não 
                # terá um item pai, ou seja, será adicionado na raiz da Treeview.
        # "end" especifica que o item será adicionado ao final da lista de itens visíveis.
        # 'values' recebe um tuple que contém os dados a serem inseridos em
                # cada coluna do Treeview.
        # Os valores de '_id', 'nome', 'idade' e 'email' são extraídos de 
                # cada documento e convertidos para string quando necessário.
        tree.insert("", "end", values=(str(doc["_id"]), doc["nome"], doc["idade"], doc["email"]))
    
    # Após carregar todos os dados, a função 'atualizar_total' é chamada.
    # Esta função atualiza um label na interface para mostrar o número total de 
            # itens agora visíveis na Treeview, fornecendo feedback 
            # visual imediato ao usuário.
    atualizar_total()



# Define a função 'atualizar_total', que atualiza o texto de um label na interface
            # gráfica para mostrar o número total de itens atualmente visíveis na Treeview.
def atualizar_total():
    
    """Atualiza o total de itens visíveis na Treeview."""

    # Conta o número de itens na Treeview. 'get_children()' retorna todos os
            # itens presentes na Treeview, e 'len()' conta quantos itens existem.
    total = len(tree.get_children())
    
    # Atualiza o texto do label 'lbl_total' para refletir o número 
            # total de itens visíveis na Treeview.
    # 'text=f"Total de itens: {total}"' configura o texto do label 
            # para mostrar essa contagem.
    lbl_total.config(text=f"Total de itens: {total}")


# Inicia a definição da função 'adicionar_dados', que é usada para 
        # adicionar novos registros ao MongoDB.
# Esta função não aceita parâmetros externos e interage diretamente com a 
        # interface gráfica para obter os dados.
def adicionar_dados():
    
    """Adiciona um novo registro ao MongoDB."""

    # Acessa o valor no campo de entrada 'nome' na interface gráfica e 
            # armazena na variável 'nome'.
    nome = entrada_nome.get()

    # Acessa o valor no campo de entrada 'idade' na interface gráfica e 
            # armazena na variável 'idade'.
    idade = entrada_idade.get()

    # Acessa o valor no campo de entrada 'email' na interface gráfica e 
            # armazena na variável 'email'.
    email = entrada_email.get()

    # Verifica se os campos 'nome', 'idade' ou 'email' estão vazios. 
            # Caso qualquer um esteja, exibe uma mensagem de erro.
    if not nome or not idade or not email:
        
        # Mostra uma caixa de diálogo de erro informando que todos os 
                # campos são necessários.
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        
        # Encerra a função sem executar as etapas subsequentes, 
                # impedindo a inserção de dados incompletos.
        return

    # Tentativa de converter o valor de 'idade' para um número inteiro para
                # garantir que o dado inserido é válido para idade.
    try:
        
        idade = int(idade)

    # Executa o seguinte bloco caso 'idade' não possa ser convertido em um inteiro.
    except ValueError:  
        
        # Mostra uma mensagem de erro se 'idade' não for um número, 
                # informando o usuário do erro de entrada.
        messagebox.showerror("Erro", "Idade deve ser um número!")
        
        # Encerra a função, evitando a adição de dados incorretos.
        return

    # Insere os dados coletados na coleção 'colecao' no MongoDB.
    # Cria um documento dentro da coleção que contém o nome, a
            # idade (já convertida para inteiro) e o email.
    colecao.insert_one({"nome": nome, "idade": idade, "email": email})

    # Após inserir os dados com sucesso, mostra uma mensagem 
            # informando o sucesso da operação.
    messagebox.showinfo("Sucesso", "Dados cadastrados com sucesso!")

    # Atualiza a lista de registros mostrada na interface, chamando a 
            # função 'carregar_dados' para refletir o registro recém-adicionado.
    carregar_dados()

    # Limpa os campos de entrada para que estejam prontos para 
            # uma nova inserção.
    # Esta etapa é crucial para evitar inserções acidentais do 
            # mesmo dado mais de uma vez.
    limpar_campos()



# Define a função 'limpar_campos' que é responsável por limpar todos os 
        # campos de entrada na interface gráfica.
def limpar_campos():
    
    """Limpa os campos de entrada."""
    
    # Limpa o campo de entrada do nome.
    # 'entrada_nome.delete(0, tk.END)' remove todo o texto do campo 'entrada_nome'.
    # O primeiro argumento '0' indica o início do campo, e 'tk.END' indica o fim do campo, 
    # significando que tudo entre esses dois pontos será deletado.
    entrada_nome.delete(0, tk.END)
    
    # Limpa o campo de entrada da idade.
    # Funciona da mesma forma que o comando anterior, removendo 
            # todo o texto do campo 'entrada_idade'.
    entrada_idade.delete(0, tk.END)
    
    # Limpa o campo de entrada do email.
    # Novamente, usa o mesmo método para remover todo o texto do 
            # campo 'entrada_email'.
    entrada_email.delete(0, tk.END)
    


# Define a função 'alterar_dados', que é usada para modificar os dados de
            # um registro já existente no banco de dados MongoDB.
def alterar_dados():
    
    """Altera o registro selecionado no MongoDB."""

    # Obtém o(s) item(ns) atualmente selecionado(s) na Treeview e 
            # armazena na variável 'selecionado'.
    selecionado = tree.selection()

    # Verifica se algum item foi realmente selecionado na Treeview
            # antes de tentar alterar.
    if not selecionado:
        
        # Mostra uma mensagem de erro caso nenhum item esteja selecionado
                # quando o usuário tentar alterar.
        messagebox.showerror("Erro", "Selecione um registro para alterar!")
        
        # Encerra a função sem fazer alterações se nenhum item
                # estiver selecionado.
        return

    # Acessa os dados do item selecionado na Treeview.
    item = tree.item(selecionado)
    
    # Extrai o ID do documento MongoDB do primeiro valor no item selecionado, 
            # que é usado para identificar unicamente o registro no banco de dados.
    doc_id = item["values"][0]

    # Recupera o texto atual dos campos de entrada de nome, idade e email na 
            # interface gráfica e armazena nas respectivas variáveis.
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    email = entrada_email.get()

    
    # Verifica se algum dos campos de entrada 'nome', 'idade' ou 'email' está vazio.
    if not nome or not idade or not email:
        
        # Caso algum campo esteja vazio, exibe uma mensagem de erro informando 
                # que todos os campos são obrigatórios.
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        
        # Interrompe a execução da função, não prosseguindo com a
                # atualização dos dados.
        return
    
    # Tenta converter o valor da idade para um inteiro, necessário para garantir
            # que a idade seja armazenada corretamente no banco.
    try:
        
        idade = int(idade)

    # Captura a exceção caso o valor fornecido não possa ser 
            # convertido em inteiro.
    except ValueError:  
        
        # Mostra uma mensagem de erro caso o valor fornecido para
                # idade não seja um número válido.
        messagebox.showerror("Erro", "Idade deve ser um número!")
        
        # Encerra a função sem fazer alterações se a idade não 
                # for um número válido.
        return
    
    # Atualiza o registro na coleção 'colecao' do MongoDB
            # usando o ObjectId do documento.
    # A operação '$set' atualiza os campos 'nome', 'idade' e 'email' 
            # com os novos valores fornecidos.
    colecao.update_one({"_id": ObjectId(doc_id)}, {"$set": {"nome": nome, "idade": idade, "email": email}})
    
    # Exibe uma mensagem informando que o registro foi alterado
            # com sucesso no banco de dados.
    messagebox.showinfo("Sucesso", "Registro alterado com sucesso!")
    
    # Chama a função 'carregar_dados' para recarregar e exibir os 
            # dados atualizados na Treeview.
    carregar_dados()
    
    # Chama a função 'limpar_campos' para limpar os campos de entrada, 
            # preparando a interface para novas entradas ou seleções.
    limpar_campos()


# Define a função 'excluir_dados' que é responsável por excluir
            # registros selecionados do banco de dados MongoDB.
def excluir_dados():
    
    """Exclui o registro selecionado do MongoDB."""

    # Obtém o item atualmente selecionado na interface gráfica Treeview e
            # armazena na variável 'selecionado'.
    selecionado = tree.selection()

    # Verifica se algum item foi realmente selecionado na Treeview.
    if not selecionado:
        
        # Mostra uma mensagem de erro caso nenhum item esteja selecionado 
                # quando o usuário tentar excluir.
        messagebox.showerror("Erro", "Selecione um registro para excluir!")
        
        # Encerra a função prematuramente, não permitindo 
                # prosseguir com a exclusão.
        return

    # Obtém os dados do item selecionado na Treeview, especificamente o 
            # documento MongoDB correspondente.
    item = tree.item(selecionado)
    
    # Extrai o ID do documento MongoDB do primeiro valor no item selecionado, 
            # que é necessário para identificar unicamente o registro no banco de dados.
    doc_id = item["values"][0]

    # Executa a operação de exclusão no MongoDB usando o ObjectId do documento,
            # garantindo que o registro correto seja excluído.
    colecao.delete_one({"_id": ObjectId(doc_id)})

    # Exibe uma mensagem de sucesso ao usuário, informando que o registro
            # foi excluído com sucesso do banco de dados.
    messagebox.showinfo("Sucesso", "Registro excluído com sucesso!")

    # Chama a função 'carregar_dados' para atualizar a lista de registros
            # mostrada na interface, refletindo a mudança após a exclusão.
    carregar_dados()

    # Chama a função 'limpar_campos' para limpar os campos de entrada
            # após a exclusão do registro.
    limpar_campos()



# Define a função 'filtrar_dados' que ajusta os registros mostrados ao usuário na 
        # interface gráfica, baseando-se nos dados que ele digita nos campos de entrada.
def filtrar_dados():
    
    """Filtra os dados com base nos campos preenchidos."""

    # Acessa o valor que o usuário inseriu no campo 'Nome'.
    nome = entrada_nome.get()
    
    # Acessa o valor que o usuário inseriu no campo 'Idade'.
    idade = entrada_idade.get()
    
    # Acessa o valor que o usuário inseriu no campo 'Email'.
    email = entrada_email.get()

    # Cria um dicionário para armazenar condições de busca que serão
            # usadas para filtrar os dados no banco de dados.
    filtros = {}

    # Checa se o usuário preencheu algo no campo 'Nome'.
    if nome:
        
        # Utiliza a expressão regular ($regex) para encontrar documentos 
                # onde o 'nome' contém o texto inserido pelo usuário.
        # A expressão regular é uma forma poderosa de especificar
                # padrões de texto para busca.
        # "$options": "i" torna a busca insensível a maiúsculas e minúsculas, 
                # permitindo que 'ana', 'Ana' e 'ANA' sejam considerados iguais.
        filtros["nome"] = {"$regex": nome, "$options": "i"}

    # Checa se o usuário preencheu algo no campo 'Idade'.
    if idade:
        
        # Tenta converter a entrada de idade de texto para número.
        try:
            
            idade = int(idade)
            
            # Se bem-sucedido, o filtro busca documentos onde a 'idade' é
                    # exatamente o número fornecido.
            filtros["idade"] = idade

        # Caso a conversão falhe porque a entrada não é numérica.
        except ValueError:  
            
            # Mostra uma mensagem de erro avisando que a idade precisa ser um número.
            messagebox.showerror("Erro", "Idade deve ser um número!")
            
            # Encerra a execução da função sem aplicar os filtros, para que o 
                    # usuário possa corrigir a entrada.
            return

    # Checa se o usuário preencheu algo no campo 'Email'.
    if email:
        
        # Similar ao filtro de nome, usa uma expressão regular para encontrar 
                # documentos onde o 'email' contém o texto inserido.
        filtros["email"] = {"$regex": email, "$options": "i"}

    # Chama a função 'carregar_dados', passando os filtros definidos, que 
            # atualiza a lista de registros mostrada na interface.
    carregar_dados(filtros)


# Define a função 'exportar_para_excel' que é responsável por exportar os 
        # dados exibidos na Treeview para um arquivo Excel.
def exportar_para_excel():
    
    """Exporta os dados visíveis na Treeview para um arquivo Excel."""
    
    # Cria uma lista vazia para armazenar os registros.
    registros = []
    
    # Itera sobre cada item presente na Treeview. 'get_children()' retorna 
            # todos os itens (linhas) que estão atualmente visíveis na Treeview.
    for item in tree.get_children():
        
        # Para cada item, acessa os dados associados (ID, Nome, Idade, Email) e
                # adiciona à lista de registros.
        # 'tree.item(item, "values")' obtém os valores dos campos de 
                # cada item na Treeview.
        registros.append(tree.item(item, "values"))
    
    # Cria um DataFrame do pandas a partir da lista de registros. DataFrames são 
            # estruturas de dados tabulares muito usadas em análise de dados.
    # 'columns=["ID", "Nome", "Idade", "Email"]' especifica os nomes das colunas no 
            # DataFrame, correspondentes aos dados extraídos da Treeview.
    df = pd.DataFrame(registros, columns=["ID", "Nome", "Idade", "Email"])
    
    # Define o nome do arquivo Excel onde os dados serão salvos.
    arquivo = "dados_exportados.xlsx"
    
    # Salva o DataFrame em um arquivo Excel. 'index=False' diz ao pandas para não 
            # incluir uma coluna de índice no arquivo Excel, deixando apenas os dados.
    df.to_excel(arquivo, index=False)
    
    # Exibe uma mensagem informando ao usuário que os dados foram exportados
            # com sucesso para o arquivo especificado.
    messagebox.showinfo("Sucesso", f"Dados exportados para o arquivo '{arquivo}' com sucesso!")



# Define a função 'selecionar_item', que é chamada quando um
        # item é selecionado na Treeview.
# Esta função recebe um parâmetro 'evento', que contém informações
        # sobre o evento de seleção.
def selecionar_item(evento):
    
    """Preenche os campos de entrada com os dados do item selecionado na Treeview."""

    # Obtém o item que foi selecionado na Treeview.
    selecionado = tree.selection()

    # Verifica se algum item foi realmente selecionado.
    if selecionado:
        
        # Acessa os dados do item selecionado.
        item = tree.item(selecionado)
        
        # 'values' contém os dados do registro selecionado na Treeview, 
                # como ID, nome, idade e email.
        valores = item["values"]

        # Limpa o campo de entrada do nome para evitar que
                # dados antigos sejam misturados com novos.
        entrada_nome.delete(0, tk.END)
        
        # Insere o nome do registro selecionado no campo de entrada do nome.
        entrada_nome.insert(0, valores[1])

        # Limpa o campo de entrada da idade.
        entrada_idade.delete(0, tk.END)
        
        # Insere a idade do registro selecionado no campo de entrada da idade.
        entrada_idade.insert(0, valores[2])

        # Limpa o campo de entrada do email.
        entrada_email.delete(0, tk.END)
        
        # Insere o email do registro selecionado no campo de entrada do email.
        entrada_email.insert(0, valores[3])



# Cria uma nova janela Tkinter, que serve como a janela 
        # principal para a aplicação.
janela = tk.Tk()

# Define o título da janela, que aparece na barra de título da janela.
janela.title("Gerenciador de Dados com MongoDB")

# Configura as dimensões iniciais da janela. '800x650' define a 
        # largura de 800 pixels e a altura de 650 pixels.
janela.geometry("800x650")

# Impede que a janela seja redimensionada, tanto em largura
        # quanto em altura.
janela.resizable(False, False)

# Criação de um 'Frame' (quadro) no topo da janela principal.
        # Um 'Frame' é um container que agrupa outros widgets.
# 'bg="#2a9d8f"' define a cor de fundo do frame usando um 
        # valor hexadecimal para a cor.
# 'height=50' configura a altura do frame para 50 pixels.
frame_topo = tk.Frame(janela, bg="#2a9d8f", height=50)

# Adiciona o 'frame_topo' à janela principal. 'fill="x"' faz com 
        # que o frame se expanda horizontalmente para preencher 
        # todo o espaço disponível.
frame_topo.pack(fill="x")

# Cria um 'Label' (etiqueta) para exibir o título dentro do 'frame_topo'.
# 'text="Gerenciador de Dados"' define o texto que aparecerá no label.
# 'bg="#2a9d8f"' e 'fg="white"' configuram a cor de fundo e a 
        # cor do texto do label, respectivamente.
# 'font=("Helvetica", 16, "bold")' define a fonte do texto como 
        # Helvetica, tamanho 16 e em negrito.
lbl_titulo = tk.Label(frame_topo, 
                      text="Gerenciador de Dados", 
                      bg="#2a9d8f", 
                      fg="white", 
                      font=("Helvetica", 16, "bold"))

# Adiciona o 'lbl_titulo' ao 'frame_topo'. 'pady=10' adiciona um
        # padding vertical de 10 pixels acima e abaixo do label 
        # para dar espaço extra.
lbl_titulo.pack(pady=10)


# Cria outro 'Frame' chamado 'frame_dados' na janela principal 
        # para conter os campos de entrada e outros widgets.
# 'padx=20' e 'pady=10' adicionam padding horizontal de 20 pixels e 
        # vertical de 10 pixels em torno do conteúdo interno do frame.
frame_dados = tk.Frame(janela, 
                       padx=20, 
                       pady=10)

# Adiciona o 'frame_dados' à janela principal. 
# 'fill="x"' faz com que o frame se expanda horizontalmente
        # para preencher todo o espaço disponível.
frame_dados.pack(fill="x")

# Cria um Label (etiqueta) para o campo 'Nome' e o adiciona ao 'frame_dados'.
# 'text="Nome:"' define o texto do Label como "Nome:".
# 'font=("Helvetica", 12)' define a fonte do texto como Helvetica, tamanho 12.
# O método 'grid' é usado para posicionar o Label na primeira
        # linha (row=0) e primeira coluna (column=0) do 'frame_dados'.
# 'sticky="e"' faz com que o Label seja alinhado à direita 
        # dentro da célula da grade (East - leste).
tk.Label(frame_dados, 
         text="Nome:", 
         font=("Helvetica", 12)).grid(row=0, column=0, sticky="e")

# Cria um Entry (campo de entrada) para que o usuário 
        # possa digitar seu nome e o adiciona ao 'frame_dados'.
# 'font=("Helvetica", 12)' define a fonte do texto 
        # dentro do campo de entrada.
entrada_nome = tk.Entry(frame_dados, font=("Helvetica", 12))

# Posiciona o campo de entrada na grade: na primeira 
        # linha (row=0) e segunda coluna (column=1).
# 'padx=10' e 'pady=5' adicionam um espaçamento externo de 10 
        # pixels horizontalmente e 5 pixels verticalmente em
        # torno do campo de entrada.
entrada_nome.grid(row=0, column=1, padx=10, pady=5)


# Cria um Label para o campo 'Idade' e o adiciona ao 'frame_dados'.
# 'text="Idade:"' define o texto do Label como "Idade:".
# 'font=("Helvetica", 12)' define a fonte do texto como Helvetica, tamanho 12.
# O Label é posicionado na segunda linha (row=1) e primeira 
        # coluna (column=0) do 'frame_dados'.
# 'sticky="e"' faz com que o Label seja alinhado à direita dentro da célula da grade.
tk.Label(frame_dados, 
         text="Idade:", 
         font=("Helvetica", 12)).grid(row=1, column=0, sticky="e")

# Cria um Entry para que o usuário possa digitar sua 
        # idade e o adiciona ao 'frame_dados'.
# 'font=("Helvetica", 12)' define a fonte do texto 
        # dentro do campo de entrada.
entrada_idade = tk.Entry(frame_dados, font=("Helvetica", 12))

# Posiciona o campo de entrada na grade: na segunda 
        # linha (row=1) e segunda coluna (column=1).
# 'padx=10' e 'pady=5' adicionam um espaçamento externo de 10 pixels 
        # horizontalmente e 5 pixels verticalmente em 
        # torno do campo de entrada.
entrada_idade.grid(row=1, column=1, padx=10, pady=5)


# Cria um Label (rótulo) para o campo 'Email' e o adiciona ao 'frame_dados'.
# 'text="Email:"' define o texto do Label como "Email:".
# 'font=("Helvetica", 12)' especifica que o texto dentro do Label 
        # deve usar a fonte Helvetica no tamanho 12.
# O método 'grid' posiciona o Label na terceira linha (row=2) e na 
        # primeira coluna (column=0) do grid no 'frame_dados'.
# 'sticky="e"' alinha o Label à direita (leste) dentro de sua 
        # célula no grid, garantindo que ele fique alinhado 
        # com os Labels de 'Nome' e 'Idade'.
tk.Label(frame_dados, 
         text="Email:", 
         font=("Helvetica", 12)).grid(row=2, column=0, sticky="e")

# Cria um Entry (campo de entrada de texto) para que o usuário 
        # possa digitar seu email e o adiciona ao 'frame_dados'.
# 'font=("Helvetica", 12)' aplica a mesma fonte Helvetica 
        # tamanho 12 ao texto que será digitado no campo de entrada.
entrada_email = tk.Entry(frame_dados, 
                         font=("Helvetica", 12))

# Posiciona o campo de entrada 'entrada_email' no grid: ele 
        # fica na terceira linha (row=2) e na segunda coluna (column=1).
# 'padx=10' adiciona um espaçamento horizontal de 10 pixels em 
        # cada lado do Entry, ajudando a separá-lo visualmente do Label.
# 'pady=5' adiciona um espaçamento vertical de 5 pixels acima e 
        # abaixo do Entry, mantendo uma distância uniforme entre as 
        # linhas para melhor estética.
entrada_email.grid(row=2, 
                   column=1, 
                   padx=10, 
                   pady=5)

# Cria um novo Frame (container) chamado 'frame_botoes' que 
        # será usado para conter os botões da interface.
# Este Frame é adicionado à janela principal ('janela').
# 'pady=10' adiciona um espaçamento vertical de 10 pixels acima e 
        # abaixo do frame, proporcionando um espaço visual entre o 
        # 'frame_dados' e onde os botões serão colocados.
frame_botoes = tk.Frame(janela, pady=10)

# Usa o método 'pack' para adicionar o 'frame_botoes' à janela principal.
# 'fill="x"' faz com que o Frame expanda horizontalmente para 
        # preencher todo o espaço disponível na largura da janela,
        # assegurando que os botões dentro deste frame possam
        # também expandir ou alinhar-se conforme necessário.
frame_botoes.pack(fill="x")

# Cria um botão chamado 'btn_adicionar' no 'frame_botoes'.
# 'text="Adicionar"' define o texto que aparecerá no botão.
# 'command=adicionar_dados' associa este botão à função 'adicionar_dados', 
        # que será executada quando o botão for clicado.
# 'bg="#2a9d8f"' configura a cor de fundo do botão com um código 
        # de cor hexadecimal (um verde-azulado).
# 'fg="white"' define a cor do texto no botão como branco para 
        # contraste com o fundo verde-azulado.
# 'font=("Helvetica", 12)' define a fonte do texto no
        # botão como Helvetica, tamanho 12.
# 'width=10' especifica a largura do botão, garantindo que
        # tenha espaço suficiente para o texto.
btn_adicionar = tk.Button(frame_botoes, 
                          text="Adicionar", 
                          command=adicionar_dados, 
                          bg="#2a9d8f", 
                          fg="white", 
                          font=("Helvetica", 12), width=10)

# Adiciona o botão 'btn_adicionar' ao layout do 'frame_botoes'.
# 'side="left"' faz com que o botão seja posicionado à esquerda dentro do frame.
# 'padx=10' adiciona um espaçamento horizontal de 10 pixels em 
        # torno do botão, ajudando a separá-lo de outros 
        # elementos no frame.
btn_adicionar.pack(side="left", padx=10)

# Cria um botão chamado 'btn_alterar' no 'frame_botoes'.
# 'text="Alterar"' define o texto que aparecerá no botão.
# 'command=alterar_dados' associa este botão à função 'alterar_dados', 
        # que será executada quando o botão for clicado.
# 'bg="#f4a261"' configura a cor de fundo do botão com um código 
        # de cor hexadecimal (um laranja claro).
# 'fg="white"' define a cor do texto no botão como branco, 
        # criando um contraste com o fundo laranja.
# 'font=("Helvetica", 12)' define a fonte do texto no botão 
        # como Helvetica, tamanho 12.
# 'width=10' especifica a largura do botão, assegurando que 
        # seja grande o suficiente para o texto.
btn_alterar = tk.Button(frame_botoes, 
                        text="Alterar", 
                        command=alterar_dados, 
                        bg="#f4a261", 
                        fg="white", 
                        font=("Helvetica", 12), 
                        width=10)

# Adiciona o botão 'btn_alterar' ao layout do 'frame_botoes'.
# 'side="left"' faz com que o botão seja posicionado à esquerda 
        # dentro do frame, ao lado do botão 'Adicionar'.
# 'padx=10' adiciona um espaçamento horizontal de 10 pixels em 
        # torno do botão, mantendo um espaçamento adequado 
        # entre este e outros botões.
btn_alterar.pack(side="left", padx=10)

# Cria um botão chamado 'btn_excluir' dentro do 'frame_botoes'.
# 'text="Excluir"' configura o texto que aparecerá no botão.
# 'command=excluir_dados' associa este botão à função 'excluir_dados', 
        # que será chamada quando o botão for clicado.
# 'bg="#e76f51"' define a cor de fundo do botão usando um código 
        # hexadecimal (um laranja-avermelhado).
# 'fg="white"' estabelece a cor do texto como branco, proporcionando um 
        # alto contraste com o fundo laranja-avermelhado.
# 'font=("Helvetica", 12)' especifica a fonte do texto no 
        # botão como Helvetica, tamanho 12.
# 'width=10' define a largura do botão para garantir que o 
        # texto caiba confortavelmente.
btn_excluir = tk.Button(frame_botoes, 
                        text="Excluir", 
                        command=excluir_dados, 
                        bg="#e76f51", 
                        fg="white", 
                        font=("Helvetica", 12), 
                        width=10)

# Posiciona o botão 'btn_excluir' à esquerda dentro do 'frame_botoes'.
# 'side="left"' orienta que o botão fique alinhado à esquerda 
        # junto aos outros botões já posicionados.
# 'padx=10' adiciona uma margem horizontal de 10 pixels ao redor 
        # do botão, ajudando a separá-lo dos botões adjacentes.
btn_excluir.pack(side="left", 
                 padx=10)

# Cria um botão chamado 'btn_filtrar' dentro do 'frame_botoes'.
# 'text="Filtrar"' define o texto que será exibido no botão.
# 'command=filtrar_dados' vincula este botão à função 'filtrar_dados', 
        # que será executada ao clicar no botão.
# 'bg="#264653"' configura a cor de fundo do botão com um código de 
        # cor hexadecimal (um azul escuro profundo).
# 'fg="white"' define a cor do texto no botão como branco, criando um 
        # contraste visual eficaz com o fundo escuro.
# 'font=("Helvetica", 12)' especifica que a fonte do texto no 
        # botão seja Helvetica, tamanho 12.
# 'width=10' estabelece a largura do botão para adequar-se ao texto e 
        # manter a consistência com os outros botões.
btn_filtrar = tk.Button(frame_botoes, 
                        text="Filtrar", 
                        command=filtrar_dados, 
                        bg="#264653", 
                        fg="white", 
                        font=("Helvetica", 12), 
                        width=10)

# Adiciona o botão 'btn_filtrar' ao layout do 'frame_botoes', 
        # posicionando-o à esquerda.
# 'side="left"' garante que o botão se alinhe à esquerda 
        # com os outros botões.
# 'padx=10' inclui um espaço horizontal de 10 pixels em torno do 
        # botão para evitar que ele fique demasiadamente próximo 
        # aos botões adjacentes.
btn_filtrar.pack(side="left", 
                 padx=10)


# Cria um botão chamado 'btn_exportar' dentro do 'frame_botoes'.
# 'text="Exportar para Excel"' define o texto que será exibido no
        # botão, informando claramente sua função.
# 'command=exportar_para_excel' vincula este botão à função 'exportar_para_excel',
        # que é chamada quando o botão é clicado.
# 'bg="#6a994e"' estabelece a cor de fundo do botão usando um 
        # código hexadecimal (um verde claro).
# 'fg="white"' define a cor do texto como branco, garantindo bom
        # contraste e visibilidade.
# 'font=("Helvetica", 12)' especifica a fonte do texto no botão
        # como Helvetica, tamanho 12.
# 'width=15' define a largura do botão, um pouco maior do que os outros 
        # para acomodar o texto mais longo.
btn_exportar = tk.Button(frame_botoes, 
                         text="Exportar para Excel", 
                         command=exportar_para_excel, 
                         bg="#6a994e", 
                         fg="white", 
                         font=("Helvetica", 12), 
                         width=15)

# Posiciona o botão 'btn_exportar' à esquerda dentro do 'frame_botoes'.
# 'side="left"' orienta que o botão fique alinhado à esquerda 
        # junto aos outros botões já posicionados.
# 'padx=10' adiciona uma margem horizontal de 10 pixels ao redor do 
        # botão, ajudando a separá-lo dos botões adjacentes.
btn_exportar.pack(side="left", padx=10)


# Cria um Label chamado 'lbl_total' que mostra o total de 
        # itens presentes na Treeview.
# 'text="Total de itens: 0"' inicializa o label com um texto que 
        # indica que inicialmente não há itens.
# 'font=("Helvetica", 12)' especifica a fonte do texto 
        # como Helvetica, tamanho 12.
# 'pady=10' adiciona espaçamento vertical acima e abaixo do 
        # label para uma melhor apresentação visual.
# 'bg="#f0f0f0"' define a cor de fundo do label como um cinza 
        # claro, ajudando no contraste com o texto.
lbl_total = tk.Label(janela, 
                     text="Total de itens: 0", 
                     font=("Helvetica", 12), 
                     pady=10, 
                     bg="#f0f0f0")

# Posiciona o 'lbl_total' na janela principal.
# O método 'pack()' é usado sem argumentos específicos de posicionamento, o 
        # que permite que ele ocupe o espaço necessário na parte superior da janela.
lbl_total.pack()


# Cria um Frame chamado 'frame_lista' que irá conter a Treeview ou 
        # outros widgets relacionados à lista de dados.
# 'pady=20' adiciona espaçamento vertical de 20 pixels acima e abaixo do 
        # frame, proporcionando isolamento visual dos outros elementos.
frame_lista = tk.Frame(janela, pady=20)

# Adiciona o 'frame_lista' à janela principal, configurando-o para 
        # expandir e preencher tanto a largura quanto a altura disponíveis.
# 'fill="both"' faz com que o frame se expanda tanto horizontal quanto verticalmente.
# 'expand=True' permite que o frame aproveite qualquer espaço extra na 
        # janela, assegurando que a lista de dados utilize o máximo de espaço possível.
frame_lista.pack(fill="both", expand=True)

# Cria um objeto de estilo para customizar a aparência dos widgets 
        # do tipo Treeview da biblioteca ttk.
estilo = ttk.Style()

# Configura o estilo para todos os Treeviews da aplicação.
# 'font=("Helvetica", 12)' define a fonte e tamanho do texto dentro das 
        # células do Treeview, tornando os dados mais legíveis.
# Aumenta a fonte dos dados para facilitar a leitura.
estilo.configure("Treeview", font=("Helvetica", 12))  

# Configura o estilo dos cabeçalhos das colunas do Treeview.
# 'font=("Helvetica", 12, "bold")' define a fonte, tamanho e 
        # estilo (negrito) dos cabeçalhos, destacando-os visualmente.
# Aumenta e enfatiza a fonte do cabeçalho.
estilo.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))  


# Cria o widget Treeview no frame 'frame_lista', que será usado
        # para exibir uma lista de dados.
# 'columns=("ID", "Nome", "Idade", "Email")' define as colunas do Treeview.
# 'show="headings"' configura o Treeview para mostrar apenas os 
        # cabeçalhos das colunas, sem a coluna da árvore.
# 'style="Treeview"' aplica o estilo configurado anteriormente ao Treeview.
tree = ttk.Treeview(frame_lista, 
                    columns=("ID", "Nome", "Idade", "Email"), 
                    show="headings", 
                    style="Treeview")

# Cria uma Scrollbar vertical para o Treeview dentro do 'frame_lista'.
# 'orient="vertical"' define a orientação da Scrollbar como vertical.
# 'command=tree.yview' vincula a barra de rolagem ao movimento vertical do Treeview.
scroll_y = ttk.Scrollbar(frame_lista, orient="vertical", command=tree.yview)

# Configura o Treeview para atualizar a posição da Scrollbar 
        # conforme o usuário rola os dados.
# 'yscrollcommand=scroll_y.set' faz com que o Treeview comunique 
        # qualquer alteração na sua visualização para a Scrollbar.
tree.configure(yscrollcommand=scroll_y.set)

# Adiciona a Scrollbar ao lado direito do 'frame_lista' e a 
        # configura para preencher o espaço verticalmente.
# 'side="right"' posiciona a Scrollbar no lado direito do frame.
# 'fill="y"' faz com que a Scrollbar preencha todo o 
        # espaço vertical disponível.
scroll_y.pack(side="right", fill="y")

# Adiciona o Treeview ao layout do 'frame_lista'.
# 'fill="both"' faz com que o Treeview expanda tanto horizontal 
        # quanto verticalmente para preencher o espaço disponível.
# 'expand=True' permite que o Treeview aproveite qualquer espaço 
        # extra no frame para mostrar mais dados.
tree.pack(fill="both", expand=True)


# Configura o cabeçalho da coluna "ID" no Treeview para exibir o texto "ID".
tree.heading("ID", text="ID")

# Configura o cabeçalho da coluna "Nome" para exibir o texto "Nome".
tree.heading("Nome", text="Nome")

# Configura o cabeçalho da coluna "Idade" para exibir o texto "Idade".
tree.heading("Idade", text="Idade")

# Configura o cabeçalho da coluna "Email" para exibir o texto "Email".
tree.heading("Email", text="Email")

# Configura as propriedades da coluna "ID".
# 'width=50' define a largura da coluna como 50 pixels.
# 'anchor="center"' alinha o texto dentro da coluna ao centro.
tree.column("ID", width=50, anchor="center")

# Configura as propriedades da coluna "Nome".
# 'width=200' define a largura da coluna como 200 pixels, 
        # oferecendo espaço adequado para nomes mais longos.
# 'anchor="w"' alinha o texto à esquerda (west).
tree.column("Nome", width=200, anchor="w")

# Configura as propriedades da coluna "Idade".
# 'width=100' define a largura da coluna como 100 pixels.
# 'anchor="center"' alinha o texto ao centro, facilitando a 
        # leitura de números.
tree.column("Idade", width=100, anchor="center")

# Configura as propriedades da coluna "Email".
# 'width=200' define a largura da coluna como 200 pixels.
# 'anchor="w"' alinha o texto à esquerda.
tree.column("Email", width=200, anchor="w")


# Vincula um evento de liberação de botão do mouse (ButtonRelease-1) ao Treeview.
# 'selecionar_item' é a função chamada quando um usuário solta o botão do
        # mouse sobre um item, permitindo interações baseadas na seleção de item.
tree.bind("<ButtonRelease-1>", selecionar_item)


# Chama a função 'carregar_dados' para preencher o Treeview 
        # com dados ao iniciar a aplicação.
carregar_dados()


# Inicia o loop principal da interface gráfica.
janela.mainloop()