"""
Estruturas de Dados Lineares
    
        Listas
        
            Lista encadeada
            
                Lista Encadeada Circular Duplamente Ligada: Semelhante 
                à circular simplesmente ligada, mas cada nó também tem um 
                ponteiro para o nó anterior.
"""

# Definição da classe No, que representa o nó da lista circular duplamente ligada
class No:
    
    # Construtor da classe No
    def __init__(self, dado):
        self.dado = dado         # Atributo 'dado' armazena o valor do nó
        self.proximo = None      # Atributo 'proximo' aponta para o próximo nó na lista; inicia como None
        self.anterior = None     # Atributo 'anterior' aponta para o nó anterior na lista; inicia como None


# Definição da classe ListaCircularDuplamenteLigada, que representa a lista propriamente dita
class ListaCircularDuplamenteLigada:
    
    # Construtor da classe ListaCircularDuplamenteLigada
    def __init__(self):
        
        # Atributo 'cabeca' aponta para o primeiro nó da lista; inicia como None
        self.cabeca = None


    def inserir(self, dado):
        
        # Criação de um novo nó com o dado passado como argumento
        novo_no = No(dado)

        # Verificação se a cabeça (primeiro nó) da lista está vazia
        if not self.cabeca:
            
            # Se a lista estiver vazia, o novo nó se torna a cabeça
            self.cabeca = novo_no

            # Como é uma lista circular, o próximo e o anterior do novo nó apontam para ele mesmo
            novo_no.proximo = novo_no  # Aponta para si mesmo
            novo_no.anterior = novo_no  # Aponta para si mesmo
            
        else:
            
            # Se a lista não estiver vazia, começamos a partir da cabeça
            temp = self.cabeca

            # Percorremos a lista até encontrar o último nó (que tem o 'proximo' 
            # apontando para a cabeça)
            while temp.proximo != self.cabeca:
                temp = temp.proximo

            # O próximo do último nó encontrado apontará para o novo nó
            temp.proximo = novo_no

            # O anterior do novo nó aponta para o nó encontrado (anteriormente último nó da lista)
            novo_no.anterior = temp

            # Como é uma lista circular, o próximo do novo nó aponta para a cabeça da lista
            novo_no.proximo = self.cabeca

            # E o anterior da cabeça da lista agora aponta para o novo nó, completando o ciclo
            self.cabeca.anterior = novo_no


    def imprimir_lista(self):
        
        # Inicializa a variável no_atual para começar a partir da cabeça da lista
        no_atual = self.cabeca

        # Inicializa um contador para acompanhar quantos nós foram impressos
        cont = 0

        # Chama a função tamanho (que precisa ser definida) para determinar quantos nós há na lista
        # Adiciona 1 ao tamanho para garantir que vamos imprimir um ciclo completo da lista circular
        n = self.tamanho() + 1

        # Continua imprimindo enquanto não imprimir todos os nós + 1 (para completar o ciclo)
        while cont < n:
            
            # Imprime o dado do nó atual e indica com '<->' que está ligado ao próximo nó
            print(no_atual.dado, end=' <-> ')

            # Move para o próximo nó
            no_atual = no_atual.proximo

            # Incrementa o contador
            cont += 1

        # Ao final da impressão, indica com '...' que a lista é circular e volta para o início
        print("...")  # Indica que a lista continua em loop


    def tamanho(self):
        
        # Inicializa um contador com o valor 1, pois a lista tem pelo menos um nó (a cabeça)
        cont = 1

        # Começa a verificação a partir da cabeça da lista
        no_atual = self.cabeca

        # Enquanto o próximo nó não for a cabeça (o que indicaria o final da lista circular)
        while no_atual.proximo != self.cabeca:
            
            # Incrementa o contador
            cont += 1

            # Move para o próximo nó
            no_atual = no_atual.proximo

        # Retorna o número total de nós na lista
        return cont


# Inicialização de uma nova lista circular duplamente ligada
lista = ListaCircularDuplamenteLigada()

# Inserção do elemento "A" na lista. 
# Como é o primeiro elemento, ele apontará para si mesmo tanto no 
# atributo 'proximo' quanto no 'anterior'.
lista.inserir("A")

# Impressão da lista. Como o elemento "A" é o único na lista, 
# a saída mostrará que ele aponta para si mesmo, indicando o comportamento 
# circular da lista.
lista.imprimir_lista()  # Saída esperada: A <-> A <-> ...

# Inserção do elemento "B" na lista.
# O elemento "B" será inserido após o "A". 
# O elemento "A" apontará para "B" no atributo 'proximo' e
# "B" apontará para "A" no atributo 'anterior'.
lista.inserir("B")

# Impressão da lista. Agora, temos dois elementos. 
# A saída mostrará o elemento "A" apontando para "B" e, em seguida, 
# "B" apontando novamente para "A", indicando o comportamento circular.
lista.imprimir_lista()  # Saída esperada: A <-> B <-> A <-> ...

# Inserção do elemento "C" na lista.
# O elemento "C" será inserido após o "B".
# O elemento "B" apontará para "C" no atributo 'proximo' e "C" apontará 
# para "B" no atributo 'anterior'.
# Além disso, "C" apontará para "A" no atributo 'proximo', e "A" apontará 
# para "C" no atributo 'anterior', fechando o ciclo da lista.
lista.inserir("C")

# Impressão da lista. A saída mostrará os três elementos e a estrutura circular da lista.
lista.imprimir_lista()  # Saída esperada: A <-> B <-> C <-> A <-> ...


"""
Neste exemplo:

    Cada No tem três atributos: dado, proximo e anterior.
    
    Quando inserimos o primeiro item na lista, os apontadores proximo 
    e anterior do nó apontam para si mesmos, formando um pequeno círculo.
    
    Para cada novo nó inserido, seu apontador proximo aponta para a cabeca 
    da lista, e seu apontador anterior aponta para o último nó na lista. Além 
    disso, o apontador proximo do que era o último nó na lista antes da inserção 
    apontará para este novo nó e o apontador anterior da cabeca da lista apontará 
    para este novo nó, garantindo que a lista permaneça circular e duplamente ligada.
    
    Para imprimir a lista e demonstrar sua circularidade, imprimimos os nós até retornar 
    à cabeca da lista, com um adicional para mostrar a ligação de volta ao início.

Esta estrutura é particularmente útil quando se quer navegar em ambas as direções 
em um ciclo, como, por exemplo, em uma playlist de reprodução circular onde se pode 
avançar ou retroceder entre as faixas.
"""
print()