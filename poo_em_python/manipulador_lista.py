print("Exercício Manipulador de Listas em Python")
"""
Requisitos:

    1. Crie uma classe chamada ManipuladorDeLista que será responsável por todas as 
    operações de manipulação de lista.
    
        - adicionar_elemento(elemento): adiciona um elemento no final da lista.
        - remover_elemento(elemento): remove a primeira ocorrência do elemento na lista.
        - encontrar_maior(): encontra e retorna o maior elemento da lista.
        - encontrar_menor(): encontra e retorna o menor elemento da lista.
        - calcular_media(): calcula e retorna a média dos elementos na lista.
        - mostrar_lista(): retorna a lista atual.

    2. Implemente uma função menu() que serve como interface do usuário. Essa 
    função deve mostrar um menu com as opções de manipulação e realizar a operação 
    escolhida pelo usuário.

    3. O programa deve continuar rodando e mostrando o menu até que o usuário escolha sair.

"""
class ManipuladorDeLista:
    
    # Método construtor que é chamado automaticamente ao criar 
    # um objeto desta classe
    def __init__(self):
        
        # Inicializa uma lista vazia como atributo de instância 
        # do objeto
        self.lista = []
        
    
    # - adicionar_elemento(elemento): adiciona um elemento no final da lista.
    
    # Método para adicionar um elemento à lista
    def adicionar_elemento(self, elemento):
        
        # Utiliza o método append para adicionar o elemento passado 
        # como argumento à lista
        self.lista.append(elemento)
        
    # - remover_elemento(elemento): remove a primeira ocorrência do elemento na lista.

    # Método para remover um elemento da lista
    def remover_elemento(self, elemento):
        
        try:
            
            # Tenta remover o elemento da lista
            self.lista.remove(elemento)
            
            # Se bem-sucedido, imprime uma mensagem de sucesso
            print("Elemento removido da lista.")
            
        except ValueError:
            
            # Se o elemento não for encontrado na lista, imprime 
            # uma mensagem de erro
            print("Elemento não encontrado na lista.")
            
    # - encontrar_maior(): encontra e retorna o maior elemento da lista.
    
    # Método para encontrar o maior elemento da lista
    def encontrar_maior(self):
        
        # Verifica se a lista não está vazia
        if self.lista:
            
            # Retorna o maior elemento da lista usando a função max()
            return max(self.lista)
        
        else:
            
            # Retorna uma mensagem se a lista estiver vazia
            return "A lista está vazia."
    
    # - encontrar_menor(): encontra e retorna o menor elemento da lista.
        
    # Método para encontrar o menor elemento da lista
    def encontrar_menor(self):
        
        # Verifica se a lista não está vazia
        if self.lista:
            
            # Retorna o menor elemento da lista usando a função min()
            return min(self.lista)
        
        else:
            
            # Retorna uma mensagem se a lista estiver vazia
            return "A lista está vazia."
        
        
    # - calcular_media(): calcula e retorna a média dos elementos na lista.
    
    # Método para calcular a média dos elementos da lista
    def calcular_media(self):
        
        # Verifica se a lista não está vazia
        if self.lista:
            
            # Retorna a média dos elementos da lista
            return sum(self.lista) / len(self.lista)
        
        else:
            
            # Retorna uma mensagem se a lista estiver vazia
            return "A lista está vazia."
        
        
    # - mostrar_lista(): retorna a lista atual.
    
    # Método para mostrar todos os elementos da lista
    def mostrar_lista(self):
        
        # Retorna o atributo de instância lista, que contém 
        # todos os elementos
        return self.lista

        
"""
2. Implemente uma função menu() que serve como interface do usuário. Essa 
    função deve mostrar um menu com as opções de manipulação e realizar a operação 
    escolhida pelo usuário.
"""
# Define a função chamada menu
def menu():
    
    # Cria uma nova instância da classe ManipuladorDeLista
    manipulador = ManipuladorDeLista()
    
    """
    3. O programa deve continuar rodando e mostrando o menu até que o usuário escolha sair.
    """
    
    # Loop infinito para manter o menu rodando até que o usuário decida sair
    while True:
        
        # Imprime as opções disponíveis no menu
        print("\nEscolha uma opção:")
        print("1. Adicionar elemento")
        print("2. Remover elemento")
        print("3. Encontrar maior elemento")
        print("4. Encontrar menor elemento")
        print("5. Calcular média")
        print("6. Mostrar lista")
        print("7. Sair")
        
        # Solicita que o usuário faça uma escolha e armazena em uma variável
        escolha = input("\nDigite o número da sua escolha: ")
        
        # Verifica se o usuário escolheu a opção 1 para adicionar um elemento
        if escolha == "1":
            
            try:
                # Solicita ao usuário que digite um elemento (int) para adicionar à lista
                elemento = int(input("Digite o elemento que você quer adicionar: "))
                
                # Utiliza o método adicionar_elemento da classe ManipuladorDeLista para adicionar o elemento
                manipulador.adicionar_elemento(elemento)
                
            except ValueError:
                # Captura um ValueError, que ocorre se o usuário não digitar um número inteiro
                print("Entrada inválida. Por favor, insira um número inteiro.")
                
        # Verifica se o usuário escolheu a opção 2 para remover um elemento
        elif escolha == "2":
            
            try:
                
                # Solicita ao usuário que digite um elemento (int) para remover da lista
                elemento = int(input("Digite o elemento que você quer remover: "))
                
                # Utiliza o método remover_elemento da classe ManipuladorDeLista para remover o elemento
                manipulador.remover_elemento(elemento)
                
            except ValueError:
                
                # Captura um ValueError, que ocorre se o usuário não digitar um número inteiro
                print("Entrada inválida. Por favor, insira um número inteiro.")
                
                
        # Verifica se o usuário escolheu a opção 3 para encontrar o maior elemento
        elif escolha == "3":
            
            print(f"O maior elemento é: {manipulador.encontrar_maior()}")
            
        
        # Verifica se o usuário escolheu a opção 4 para encontrar o menor elemento
        elif escolha == "4":
            
            print(f"O menor elemento é: {manipulador.encontrar_menor()}")
            
            
        # Verifica se o usuário escolheu a opção 5 para calcular a média dos elementos
        elif escolha == "5":
            
            print(f"A média dos elementos é: {manipulador.calcular_media()}")
            
                
        # Verifica se o usuário escolheu a opção 6 para mostrar a lista atual
        elif escolha == "6":
            
            print(f"A lista atual é: {manipulador.mostrar_lista()}")
        
        # Verifica se o usuário escolheu a opção 7 para sair do programa
        elif escolha == "7":
            
            print("Saindo do programa. Até mais!")
            
            # Encerra o loop, encerrando assim o programa
            break
            
        # Se o usuário inserir uma opção que não está no menu
        else:
            
            print("Escolha inválida. Tente novamente.")
            
            

# Verifica se este script é o ponto de entrada principal para o programa
if __name__ == "__main__":
    
    # Se for o caso, chama a função menu() para iniciar o programa
    menu()
    
    
