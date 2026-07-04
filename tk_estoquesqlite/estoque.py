import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# --- Banco de Dados ---
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()
# Criando a tabela com as colunas completas
cursor.execute('''CREATE TABLE IF NOT EXISTS produtos 
                  (id INTEGER PRIMARY KEY, nome TEXT, preco REAL, quantidade INTEGER, 
                   fornecedor TEXT, vencimento TEXT, est_min INTEGER)''')
conn.commit()

# --- Funções de Lógica ---
def converter_para_banco(data_tela):
    try: return datetime.strptime(data_tela, "%d/%m/%Y").strftime("%Y-%m-%d")
    except: return None

def converter_para_tela(data_banco):
    try: return datetime.strptime(data_banco, "%Y-%m-%d").strftime("%d/%m/%Y")
    except: return ""

def salvar_produto():
    try:
        venc_banco = converter_para_banco(ent_venc.get())
        cursor.execute("INSERT INTO produtos (nome, preco, quantidade, fornecedor, vencimento, est_min) VALUES (?,?,?,?,?,?)", 
                       (ent_nome.get(), float(ent_preco.get()), int(ent_qtd.get()), ent_fornecedor.get(), venc_banco, int(ent_min.get())))
        conn.commit(); limpar_campos(); atualizar_treeview()
    except Exception as e: messagebox.showerror("Erro", f"Dados inválidos: {e}")

def alterar_produto():
    item = tree.selection()
    if not item: return
    id_p = tree.item(item)['values'][0]
    venc_banco = converter_para_banco(ent_venc.get())
    cursor.execute("UPDATE produtos SET nome=?, preco=?, quantidade=?, fornecedor=?, vencimento=?, est_min=? WHERE id=?", 
                   (ent_nome.get(), float(ent_preco.get()), int(ent_qtd.get()), ent_fornecedor.get(), venc_banco, int(ent_min.get()), id_p))
    conn.commit(); atualizar_treeview(); limpar_campos()

def registrar_movimento(tipo):
    item = tree.selection()
    if not item: return
    v = tree.item(item)['values']
    id_p, nome, _, qtd_atual, _, _, est_min = v
    try:
        valor = int(ent_qtd.get())
        if tipo == "saida":
            if valor > qtd_atual: return messagebox.showerror("Erro", "Estoque insuficiente!")
            nova_qtd = qtd_atual - valor
            sql = "UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?"
            if nova_qtd <= est_min:
                messagebox.showwarning("Alerta", f"Atenção: O produto '{nome}' atingiu o estoque mínimo!")
        else: sql = "UPDATE produtos SET quantidade = quantidade + ? WHERE id = ?"
        cursor.execute(sql, (valor, id_p))
        conn.commit(); atualizar_treeview(); limpar_campos()
    except: messagebox.showerror("Erro", "Valor inválido.")

def deletar_produto():
    item = tree.selection()
    if not item: return
    id_p = tree.item(item)['values'][0]
    if messagebox.askyesno("Confirmar", "Deseja excluir este item?"):
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_p,))
        conn.commit(); atualizar_treeview(); limpar_campos()

def consultar_relatorio(tipo):
    for i in tree.get_children(): tree.delete(i)
    hoje = datetime.now().strftime('%Y-%m-%d')
    mes_atual = datetime.now().strftime('%Y-%m')
    
    if tipo == "minimo": query = "SELECT * FROM produtos WHERE quantidade <= est_min"
    elif tipo == "vencidos": query = f"SELECT * FROM produtos WHERE vencimento < '{hoje}'"
    elif tipo == "venc_mes": query = f"SELECT * FROM produtos WHERE vencimento LIKE '{mes_atual}%'"
    else: query = "SELECT * FROM produtos"
    
    for row in cursor.execute(query):
        row = list(row)
        if len(row) > 5 and row[5]: row[5] = converter_para_tela(row[5])
        tree.insert("", "end", values=row)

def carregar_campos(event):
    item = tree.selection()
    if not item: return
    v = list(tree.item(item)['values'])
    limpar_campos()
    ent_nome.insert(0, v[1]); ent_preco.insert(0, v[2]); ent_qtd.insert(0, v[3])
    ent_fornecedor.insert(0, v[4]); ent_venc.insert(0, v[5]); ent_min.insert(0, v[6])

def atualizar_treeview(event=None):
    for i in tree.get_children(): tree.delete(i)
    for row in cursor.execute("SELECT * FROM produtos WHERE nome LIKE ?", ('%'+ent_busca.get()+'%',)):
        row = list(row)
        if len(row) > 5 and row[5]: row[5] = converter_para_tela(row[5])
        tree.insert("", "end", values=row)

def limpar_campos():
    for ent in [ent_nome, ent_preco, ent_qtd, ent_fornecedor, ent_venc, ent_min]: ent.delete(0, 'end')

# --- Interface ---
root = tk.Tk()
root.title("Gestão de Estoque Profissional")
root.geometry("950x650")

menubar = tk.Menu(root)
menu_arq = tk.Menu(menubar, tearoff=0)
menu_arq.add_command(label="Incluir", command=salvar_produto)
menu_arq.add_command(label="Alterar", command=alterar_produto)
menu_arq.add_command(label="Excluir", command=deletar_produto)
menubar.add_cascade(label="Arquivo", menu=menu_arq)

menu_rel = tk.Menu(menubar, tearoff=0)
menu_rel.add_command(label="Estoque Mínimo Atingido", command=lambda: consultar_relatorio("minimo"))
menu_rel.add_command(label="Produtos Vencidos", command=lambda: consultar_relatorio("vencidos"))
menu_rel.add_command(label="Vencem este mês", command=lambda: consultar_relatorio("venc_mes"))
menu_rel.add_command(label="Ver Todos", command=atualizar_treeview)
menubar.add_cascade(label="Relatórios", menu=menu_rel)
root.config(menu=menubar)

frame_form = tk.LabelFrame(root, text="Dados do Produto", padx=10, pady=10)
frame_form.pack(fill="x", padx=10, pady=5)
campos = ["Nome:", "Preço:", "Qtd/Mov:", "Fornecedor:", "Vencimento (DD/MM/AAAA):", "Estoque Mínimo:"]
entries = []
for i, l in enumerate(campos):
    tk.Label(frame_form, text=l).grid(row=i, column=0, sticky="w")
    ent = tk.Entry(frame_form); ent.grid(row=i, column=1, sticky="ew")
    entries.append(ent)
ent_nome, ent_preco, ent_qtd, ent_fornecedor, ent_venc, ent_min = entries
frame_form.columnconfigure(1, weight=1)

frame_busca = tk.Frame(root); frame_busca.pack(fill="x", padx=10)
tk.Label(frame_busca, text="Buscar:").pack(side="left"); ent_busca = tk.Entry(frame_busca); ent_busca.pack(side="left", fill="x", expand=True)
ent_busca.bind("<KeyRelease>", atualizar_treeview)

frame_btns = tk.Frame(root, pady=5); frame_btns.pack(fill="x", padx=10)
tk.Button(frame_btns, text="Entrada", command=lambda: registrar_movimento("entrada"), bg="#d1e7dd").pack(side="left", padx=5)
tk.Button(frame_btns, text="Saída", command=lambda: registrar_movimento("saida"), bg="#f8d7da").pack(side="left", padx=5)

tree = ttk.Treeview(root, columns=("ID", "Nome", "Preço", "Qtd", "Fornecedor", "Venc", "Min"), show='headings')
for col in ("ID", "Nome", "Preço", "Qtd", "Fornecedor", "Venc", "Min"):
    tree.heading(col, text=col); tree.column(col, width=90)
tree.pack(fill="both", expand=True, padx=10, pady=10)
tree.bind("<<TreeviewSelect>>", carregar_campos)

atualizar_treeview()
root.mainloop()