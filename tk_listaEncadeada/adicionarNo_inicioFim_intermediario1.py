"""
Exercício Lista Encadeada com Menu Interativo


Funcionalidades a serem implementadas:

    Inserção no início: Adiciona um novo nó no início da lista.
    
    Inserção no final: Adiciona um novo nó no final da lista.
    
    Inserção após um nó específico: Permite ao usuário escolher um valor 
    existente (chave) na lista e inserir um novo nó imediatamente após ele.
    
    Imprimir lista: Imprime todos os elementos da lista em ordem.

Menu Interativo:

O programa deve exibir um menu com as seguintes opções:

    1. Inserir no início
    2. Inserir no final
    3. Inserir após um nó específico
    4. Imprimir lista
    5. Sair
"""

# Solução

# Declaração da classe 'No', que servirá como elemento base da nossa lista encadeada.
class No:
    
    # Método inicializador da classe.
    def __init__(self, dado):
        
        # Atributo 'dado' que irá armazenar a informação ou valor 
        # que desejamos guardar neste nó.
        self.dado = dado
        
        # Atributo 'proximo' é inicialmente definido como None. Este atributo será utilizado para referenciar
        # o próximo nó da lista encadeada. Quando criamos um novo nó, ele não está conectado a nenhum outro,
        # por isso 'proximo' é inicializado como None.
        self.proximo = None
        
# Declaração da classe 'ListaEncadeada', que representa a nossa lista encadeada.
class ListaEncadeada:
    
    # Método inicializador da classe.
    def __init__(self):
        
        # Atributo 'cabeca' serve como ponto de partida ou entrada para nossa lista.
        # Inicialmente, a lista está vazia, portanto 'cabeca' é definida como None.
        self.cabeca = None

    # Método que permite inserir um novo nó no início da lista encadeada.
    def inserir_no_inicio(self, dado):
        
        # Criamos um novo nó usando o valor 'dado' que é passado como argumento.
        novo_no = No(dado)
        
        # O próximo elemento após o 'novo_no' será a atual 'cabeca' da lista.
        # Se a lista estiver vazia, 'novo_no.proximo' será simplesmente None.
        novo_no.proximo = self.cabeca
        
        # Redefinimos a 'cabeca' da lista para ser o 'novo_no', movendo assim a antiga 'cabeca' 
        # para a segunda posição na lista.
        self.cabeca = novo_no
        
        
    # Método para inserir um novo nó no final da lista encadeada.
    def inserir_no_final(self, dado):

        # Criamos um novo nó com o valor 'dado' que é fornecido como argumento.
        novo_no = No(dado)

        # Verificamos se a lista encadeada está vazia (ou seja, se 'cabeca' é None).
        if not self.cabeca:
            
            # Se a lista estiver vazia, simplesmente definimos a 'cabeca' como o 'novo_no'.
            self.cabeca = novo_no
            
            # Retornamos do método, pois já inserimos o nó e não há mais nada a ser feito.
            return

        # Se a lista não estiver vazia, começamos da 'cabeca' para encontrar o último nó.
        temp = self.cabeca
        
        # Usamos um loop 'while' para percorrer a lista até que 'proximo' de um nó seja None.
        # Isto indica que encontramos o final da lista.
        while temp.proximo:
            temp = temp.proximo

        # Uma vez que o loop termina, 'temp' é o último nó da lista.
        # Definimos 'proximo' do último nó para ser o 'novo_no', inserindo assim o 'novo_no' no final da lista.
        temp.proximo = novo_no
        
    
    # Método para inserir um novo nó após um nó específico identificado por 'chave'.
    def inserir_apos_no(self, chave, dado):

        # Inicializamos 'temp' para a 'cabeca' da lista encadeada.
        temp = self.cabeca

        # Percorremos a lista encadeada com um loop 'while' para encontrar o nó cujo dado é igual a 'chave'.
        # A condição 'temp' garante que não ultrapassaremos o final da lista, enquanto 
        # 'temp.dado != chave' procura a chave.
        while temp and temp.dado != chave:
            temp = temp.proximo

        # Se 'temp' é None após o loop, isso significa que a chave não foi encontrada na lista.
        if not temp:
            print(f"O nó com dado {chave} não foi encontrado.")
            
            # Terminamos a execução do método, pois não podemos inserir após um nó que não existe.
            return

        # Se encontramos a chave, criamos um novo nó com o valor 'dado'.
        novo_no = No(dado)

        # Definimos 'proximo' do novo nó para o 'proximo' do nó 'temp' (ou seja, o nó 
        # após o nó com dado igual a 'chave').
        # Isso nos permite inserir 'novo_no' entre 'temp' e o nó que originalmente vinha após 'temp'.
        novo_no.proximo = temp.proximo

        # Atualizamos 'proximo' do nó 'temp' para apontar para 'novo_no', completando assim a inserção.
        temp.proximo = novo_no
    
    
    # Método para imprimir todos os elementos da lista encadeada em ordem.
    def imprimir_lista(self):

        # Começamos com o primeiro nó da lista, que é a 'cabeca'.
        temp = self.cabeca

        # Enquanto 'temp' não for None (isso é, enquanto não chegarmos ao final da lista),
        # continuamos a percorrer a lista e imprimir cada nó.
        while temp:

            # Imprimimos o valor ('dado') de 'temp' e utilizamos 'end' para adicionar 
            # a seta '->' após cada nó, em vez de uma nova linha.
            print(temp.dado, end=' -> ')

            # Movemos para o próximo nó na lista.
            temp = temp.proximo

        # Depois de sair do loop, imprimimos "None" para indicar o final da lista encadeada.
        print("None")
        
        
# Verifica se este script está sendo executado como o script principal
if __name__ == "__main__":
    
    # Cria uma instância da classe ListaEncadeada chamada 'lista'
    lista = ListaEncadeada()

    # Loop infinito para manter o menu interativo em execução até que o usuário decida sair
    while True:
        
        # Imprime uma linha em branco para separação visual no console
        print("\nMenu:")
        
        # As próximas linhas exibem as opções disponíveis no menu interativo
        print("1 - Inserir no início")
        print("2 - Inserir no final")
        print("3 - Inserir após um nó específico")
        print("4 - Imprimir lista")
        print("5 - Sair")
        
        # Solicita ao usuário que insira sua escolha de ação no menu
        escolha = input("Escolha uma opção: ")


        # Verifica a escolha do usuário 
        if escolha == "1":
            
            # Solicita ao usuário que insira o valor do novo nó
            dado = input("Digite o valor do novo nó: ")
            
            # Chama o método inserir_no_inicio da instância da lista, passando o dado fornecido pelo usuário
            lista.inserir_no_inicio(dado)
            
        # Verifica se o usuário escolheu a segunda opção
        elif escolha == "2":
            
            # Solicita ao usuário que insira o valor do novo nó
            dado = input("Digite o valor do novo nó: ")
            
            # Chama o método inserir_no_final da instância da lista, passando o dado fornecido pelo usuário
            lista.inserir_no_final(dado)

        # Verifica se o usuário escolheu a terceira opção
        elif escolha == "3":
            
            # Solicita ao usuário que insira o valor do nó após o qual ele deseja inserir um novo nó
            chave = input("Digite o valor do nó após o qual você deseja inserir: ")
            
            # Solicita ao usuário que insira o valor do novo nó
            dado = input("Digite o valor do novo nó: ")
            
            # Chama o método inserir_apos_no da instância da lista, 
            # passando a chave e o dado fornecidos pelo usuário
            lista.inserir_apos_no(chave, dado)

        # Verifica se o usuário escolheu a quarta opção
        elif escolha == "4":
            
            # Chama o método imprimir_lista da instância da lista para exibir todos os nós na lista
            lista.imprimir_lista()
            
        # Verifica se o usuário escolheu a quinta opção, que é para sair do menu
        elif escolha == "5":
            
            # Informa ao usuário que o programa está encerrando
            print("Saindo...")
            
            # Encerra o loop while, encerrando assim a execução do menu interativo
            break
            
        
        # Se a escolha do usuário não for nenhuma das opções acima (1-5)
        else:
            
            # Informa ao usuário que a opção escolhida é inválida e solicita que tente novamente
            print("Opção inválida. Tente novamente.")
