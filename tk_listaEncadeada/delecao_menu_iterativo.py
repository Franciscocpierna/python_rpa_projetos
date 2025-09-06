"""
Exercício Deleção em Lista Encadeada com Menu Interativo

Neste exercício, você irá implementar e interagir com uma lista 
encadeada através de um menu, focando nas operações de deleção de nós.

Funcionalidades a serem implementadas:

    Deleção do início: Remove o nó do início da lista.
    Deleção do final: Remove o nó do final da lista.
    Deleção por valor: Permite ao usuário fornecer um valor, e o nó com esse 
        valor é removido da lista.

Menu Interativo:

O programa deverá exibir um menu com as seguintes opções:

    1. Deletar do início
    2. Deletar do final
    3. Deletar por valor
    4. Imprimir lista
    5. Sair
"""

#Solução

# Definindo a classe "No" que representa um nó em uma lista encadeada.
class No:
    
    # O construtor da classe "__init__" é chamado quando um novo objeto No é criado.
    # Ele recebe um parâmetro "dado" que representa o valor armazenado neste nó.
    def __init__(self, dado):
        
        # O atributo "dado" deste nó recebe o valor passado como parâmetro.
        self.dado = dado
        
        # O atributo "proximo" é inicializado como None, indicando que
        # este nó não está ligado a outro nó inicialmente.
        self.proximo = None

# Definindo a classe "ListaEncadeada" que representa a própria lista encadeada.
class ListaEncadeada:
    
    # O construtor da classe "__init__" é chamado quando um novo objeto 
    # ListaEncadeada é criado.
    def __init__(self):
        
        # O atributo "cabeca" da lista é inicializado como None, indicando 
        # que a lista está vazia.
        self.cabeca = None
        
        
    # Definindo um método chamado "deletar_do_inicio" na classe ListaEncadeada.
    def deletar_do_inicio(self):
        
        # Verificando se a lista está vazia, ou seja, se a cabeça (self.cabeca) está 
        # definida como None.
        if not self.cabeca:
            
            # Se a lista estiver vazia, exibimos uma mensagem informando que não 
            # há nada para deletar.
            print("Lista vazia. Não há o que deletar.")
            
            # Retornamos imediatamente para encerrar a função sem fazer mais nada.
            return
        
        # Se a lista não estiver vazia, atualizamos a cabeça (self.cabeca) para apontar 
        # para o próximo nó na lista.
        self.cabeca = self.cabeca.proximo
        
    
    # Definindo um método chamado "deletar_do_final" na classe ListaEncadeada.
    def deletar_do_final(self):
        
        # Verificando se a lista está vazia, ou seja, se a cabeça (self.cabeca) está 
        # definida como None.
        if not self.cabeca:
            
            # Se a lista estiver vazia, exibimos uma mensagem informando que não 
            # há nada para deletar.
            print("Lista vazia. Não há o que deletar.")
            
            # Retornamos imediatamente para encerrar a função sem fazer mais nada.
            return
        
        # Verificando se há apenas um elemento na lista (a cabeça aponta diretamente 
        # para esse elemento).
        if not self.cabeca.proximo:
            
            # Se houver apenas um elemento, removemos esse elemento, definindo a cabeça como None.
            self.cabeca = None
            
            # Retornamos imediatamente para encerrar a função.
            return
        
        # Se houver mais de um elemento na lista, precisamos encontrar o penúltimo elemento.
        # Criamos uma variável temporária "temp" para percorrer a lista a partir da cabeça.
        temp = self.cabeca
        
        # Entramos em um loop que percorre a lista até que "temp" seja o penúltimo elemento.
        while temp.proximo.proximo:
            
            temp = temp.proximo
            
        # Quando encontramos o penúltimo elemento, definimos o próximo dele como None para remover o último elemento.
        temp.proximo = None
        
        
    # Definindo um método chamado "deletar_por_valor" na classe ListaEncadeada.
    def deletar_por_valor(self, chave):
        
        # Verificando se a lista está vazia, ou seja, se a cabeça (self.cabeca) está 
        # definida como None.
        if not self.cabeca:
            
            # Se a lista estiver vazia, exibimos uma mensagem informando que não há 
            # nada para deletar.
            print("Lista vazia. Não há o que deletar.")
            
            # Retornamos imediatamente para encerrar a função sem fazer mais nada.
            return
        
        # Verificando se o valor a ser deletado está na cabeça da lista.
        if self.cabeca.dado == chave:
            
            # Se estiver na cabeça, removemos a cabeça e atualizamos a cabeça 
            # para o próximo elemento da lista.
            self.cabeca = self.cabeca.proximo
            
            # Retornamos imediatamente para encerrar a função.
            return
        
        # Se o valor não estiver na cabeça, criamos uma variável 
        # temporária "temp" para percorrer a lista a partir da cabeça.
        temp = self.cabeca
        
        # Entramos em um loop que percorre a lista até encontrar o nó 
        # que contém o valor desejado ou até o final da lista.
        while temp.proximo and temp.proximo.dado != chave:
            
            temp = temp.proximo
            
        # Se chegarmos ao final da lista sem encontrar o valor, exibimos 
        # uma mensagem informando que o valor não foi encontrado.
        if not temp.proximo:
            
            print(f"O valor {chave} não foi encontrado na lista.")
            
            # Retornamos imediatamente para encerrar a função.
            return
        
        # Se encontrarmos o nó com o valor desejado, ajustamos 
        # as referências para remover o nó da lista.
        temp.proximo = temp.proximo.proximo
        
    
    # Definindo um método chamado "imprimir_lista" na classe ListaEncadeada.
    def imprimir_lista(self):
        
        # Criamos uma variável temporária "temp" e inicializamos com a cabeça da lista.
        temp = self.cabeca
        
        # Entramos em um loop que percorre a lista a partir da cabeça até o último elemento.
        while temp:
            
            # Imprimimos o valor de dados (temp.dado) do nó atual, seguido por uma seta "->".
            print(temp.dado, end=' -> ')
            
            # Atualizamos "temp" para apontar para o próximo nó na lista.
            temp = temp.proximo
            
        # Quando chegamos ao final da lista (temp é None), imprimimos "None" para indicar o fim da lista.
        print("None")
        
        
# Verifica se o arquivo atual é o principal (está sendo executado diretamente) 
# e não importado por outro arquivo
if __name__ == "__main__":
    
    # Cria uma nova instância (objeto) da classe ListaEncadeada
    lista = ListaEncadeada()
    
    # Inicializa a lista encadeada com três nós contendo os 
    # valores "A", "B" e "C" respectivamente
    lista.cabeca = No("A")  # Define o primeiro nó com valor "A"
    lista.cabeca.proximo = No("B")  # Define o nó seguinte ao primeiro nó com valor "B"
    lista.cabeca.proximo.proximo = No("C")  # Define o terceiro nó com valor "C"
    lista.cabeca.proximo.proximo.proximo = No("D")  # Define o quarto nó com valor "D"
    lista.cabeca.proximo.proximo.proximo.proximo = No("E")  # Define o quinto nó com valor "E"

    # Loop infinito para apresentar o menu interativo ao usuário
    while True:
        
        # Exibe o menu com as opções disponíveis para o usuário
        print("\nMenu:")
        print("1 - Deletar do início")
        print("2 - Deletar do final")
        print("3 - Deletar por valor")
        print("4 - Imprimir lista")
        print("5 - Sair")

        # Solicita ao usuário que escolha uma opção do menu
        escolha = input("Escolha uma opção: ")


        # Verifica se a escolha do usuário foi "1" para deletar o primeiro nó da lista
        if escolha == "1":
            lista.deletar_do_inicio()

        # Caso a escolha tenha sido "2", deleta o último nó da lista
        elif escolha == "2":
            lista.deletar_do_final()

        # Se a escolha foi "3", solicita ao usuário o valor do nó que ele deseja deletar
        elif escolha == "3":
            valor = input("Digite o valor do nó a ser deletado: ")
            
            # Chama o método para deletar o nó com o valor fornecido
            lista.deletar_por_valor(valor)

        # Se a escolha foi "4", imprime todos os nós da lista
        elif escolha == "4":
            lista.imprimir_lista()

        # Se a escolha foi "5", sai do programa
        elif escolha == "5":
            print("Saindo...")
            
            # Encerra o loop, terminando a execução do programa
            break

        # Caso a opção escolhida não esteja entre as disponíveis, informa ao 
        # usuário que a opção é inválida
        else:
            print("Opção inválida. Tente novamente.")
