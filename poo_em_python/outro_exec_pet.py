"""
Exercício Pet


No mesmo exercício anterior, adicione um menu interativo com as seguintes informações:

    1. Definir o nome do pet
    2. Definir a idade do pet
    3. Definir o peso do pet
    4. Exibir informações do pet
    5. Sair

"""

#Solução

# 1. Crie uma classe chamada Pet.
# Definindo a classe Pet
class Pet:
    
    """
    2. A classe deve ter os seguintes atributos privados: _nome, _idade e _peso.
        - Utilize métodos "getters" para cada um desses atributos.
        - Utilize métodos "setters" para cada um desses atributos. 
    """
    # Método construtor para inicializar os atributos quando um objeto da classe é criado
    def __init__(self):
        
        # Inicializa o atributo '_nome' como uma string vazia. 
        # O prefixo "_" indica que é um atributo protegido.
        self._nome = ""
        
        # Inicializa o atributo '_idade' como 0. 
        # O prefixo "_" indica que é um atributo protegido.
        self._idade = 0
        
        # Inicializa o atributo '_peso' como 0.0. 
        # O prefixo "_" indica que é um atributo protegido.
        self._peso = 0.0
        
    # Método "getter" para o nome, permite obter o valor do atributo '_nome'
    def get_nome(self):
        
        return self._nome
    
    """
    Os "setters" devem conter as seguintes validações:
            - O nome deve ser uma string e não pode ser vazio.
            - A idade deve ser um número inteiro e deve ser maior ou igual a 0.
            - O peso deve ser um número flutuante e deve ser maior que 0.
    """

    # Método "setter" para o nome, permite definir um novo valor para o atributo '_nome'
    def set_nome(self, novo_nome):
        
        """
        Os "setters" devem conter as seguintes validações:
            - O nome deve ser uma string e não pode ser vazio.
        """
        # Verifica se o novo_nome é uma string e se não está vazio
        if isinstance(novo_nome, str) and novo_nome != "":
            
            # Atualiza o valor do atributo '_nome'
            self._nome = novo_nome
            
        else:
            
            # Imprime uma mensagem de erro se o nome fornecido não for válido
            print("Nome inválido.")
            
    # Método "getter" para a idade, permite obter o valor do atributo '_idade'
    def get_idade(self):
        
        return self._idade
    
    
    # Método "setter" para a idade, permite definir um novo valor para o atributo '_idade'
    def set_idade(self, nova_idade):
        
        """
            Os "setters" devem conter as seguintes validações:
            - A idade deve ser um número inteiro e deve ser maior ou igual a 0.
        """
        # Verifica se a nova_idade é um inteiro e se é maior ou igual a 0
        if isinstance(nova_idade, int) and nova_idade >= 0:
            
            # Atualiza o valor do atributo '_idade'
            self._idade = nova_idade
            
        else:
            
            # Imprime uma mensagem de erro se a idade fornecida não for válida
            print("Idade inválida.")
            
    # ---------------------------------------------
    
    # Método "getter" para o peso, permite obter o valor do atributo '_peso'
    def get_peso(self):
        
        return self._peso

    # Método "setter" para o peso, permite definir um novo valor para o atributo '_peso'
    def set_peso(self, novo_peso):
        
        """
        Os "setters" devem conter as seguintes validações:
                - O peso deve ser um número flutuante e deve ser maior que 0.
        """
        
        # Verifica se o novo_peso é um número flutuante e se é maior que 0
        if isinstance(novo_peso, float) and novo_peso > 0:
            
            # Atualiza o valor do atributo '_peso'
            self._peso = novo_peso
            
        else:
            
            # Imprime uma mensagem de erro se o peso fornecido não for válido
            print("Peso inválido.")
            
            
      
    # 3. Adicione um método exibir_info() que mostre as informações do pet.
    def exibir_info(self):
        
        print(f"Nome: {self._nome}")
        print(f"Idade: {self._idade}")
        print(f"Peso: {self._peso} kg")
        
        
# Função para mostrar o menu de opções
def mostrar_menu():
    
    print("\n---- Menu de Gerenciamento de Pet ----")
    print("1. Definir o nome do pet")
    print("2. Definir a idade do pet")
    print("3. Definir o peso do pet")
    print("4. Exibir informações do pet")
    print("5. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    return escolha

# Função principal que coordena a execução do programa.
def main():
    
    # Cria uma nova instância (objeto) da classe Pet.
    # O objeto representará um pet específico.
    meu_pet = Pet()
    
    # Inicia um loop infinito para exibir o menu e interagir com o usuário.
    while True:
        
        # Chama a função 'mostrar_menu()' para exibir as opções do menu e
        # captura a escolha do usuário como uma string.
        escolha = mostrar_menu()
        
        # Verifica se o usuário escolheu a opção 1 para definir o nome do pet.
        if escolha == '1':
            
            # Solicita que o usuário digite o nome do pet.
            nome = input("Digite o novo nome do pet: ")
            
            # Utiliza o método 'set_nome' para atualizar o nome do pet.
            meu_pet.set_nome(nome)
            
        # Verifica se o usuário escolheu a opção 2 para definir a idade do pet.
        elif escolha == '2':
            
            # Utiliza um bloco try-except para capturar erros na conversão de tipos.
            try:
                
                # Solicita que o usuário digite a idade do pet e tenta converter para int.
                idade = int(input("Digite a nova idade do pet: "))
                
                # Utiliza o método 'set_idade' para atualizar a idade do pet.
                meu_pet.set_idade(idade)
                
            # Se a conversão falhar, um ValueError será lançado.
            except ValueError:
                
                # Informa ao usuário que o valor inserido não é um número inteiro válido.
                print("Idade inválida. Por favor, insira um número inteiro.")
                
        # Verifica se o usuário escolheu a opção 3 para definir o peso do pet.
        elif escolha == '3':
            
            # Utiliza um bloco try-except para capturar erros na conversão de tipos.
            try:
                
                # Solicita que o usuário digite o peso do pet e tenta converter para float.
                peso = float(input("Digite o novo peso do pet: "))
                
                # Utiliza o método 'set_peso' para atualizar o peso do pet.
                meu_pet.set_peso(peso)
                
            # Se a conversão falhar, um ValueError será lançado.
            except ValueError:
                
                # Informa ao usuário que o valor inserido não é um número válido.
                print("Peso inválido. Por favor, insira um número.")
                
        # Verifica se o usuário escolheu a opção 4 para exibir as informações do pet.
        elif escolha == '4':
            
            # Chama o método 'exibir_info' para mostrar as informações atuais do pet.
            meu_pet.exibir_info()
            
        # Verifica se o usuário escolheu a opção 5 para sair do programa.
        elif escolha == '5':
            
            # Exibe uma mensagem informando que o programa será encerrado.
            print("Saindo do programa...")
            
            # Encerra o loop, encerrando assim o programa.
            break
            
        # Caso o usuário não escolha uma opção válida, uma mensagem de erro é exibida.
        else:
            
            print("Opção inválida. Tente novamente.")
            

# Chama a função 'main' para iniciar a execução do programa.
main()