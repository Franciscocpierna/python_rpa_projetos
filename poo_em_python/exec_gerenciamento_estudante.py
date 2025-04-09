"""
Exercício: Sistema de Gerenciamento de Estudantes

Descrição

Neste exercício, você irá criar uma aplicação simples para gerenciar informações 
sobre estudantes. O sistema deve ser capaz de adicionar novos estudantes, atualizar 
suas notas, visualizar informações de estudantes específicos e listar todos os estudantes.

Funcionalidades

    1. Adicionar um novo estudante.
    2. Atualizar a nota de um estudante existente.
    3. Visualizar informações de um estudante.
    4. Listar todos os estudantes.
    5. Sair do programa.

Detalhes da Implementação

    Utilize Programação Orientada a Objetos para estruturar seu código.
    Crie uma classe Estudante com atributos nome, idade e nota.
    Crie métodos getters e setters apropriados para cada atributo.
    Utilize um menu para interagir com o usuário e executar as diferentes funcionalidades.
"""

#Solução

# Definindo a classe Estudante
class Estudante:
    
    # Método construtor para inicializar os atributos nome, idade e nota
    def __init__(self, nome, idade, nota):
        
        # Inicializa o atributo 'nome' com o valor passado como argumento
        self.nome = nome
        
        # Inicializa o atributo 'idade' com o valor passado como argumento
        self.idade = idade
        
        # Inicializa o atributo 'nota' com o valor passado como argumento
        self.nota = nota
        
    # Método getter para o atributo 'nome'
    def get_nome(self):
        
        # Retorna o valor do atributo 'nome'
        return self.nome
    
    # Método setter para o atributo 'nome'
    def set_nome(self, nome):
        
        # Atualiza o valor do atributo 'nome' com o novo valor passado como argumento
        self.nome = nome
        
    # Método getter para o atributo 'idade'
    def get_idade(self):
        
        # Retorna o valor do atributo 'idade'
        return self.idade

    
    # Método setter para o atributo 'idade'
    def set_idade(self, idade):
        
        # Atualiza o valor do atributo 'idade' com o novo valor passado como argumento
        self.idade = idade
        
        
    # Método getter para o atributo 'nota'
    def get_nota(self):
        
        # Retorna o valor do atributo 'nota'
        return self.nota
    
    # Método setter para o atributo 'nota'
    def set_nota(self, nota):
        
        # Atualiza o valor do atributo 'nota' com o novo valor passado como argumento
        self.nota = nota
        

# Função para exibir o menu e interagir com o usuário
def menu():
    
    # Lista vazia chamada 'estudantes' para armazenar objetos da classe Estudante
    estudantes = []
    
    # Inicia um loop infinito para manter o menu rodando
    while True:
        
        # Exibe as opções do menu para o usuário
        print("\n1. Adicionar Estudante")
        print("2. Atualizar Nota")
        print("3. Visualizar Estudante")
        print("4. Listar Estudantes")
        print("5. Sair")
        
        # Pede para o usuário escolher uma das opções e armazena a escolha na variável 'escolha'
        escolha = input("\nEscolha uma opção: ")
        
        # Verifica se a opção escolhida é "1" para Adicionar Estudante
        if escolha == "1":
            
            # Solicita o nome do estudante
            nome = input("Digite o nome do estudante: ")
            
            # Solicita a idade do estudante e converte para inteiro
            idade = int(input("Digite a idade do estudante: "))
            
            # Solicita a nota do estudante e converte para float
            nota = float(input("Digite a nota do estudante: "))
            
            # Cria um novo objeto da classe Estudante usando os dados inseridos
            novo_estudante = Estudante(nome, idade, nota)
            
            # Adiciona o novo objeto estudante à lista 'estudantes'
            estudantes.append(novo_estudante)
            
            # Exibe uma mensagem informando que o estudante foi adicionado com sucesso
            print(f"Estudante {nome} adicionado com sucesso!")
     
            
        # Verifica se a opção escolhida é "2" para Atualizar Nota
        elif escolha == "2":
            
            # Solicita o nome do estudante cuja nota será atualizada
            nome = input("Digite o nome do estudante para atualizar a nota: ")

            # Itera sobre cada objeto 'estudante' na lista 'estudantes'
            for estudante in estudantes:
                
                # Verifica se o nome do estudante na lista é igual ao nome inserido pelo usuário
                
                if estudante.get_nome() == nome:
                    
                    # Solicita a nova nota e a converte para float
                    nova_nota = float(input("Digite a nova nota: "))
                    
                    # Atualiza a nota do estudante usando o método setter
                    estudante.set_nota(nova_nota)
                    
                    # Exibe uma mensagem informando que a nota foi atualizada com sucesso
                    print("Nota atualizada com sucesso!")
                    
                    # Sai do loop 'for' já que o estudante foi encontrado e a nota atualizada
                    break
                    
            # O bloco 'else' será executado se o loop 'for' não encontrar um estudante com o nome inserido
            else:
                
                # Exibe uma mensagem informando que o estudante não foi encontrado
                print("Estudante não encontrado.")
                
        # Verifica se a opção escolhida é "3" para Visualizar Estudante
        elif escolha == "3":
            
            # Solicita o nome do estudante cujas informações serão visualizadas
            nome = input("Digite o nome do estudante para visualizar as informações: ")

            # Itera sobre cada objeto 'estudante' na lista 'estudantes'
            for estudante in estudantes:
                
                # Verifica se o nome do estudante na lista é igual ao nome inserido pelo usuário
                
                if estudante.get_nome() == nome:
                    
                    # Exibe as informações do estudante usando os métodos getters
                    print(f"Nome: {estudante.get_nome()}, Idade: {estudante.get_idade()}, Nota: {estudante.get_nota()}")
                    
                    # Sai do loop 'for' já que o estudante foi encontrado e suas informações foram exibidas
                    break
                    
            # O bloco 'else' será executado se o loop 'for' não encontrar um estudante com o nome inserido
            else:
                
                # Exibe uma mensagem informando que o estudante não foi encontrado
                print("Estudante não encontrado.")
                
        # Verifica se a opção escolhida é "4" para listar todos os estudantes
        elif escolha == "4":
            
            # Exibe uma mensagem introdutória para a listagem de estudantes
            print("Listando todos os estudantes:")

            # Itera sobre cada objeto 'estudante' na lista 'estudantes'
            for estudante in estudantes:
                
                # Exibe as informações de cada estudante usando os métodos getters
                print(f"Nome: {estudante.get_nome()}, Idade: {estudante.get_idade()}, Nota: {estudante.get_nota()}")

        # Verifica se a opção escolhida é "5" para sair do programa
        elif escolha == "5":
            
            # Exibe uma mensagem informando que o programa será encerrado
            print("Saindo do programa.")
            
            # Interrompe o loop do menu, efetivamente encerrando o programa
            break
            
            
        # Verifica se a opção escolhida não corresponde a nenhuma das anteriores
        else:
            
            # Exibe uma mensagem informando que a opção escolhida é inválida
            print("Opção inválida.")
                    

                

# Verifica se este script é o ponto de entrada para a execução do programa
if __name__ == "__main__":
    
    # Chama a função 'menu' para iniciar o programa
    menu()
    