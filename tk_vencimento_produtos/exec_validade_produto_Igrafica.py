import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

#Lista de produtos
produtos = []

def cadastrar_produto( entry_codigo,  entry_nome, entry_data):
    
    #Obtem os valores inseridos nos campos de entrada
    codigo = entry_codigo.get()
    nome = entry_nome.get()
    data_validade = entry_data.get()
    
    try:
        
        # Converter a string da data de validade para o formato de data
        data_validade = datetime.strptime(data_validade, "%d/%m/%Y").date()
        
    except ValueError:
        
        # Exibir uma mensagem de erro se o formato da data for inválido
        messagebox.showerror("Erro", "Formato de data inválido. Use o formato dd/mm/aaaa.")
        
        return
    
    # Criar um dicionário com os dados do produto
    produto = {
        "codigo": codigo,
        "nome": nome,
        "validade": data_validade
    }

    # Adicionar o produto à lista de produtos
    produtos.append(produto)

    # Exibir uma mensagem de sucesso
    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
       

def abrir_tela_cadastro():
    
    #Criar a janela secundária
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastrar Produto")
    
    # Definir as dimensões da janela
    largura_janela = 600
    altura_janela = 230

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
                           text = "Código:",
                           bg="#FFFFFF",
                           font="Arial 16")
    label_codigo.grid(row = 0, column = 0, padx = 10, pady = 10, sticky="e")
    
    #Campo de entrada de dados
    entry_codigo = tk.Entry(janela_cadastro,
                           font="Arial 16")
    entry_codigo.grid(row = 0, column = 1, padx = 10, pady = 10)
    
    #-------------------------------
    
    label_nome = tk.Label(janela_cadastro,
                           text = "Nome:",
                           bg="#FFFFFF",
                           font="Arial 16")
    label_nome.grid(row = 1, column = 0, padx = 10, pady = 10, sticky="e")
    
    #Campo de entrada de dados
    entry_nome = tk.Entry(janela_cadastro,
                           font="Arial 16")
    entry_nome.grid(row = 1, column = 1, padx = 10, pady = 10)
    
    #-------------------------------
    
    label_data = tk.Label(janela_cadastro,
                           text = "Date de Validade (dd/mm/aaaa):",
                           bg="#FFFFFF",
                           font="Arial 16")
    label_data.grid(row = 2, column = 0, padx = 10, pady = 10, sticky="e")
    
    #Campo de entrada de dados
    entry_data = tk.Entry(janela_cadastro,
                           font="Arial 16")
    entry_data.grid(row = 2, column = 1, padx = 10, pady = 10)
    
    
    #Campo de entrada de dados
    botao_cadastrar_produto = tk.Button(janela_cadastro,
                           font="Arial 16",
                           text="Cadastrar",
                           command = lambda: cadastrar_produto( entry_codigo,  entry_nome, entry_data))
    botao_cadastrar_produto.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 10, sticky="NSEW")
    
    
    #Executa a janela cadastro
    janela_cadastro.mainloop()

def consultar_produtos(combo_opcoes, texto_resultado):
    
        #Obtem a opção selecionada
        opcao = combo_opcoes.get()

        if opcao == "Tranquilo":

            dias_min = 91 
            dias_max = float('inf') #inf - Numero infinito positivo

        elif opcao == "Alerta":

            dias_min = 31 
            dias_max = 90 
            
        elif opcao == "Critico":

            dias_min = 1
            dias_max = 30
            
        elif opcao == "Produto Vencido":

            dias_min = float('-inf')
            dias_max = 0
        
        # Obtém a data atual
        data_atual = datetime.now().date()

        # Inicializa uma variável para armazenar o resultado
        resultado = ""

        # Percorre a lista de produtos
        for produto in produtos:

            # Calcula a diferença de tempo entre a validade do produto e a data atual
            diferenca_tempo = produto["validade"] - data_atual

            # Verifica se a diferença de tempo está dentro dos limites definidos
            """
            O .days é um atributo de objetos do tipo timedelta da biblioteca datetime.

            diferenca_tempo é uma variável que representa a diferença de tempo 
            entre a data de validade do produto e a data atual. Essa diferença de tempo 
            é um objeto do tipo timedelta, que representa uma duração de tempo.

            Ao acessar o atributo .days desse objeto, obtemos o número de dias contidos 
            na diferença de tempo. Isso nos permite comparar a diferença de tempo em dias 
            com os valores de dias_min e dias_max para realizar a filtragem dos produtos.

            Portanto, a expressão diferenca_tempo.days retorna o número de dias da diferença 
            de tempo entre a data de validade e a data atual.
            """
            if dias_min <= diferenca_tempo.days <= dias_max:

                # Adiciona as informações do produto ao resultado
                resultado += f"Código: {produto['codigo']}\n"
                resultado += f"Produto: {produto['nome']}\n"
                resultado += f"Data de validade: {produto['validade'].strftime('%d/%m/%Y')}\n"

                # Verifica se o produto está vencido ou não
                if diferenca_tempo.days <= 0:

                    resultado += "Status: Produto Vencido!\n"

                else:

                    resultado += f"Dias restantes: {diferenca_tempo.days}\n"

                resultado += "\n"
          
        #Limpando o conteúdo da caixa de texto de resultados
        texto_resultado.delete("1.0", tk.END)
        
        texto_resultado.insert(tk.END, resultado)

def abrir_tela_consulta():
    
    #Criar a janela secundária
    janela_consulta = tk.Toplevel()
    janela_consulta.title("Consultar Produtos")
    
    # Definir as dimensões da janela
    largura_janela = 1050
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
    
    #Cria um frame para agrupar os elementos
    frame_topo = tk.Frame(janela_consulta, bg="#FFFFFF")
    frame_topo.pack(pady=10)
    
    #Criar os elementos da interface de cadastro
    #sticky="e" - Alinhar na direita
    label_opcoes = tk.Label(frame_topo,
                           text = "Opções de Consulta:",
                           bg="#FFFFFF",
                           font="Arial 16")
    label_opcoes.pack(side = tk.LEFT, padx=10)
    
    
    #Cria a combobox para as opções de consulta
    combo_opcoes = ttk.Combobox(frame_topo, 
                               values=["Tranquilo", "Alerta", "Critico", "Produto Vencido"],
                               font="Arial 16")
    combo_opcoes.pack(side = tk.LEFT, padx=10)
    
    
    #Cria o botão para consultar
    botao_consultar_produto = tk.Button(frame_topo, 
                               text = "Consultar",
                               font="Arial 16",
                               command = lambda: consultar_produtos(combo_opcoes, texto_resultado))
    botao_consultar_produto.pack(side = tk.LEFT, padx=10)
    
    
    texto_resultado = tk.Text(janela_consulta, 
                             font="Arial 14")
    texto_resultado.pack(pady = 10, fill=tk.BOTH, expand=True)
    


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