import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import pandas as pd
import xlsxwriter

from tkinter import filedialog

#Lista para armazenar os produtos
produtos = []


def cadastrar_produto( entry_codigo, entry_departamento, entry_nome, entry_data_compra, entry_data_validade, entry_quantidade):
    
    codigo = entry_codigo.get()
    departamento = entry_departamento.get()
    nome = entry_nome.get()
    data_compra = entry_data_compra.get()
    data_validade = entry_data_validade.get()
    quantidade = entry_quantidade.get()
    
    try:
        
        #Converter as strings das datas para o formato de data
        data_compra = pd.to_datetime(data_compra, format="%d/%m/%Y").strftime('%d/%m/%Y')
        data_validade = pd.to_datetime(data_validade, format="%d/%m/%Y").strftime('%d/%m/%Y')
    
    except ValueError:
        
        messagebox.showerror("Erro", "Formato de data inválido. Use o formato dd/mm/aaaa.")
        
    #Criando um DataFrame com os dados do produto
    produto = {        
        "Código Produto" : codigo,
        "Depatamento" : departamento,
        "Nome Produto" : nome,
        "Data Compra" : data_compra,
        "Validade" : data_validade,
        "Quantidade" : quantidade
    }
    
    df = pd.DataFrame([produto])
    
    #Verifica se o arquivo de Excel existe
    try:
        
        excel_data = pd.read_excel(r"C:\python_projetos\python_rpa_projetos\tk_vencimento_produtos\Dados.xlsx")
        
        #Concatenar o novo produto do DataFrame existente
        df = pd.concat([excel_data, df], ignore_index=True)
        
    except FileNotFoundError:
        
        pass #O arquivo não existe, contiará apenas com o Dataframe criado
        
    """
    Definindo o caminho do arquivo Excel onde os dados serão armazenados. A variável 
    excel_file_path recebe a string "C:/Users/55119/Desktop/Validade Produtos/Dados.xlsx", que é o 
    caminho completo para o arquivo de dados.

    Em seguida, é utilizada a função pd.ExcelWriter() do pandas para criar um objeto de 
    escrita para o arquivo Excel especificado. Os argumentos passados para essa função são:

    excel_file_path: O caminho do arquivo Excel.
    
    engine="openpyxl": Especifica o mecanismo a ser usado para escrever no arquivo, no caso, 
    o "openpyxl" é o mecanismo padrão utilizado pelo pandas para manipulação de arquivos Excel.
    
    mode="a": Indica que o arquivo será aberto em modo de adição (append), ou seja, se o arquivo 
    já existir, os novos dados serão adicionados a ele. Se o arquivo não existir, um novo arquivo será criado.

    f_sheet_exists="replace": Indica que, se a planilha "Produtos" já existir no arquivo, ela será 
    substituída pelo novo conjunto de dados.

    Após criar o objeto de escrita, a função to_excel() do DataFrame df é utilizada para escrever 
    os dados no arquivo Excel. Os argumentos passados para essa função são:

    writer: O objeto de escrita do arquivo Excel.
    
    sheet_name="Produtos": O nome da planilha onde os dados serão escritos.

    index=False: Indica que o índice do DataFrame não será incluído no arquivo Excel.

    Em resumo, essa parte do código cria um arquivo Excel, se não existir, ou adiciona novos 
    dados a um arquivo Excel existente, na planilha "Produtos".
    """
    excel_file_path = r"C:\python_projetos\python_rpa_projetos\tk_vencimento_produtos\Dados.xlsx"
    with pd.ExcelWriter(excel_file_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name="Produtos", index=False)

    # Exibir uma mensagem de sucesso
    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
    janela_cadastro.destroy()


def abrir_tela_cadastro():
    
    global janela_cadastro
    
    #Criar a janela secundária
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastrar Produto")
    
    # Definir as dimensões da janela
    largura_janela = 600
    altura_janela = 400

    # Obter as dimensões da tela
    largura_tela = janela_cadastro.winfo_screenwidth()
    altura_tela = janela_cadastro.winfo_screenheight()

    # Calcular as coordenadas para centralizar a janela
    pos_x = int(largura_tela / 2 - largura_janela / 2)
    pos_y = int(altura_tela / 2 - altura_janela / 2)

    # Definir a posição e o tamanho da janela
    janela_cadastro.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    
    # Definir a cor de fundo da janela
    janela_cadastro.configure(bg="#FFFFFF")
    
    #Criar os elementos da interface de cadastro
    #sticky="e" - Alinhar na direita
    label_codigo = tk.Label(janela_cadastro,
                           text = "Código Produto:",
                           bg="#FFFFFF",
                           font="Arial 16")
    label_codigo.grid(row = 0, column = 0, padx = 10, pady = 10, sticky="e")
    
    #Campo de entrada de dados
    entry_codigo = tk.Entry(janela_cadastro,
                           font="Arial 16")
    entry_codigo.grid(row = 0, column = 1, padx = 10, pady = 10)
    
    #---------------------------------------------
    
    label_departamento = tk.Label(janela_cadastro,
                           text = "Departamento:",
                           bg="#FFFFFF",
                           font="Arial 16")
    label_departamento.grid(row = 1, column = 0, padx = 10, pady = 10, sticky="e")
    
    #Campo de entrada de dados
    entry_departamento = tk.Entry(janela_cadastro,
                           font="Arial 16")
    entry_departamento.grid(row = 1, column = 1, padx = 10, pady = 10)
    
    #---------------------------------------------
    
    label_nome = tk.Label(janela_cadastro,
                           text = "Nome Produto:",
                           bg="#FFFFFF",
                           font="Arial 16")
    label_nome.grid(row = 2, column = 0, padx = 10, pady = 10, sticky="e")
    
    #Campo de entrada de dados
    entry_nome = tk.Entry(janela_cadastro,
                           font="Arial 16")
    entry_nome.grid(row = 2, column = 1, padx = 10, pady = 10)
    
    #---------------------------------------------
    
    label_data_compra = tk.Label(janela_cadastro,
                           text = "Data Compra (dd/mm/aaaa):",
                           bg="#FFFFFF",
                           font="Arial 16")
    label_data_compra.grid(row = 3, column = 0, padx = 10, pady = 10, sticky="e")
    
    #Campo de entrada de dados
    entry_data_compra = tk.Entry(janela_cadastro,
                           font="Arial 16")
    entry_data_compra.grid(row = 3, column = 1, padx = 10, pady = 10)
    
    #---------------------------------------------
    
    label_data_validade = tk.Label(janela_cadastro,
                           text = "Data Validade (dd/mm/aaaa):",
                           bg="#FFFFFF",
                           font="Arial 16")
    label_data_validade.grid(row = 4, column = 0, padx = 10, pady = 10, sticky="e")
    
    #Campo de entrada de dados
    entry_data_validade = tk.Entry(janela_cadastro,
                           font="Arial 16")
    entry_data_validade.grid(row = 4, column = 1, padx = 10, pady = 10)
    
    #---------------------------------------------
    
    label_quantidade = tk.Label(janela_cadastro,
                           text = "Quantidade:",
                           bg="#FFFFFF",
                           font="Arial 16")
    label_quantidade.grid(row = 5, column = 0, padx = 10, pady = 10, sticky="e")
    
    #Campo de entrada de dados
    entry_quantidade = tk.Entry(janela_cadastro,
                           font="Arial 16")
    entry_quantidade.grid(row = 5, column = 1, padx = 10, pady = 10)
    
    
    botao_cadastrar_produto = tk.Button(janela_cadastro,
                           text = "Cadastrar",
                           font="Arial 16",
                           command = lambda: cadastrar_produto( entry_codigo, entry_departamento, entry_nome, entry_data_compra, entry_data_validade, entry_quantidade))
    botao_cadastrar_produto.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10, sticky="NSEW")
    
    #Abre a janela
    janela_cadastro.mainloop()
    
    

def abrir_tela_consulta():
    
    global janela_cadastro
    
    #Criar a janela secundária
    janela_consulta = tk.Toplevel()
    janela_consulta.title("Consultar Produtos")
    
    # Definir as dimensões da janela
    largura_janela = 1450
    altura_janela = 400

    # Obter as dimensões da tela
    largura_tela = janela_consulta.winfo_screenwidth()
    altura_tela = janela_consulta.winfo_screenheight()

    # Calcular as coordenadas para centralizar a janela
    pos_x = int(largura_tela / 2 - largura_janela / 2)
    pos_y = int(altura_tela / 2 - altura_janela / 2)

    # Definir a posição e o tamanho da janela
    janela_consulta.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    
    # Definir a cor de fundo da janela
    janela_consulta.configure(bg="#FFFFFF")
    
    #Cria um frame para agrupar os elementos na tela
    frame_topo = tk.Frame(janela_consulta, bg="#FFFFFF")
    frame_topo.pack(pady = 10)
    
    #Criar os elementos da interface de cadastro
    #sticky="e" - Alinhar na direita
    label_opcoes = tk.Label(frame_topo,
                           text = "Opções de Consulta:",
                           bg="#FFFFFF",
                           font="Arial 16")
    label_opcoes.pack(side = tk.LEFT, padx = 10)
    
    #Cria a combobox para as opções de consulta
    combo_opcoes = ttk.Combobox(frame_topo, 
                               values=["Tranquilo", "Alerta", "Critico", "Produto Vencido"],
                               font="Arial 16")
    combo_opcoes.pack(side = tk.LEFT, padx = 10)
    
    #Cria o botão para consulta
    botao_consultar_produtos = tk.Button(frame_topo,
                                        text = "Consultar",
                                        command = lambda: consultar_produtos(combo_opcoes, treeview_resultado),
                                        width = 20,
                                        font="Arial 16")
    botao_consultar_produtos.pack(side = tk.LEFT, padx = 10)
    
    
    #Cria a treeview para exibir os resultados
    treeview_resultado = ttk.Treeview(janela_consulta
                                      , columns=["Código Produto", "Departamento", "Nome Produto", "Data Compra", "Validade", "Quantidade", "Dias Restantes"],
                                     show="headings")
    treeview_resultado.pack(pady = 10, fill = tk.BOTH, expand = True)
    
    #Definir as colunas do Treeview
    treeview_resultado.heading("Código Produto", text="Código Produto")
    treeview_resultado.heading("Departamento", text="Departamento")
    treeview_resultado.heading("Nome Produto", text="Nome Produto")
    treeview_resultado.heading("Data Compra", text="Data Compra")
    treeview_resultado.heading("Validade", text="Validade")
    treeview_resultado.heading("Quantidade", text="Quantidade")
    treeview_resultado.heading("Dias Restantes", text="Dias Restantes")
    
    #Definir a largura das colunas da Treeview
    treeview_resultado.column("Código Produto", width=100)
    treeview_resultado.column("Departamento", width=150)
    treeview_resultado.column("Nome Produto", width=200)
    treeview_resultado.column("Data Compra", width=150)
    treeview_resultado.column("Validade", width=150)
    treeview_resultado.column("Quantidade", width=100)
    treeview_resultado.column("Dias Restantes", width=150)
    
    #Cria uma barra de rolagem para a Treeview
    scrollbar = ttk.Scrollbar(janela_consulta, 
                             orient = "vertical",
                             command = treeview_resultado.yview)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
    
    #Conecta a barra de rolagem ao Treeview
    treeview_resultado.configure(yscrollcommand=scrollbar.set)
    
    #Posiciona a Treeview e a barra de rolagem lado a lado usando o método pack
    treeview_resultado.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
    
    #Configura o estilo da Treeview
    style = ttk.Style(janela_consulta)
    style.theme_use("clam")
    style.configure("Treeview", font = "Arial 14")
    style.configure("Treeview.Heading", font = "Arial 14 bold" )
    
    def consultar_produtos( combo_opcoes, treeview_resultado ):
        
        #Obtém a opção selecionada na combobox
        opcao = combo_opcoes.get()
        
        if opcao == "Tranquilo":
            
            dias_min = 91
            dias_max = float('inf')
            
        elif opcao == "Alerta":
            
            dias_min = 31
            dias_max = 90
            
        elif opcao == "Critico":
            
            dias_min = 1
            dias_max = 30
            
        elif opcao == "Produto Vencido":
            
            dias_min = float('-inf')
            dias_max = 0
            
        #Obtém a data atual
        data_atual = datetime.now().date()
        
        #Verifica se o arquivo de Excel existe
        try:

            excel_data = pd.read_excel(r"C:\python_projetos\python_rpa_projetos\tk_vencimento_produtos\Dados.xlsx", sheet_name = "Produtos")

            
        except FileNotFoundError:

            messagebox.showerror("Erro", "Arquivo de dados não encontrado.")
            return
        
        #Converto a coluna "Validade" para o tipo dt.date
        excel_data["Validade"] = pd.to_datetime(excel_data["Validade"], format="%d/%m/%Y").dt.date
        
        #Filtra os produtos com base nas opções selecionadas
        produtos_filtrados = excel_data.loc[(excel_data["Validade"] - data_atual).dt.days.between(dias_min, dias_max)]
    
        #Limpa as linhas existentes na treeview_resultado
        treeview_resultado.delete(*treeview_resultado.get_children())
        
        
        for _, produto in produtos_filtrados.iterrows():
            
            codigo = produto["Código Produto"]
            departamento = produto["Depatamento"]
            nome = produto["Nome Produto"]
            data_compra = datetime.strptime(produto["Data Compra"], "%d/%m/%Y").date().strftime("%d/%m/%Y")
            validade = produto["Validade"].strftime("%d/%m/%Y")
            quantidade = produto["Quantidade"]
            diferenca_tempo = produto["Validade"] - data_atual
            dias_restantes = diferenca_tempo.days
            
            #Adiciona uma linha na treeview
            treeview_resultado.insert("", tk.END, values = (codigo, departamento, nome, data_compra, validade, quantidade, dias_restantes))
            
    #Cria o botão para consulta
    botao_exportar = tk.Button(frame_topo,
                                        text = "Exportar para Excel",
                                        command = lambda: exportar_para_excel( treeview_resultado ),
                                        width = 20,
                                        font="Arial 16")
    botao_exportar.pack(side = tk.LEFT, padx = 10)
    
    def exportar_para_excel( treeview ):
        
        #Abre uma caixa de diálogo para selecionar o local de salvamento do arquivo
        filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Arquivo Excel", "*.xlsx")])
    
        #Verifica se o usuário cancelou a seleção
        if not filename:
            
            return
        
        #Obter as colunas do treeview
        columns = [treeview.heading(coluna)["text"] for coluna in treeview["columns"]]
        
        
        #Cria uma lista vazia para armazenar os Dataframes
        lista_de_linhas_da_listview = []
        
        #Obtém os dados da Treeview
        for item in treeview.get_children():
            
            values = [treeview.item(item, "values")]
            linha = pd.DataFrame(values, columns=columns)
            lista_de_linhas_da_listview.append(linha)
            
        df_concat = pd.concat(lista_de_linhas_da_listview, ignore_index=True)
        
        #Salva o Dataframe em um arquivo de Excel
        try:
            
            df_concat.to_excel(filename, index=False)
            
        except Exception as e:
            
            messagebox.showerror("Exportar para Excel", f"Ocorreu um erro ao exportar os dados: {str(e)}")
        
    
    #Abre a janela
    janela_consulta.mainloop()
    

# Criar a janela principal do menu
janela_menu_principal = tk.Tk()
janela_menu_principal.title("Menu Principal")

# Definir as dimensões da janela
largura_janela = 400
altura_janela = 300

# Obter as dimensões da tela
largura_tela = janela_menu_principal.winfo_screenwidth()
altura_tela = janela_menu_principal.winfo_screenheight()

# Calcular as coordenadas para centralizar a janela
pos_x = int(largura_tela / 2 - largura_janela / 2)
pos_y = int(altura_tela / 2 - altura_janela / 2)

# Definir a posição e o tamanho da janela
janela_menu_principal.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


# Definir a cor de fundo da janela
janela_menu_principal.configure(bg="#FFFFFF")

#Criar os elementos da interface do menu principal
label_menu_principal = tk.Label(janela_menu_principal,
                               text="------------ MENU PRINCIPAL ------------",
                               bg="#FFFFFF",
                               font=("Arial 16"))
label_menu_principal.pack(pady = 20)


#Criando os botões na tela
botao_cadastrar = tk.Button(janela_menu_principal,
                               text="Cadastrar",
                               font=("Arial 16"),
                               command = abrir_tela_cadastro,
                               width = 30)
botao_cadastrar.pack(pady = 10)



botao_consultar = tk.Button(janela_menu_principal,
                               text="Consultar Produtos",
                               font=("Arial 16"),
                               command = abrir_tela_consulta,
                               width = 30)
botao_consultar.pack(pady = 10)


botao_sair = tk.Button(janela_menu_principal,
                               text="Sair",
                               font=("Arial 16"),
                               command = janela_menu_principal.destroy,
                               width = 30)
botao_sair.pack(pady = 10)

# Executar a janela principal do menu
janela_menu_principal.mainloop()