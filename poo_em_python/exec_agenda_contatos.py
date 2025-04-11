"""
Exercício Agenda de Contatos - Programação Orientada a Objetos

Objetivo:

O objetivo deste exercício é criar uma aplicação de gerenciamento de 
agenda de contatos usando Programação Orientada a Objetos (POO) em Python.

Descrição:

Você deve criar uma classe chamada Contato que irá representar um contato 
individual na agenda. Cada contato deve ter três atributos: nome, telefone e email.

Além disso, você deve criar uma classe chamada Agenda que irá gerenciar os 
contatos. Esta classe deve conter métodos para adicionar, remover, listar e buscar contatos.

A aplicação deve também possuir um menu interativo para o usuário, permitindo 
que ele execute as seguintes ações:

    1. Adicionar um novo contato.
    2. Remover um contato existente.
    3. Listar todos os contatos na agenda.
    4. Buscar um contato pelo nome.
    5. Sair da aplicação.

Instruções:

    1. Comece definindo a classe Contato com os atributos e métodos necessários.
    2. Em seguida, defina a classe Agenda que contém uma lista de objetos da classe Contato.
    3. Implemente os métodos de Agenda para adicionar, remover, listar e buscar contatos.
    4. Crie uma função menu para gerenciar a interação com o usuário.
    5. No método main (ponto de entrada do programa), instancie um objeto da classe 
       Agenda e comece o loop do menu para o usuário.
"""

#Solução

"""
Você deve criar uma classe chamada Contato que irá representar um contato 
individual na agenda. Cada contato deve ter três atributos: nome, telefone e email.
"""
# Definindo a classe Contato para modelar um contato individual
class Contato:

    """
        1. Comece definindo a classe Contato com os atributos e métodos necessários.
    """
    # Método construtor para inicializar os atributos do objeto Contato
    def __init__(self, nome, telefone, email):
        
        # Inicializa o atributo 'nome' com o valor passado como argumento
        self.nome = nome
        
        # Inicializa o atributo 'telefone' com o valor passado como argumento
        self.telefone = telefone
        
        # Inicializa o atributo 'email' com o valor passado como argumento
        self.email = email
        
"""
Além disso, você deve criar uma classe chamada Agenda que irá gerenciar os 
contatos. Esta classe deve conter métodos para adicionar, remover, listar e buscar contatos.
"""

# Definindo a classe Agenda para gerenciar uma lista de contatos
class Agenda:

    """
        2. Em seguida, defina a classe Agenda que contém uma lista de objetos da classe Contato.
    """
    # Método construtor para inicializar o atributo que irá armazenar os contatos
    def __init__(self):
        
        # Inicializa o atributo 'contatos' como uma lista vazia
        # Este atributo será usado para armazenar objetos da classe Contato
        self.contatos = []
        
    """
        3. Implemente os métodos de Agenda para adicionar, remover, listar e buscar contatos.
    """
    # Método para adicionar um novo objeto Contato à lista de contatos
    def adicionar_contato(self, contato):
        
        # Utiliza o método append da lista para adicionar o novo contato ao 
        # final da lista de contatos
        self.contatos.append(contato)
        
    # Método para remover um contato com base em seu nome
    def remover_contato(self, nome):

        # Loop for para iterar por cada objeto 'contato' na lista de contatos 'self.contatos'
        for contato in self.contatos:

            # Verifica se o atributo 'nome' do objeto 'contato' é igual 
            # ao nome fornecido como argumento
            print("contato",contato)# imprime o objeto contato
            if contato.nome == nome:

                # Se encontrado, remove o objeto 'contato' da lista 'self.contatos'
                self.contatos.remove(contato)

                # Retorna True para indicar que o contato foi removido com sucesso
                return True

        # Retorna False para indicar que o contato não foi encontrado na lista
        return False
    
    # Método para buscar um contato pelo nome
    def buscar_contato(self, nome):

        # Loop for que itera sobre cada objeto 'contato' na lista 'self.contatos'
        for contato in self.contatos:

            # Verifica se o atributo 'nome' do objeto 'contato' é igual ao nome fornecido como argumento
            if contato.nome == nome:

                # Se um contato é encontrado, retorna o objeto 'contato'
                return contato

        # Se o loop termina sem encontrar um contato, retorna None
        return None

    # Método para listar todos os contatos
    def listar_contatos(self):

        # Retorna a lista completa de contatos armazenados em 'self.contatos'
        return self.contatos
    

# Função de menu para interação do usuário
def menu():
    
    # Cria uma nova instância da classe Agenda
    agenda = Agenda()
    
    # Loop infinito para manter o menu rodando
    while True:
        
        """
        A aplicação deve também possuir um menu interativo para o usuário, permitindo 
        que ele execute as seguintes ações:

            1. Adicionar um novo contato.
            2. Remover um contato existente.
            3. Listar todos os contatos na agenda.
            4. Buscar um contato pelo nome.
            5. Sair da aplicação.
        """
        
        """
            4. Crie uma função menu para gerenciar a interação com o usuário.
        """
        # Exibe as opções do menu para o usuário
        print("\n1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Listar Contatos")
        print("4. Buscar Contato")
        print("5. Sair")
        
        # Coleta a escolha do usuário
        escolha = input("\nEscolha uma opção: ")
        
        # Executa a ação correspondente à escolha do usuário
        if escolha == "1":
            
            # Solicita as informações do novo contato
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            
            # Cria uma nova instância da classe Contato com as informações fornecidas
            novo_contato = Contato(nome, telefone, email)
            
            # Usa o método adicionar_contato da instância da classe Agenda para adicionar o novo contato
            agenda.adicionar_contato(novo_contato)
            
            # Exibe uma mensagem informando que o contato foi adicionado com sucesso
            print(f"Contato {nome} adicionado com sucesso!")
            
        # Continuação da função de menu
        elif escolha == "2":

            # Solicita o nome do contato a ser removido
            nome = input("Digite o nome do contato a ser removido: ")

            # Chama o método remover_contato e verifica se o contato foi removido
            if agenda.remover_contato(nome):
                
                print("Contato removido com sucesso!")
                
            else:
                
                print("Contato não encontrado.")
                
        # Continuação da função de menu
        elif escolha == "3":

            # Exibe uma mensagem indicando que os contatos serão listados
            print("Listando todos os contatos:")

            # Percorre a lista de contatos e os exibe
            for contato in agenda.listar_contatos():
                
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")
                
        # Continuação da função de menu
        elif escolha == "4":

            # Solicita o nome do contato a ser buscado
            nome = input("Digite o nome do contato a ser buscado: ")

            # Busca o contato pelo nome
            contato = agenda.buscar_contato(nome)

            # Verifica se o contato foi encontrado e o exibe
            if contato:
                
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")
            
            else:
                print("Contato não encontrado.")
                
        # Continuação da função de menu
        elif escolha == "5":

            # Exibe uma mensagem indicando o término do programa e encerra o loop
            print("Saindo do programa.")
            
            break
            
        else:

            # Exibe uma mensagem de erro para uma opção inválida
            print("Opção inválida.")
            

"""
    5. No método main (ponto de entrada do programa), instancie um objeto da classe 
           Agenda e comece o loop do menu para o usuário.
"""
# Ponto de entrada do programa, inicia a função de menu
# A linha 'if __name__ == "__main__":' garante que o bloco de código a seguir será executado
# apenas se este script Python for o programa principal em execução, e não quando for 
# importado como um módulo em outro script.
if __name__ == "__main__":
    
    # Chama a função 'menu', que inicia o loop de interface com o usuário para o aplicativo.
    # É aqui que todas as interações com o usuário começam.
    menu()
    