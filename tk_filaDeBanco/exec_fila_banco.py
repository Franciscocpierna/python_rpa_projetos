"""
Exercício de Lógica de Programação - Fila de Banco

Você foi contratado para desenvolver um algoritmo para gerenciar a fila de atendimento 
de um banco. Neste banco, existem dois tipos de atendimento: normal e preferencial. 
Sempre que chega um cliente preferencial, ele deve ser atendido imediatamente, passando 
à frente de todos os clientes exceto dos outros clientes preferenciais que já estavam na 
fila. Os clientes normais são atendidos seguindo a ordem de chegada.

Você deve implementar uma solução em linguagem de programação que atenda aos seguintes requisitos:

    O algoritmo deve solicitar ao usuário que digite sua senha.
    O usuário pode digitar "P" para senha preferencial ou "N" para senha normal.
    Se o usuário digitar uma senha preferencial, ele deve ser adicionado ao início da fila.
    Se o usuário digitar uma senha normal, ele deve ser adicionado ao final da fila.
    Sempre que um cliente for atendido, o algoritmo deve exibir a senha do cliente e removê-lo da fila.
    O algoritmo deve continuar atendendo os clientes até que não haja mais ninguém na fila.

Considere que as senhas dos clientes são sequenciais e iniciam em 1. Ou seja, o primeiro cliente terá senha 1, 
o segundo cliente terá senha 2 e assim por diante.

Escreva o código em Python para implementar essa solução.

Observações:

    - Certifique-se de incluir um mecanismo para encerrar o programa quando não houver mais 
    clientes na fila.
    
    - Considere que a fila inicialmente está vazia.
    Você pode utilizar estruturas de dados como listas, filas ou arrays para implementar a fila de atendimento.
"""

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
def adicionar_cliente():
    
    #Utilizando a variável senha global
    global senha
    
    tipo_senha = input("Digite o tipo de senha (P - Preferencial, N - Normal): ")
    
    #Verifica se o tipo de senha é preferencial
    if tipo_senha.upper() == "P":
        
        #Criando um objeto Cliente com a senha atual e o tipo Preferencial
        cliente = Cliente(senha, "preferencial")
        
        #Adicionando o cliente à fila de clientes preferenciais
        fila_preferencial.append(cliente)
        
    elif tipo_senha.upper() == "N":
        
        #Criando um objeto Cliente com a senha atual e o tipo Preferencial
        cliente = Cliente(senha, "normal")
        
        #Adicionando o cliente à fila de clientes preferenciais
        fila_normal.append(cliente)
        
    else:
        
        print("\nOpção inválida. Tente novamente.")
        
        return
    
    print(f"\nCliente com senha {cliente.senha} ({cliente.tipo}) adicionado à fila")
    
    #senha = senha + 1
    senha += 1

#Função para exibir a fila de atendimento
def exibir_fila():
    
    #Verificando se há clientes tanto na fila preferencial como na fila normal
    if len(fila_preferencial) > 0 or len(fila_normal) > 0:
        
        print("\nFila de atendimento:")
        
        #Iterando sobre os clientes da fila preferencial e exibindo suas informações
        for cliente in fila_preferencial:
            
            print(f"Senha {cliente.senha} ({cliente.tipo})")
            
        #Iterando sobre os clientes da fila normal e exibindo suas informações
        for cliente in fila_normal:
            
            print(f"Senha {cliente.senha} ({cliente.tipo})")
            
    else:
        
        print("\nA fila está vazia.")
        
def remover_cliente():
    
    #Verificando se há clientes tanto na fila preferencial como na fila normal
    if len(fila_preferencial) > 0:
        
        #Removendo o cliente do inicio da fila preferencial e armazenando-o na variável cliente_removido 
        cliente_removido = fila_preferencial.pop(0)
        
        print(f"\nCliente com senha {cliente_removido.senha} ({cliente_removido.tipo}) removido da fila.")
        
    elif len(fila_normal) > 0:
        
        #Removendo o cliente do inicio da fila normal e armazenando-o na variável cliente_removido 
        cliente_removido = fila_normal.pop(0)
        
        print(f"\nCliente com senha {cliente_removido.senha} ({cliente_removido.tipo}) removido da fila.")
        
    else:
        
        print("\nA fila está vazia.")
        
def chamar_proximo():
    
    #Verificando se há clientes tanto na fila preferencial como na fila normal
    if len(fila_preferencial) > 0:
        
        #Removendo o cliente do inicio da fila preferencial e armazenando-o na variável cliente_chamado 
        cliente_chamado = fila_preferencial.pop(0)
        
        print(f"\nChamando o proximo cliente: senha {cliente_chamado.senha} ({cliente_chamado.tipo}).")
        
    elif len(fila_normal) > 0:
        
        #Removendo o cliente do inicio da fila normal e armazenando-o na variável cliente_chamado 
        cliente_chamado = fila_normal.pop(0)
        
        print(f"\nChamando o proximo cliente: senha {cliente_chamado.senha} ({cliente_chamado.tipo}).")
        
    else:
        
        print("\nA fila está vazia.")
    
opcao = ""

#while - enquanto
while opcao != "5":
    
    print("\n------- Menu ------")
    print("1 - Adicionar Cliente na Fila")
    print("2 - Exibir Fila")
    print("3 - Remover Cliente da Fila")
    print("4 - Chamar o Próximo")
    print("5 - Encerrar")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        
        adicionar_cliente()
        
    elif opcao == "2":
        
        exibir_fila()
        
    elif opcao == "3":
        
        remover_cliente()
        
    elif opcao == "4":
        
        chamar_proximo()
        
    elif opcao == "5":
        
        print("\nPrograma encerrado com sucesso!")
        break
        
    else:
        
        print("\Opção inválida. Tente novamente!")
    
