from tkinter import *  # Importa a biblioteca tkinter para criar interfaces gráficas
from tkinter import messagebox  # Importa a função messagebox do tkinter para exibir mensagens de diálogo
from datetime import date  # Importa a classe date do módulo datetime

# Classe Cliente que representa um cliente com nome e pedido
class Cliente:
    """
        def: É a palavra-chave em Python usada para definir uma função ou método.
        
        __init__: É o nome especial do método de inicialização em Python.
        
        self: É uma referência ao próprio objeto que está sendo criado. Ele é usado para acessar os atributos 
        e métodos da instância dentro da classe.
        
        (self, nome): É a assinatura do método __init__. Ele recebe o parâmetro self (que representa o 
        objeto sendo criado) e o parâmetro nome.
    """
    def __init__(self, nome):
        
        self.nome = nome  # Atributo que armazena o nome do cliente
        self.pedido = Pedido()  # Atributo que armazena um objeto da classe Pedido para o cliente

# Classe Pedido que representa um pedido com uma lista de itens e taxa de serviço
class Pedido:
    def __init__(self):
        self.itens = []  # Atributo que armazena a lista de itens do pedido
        self.taxa_servico = 0.0  # Atributo que armazena a taxa de serviço do pedido

        
class ItemVenda:
    
    # O método __init__ é o construtor da classe ItemVenda e é executado quando um objeto é criado
    # Ele recebe dois parâmetros: nome e preco
    def __init__(self, nome, preco):
        
        # A linha a seguir atribui o valor do parâmetro nome ao atributo nome do objeto atual (self)
        self.nome = nome

        # A linha a seguir atribui o valor do parâmetro preco ao atributo preco do objeto atual (self)
        self.preco = preco

def cadastrar_cliente():
    
    # Cria a janela de cadastro de cliente
    janela_cadastrar_cliente = Toplevel(root)
    janela_cadastrar_cliente.title("Cadastrar Cliente")
    janela_cadastrar_cliente.configure(bg="white")

    # Obtém as dimensões da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Define a largura e a altura da janela de cadastro
    largura_janela = 300
    altura_janela = 200

    # Calcula as coordenadas para centralizar a janela
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    # Define a geometria da janela de cadastro
    janela_cadastrar_cliente.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
    
    # Cria um Frame para conter os elementos
    frame = Frame(janela_cadastrar_cliente, bg="white")
    frame.pack(expand=True)

    # Cria um rótulo para o campo de nome
    nome_rotulo = Label(frame,
                       text = "Digite o nome do cliente:",
                       font="Arial 14",
                       bg="white")
    nome_rotulo.pack(pady=10)
    
    # Cria uma entrada de texto para o nome
    nome_entrada = Entry(frame, font="Arial 14")
    nome_entrada.pack(pady=10)
    
    def cadastrar():
        
        # Obtém o nome digitado pelo usuário
        nome = nome_entrada.get()

        # Cria um objeto Cliente com o nome fornecido
        cliente = Cliente(nome)

        # Adiciona o cliente à lista de clientes
        clientes.append(cliente)
        
        # Fecha a janela de cadastro
        janela_cadastrar_cliente.destroy()

        # Exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso.")
    
    # Cria um botão para cadastrar o cliente
    cadastrar_botao = Button(frame,
                            text = "Cadastrar",
                            font="Arial 14",
                            command = cadastrar)
    cadastrar_botao.pack(pady=10)

    
def selecionar_cliente():
    
    # Cria a janela de cadastro de cliente
    janela_selecionar_cliente = Toplevel(root)
    janela_selecionar_cliente.title("Selecionar Cliente")
    janela_selecionar_cliente.configure(bg="white")

    # Obtém as dimensões da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Define a largura e a altura da janela de cadastro
    largura_janela = 500
    altura_janela = 300

    # Calcula as coordenadas para centralizar a janela
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    # Define a geometria da janela de cadastro
    janela_selecionar_cliente.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
    
    if len(clientes) == 0:
        
        # Verifica se não há clientes cadastrados
        mensagem_label = Label(janela_selecionar_cliente,
                              text = "Nenhum cliente cadastrado.",
                              font = "Arial 16",
                              bg="white")
        mensagem_label.pack(pady=10)
        
    else:
        
        # Se há clientes cadastrados, exibe a lista de clientes
        clientes_label = Label(janela_selecionar_cliente,
                              text = "Clientes Cadastrados.",
                              font = "Arial 16",
                              bg="white")
        clientes_label.pack(pady=10)
        
        # Percorre a lista de clientes e exibe cada um deles
        #O enumerate é uma função embutida do Python que retorna um objeto enumerado que consiste 
        #em pares de valores (índice, elemento).
        for i, cliente in enumerate(clientes):
            
            clientes_label = Label(janela_selecionar_cliente, 
                                   text = "{}. {}".format(i+1, cliente.nome),
                                   font = "Arial 16",
                                  bg="white")
            clientes_label.pack(pady=10)
            
        # Solicita ao usuário que digite o número do cliente que deseja selecionar
        selecionar_label = Label(janela_selecionar_cliente,
                              text = "Digite o número do cliente que deseja selecionar:",
                              font = "Arial 16",
                              bg="white")
        selecionar_label.pack(pady=10)
        
        # Cria uma entrada de texto para o usuário digitar o número do cliente
        selecionar_entry = Entry(janela_selecionar_cliente, font="Arial 14")
        selecionar_entry.pack(pady=10)
        
        def selecionar():
        
            # Obtém o índice do cliente selecionado
            cliente_index = int(selecionar_entry.get()) - 1
            
            #Verica se o número do cliente é inválido
            if cliente_index < 0 or cliente_index >= len(clientes):
                
                #Mensagem
                messagebox.showerror("Erro", "Número de cliente inválido.")
                
            else:
                
                # Seleciona o cliente e exibe o menu de produtos
                cliente_selecionado = clientes[cliente_index]
                exibir_menu_produtos(cliente_selecionado)
                
        
        selecionar_botao = Button(janela_selecionar_cliente,
                                 text="Selecionar",
                                 font = "Arial 14",
                                 command = selecionar)
        selecionar_botao.pack(pady=10)
        
        
def exibir_menu_produtos(cliente):
    
    # Cria a janela de cadastro de cliente
    janela_menu_produtos = Toplevel(root)
    janela_menu_produtos.title("Menu de Produtos")
    janela_menu_produtos.configure(bg="white")

    # Obtém as dimensões da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Define a largura e a altura da janela de cadastro
    largura_janela = 400
    altura_janela = 400

    # Calcula as coordenadas para centralizar a janela
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    # Define a geometria da janela de cadastro
    janela_menu_produtos.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
    
    #Define a lista de produtos disponiveis
    produtos = [
        ItemVenda("100 - Sanduíche", 12.00),
        ItemVenda("200 - Coxinha", 8.00),
        ItemVenda("300 - Pastel", 8.00),
        ItemVenda("400 - Café", 5.00),
        ItemVenda("500 - Refrigerante", 5.00),
        ItemVenda("600 - Sorvete", 8.00),
        ItemVenda("700 - Hambúrguer", 15.00),
        ItemVenda("800 - Batata Frita", 10.00),
        ItemVenda("900 - Milkshake", 12.00),
        ItemVenda("1000 - Salgado", 5.00),
        ItemVenda("1100 - Pizza", 20.00),
        ItemVenda("1200 - Suco Natural", 6.00),
        ItemVenda("1300 - Hot Dog", 7.00),
        ItemVenda("1400 - Açaí", 10.00),
        ItemVenda("1500 - Frango Frito", 9.00),
        ItemVenda("1600 - Refrigerante Diet", 6.00),
        ItemVenda("1700 - Salada", 8.00),
        ItemVenda("1800 - Combo Lanche", 18.00),
        ItemVenda("1900 - Sopa", 7.00),
        ItemVenda("2000 - Bolo", 6.00)
    ]
    
    def atualizar_lista_produtos():
        
        menu_listbox.delete(0, END)
        for produto in produtos:
            
            menu_listbox.insert(END, "{} - R$ {:.2f}".format(produto.nome, produto.preco))
            
    # Função para atualizar a exibição do carrinho e o total
    def atualizar_carrinho():
        carrinho_listbox.delete(0, END)  # Limpa a exibição atual do carrinho na lista
        for item in carrinho:
            # Insere cada item do carrinho na lista de carrinho_listbox
            carrinho_listbox.insert(END, "{} - R$ {:.2f}".format(item.nome, item.preco))
        total_label.config(text="Total: R$ {:.2f}".format(calcular_total()))  # Atualiza o texto do label de total com o valor atualizado do total
        
    def calcular_total():
        
        total = 100
        
        return total
    
    #Cria uma lista vazia para o carrinho
    carrinho = []
    
    #Cria um campo de Label para exibir as informações
    info_label = Label(janela_menu_produtos, text="", font="Arial 14", bg="#FFFFFF")
    info_label.pack(pady=10)
    
    frame_principal = Frame(janela_menu_produtos, bg="#FFFFFF")
    frame_principal.pack(pady = 10)
    
    menu_frame = Frame(frame_principal, bg="#FFFFFF")
    menu_frame.pack(pady = 10)
    
    produtos_label = Label(menu_frame,
                          text="Podutos Disponíveis",
                          bg="#FFFFFF",
                          font="Arial 12")
    produtos_label.pack(pady=10)
    
    menu_listbox = Listbox(menu_frame, font="Arial 14")
    menu_listbox.pack(side=LEFT)
    
    # Adiciona uma barra de rolagem à lista de produtos
    scrollbar_menu = Scrollbar(menu_frame)  # Cria um objeto Scrollbar para a lista de produtos
    scrollbar_menu.pack(side=RIGHT, fill=Y)  # Posiciona a barra de rolagem no lado direito do menu e a faz preencher verticalmente
    menu_listbox.config(yscrollcommand=scrollbar_menu.set)  # Configura a lista de produtos para usar a barra de rolagem vertical
    scrollbar_menu.config(command=menu_listbox.yview)  # Configura a barra de rolagem para controlar a visualização vertical da lista de produtos
    
    
    def adicionar_carrinho():
        
        # Obtém o índice do produto selecionado na lista do menu
        indice = menu_listbox.curselection()

        # Verifica se algum produto foi selecionado
        if indice:
            
            # Obtém o produto selecionado
            produto = produtos[indice[0]]
            
            # Adiciona o produto ao carrinho
            carrinho.append(produto)
            
            # Remove o produto da lista de produtos
            produtos.pop(indice[0])
            
            info_label.config(text="Produto adicionado ao carrinho.")
            
            atualizar_carrinho()
            atualizar_lista_produtos()
            
            
            
        else:
            info_label.config(text="Selecione um produto para adicionar ao carrinho.")    
    
    adicional_botao = Button(menu_frame,
                            text = "Adicionar ao Carrinho",
                            font="Arial 14",
                            command = adicionar_carrinho)
    adicional_botao.pack(pady=5)
    
    carrinho_frame = Frame(frame_principal, bg="#FFFFFF")
    carrinho_frame.pack(pady = 10)
    
    
    carrinho_listbox = Listbox(menu_frame, font="Arial 14")
    carrinho_listbox.pack(side=LEFT)
    
    total_label = Label(carrinho_frame,
                          text="Total: R$ 0.00",
                          bg="#FFFFFF",
                          font="Arial 12")
    total_label.pack(pady=10)
    
    atualizar_lista_produtos()
    
def sair():
    
    root.destroy()

# Cria uma instância da classe Tk
root = Tk()

# Define o título da janela
root.title("Sistema de Pedidos")

# Configura o fundo da janela como branco
root.configure(bg="white")

# Define a janela em modo de tela cheia
root.attributes("-fullscreen", True)

# Cria uma lista vazia para armazenar os clientes
clientes = []

# Cria um rótulo com uma mensagem de boas-vindas
mensagem_label = Label(root, 
                       text="Bem vindo ao Sistema de Pedidos!",
                      font="Arial 16",
                      bg="white")
mensagem_label.pack(pady = 50)

botao_frame = Frame(root, bg="white")
botao_frame.pack()

# Cria um botão para cadastrar um cliente
"""
Os parâmetros ipadx e ipady definem o espaçamento interno horizontal e vertical do conteúdo do 
botão, respectivamente. Eles controlam o preenchimento interno do botão, ou seja, o espaço adicional 
entre o texto do botão e as bordas do próprio botão.

O valor ipadx=20 define um espaçamento interno horizontal de 20 pixels, enquanto ipady=10 define 
um espaçamento interno vertical de 10 pixels. Isso permite ajustar o tamanho do botão e o espaçamento 
interno para obter uma aparência visualmente agradável.
"""
cadastrar_cliente_button = Button(botao_frame,
                                 text="1. Cadastrar Cliente",
                                 font="Arial 16",
                                 command = cadastrar_cliente,
                                 width = 40)
cadastrar_cliente_button.pack(side = TOP, padx=50, pady=10, ipadx=20, ipady=10)


# Cria um botão para selecionar um cliente
selecionar_cliente_button = Button(botao_frame,
                                 text="2. Selecionar Cliente",
                                 font="Arial 16",
                                 command = selecionar_cliente,
                                 width = 40)
selecionar_cliente_button.pack(side = TOP, padx=50, pady=10, ipadx=20, ipady=10)

# Cria um botão para visualizar os pedidos de todos os clientes
visualizar_pedidos_button = Button(botao_frame,
                                 text="3. Visualizar Pedidos de Todos os Clientes",
                                 font="Arial 16",
                                 command = cadastrar_cliente,
                                 width = 40)
visualizar_pedidos_button.pack(side = TOP, padx=50, pady=10, ipadx=20, ipady=10)

# Cria um botão para sair do sistema
sair_button = Button(botao_frame,
                                 text="4. Sair",
                                 font="Arial 16",
                                 command = sair,
                                 width = 40)
sair_button.pack(side = TOP, padx=50, pady=10, ipadx=20, ipady=10)

# Inicia o loop principal da aplicação
root.mainloop()

