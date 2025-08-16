import tkinter as tk

#Definindo a classe cliente
class Cliente:
    
    #Método de inicialização da classe cliente, que recebe a senha e o tipo como parâmetros
    def __init__(self, senha, tipo):
        
        #Atribuindo a senha recebida ao atributo "senha" do objeto cliente
        self.senha = senha
        
        #Atribuindo o tipo recebido ao atributo "tipo" do objeto cliente
        self.tipo = tipo
        
#Inializando a lista de clientes preferenciais vazia
fila_preferencial = []

#Inializando a lista de clientes normais vazia
fila_normal = []

#Inicializando a variável senha com o valor inicial de 1
senha = 1
    
#Função para adicionar um cliente na fila
def adicionar_cliente(adicionar_cliente_tela, mensagem_label, error_label):
    
    global senha
    
    #Obtendo o tipo da senha selecionado na tela
    tipo_senha = tipo_senha_var.get()
    
    if tipo_senha == "P":
        
        #Criando um objeto cliente com a senha atual e o tipo "preferencial"
        cliente = Cliente(senha, "preferencial")
        
        #Adicionando o cliente à fila preferencial
        fila_preferencial.append(cliente)
        
    elif tipo_senha == "N":
        
        #Criando um objeto cliente com a senha atual e o tipo "preferencial"
        cliente = Cliente(senha, "normal")
        
        #Adicionando o cliente à fila preferencial
        fila_normal.append(cliente)
        
    else:
        
        error_label.config(text="Opção inválida. Tente novamente.")
        
        return
    
    mensagem_label.config(text=f"Cliente com senha {cliente.senha} ({cliente.tipo}) adicionado à fila.")
    
    #Incrementando o valor da senha
    #senha = senha + 1
    senha += 1
    
def abrir_adicionar_cliente():
    
    #Cria uma tela secundária
    adicionar_cliente_tela = tk.Toplevel(tela_principal)
    adicionar_cliente_tela.title("Adicionar Cliente")
    adicionar_cliente_tela.geometry("500x400")    
    adicionar_cliente_tela.configure(background="#FFFFFF") #Cor branco

    #Obtem a largura e altura da tela
    largura_tela = adicionar_cliente_tela.winfo_screenwidth()
    altura_tela = adicionar_cliente_tela.winfo_screenheight()

    #Calcular as coordenadas x e y para centralizar a tela
    posicao_x = int(largura_tela / 2 - 500 / 2)
    posicao_y = int(altura_tela / 2 - 400 / 2)

    #Definir o posicionamento da janela
    adicionar_cliente_tela.geometry(f"500x400+{posicao_x}+{posicao_y}")
    
    #Campo que exibe as mensagens
    mensagem_label = tk.Label(adicionar_cliente_tela,
                             text="",
                             font=("Arial 16"),
                             background="#FFFFFF",
                             pady=30)
    mensagem_label.pack() #Adiciona e centraliza
    
    error_label = tk.Label(adicionar_cliente_tela,
                             text="",
                             font=("Arial 16"),
                             background="#FFFFFF")
    error_label.pack() #Adiciona e centraliza
    
    #Cria uma variavel do tipo StringVar para armazenar o tipo de senha selecionado
    global tipo_senha_var
    tipo_senha_var = tk.StringVar()
    tipo_senha_var.set("N")
    
    #Cria opção preferencial
    preferencial_radio = tk.Radiobutton(adicionar_cliente_tela,
                                       text="Senha Preferencial",
                                       variable = tipo_senha_var,
                                       value = "P",
                                       font = ("Arial 16"),
                                       bg= "#FFFFFF")
    preferencial_radio.pack() #Cria e centraliza
    
    #Cria opção preferencial
    normal_radio = tk.Radiobutton(adicionar_cliente_tela,
                                       text="Senha Normal",
                                       variable = tipo_senha_var,
                                       value = "N",
                                       font = ("Arial 16"),
                                       bg= "#FFFFFF")
    normal_radio.pack() #Cria e centraliza
    
    #Cria um botão para adicionar o cliente. chamando a função
    adicionar_cliente_button = tk.Button(adicionar_cliente_tela,
                                       text="Adicionar Cliente",
                                       font = ("Arial 16"),
                                       bg= "#FFFFFF",
                                       command = lambda: adicionar_cliente(adicionar_cliente_tela, mensagem_label, error_label))
    adicionar_cliente_button.pack() #Cria e centraliza
    

#Função para exibir a fila de atendimento
def exibir_fila():
    
    #Inicializa uma string vazia para armazenar a representação da fila
    fila_texto = ""
    
    if fila_preferencial or fila_normal:
        
        # Se houver clientes na fila preferencial ou na fila normal
        # Percorrer a fila preferencial e adicionar a representação de cada cliente à string da fila
        for cliente in fila_preferencial:
            fila_texto += f"Senha {cliente.senha} ({cliente.tipo})\n"

        # Percorrer a fila normal e adicionar a representação de cada cliente à string da fila
        for cliente in fila_normal:
            fila_texto += f"Senha {cliente.senha} ({cliente.tipo})\n"
    
    else:
        
        # Caso contrário, se a fila estiver vazia, definir a string da fila como "A fila está vazia."
        fila_texto = "A fila está vazia."
        
    #Cria uma tela secundária
    exibir_fila_tela = tk.Toplevel(tela_principal)
    exibir_fila_tela.title("Ecibir Fila")
    exibir_fila_tela.geometry("500x400")    
    exibir_fila_tela.configure(background="#FFFFFF") #Cor branco

    #Obtem a largura e altura da tela
    largura_tela = exibir_fila_tela.winfo_screenwidth()
    altura_tela = exibir_fila_tela.winfo_screenheight()

    #Calcular as coordenadas x e y para centralizar a tela
    posicao_x = int(largura_tela / 2 - 500 / 2)
    posicao_y = int(altura_tela / 2 - 400 / 2)

    #Definir o posicionamento da janela
    exibir_fila_tela.geometry(f"500x400+{posicao_x}+{posicao_y}")
    
    #Cria um label para exibir a string da fila
    fila_label = tk.Label(exibir_fila_tela, 
                         text=fila_texto,
                         font=("Arial, 16"),
                         bg = "#FFFFFF",
                         pady = 30)
    fila_label.pack()
    
def remover_cliente():
    
    #Verifica se a fila fila_preferencial não está vazia
    if fila_preferencial:
        
        #Remove o primeiro cliente da fila preferencial e armazena em cliente_removido
        cliente_removido = fila_preferencial.pop(0)

        #Atualiza o texto do rótulo proximo_label co informações do cliente que foi removido
        proximo_label.config(text=f"Cliente removido: Senha {cliente_removido.senha} ({cliente_removido.tipo})")
            
    elif fila_normal:
                             
        #Remove o primeiro cliente da fila normal e armazena em cliente_removido
        cliente_removido = fila_normal.pop(0)

        #Atualiza o texto do rótulo proximo_label co informações do cliente que foi removido
        proximo_label.config(text=f"Cliente removido: Senha {cliente_removido.senha} ({cliente_removido.tipo})")
                             
    else:
                             
        proximo_label.config(text="A fila está vazia.")
        
def chamar_proximo():
    
    
    #Verifica se a fila fila_preferencial não está vazia
    if fila_preferencial:
        
        #Remove o primeiro cliente da fila preferencial e armazena em cliente_chamado
        cliente_chamado = fila_preferencial.pop(0)

        #Atualiza o texto do rótulo proximo_label co informações do cliente que foi removido
        proximo_label.config(text=f"Chamando o próximo cliente: Senha {cliente_chamado.senha} ({cliente_chamado.tipo})")
            
    elif fila_normal:
                             
        #Remove o primeiro cliente da fila normal e armazena em cliente_chamado
        cliente_chamado = fila_normal.pop(0)

        #Atualiza o texto do rótulo proximo_label co informações do cliente que foi removido
        proximo_label.config(text=f"Chamando o próximo cliente: Senha {cliente_chamado.senha} ({cliente_chamado.tipo})")
                             
    else:
                             
        proximo_label.config(text="A fila está vazia.")   
    
            
    
#Função para encerrar o programa
def encerrar_programa():
    
    #Sai do sistema
    tela_principal.destroy()
    
#Janela principal
tela_principal = tk.Tk()
tela_principal.title("Fila de Banco") #Titulo da tela
tela_principal.geometry("600x500") #Tamanho da tela
tela_principal.configure(background="#FFFFFF") #Cor branco

#Obtem a largura e altura da tela
largura_tela = tela_principal.winfo_screenwidth()
altura_tela = tela_principal.winfo_screenheight()

#Calcular as coordenadas x e y para centralizar a tela
posicao_x = int(largura_tela / 2 - 600 / 2)
posicao_y = int(altura_tela / 2 - 500 / 2)

#Definir o posicionamento da janela
tela_principal.geometry(f"600x500+{posicao_x}+{posicao_y}")

#Criando um campo informativo
titulo_label = tk.Label(tela_principal, 
                       text="Fila de Banco",
                       font=("Arial", 20, "bold"),
                       background="#FFFFFF")
titulo_label.pack(pady=10) #Cria e centraliza na tela

#Adiciona um botão na tela
adicionar_cliente_button = tk.Button(tela_principal, 
                       text="Adicionar Cliente",
                       font=("Arial", 16, "bold"),
                       width=40,
                       command = abrir_adicionar_cliente)
adicionar_cliente_button.pack(pady=5) #Cria e centraliza na tela

#-----------------------------------

#Adiciona um botão na tela
exibir_fila_button = tk.Button(tela_principal, 
                       text="Exibir Fila",
                       font=("Arial", 16, "bold"),
                       width=40,
                       command = exibir_fila)
exibir_fila_button.pack(pady=5) #Cria e centraliza na tela


#-----------------------------------

#Adiciona um botão na tela
remover_cliente_button = tk.Button(tela_principal, 
                       text="Remover Cliente da Fila",
                       font=("Arial", 16, "bold"),
                       width=40,
                       command = remover_cliente)
remover_cliente_button.pack(pady=5) #Cria e centraliza na tela

#-----------------------------------

#Adiciona um botão na tela
chamar_proximo_button = tk.Button(tela_principal, 
                       text="Chamar Próximo Cliente",
                       font=("Arial", 16, "bold"),
                       width=40,
                       command = chamar_proximo)
chamar_proximo_button.pack(pady=5) #Cria e centraliza na tela

#-----------------------------------

#Criando um campo informativo
proximo_label = tk.Label(tela_principal, 
                       text="",
                       font=("Arial", 16, "bold"),
                       background="#FFFFFF")
proximo_label.pack(pady=10) #Cria e centraliza na tela

#-----------------------------------

#Criando um campo informativo
removido_label = tk.Label(tela_principal, 
                       text="",
                       font=("Arial", 16, "bold"),
                       background="#FFFFFF")
removido_label.pack(pady=10) #Cria e centraliza na tela

#-----------------------------------

#Adiciona um botão na tela
encerrar_button = tk.Button(tela_principal, 
                       text="Sair",
                       font=("Arial", 16, "bold"),
                       width=40,
                       command = encerrar_programa)
encerrar_button.pack(pady=5) #Cria e centraliza na tela

#Inicial a tela
tela_principal.mainloop()