# Definindo a classe Carro
# Definindo uma classe chamada Carro
class Carro:
    
    # Método inicializador (construtor) da classe que é invocado quando um objeto 
    # da classe é criado
    def __init__(self, marca, modelo, cor):
        self.marca = marca      # Define o atributo marca do carro com o valor fornecido
        self.modelo = modelo    # Define o atributo modelo do carro com o valor fornecido
        self.cor = cor          # Define o atributo cor do carro com o valor fornecido
        self.velocidade = 0     # Inicializa o atributo velocidade atual do carro com 0

        
    # Método que aumenta a velocidade do carro em 10 km/h
    def acelerar(self):
        
        # Incrementa a velocidade atual em 10 km/h
        # self.velocidade = self.velocidade + 10
        self.velocidade += 10
        
        # Exibe a velocidade atual do carro
        print(f"Velocidade atual: {self.velocidade} km/h")
        
    # Método que diminui a velocidade do carro em 10 km/h
    def frear(self):
        
        # Decrementa a velocidade atual em 10 km/h
        # self.velocidade = self.velocidade - 10
        self.velocidade -= 10
        
        # Garante que a velocidade não se torne negativa
        if self.velocidade < 0:
            self.velocidade = 0
        
        # Exibe a velocidade atual do carro
        print(f"Velocidade atual: {self.velocidade} km/h")
        
    # Método que exibe as informações básicas do carro
    def exibir_info(self):
        
        # Exibe a marca, modelo e cor do carro
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}, Velocidade: {self.velocidade} km/h")


# Lista para armazenar objetos da classe Carro
lista_carros = []

# Menu Interativo
# O loop while True cria um loop infinito, tornando o menu interativo até que o usuário escolha sair
while True:
    
    # Exibe o menu de opções para o usuário
    print("\n--- Menu ---")
    print("1. Adicionar novo carro")
    print("2. Exibir informações dos carros")
    print("3. Acelerar um carro")
    print("4. Frear um carro")
    print("5. Sair")
    
    # Solicita ao usuário que faça uma escolha e armazena a entrada na variável 'escolha'
    escolha = input("Escolha uma opção: ")

    # Se o usuário escolher "1", o programa solicitará detalhes sobre o novo carro
    if escolha == "1":
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        cor = input("Digite a cor do carro: ")
        
        # Cria um novo objeto da classe Carro e adiciona à lista de carros
        novo_carro = Carro(marca, modelo, cor)
        lista_carros.append(novo_carro)
        
    # Se o usuário escolher "2", o programa exibirá informações de todos os carros na lista
    elif escolha == "2":
        
        if lista_carros:  # Verifica se a lista de carros não está vazia
            for carro in lista_carros:  # Itera sobre cada objeto 'carro' na lista 'lista_carros'
                carro.exibir_info()  # Chama o método exibir_info() para cada carro
        else:
            print("Nenhum carro adicionado ainda.")
            
    # Se o usuário escolher "3", o programa permitirá acelerar um carro específico
    elif escolha == "3":
        
        modelo = input("Digite o modelo do carro que você deseja acelerar: ")
        
        # Procura pelo carro com o modelo especificado
        for carro in lista_carros:
            
            if carro.modelo == modelo:  # Se encontrar, acelera o carro
                carro.acelerar()
                break  # Sai do loop for
                
        else:
            
            print("Modelo não encontrado.")  # Se não encontrar nenhum carro com o modelo especificado
            
    # Se o usuário escolher "4", o programa permitirá frear um carro específico
    elif escolha == "4":
        
        modelo = input("Digite o modelo do carro que você deseja frear: ")
        
        # Procura pelo carro com o modelo especificado
        for carro in lista_carros:
            
            if carro.modelo == modelo:  # Se encontrar, freia o carro
                
                carro.frear()
                
                break  # Sai do loop for
        else:
            
            print("Modelo não encontrado.")  # Se não encontrar nenhum carro com o modelo especificado
            
            
    # Se o usuário escolher "5", o programa termina
    elif escolha == "5":
        
        print("Saindo do programa.")
        
        break  # Encerra o loop while, terminando o programa
    
    # Se o usuário inserir uma opção inválida
    else:
        
        print("Opção inválida. Tente novamente.")  # Mensagem para opções que não estão no menu

        
        
"""
    Marca: Toyota,    Modelo: Corolla
    Marca: Ford,      Modelo: Mustang
    Marca: Honda,     Modelo: Civic
    Marca: Chevrolet, Modelo: Malibu
    Marca: BMW,       Modelo: 3 Series
"""
print()