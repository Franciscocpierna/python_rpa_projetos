# Importando o módulo date da biblioteca datetime
from datetime import date

# Definindo a classe Cliente
class Cliente:
    
    def __init__(self, nome):
        
        # Inicializando o atributo nome com o valor fornecido
        self.nome = nome
        
        # Inicializando o atributo pedido como uma instância da classe Pedido
        self.pedido = Pedido()

# Definindo a classe Pedido
class Pedido:
    
    def __init__(self):
        
        # Inicializando o atributo itens como uma lista vazia
        self.itens = []
        
        # Inicializando o atributo taxa_servico com o valor 0.0
        self.taxa_servico = 0.0
    
    def adicionar_item(self, item):
        
        # Adicionando o item fornecido à lista de itens
        self.itens.append(item)
    
    def remover_item(self, item):
        
        # Removendo o item fornecido da lista de itens
        self.itens.remove(item)
    
    def calcular_total(self):
        
        # Inicializando a variável total com o valor 0.0
        total = 0.0
        
        # Percorrendo todos os itens na lista de itens
        for item in self.itens:
            
            # Somando o preço de cada item ao total
            total += item.preco
            
        # Adicionando a taxa de serviço ao total
        total += self.taxa_servico
        
        # Retornando o valor total
        return total

    
    def gerar_nota_fiscal(self, cliente):
        
        # Imprimindo o cabeçalho da nota fiscal
        print("----- Nota Fiscal -----")
        
        # Imprimindo o nome do cliente
        print("Cliente:", cliente.nome)
        
        # Imprimindo a seção dos itens
        print("Itens:")

        # Iterando sobre cada item na lista de itens
        for item in self.itens:

            # Imprimindo o nome e preço de cada item
            print("- Nome: {}, Preço: R$ {:.2f}".format(item.nome, item.preco))
            
        # Imprimindo a taxa de serviço
        print("Taxa de Serviço: R$ {:.2f}".format(self.taxa_servico))
            
        # Imprimindo o total do pedido
        print("Total: R$ {:.2f}".format(self.calcular_total()))

# Definindo a classe ItemVenda
class ItemVenda:
    
    def __init__(self, nome, preco, data_validade):
        
        # Inicializando os atributos nome, preco e data_validade com os valores fornecidos
        self.nome = nome
        self.preco = preco
        self.data_validade = data_validade

# Definindo a função cadastrar_cliente
def cadastrar_cliente():
    
    # Solicitando ao usuário que digite o nome do cliente
    nome = input("Digite o nome do cliente: ")
    
    # Criando um objeto Cliente com o nome fornecido
    cliente = Cliente(nome)
    
    # Retornando o objeto Cliente criado
    return cliente


def exibir_clientes(clientes):
    
    # Imprimindo uma linha em branco e o cabeçalho dos clientes cadastrados
    print("\nClientes cadastrados:")
    
    # Iterando sobre cada cliente na lista de clientes
    for i, cliente in enumerate(clientes):
        
        # Imprimindo o número e o nome de cada cliente
        print("{}. {}".format(i+1, cliente.nome))

def selecionar_cliente(clientes):
    
    # Chamando a função exibir_clientes para mostrar a lista de clientes
    exibir_clientes(clientes)
    
    # Solicitando ao usuário que selecione o número do cliente
    escolha = int(input("Selecione o número do cliente: "))
    
    # Verificando se a escolha é válida (dentro dos limites da lista de clientes)
    if escolha >= 1 and escolha <= len(clientes):
        
        # Retornando o cliente selecionado
        return clientes[escolha-1]
    
    else:
        
        # Imprimindo uma mensagem de opção inválida e retornando None
        print("Opção inválida.")
        return None

def exibir_menu_produtos():
    # Imprimindo o menu de produtos disponíveis
    print("\nMenu de produtos:")
    print("100 - Sanduíche - R$ 12,00")
    print("200 - Coxinha - R$ 8,00")
    print("300 - Pastel - R$ 8,00")
    print("400 - Café - R$ 5,00")
    print("500 - Refrigerante - R$ 5,00")
    print("0 - Voltar")


def adicionar_item_cliente(cliente):
    
    # Loop infinito para adicionar itens ao pedido do cliente
    while True:
        
        # Chamando a função exibir_menu_produtos para mostrar os produtos disponíveis
        exibir_menu_produtos()
        
        # Solicitando ao usuário que digite o código do produto
        codigo = int(input("Digite o código do produto: "))
        
        # Verificando o código do produto e adicionando-o ao pedido do cliente correspondente
        if codigo == 100:
            
            # Definindo os detalhes do lanche
            nome = "Sanduíche"
            preco = 12.00
            data_validade = date.today()
            
            # Criando um objeto ItemVenda com os detalhes do lanche
            lanche = ItemVenda(nome, preco, data_validade)
            
            # Adicionando o lanche ao pedido do cliente
            cliente.pedido.adicionar_item(lanche)
            
            # Imprimindo uma mensagem informando que o produto foi adicionado ao pedido
            print("Produto adicionado ao pedido.")
            
        elif codigo == 200:
            
            nome = "Coxinha"
            preco = 8
            data_validade = date.today()
            lanche = ItemVenda(nome, preco, data_validade)
            cliente.pedido.adicionar_item(lanche)
            
            print("Produto adicionado ao pedido.")
            
        elif codigo == 300:
            
            nome = "Pastel"
            preco = 8
            data_validade = date.today()
            lanche = ItemVenda(nome, preco, data_validade)
            cliente.pedido.adicionar_item(lanche)
            
            print("Produto adicionado ao pedido.")
            
        elif codigo == 400:
            
            nome = "Café"
            preco = 5
            data_validade = date.today()
            lanche = ItemVenda(nome, preco, data_validade)
            cliente.pedido.adicionar_item(lanche)
            
            print("Produto adicionado ao pedido.")
                  
        elif codigo == 500:
                  
            nome = "Refrigerante"
            preco = 5
            data_validade = date.today()
            lanche = ItemVenda(nome, preco, data_validade)
            cliente.pedido.adicionar_item(lanche)
                  
            print("Produto adicionado ao pedido.")
                  
        elif codigo == 0:
                  
            # Encerrando o loop quando o usuário digitar 0
            break
                  
        else:
                  
            # Imprimindo uma mensagem de código de produto inválido
            print("Código de produto inválido.")


def visualizar_pedidos(clientes):
    
    # Verificando se há clientes cadastrados
    if clientes:
                  
        print("Pedidos de todos os clientes:")
        
        # Iterando sobre cada cliente
        for cliente in clientes:
            
            # Imprimindo o cabeçalho dos pedidos do cliente atual
            print("\n--- Pedidos do cliente {} ---".format(cliente.nome))
            
            # Verificando se o cliente possui itens no pedido
            if cliente.pedido.itens:
                
                # Gerando a nota fiscal do pedido para o cliente atual
                cliente.pedido.gerar_nota_fiscal(cliente)
                
            else:
                
                # Imprimindo uma mensagem informando que o cliente não realizou um pedido
                print("O cliente {} ainda não realizou um pedido.".format(cliente.nome))
                
    else:
        
        # Imprimindo uma mensagem informando que nenhum cliente está cadastrado
        print("Nenhum cliente cadastrado.")


# Lista de clientes cadastrados
clientes = []

while True:
    
    # Exibindo o menu principal da lanchonete
    print("\n--- Sistema da Lanchonete ---")
    print("1. Cadastrar cliente")
    print("2. Selecionar cliente")
    print("3. Visualizar pedidos de todos os clientes")
    print("4. Sair")

    # Solicitando a opção desejada ao usuário
    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        
        # Opção de cadastrar cliente
        cliente = cadastrar_cliente()
        clientes.append(cliente)
        
        print("Cliente cadastrado com sucesso.")
        
    elif opcao == 2:
        
        # Opção de selecionar cliente
        cliente = selecionar_cliente(clientes)
        
        if cliente:
            
            # Se um cliente válido foi selecionado, permite adicionar itens ao pedido
            adicionar_item_cliente(cliente)
            
    elif opcao == 3:
        
        # Opção de visualizar pedidos de todos os clientes
        visualizar_pedidos(clientes)
        
    elif opcao == 4:
        
        # Opção de sair do programa
        print("Encerrando o programa...")
        
        break
        
    else:
        
        # Opção inválida
        print("Opção inválida. Digite novamente.")