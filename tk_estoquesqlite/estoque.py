import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
####
from tkinter import filedialog
import shutil
import os
from datetime import date
####
# --- Banco de Dados ---
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()
'''
# Executa o comando PRAGMA passando apenas o nome da tabela
cursor.execute("PRAGMA table_info(produtos);")
colunas = cursor.fetchall()
print(colunas) para ver a estrutura da tabela usamos o PRAGMA
'''
# Criando a tabela com as colunas completas
cursor.execute('''CREATE TABLE IF NOT EXISTS produtos 
                  (id INTEGER PRIMARY KEY, nome TEXT, preco REAL, quantidade INTEGER, 
                   fornecedor TEXT, vencimento TEXT, est_min INTEGER, data_inclusao TEXT)''')
conn.commit()




# --- Funções de Lógica ---
def converter_para_banco(data_tela):
    """
    Converte uma string de data do formato brasileiro (DD/MM/AAAA)
    para o formato padrão de banco de dados (AAAA-MM-DD).
    Retorna None em caso de erro na conversão.

Esta linha de código em Python é muito utilizada para converter o formato de uma data (geralmente vinda de uma tela, input de usuário 
ou banco de dados) do formato brasileiro (DD/MM/AAAA) para o formato padrão de banco de dados/internacional (AAAA-MM-DD).

Abaixo, a explicação detalhada de cada comando e parte dessa instrução:

1. datetime
O que é: É um módulo nativo do Python (chamado datetime) que fornece classes para manipulação de datas e horas.

Função: Para usar essa linha, você precisa ter importado o módulo antes no seu código (ex: from datetime import datetime).

2. .strptime(data_tela, "%d/%m/%Y")
Este é o primeiro método executado, responsável por ler e transformar uma string em um objeto de data do Python.

data_tela: É a variável que contém a data em formato de texto (string), por exemplo: "25/12/2026".

.strptime(): Significa string parse time (analisar tempo a partir de uma string). Ele pega um texto e o converte para um objeto 
de data/hora compreensível pelo Python.

"%d/%m/%Y": É a máscara de leitura que diz ao Python como a string original está organizada:

%d: Dia com dois dígitos (01 até 31).

/: O caractere literal de barra que separa os valores.

%m: Mês com dois dígitos (01 até 12).

/: O caractere de barra.

%Y: Ano com quatro dígitos (ex: 2026).

Resultado parcial: O trecho até aqui pega a string "25/12/2026" e a transforma em um objeto de data do Python: 
datetime.date(2026, 12, 25).

3. .strftime("%Y-%m-%d")
Este é o segundo método executado, responsável por converter o objeto de data de volta para string, mas agora em um novo formato.

.strftime(): Significa string format time (formatar tempo em string). Ele pega o objeto de data gerado pelo passo anterior e o 
formata como texto de acordo com a máscara informada.

"%Y-%m-%d": É a máscara de saída:

%Y: Ano com quatro dígitos (2026).

-: O caractere de hífen que separa os valores.

%m: Mês com dois dígitos (12).

-: O caractere de hífen.

%d: Dia com dois dígitos (25).

Resultado final: O objeto de data é transformado em uma nova string no formato americano/internacional: "2026-12-25".
    """
    try: return datetime.strptime(data_tela, "%d/%m/%Y").strftime("%Y-%m-%d")
    except: return None


def converter_para_tela(data_banco):
    """
    Converte uma string de data do formato de banco de dados (AAAA-MM-DD)
    para o formato brasileiro (DD/MM/AAAA) para exibição na interface.
    Retorna uma string vazia em caso de erro na conversão.
    """

    try: return datetime.strptime(data_banco, "%Y-%m-%d").strftime("%d/%m/%Y")
    except: return ""

def converter_para_bancoPreco(valor):
    #30.0 ou 30,00 

    try:
    # Se for um widget do Tkinter (Entry), pega o texto. Senão, usa o valor direto.
     if hasattr(valor, "get"):
      texto = str(valor.get())
     else:
      texto = str(valor)

     # Se estiver vazio, retorna vazio
     if not texto:
      return ""
     # Converte para float e formata com 2 casas decimais garantidas
     # O objeto numero continua sendo um número (float) na memória do Python. O que acontece é que a expressão inteira 
     # após o return se torna uma string.

     # Se tem vírgula, o ponto é separador de milhar (remove ponto, troca vírgula por ponto)
     if "," in texto:
       texto_tratado = texto.replace(".", "").replace(",", ".")
     else:
       # Se NÃO tem vírgula, o ponto é decimal (mantém o ponto)
       texto_tratado = texto

     
     numero = float(texto_tratado)
     return f"{numero:.2f}".replace(",", ".")
    except ValueError:
      # Captura especificamente se o texto digitado não for um número válido
      return 0.00

def converter_para_telaPreco(event):

  try:
    # Pega dinamicamente o campo que disparou o evento (ent_preco)
    valor = event.widget
    if valor.get() =="":
        messagebox1("valor não pode ficar vazio")
        valor.focus()   
        return
    texto = str(valor.get())
    
   # Converte para float e formata com 2 casas decimais garantidas
   # O objeto numero continua sendo um número (float) na memória do Python. O que acontece é que a expressão inteira 
   # após o return se torna uma string.
    numero = float(texto)
    # ent_preco.delete(0, "end")
    # ent_preco.insert(0, f"{numero:.2f}".replace(".", ","))  
    widget.delete(0, "end")
    widget.insert(0, f"{numero:.2f}".replace(".", ","))
    return f"{numero:.2f}".replace(".", ",")
  except:
    return 0.00


def converter_para_telaPreco1(valor):

  try:
    texto = str(valor)

    # Se estiver vazio, retorna vazio
    if not texto:
      return ""
   # Converte para float e formata com 2 casas decimais garantidas
   # O objeto numero continua sendo um número (float) na memória do Python. O que acontece é que a expressão inteira 
   # após o return se torna uma string.
    numero = float(texto)
    # ent_preco.delete(0, "end")
    # ent_preco.insert(0, f"{numero:.2f}".replace(".", ","))  
    # ent_preco.delete(0, "end")
    # ent_preco.insert(0, f"{numero:.2f}".replace(".", ","))
    return f"{numero:.2f}".replace(".", ",")
  except:
    return 0.00


def salvar_produto():
    try:
       if ent_nome.get()== None or ent_qtd.get()==None or ent_fornecedor.get()==None or ent_venc.get() ==None or ent_min.get()==None:
            messagebox1("dados importantes vazios")
            ent_nome.focus()
            return
       if ent_nome.get()=="" or ent_qtd.get()=="" or ent_fornecedor.get()=="" or ent_venc.get() =="" or ent_min.get()=="":
            messagebox1("dados importantes vazios")
            ent_nome.focus()
            return
       preco = converter_para_bancoPreco(ent_preco.get())
       
           # Se o usuário deixou vazio, você pode tratar antes do execute para não mandar float("")
       preco_banco = float(preco) if preco else 0.0  # ou 0
       venc_banco = converter_para_banco(ent_venc.get())
       cursor.execute("INSERT INTO produtos (nome, preco, quantidade, fornecedor, vencimento, est_min, data_inclusao) VALUES (?, ?, ?, ?, ?, ?, DATE('now'))",
                       (ent_nome.get(), preco_banco, int(ent_qtd.get()), ent_fornecedor.get(), venc_banco, int(ent_min.get())))
        
       conn.commit()
       limpar_campos() 
       atualizar_treeview()
    except Exception as e: messagebox.showerror("Erro", f"Dados inválidos: {e}")

def alterar_produto():
    item = tree.selection()
    if not item: return
    id_p = tree.item(item)['values'][0]
    if ent_nome.get()== "None" or ent_qtd.get()=="None" or ent_fornecedor.get()=="None" or ent_venc.get() =="None" or ent_min.get()=="None":
            messagebox1("dados importantes vazios")
            ent_nome.focus()
            return
    if ent_nome.get()=="" or ent_qtd.get()=="" or ent_fornecedor.get()=="" or ent_venc.get() =="" or ent_min.get()=="":
            messagebox1("dados importantes vazios")
            ent_nome.focus()
            return
    preco = converter_para_bancoPreco(ent_preco.get())
    # Atualiza o Entry
    
    # Se o usuário deixou vazio, você pode tratar antes do execute para não mandar float("")
    preco_banco = float(preco) if preco else 0.0  # ou 0 
    venc_banco = converter_para_banco(ent_venc.get())
    data_inclusao= converter_para_banco(ent_inc.get())
    cursor.execute("UPDATE produtos SET nome=?, preco=?, quantidade=?, fornecedor=?, vencimento=?, est_min=?, data_inclusao=? WHERE id=?", 
                   (ent_nome.get(), preco_banco, int(ent_qtd.get()), ent_fornecedor.get(), venc_banco, int(ent_min.get()),data_inclusao, id_p))
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

    # Itera sobre os registros retornados pela consulta SQL
    for row in cursor.execute(query):
       # Converte a tupla de dados em lista para permitir edição
       row = list(row)
    
      # Verifica se a coluna de data (índice 5) existe e contém um valor
       if len(row) > 5 and row[5]: 
        # Aplica a função de formatação para exibir a data no padrão brasileiro
        row[5] = converter_para_tela(row[5]) 

       if len(row) > 7 and row[7]: 
        # Aplica a função de formatação para exibir a data no padrão brasileiro
        row[7] = converter_para_tela(row[7])    
    
         # Adiciona a linha formatada na Treeview
       tree.insert("", "end", values=row)
    
    '''for row in cursor.execute(query):
        row = list(row)
        if len(row) > 5 and row[5]: row[5] = converter_para_tela(row[5])
        tree.insert("", "end", values=row) '''

def carregar_campos(event):
    item = tree.selection()
    if not item: return
    v = list(tree.item(item)['values'])
    limpar_campos()
    ent_nome.insert(0, v[1]); ent_preco.insert(0, v[2]); ent_qtd.insert(0, v[3])
    ent_fornecedor.insert(0, v[4]); ent_venc.insert(0, v[5]); ent_min.insert(0, v[6]); ent_inc.insert(0, v[7])

def atualizar_treeview(event=None):
    #tree.delete(*tree.get_children()) também apaga todos os itens da treview
    for i in tree.get_children(): tree.delete(i)
    for row in cursor.execute("SELECT * FROM produtos WHERE nome LIKE ?", ('%'+ent_busca.get()+'%',)):
        row = list(row)
        #print(row)
        if len(row) > 2 and row[2]: row[2] = converter_para_telaPreco1(row[2])
        if len(row) > 5 and row[5]: row[5] = converter_para_tela(row[5])
        if len(row) > 7 and row[7]: row[7] = converter_para_tela(row[7]) 
          
             
        tree.insert("", "end", values=row)

def limpar_campos():
    for ent in [ent_nome, ent_preco, ent_qtd, ent_fornecedor, ent_venc, ent_min, ent_inc]: ent.delete(0, 'end')

#####

# def ganhou_foco(event):
#     if ent_inc.get()=='':
#         ent_inc.insert(0, converter_para_tela(date.today().isoformat()))

      
def fechar_programa():
    conn.close()  # Fecha a conexão com segurança
    root.destroy() # Destrói a janela



def salvar_bco():
    # 1. Solicita ao usuário que escolha o arquivo de banco de dados original
    arquivo_origem = filedialog.askopenfilename(
        title="Selecione o arquivo de banco de dados para copiar",
        filetypes=[("Banco de dados SQLite", "*.db")],
        initialdir="." # Começa a busca no diretório atual
    )

    # Se o usuário cancelar a seleção, encerra a função
    if not arquivo_origem:
        return

    # 2. Solicita ao usuário onde ele deseja salvar a cópia
    caminho_destino = filedialog.asksaveasfilename(
        defaultextension=".db",
        filetypes=[("Banco de dados SQLite", "*.db")],
        title="Salvar cópia do banco de dados",
        initialfile=f"copia_{os.path.basename(arquivo_origem)}"
    )

    # 3. Executa a cópia se o caminho de destino for definido
    if caminho_destino:
        try:
            shutil.copy2(arquivo_origem, caminho_destino)
            messagebox.showinfo("Sucesso", f"Backup realizado com sucesso em:\n{caminho_destino}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao realizar backup: {e}")
##########

def verificadatac(memdata1):

    data2=memdata1.split('/')

    dia = int(data2[0])
    mes = int(data2[1] )
    ano = int(data2[2])

    valida = False
    
    # Meses com 31 dias
    if( mes==1 or mes==3 or mes==5 or mes==7 or \
        mes==8 or mes==10 or mes==12):
        if(dia<=31):
            valida = True
    # Meses com 30 dias
    elif( mes==4 or mes==6 or mes==9 or mes==11):
        if(dia<=30):
            valida = True
    elif mes==2:
        # Testa se é bissexto
        if (ano%4==0 and ano%100!=0) or (ano%400==0):
            if(dia<=29):
                valida = True
        elif(dia<=28):
                valida = True

    if(valida) == False:
       
        messagebox1("Data Inválida digite novamente")
        return valida 
    return valida

def dadosdataini(event):
 # Pega dinamicamente o campo que disparou o evento (ent_inic ou ent_venc)
 dataini = event.widget   
 indice=len(dataini.get())
 if indice==0:
   return
 indice=indice-1


 memdata=dataini.get()

 if str(indice) in ("0","1","3","4","6","7","8","9"):
    if memdata[indice].isnumeric():
       if indice ==1 or indice ==4:
          memdata=memdata+"/"
          dataini.delete(0,END)
          dataini.insert(0,memdata)
          return
       elif indice == 9:
           valida=verificadatac(memdata)
           if valida==False:
             dataini.delete(0,END) 
             dataini.focus()
             return
           else:
             return 
       else:         
           return
    else:
      messagebox1("data tem que ser numerica nessa posição") 
      dataini.delete(0,END)
      dataini.focus()
      return
 
 elif indice==2 or indice==5:
     if memdata[indice] not in ("/"):
         messagebox1("digite barra automatica nesta posição é data")
         dataini.delete(0,END)
         dataini.focus()
         return   
     else:
        return 
   
 if len(dataini.get())==0:
      dataini.focus()
      return 
 if len(dataini.get()) ==1:
    digitado=dataini.get()
    if digitado in ("0","1","2","3","4","5","6","7","8","9"):
       return
    else: 
       messagebox1("digite números é data")
       dataini.delete(0,END)
       dataini.focus()   
       return
 if len(dataini.get()) ==2:
      memdata=dataini.get()
      if memdata.isnumeric():
         memdata=memdata+"/"
         dataini.delete(0,END)
         dataini.insert(0,memdata)
      else:
         messagebox1("digite números é data")
         dataini.delete(0,END)
         dataini.focus()
         return   
 elif len(dataini.get())==5:
         memdata1=dataini.get()
         memdata=dataini.get().split('/')
         memdata=memdata[1]
         if memdata[1].isnumeric():
           memdata1=memdata1+"/"
           dataini.delete(0,END)
           dataini.insert(0,memdata1)
           return
         else:
           messagebox1("digite números é data")
           dataini.delete(0,END)
           dataini.focus()   
           return
 elif len(dataini.get())==10:
         memdata=dataini.get()
         memdata1=memdata
         memdata=dataini.get().split('/')
         memdata=memdata[2]
         if memdata[2].isnumeric():
           dataini.delete(0,END)
           dataini.insert(0,memdata1)
           valida=verificadatac(memdata1)
           if valida==False:
             dataini.delete(0,END) 
             dataini.focus()   
           return
         else:
           messagebox1("digite números é data") 
           dataini.delete(0,END)
           dataini.focus()   
           return


def vercampos1(event):
  # Pega dinamicamente o campo que disparou o evento (ent_inic ou ent_venc)
  dataini = event.widget     
  if ent_inc.get()=='':
      ent_inc.insert(0, converter_para_tela(date.today().isoformat()))

  if len(dataini.get())>10:
       messagebox1("campo data tamanho 10 digite novamente")
       dataini.delete(0,END)
       dataini.focus()
  

# --- Interface ---
root = tk.Tk()
root.title("Gestão de Estoque Profissional")
root.geometry("950x650")
def messagebox1(mensagem, janela_pai=root):
    # Cria uma nova janela pop-up
    top = tk.Toplevel(janela_pai)
    top.title("Aviso")
    top.geometry("450x200")
    top.transient(janela_pai)
    
    # Centraliza a janela
    top.update_idletasks()
    x = janela_pai.winfo_x() + (janela_pai.winfo_width() // 2) - 225
    y = janela_pai.winfo_y() + (janela_pai.winfo_height() // 2) - 100
    top.geometry(f"+{x}+{y}")

    # Texto com quebra automática para nunca cortar a mensagem
    lbl_mensagem = tk.Label(top, text=mensagem, wraplength=420, justify="left", font=("Arial", 10))
    lbl_mensagem.pack(padx=15, pady=15, fill="both", expand=True)

    # Botão OK para fechar com segurança
    btn_ok = ttk.Button(top, text="OK", command=top.destroy)
    btn_ok.pack(pady=10)
    
    # Permite fechar a janela também ao apertar a tecla Enter ou Escape
    top.bind("<Return>", lambda event: top.destroy())
    top.bind("<Escape>", lambda event: top.destroy())
    
    btn_ok.focus()



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
##########

menu_copia = tk.Menu(menubar, tearoff=0)
menu_copia.add_command(label="Copia de segurança", command=lambda: salvar_bco())
#menu_copia.add_command(label="Copia de segurança", command=salvar_bco) sem parenteses
menubar.add_cascade(label="Copiar banco de dados", menu=menu_copia)


   


frame_form = tk.LabelFrame(root, text="Dados do Produto", padx=10, pady=10)
frame_form.pack(fill="x", padx=10, pady=5)
campos = ["Nome:", "Preço:", "Qtd/Mov:", "Fornecedor:", "Vencimento (DD/MM/AAAA):", "Estoque Mínimo:","Data Inclusão"]
# entries = []
# for i, l in enumerate(campos):
#     tk.Label(frame_form, text=l).grid(row=i, column=0, sticky="w")
#     ent = tk.Entry(frame_form); ent.grid(row=i, column=1, sticky="ew")
#     entries.append(ent)
# ent_nome, ent_preco, ent_qtd, ent_fornecedor, ent_venc, ent_min = entries

# Inicializa uma lista vazia para armazenar as referências dos campos de entrada (Entry)
entries = []

# Itera sobre a lista 'campos', obtendo o índice (i) e o nome do campo (l)
for i, l in enumerate(campos):
    # Cria e posiciona um rótulo (Label) com o nome do campo na coluna 0
    tk.Label(frame_form, text=l).grid(row=i, column=0, sticky="w")
    
    # Cria um campo de entrada (Entry), posiciona na coluna 1 e expande horizontalmente
    ent = tk.Entry(frame_form)
    ent.grid(row=i, column=1, sticky="ew")
    
    # Adiciona o objeto 'Entry' criado à lista 'entries' para acesso posterior
    entries.append(ent)
     
# Desempacota a lista 'entries' atribuindo cada campo a uma variável específica 
# (essencial para ler ou limpar os dados de cada campo individualmente depois)
ent_nome, ent_preco, ent_qtd, ent_fornecedor, ent_venc, ent_min, ent_inc = entries
frame_form.columnconfigure(1, weight=1)

frame_busca = tk.Frame(root); frame_busca.pack(fill="x", padx=10)
tk.Label(frame_busca, text="Buscar:").pack(side="left"); ent_busca = tk.Entry(frame_busca); ent_busca.pack(side="left", fill="x", expand=True)

ent_venc.bind("<KeyRelease>", dadosdataini)
ent_inc.bind("<KeyRelease>", dadosdataini)
#ent_venc.bind("<FocusIn>",vercampos1)
ent_venc.bind("<FocusOut>",vercampos1)
#<FocusOut>
ent_preco.bind("<FocusOut>",converter_para_telaPreco)
#ent_preco.bind("<FocusOut>", lambda event: converter_para_telaPreco())

ent_inc.bind("<FocusOut>",vercampos1)
ent_busca.bind("<KeyRelease>", atualizar_treeview)

frame_btns = tk.Frame(root, pady=5); frame_btns.pack(fill="x", padx=10)
tk.Button(frame_btns, text="Entrada", command=lambda: registrar_movimento("entrada"), bg="#d1e7dd").pack(side="left", padx=5)
tk.Button(frame_btns, text="Saída", command=lambda: registrar_movimento("saida"), bg="#f8d7da").pack(side="left", padx=5)

tree = ttk.Treeview(root, columns=("ID", "Nome", "Preço", "Qtd", "Fornecedor", "Venc", "Min", "Data de Inclusão"), show='headings')
for col in ("ID", "Nome", "Preço", "Qtd", "Fornecedor", "Venc", "Min","Data de Inclusão",):
    tree.heading(col, text=col); tree.column(col, width=90)
tree.pack(fill="both", expand=True, padx=10, pady=10)
tree.bind("<<TreeviewSelect>>", carregar_campos)
'''
o for se resume em 2 linhas
for col in ("ID", "Nome", "Preço", "Qtd", "Fornecedor", "Venc", "Min","Data de Inclusão",):
    tree.heading(col, text=col); tree.column(col, width=90)   

# Configuração manual coluna por coluna (sem o loop for)
tree.heading("ID", text="ID")
tree.column("ID", width=90)

tree.heading("Nome", text="Nome")
tree.column("Nome", width=90)

tree.heading("Preço", text="Preço")
tree.column("Preço", width=90)

tree.heading("Qtd", text="Qtd")
tree.column("Qtd", width=90)

tree.heading("Fornecedor", text="Fornecedor")
tree.column("Fornecedor", width=90)

tree.heading("Venc", text="Venc")
tree.column("Venc", width=90)

tree.heading("Min", text="Min")
tree.column("Min", width=90)

tree.heading("Data de Inclusão", text="Data de Inclusão")
tree.column("Data de Inclusão", width=90)

'''

atualizar_treeview()
# Configura o botão "X" da janela para chamar a função de fechamento
root.protocol("WM_DELETE_WINDOW", fechar_programa)

root.mainloop()

'''
ALTERAÇÃO DE ESTRUTURA DE TABELA SQLITE

1. A Estratégia de "Adição com Valor Padrão"
Se você quer adicionar um campo (por exemplo, categoria ou status) sem quebrar os registros antigos, 
você deve definir um valor padrão (DEFAULT).

Comando SQL:
ALTER TABLE produtos ADD COLUMN categoria TEXT NOT NULL DEFAULT 'Geral';

2. A Estratégia Avançada (Para Mudanças Complexas)
Se a nova estrutura for mais complexa do que apenas um valor padrão (por exemplo, se você precisar calcular o novo valor com base em outros campos existentes), o ALTER TABLE simples não serve. Nesse caso, você deve usar o padrão de migração:

Criar uma tabela temporária com a nova estrutura.

Copiar os dados da tabela original para a nova, tratando a lógica dos campos.

Remover a tabela original.

Renomear a tabela temporária para o nome original.

Exemplo prático (SQL):


-- 1. Cria a nova tabela com a estrutura correta
CREATE TABLE produtos_novo (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    preco REAL,
    nova_coluna TEXT NOT NULL -- O novo campo
);

-- 2. Migra os dados com uma lógica de conversão (CASE, por exemplo)


INSERT INTO produtos_novo (id, nome, preco, nova_coluna)
SELECT id, nome, preco, 
       CASE WHEN preco > 100 THEN 'Premium' ELSE 'Comum' END
FROM produtos;

-- 3. Remove a antiga
DROP TABLE produtos;

-- 4. Renomeia a nova
ALTER TABLE produtos_novo RENAME TO produtos;





INSERT INTO produtos_novo (id, nome, preco, nova_coluna)
SELECT id, nome, preco, 'ESTOQUE_INICIAL' -- Este texto é o valor que populará a nova coluna
FROM produtos;



Quando você adiciona um campo de data em uma tabela já populada, o maior risco é o campo ficar com valor NULL 
(vazio) ou com uma data incorreta, o que pode quebrar funções de cálculo ou filtros 
(como o strftime que você usou anteriormente).

Para o seu estoque.db, a melhor estratégia depende de qual informação você deseja colocar nesse novo campo.

Estratégia: Adicionar com Valor Padrão (Recomendado)
Se você quer que todos os registros antigos recebam a data de hoje (data da criação da coluna), 
você pode usar o DEFAULT CURRENT_DATE.

ALTER TABLE produtos ADD COLUMN data_inclusao DATE NOT NULL DEFAULT (DATE('now'));

ou faça assim

-- 1. Cria nova tabela com a coluna 'data_inclusao'
CREATE TABLE produtos_novo (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    preco REAL,
    data_inclusao DATE NOT NULL
);

-- 2. Migra os dados calculando a data (Exemplo: 2026-07-17 menos 1 dia por ID)


INSERT INTO produtos_novo (id, nome, preco, data_inclusao)
SELECT id, nome, preco, DATE('now', '-' || id || ' days')
FROM produtos;

-- 3. Troca as tabelas
DROP TABLE produtos;
ALTER TABLE produtos_novo RENAME TO produtos;
'''

