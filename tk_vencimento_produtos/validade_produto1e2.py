import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import pandas as pd
import xlsxwriter
from tkinter import filedialog

# Lista para armazenar os produtos (não utilizada, mas mantida por referência)
produtos = []

# --- FUNÇÕES DE LÓGICA DE NEGÓCIO ---

def cadastrar_produto(entry_codigo, entry_departamento, entry_nome, entry_data_compra, entry_data_validade, entry_quantidade):
    """Função para cadastrar um produto e salvar em um arquivo Excel."""
    
    codigo = entry_codigo.get()
    departamento = entry_departamento.get()
    nome = entry_nome.get()
    data_compra = entry_data_compra.get()
    data_validade = entry_data_validade.get()
    quantidade = entry_quantidade.get()
    
    try:
        data_compra = pd.to_datetime(data_compra, format="%d/%m/%Y").strftime('%d/%m/%Y')
        data_validade = pd.to_datetime(data_validade, format="%d/%m/%Y").strftime('%d/%m/%Y')
    
    except ValueError:
        messagebox.showerror("Erro", "Formato de data inválido. Use o formato dd/mm/aaaa.")
        return
        
    produto = {
        "Código Produto": codigo,
        "Depatamento": departamento,
        "Nome Produto": nome,
        "Data Compra": data_compra,
        "Validade": data_validade,
        "Quantidade": quantidade
    }
    
    df_novo_produto = pd.DataFrame([produto])
    excel_file_path = r"C:\python_projetos\python_rpa_projetos\tk_vencimento_produtos\Dados.xlsx"
    
    try:
        excel_data = pd.read_excel(excel_file_path)
        df_final = pd.concat([excel_data, df_novo_produto], ignore_index=True)
    
    except FileNotFoundError:
        df_final = df_novo_produto
    
    # CORREÇÃO: O parâmetro 'if_sheet_exists' foi removido pois ele é incompatível com o modo de escrita 'w'.
    with pd.ExcelWriter(excel_file_path, engine="openpyxl", mode="w") as writer:
        df_final.to_excel(writer, sheet_name="Produtos", index=False)
    
    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
    janela_cadastro.destroy()


def exportar_para_excel(treeview):
    """Função para exportar os dados exibidos no Treeview para um arquivo Excel."""
    
    filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Arquivo Excel", "*.xlsx")])

    if not filename:
        return

    columns = [treeview.heading(coluna)["text"] for coluna in treeview["columns"]]
    
    lista_de_linhas_da_listview = []
    
    for item in treeview.get_children():
        values = treeview.item(item, "values")
        lista_de_linhas_da_listview.append(values)
        
    df_concat = pd.DataFrame(lista_de_linhas_da_listview, columns=columns)
    
    try:
        df_concat.to_excel(filename, index=False)
        messagebox.showinfo("Exportar", "Dados exportados com sucesso!")
    except Exception as e:
        messagebox.showerror("Exportar para Excel", f"Ocorreu um erro ao exportar os dados: {str(e)}")


def consultar_produtos(combo_opcoes, treeview_resultado):
    """
    CORREÇÃO COMPLETA:
    Esta função foi refeita para ser mais robusta. Em vez de tentar converter a coluna inteira de uma vez,
    o código agora itera linha por linha. Se encontrar uma data inválida, ele simplesmente ignora a linha
    e continua, evitando que o programa trave.
    A forma como a data é armazenada e exibida foi corrigida para evitar o erro de formato.
    """
    
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
    else:
        messagebox.showerror("Erro", "Selecione uma opção de consulta.")
        return

    data_atual = datetime.now().date()
    excel_file_path = r"C:\python_projetos\python_rpa_projetos\tk_vencimento_produtos\Dados.xlsx"
    
    try:
        excel_data = pd.read_excel(excel_file_path, sheet_name="Produtos")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de dados não encontrado.")
        return
        
    treeview_resultado.delete(*treeview_resultado.get_children())
    
    produtos_encontrados = []
    
    for index, row in excel_data.iterrows():
        try:
            # Tenta converter a data da validade para o tipo de dado de data.
            validade = pd.to_datetime(row["Validade"], format="%d/%m/%Y").date()
            
            diferenca_tempo = validade - data_atual
            dias_restantes = diferenca_tempo.days
            
            if dias_min <= dias_restantes <= dias_max:
                # CORREÇÃO: Cria um dicionário com os dados do produto para garantir que a 'validade'
                # seja o objeto de data já convertido, e não o texto original.
                produto_para_exibir = {
                    "Código Produto": row["Código Produto"],
                    "Depatamento": row["Depatamento"],
                    "Nome Produto": row["Nome Produto"],
                    "Data Compra": row["Data Compra"],
                    "Validade": validade,  # Usa o objeto de data convertido
                    "Quantidade": row["Quantidade"],
                    "Dias Restantes": dias_restantes
                }
                produtos_encontrados.append(produto_para_exibir)
        except (ValueError, TypeError):
            # Se a conversão falhar, a linha é simplesmente ignorada para evitar o erro.
            continue

    for produto in produtos_encontrados:
        data_compra_formatada = produto["Data Compra"]
        # CORREÇÃO: Agora o .strftime() funciona porque 'produto["Validade"]' é um objeto de data.
        validade_formatada = produto["Validade"].strftime("%d/%m/%Y")
        
        treeview_resultado.insert("", tk.END, values=(
            produto["Código Produto"],
            produto["Depatamento"],
            produto["Nome Produto"],
            data_compra_formatada,
            validade_formatada,
            produto["Quantidade"],
            produto["Dias Restantes"]
        ))


def limpar_dados_excel():
    """
    CORREÇÃO: Esta função limpa a planilha.
    O parâmetro 'if_sheet_exists' foi removido pois ele é incompatível com o modo de escrita 'w'.
    """
    excel_file_path = r"C:\python_projetos\python_rpa_projetos\tk_vencimento_produtos\Dados.xlsx"
    
    try:
        df = pd.read_excel(excel_file_path)

        df["Validade"] = pd.to_datetime(df["Validade"], format="%d/%m/%Y", errors='coerce')
        
        df_limpo = df.dropna(subset=['Validade'])
        
        with pd.ExcelWriter(excel_file_path, engine="openpyxl", mode="w") as writer:
            df_limpo.to_excel(writer, sheet_name="Produtos", index=False)
            
        messagebox.showinfo("Sucesso", "A planilha de dados foi limpa com sucesso!")

    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de dados não encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao limpar os dados: {str(e)}")

# --- FUNÇÕES DE INTERFACE (TKINTER) ---

def abrir_tela_cadastro():
    """Cria e exibe a janela de cadastro de produtos."""
    global janela_cadastro
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastrar Produto")
    
    largura_janela = 600
    altura_janela = 400
    largura_tela = janela_cadastro.winfo_screenwidth()
    altura_tela = janela_cadastro.winfo_screenheight()
    pos_x = int(largura_tela / 2 - largura_janela / 2)
    pos_y = int(altura_tela / 2 - altura_janela / 2)
    janela_cadastro.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    janela_cadastro.configure(bg="#FFFFFF")
    
    label_codigo = tk.Label(janela_cadastro, text="Código Produto:", bg="#FFFFFF", font="Arial 16")
    label_codigo.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_codigo = tk.Entry(janela_cadastro, font="Arial 16")
    entry_codigo.grid(row=0, column=1, padx=10, pady=10)
    
    label_departamento = tk.Label(janela_cadastro, text="Departamento:", bg="#FFFFFF", font="Arial 16")
    label_departamento.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_departamento = tk.Entry(janela_cadastro, font="Arial 16")
    entry_departamento.grid(row=1, column=1, padx=10, pady=10)
    
    label_nome = tk.Label(janela_cadastro, text="Nome Produto:", bg="#FFFFFF", font="Arial 16")
    label_nome.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entry_nome = tk.Entry(janela_cadastro, font="Arial 16")
    entry_nome.grid(row=2, column=1, padx=10, pady=10)
    
    label_data_compra = tk.Label(janela_cadastro, text="Data Compra (dd/mm/aaaa):", bg="#FFFFFF", font="Arial 16")
    label_data_compra.grid(row=3, column=0, padx=10, pady=10, sticky="e")
    entry_data_compra = tk.Entry(janela_cadastro, font="Arial 16")
    entry_data_compra.grid(row=3, column=1, padx=10, pady=10)
    
    label_data_validade = tk.Label(janela_cadastro, text="Data Validade (dd/mm/aaaa):", bg="#FFFFFF", font="Arial 16")
    label_data_validade.grid(row=4, column=0, padx=10, pady=10, sticky="e")
    entry_data_validade = tk.Entry(janela_cadastro, font="Arial 16")
    entry_data_validade.grid(row=4, column=1, padx=10, pady=10)
    
    label_quantidade = tk.Label(janela_cadastro, text="Quantidade:", bg="#FFFFFF", font="Arial 16")
    label_quantidade.grid(row=5, column=0, padx=10, pady=10, sticky="e")
    entry_quantidade = tk.Entry(janela_cadastro, font="Arial 16")
    entry_quantidade.grid(row=5, column=1, padx=10, pady=10)
    
    botao_cadastrar_produto = tk.Button(janela_cadastro, text="Cadastrar", font="Arial 16",
                                       command=lambda: cadastrar_produto(entry_codigo, entry_departamento, entry_nome, entry_data_compra, entry_data_validade, entry_quantidade))
    botao_cadastrar_produto.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")
    
    janela_cadastro.mainloop()
    
def abrir_tela_consulta():
    """Cria e exibe a janela de consulta de produtos."""
    janela_consulta = tk.Toplevel()
    janela_consulta.title("Consultar Produtos")
    
    largura_janela = 1450
    altura_janela = 400
    largura_tela = janela_consulta.winfo_screenwidth()
    altura_tela = janela_consulta.winfo_screenheight()
    pos_x = int(largura_tela / 2 - largura_janela / 2)
    pos_y = int(altura_tela / 2 - altura_janela / 2)
    janela_consulta.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    janela_consulta.configure(bg="#FFFFFF")
    
    frame_topo = tk.Frame(janela_consulta, bg="#FFFFFF")
    frame_topo.pack(pady=10)
    
    label_opcoes = tk.Label(frame_topo, text="Opções de Consulta:", bg="#FFFFFF", font="Arial 16")
    label_opcoes.pack(side=tk.LEFT, padx=10)
    
    combo_opcoes = ttk.Combobox(frame_topo, values=["Tranquilo", "Alerta", "Critico", "Produto Vencido"], font="Arial 16")
    combo_opcoes.pack(side=tk.LEFT, padx=10)
    
    botao_consultar_produtos = tk.Button(frame_topo, text="Consultar", font="Arial 16",
                                        command=lambda: consultar_produtos(combo_opcoes, treeview_resultado), width=20)
    botao_consultar_produtos.pack(side=tk.LEFT, padx=10)
    
    botao_exportar = tk.Button(frame_topo, text="Exportar para Excel", font="Arial 16",
                                command=lambda: exportar_para_excel(treeview_resultado), width=20)
    botao_exportar.pack(side=tk.LEFT, padx=10)

    treeview_resultado = ttk.Treeview(janela_consulta, columns=[
        "Código Produto", "Departamento", "Nome Produto", "Data Compra", "Validade", "Quantidade", "Dias Restantes"
    ], show="headings")
    
    treeview_resultado.heading("Código Produto", text="Código Produto")
    treeview_resultado.heading("Departamento", text="Departamento")
    treeview_resultado.heading("Nome Produto", text="Nome Produto")
    treeview_resultado.heading("Data Compra", text="Data Compra")
    treeview_resultado.heading("Validade", text="Validade")
    treeview_resultado.heading("Quantidade", text="Quantidade")
    treeview_resultado.heading("Dias Restantes", text="Dias Restantes")
    
    treeview_resultado.column("Código Produto", width=100)
    treeview_resultado.column("Departamento", width=150)
    treeview_resultado.column("Nome Produto", width=200)
    treeview_resultado.column("Data Compra", width=150)
    treeview_resultado.column("Validade", width=150)
    treeview_resultado.column("Quantidade", width=100)
    treeview_resultado.column("Dias Restantes", width=150)
    
    scrollbar = ttk.Scrollbar(janela_consulta, orient="vertical", command=treeview_resultado.yview)
    treeview_resultado.configure(yscrollcommand=scrollbar.set)
    
    treeview_resultado.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    style = ttk.Style(janela_consulta)
    style.theme_use("clam")
    style.configure("Treeview", font="Arial 14")
    style.configure("Treeview.Heading", font="Arial 14 bold")
    
    janela_consulta.mainloop()

# --- INTERFACE PRINCIPAL ---

janela_menu_principal = tk.Tk()
janela_menu_principal.title("Menu Principal")

largura_janela = 400
altura_janela = 300
largura_tela = janela_menu_principal.winfo_screenwidth()
altura_tela = janela_menu_principal.winfo_screenheight()
pos_x = int(largura_tela / 2 - largura_janela / 2)
pos_y = int(altura_tela / 2 - altura_janela / 2)
janela_menu_principal.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
janela_menu_principal.configure(bg="#FFFFFF")

label_menu_principal = tk.Label(janela_menu_principal,
                               text="------------ MENU PRINCIPAL ------------",
                               bg="#FFFFFF",
                               font=("Arial 16"))
label_menu_principal.pack(pady=20)

botao_cadastrar = tk.Button(janela_menu_principal,
                            text="Cadastrar",
                            font=("Arial 16"),
                            command=abrir_tela_cadastro,
                            width=30)
botao_cadastrar.pack(pady=10)

botao_consultar = tk.Button(janela_menu_principal,
                            text="Consultar Produtos",
                            font=("Arial 16"),
                            command=abrir_tela_consulta,
                            width=30)
botao_consultar.pack(pady=10)

botao_limpar = tk.Button(janela_menu_principal,
                         text="Limpar Dados da Planilha",
                         font=("Arial 16"),
                         command=limpar_dados_excel,
                         width=30)
botao_limpar.pack(pady=10)

botao_sair = tk.Button(janela_menu_principal,
                      text="Sair",
                      font=("Arial 16"),
                      command=janela_menu_principal.destroy,
                      width=30)
botao_sair.pack(pady=10)

janela_menu_principal.mainloop()