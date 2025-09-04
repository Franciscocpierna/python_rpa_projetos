"""
Estruturas de Dados Lineares
    
        Listas
        
            Lista encadeada
            
                Lista Encadeada Duplamente Ligada: Cada nó aponta para o 
                próximo e para o nó anterior na lista.
                
Uma lista encadeada duplamente ligada (ou lista duplamente encadeada) é 
uma estrutura de dados que consiste em um conjunto de nós onde cada nó 
contém um dado e dois apontadores: um para o próximo nó e outro para o nó 
anterior na sequência. Aqui está um exemplo prático em Python:
                
"""

# Este trecho define a estrutura básica de um nó para uma lista duplamente ligada.

# Definição da classe 'No', que representa um nó em uma lista duplamente ligada.
class No:
    
    # O construtor da classe 'No' é usado para inicializar um novo nó.
    def __init__(self, dado):
        
        # 'dado' é o valor ou informação que o nó irá armazenar. 
        # Pode ser qualquer tipo de dado: int, string, float, etc.
        self.dado = dado
        
        # 'anterior' é uma referência ao nó anterior na lista duplamente ligada.
        # Inicialmente é definido como None, pois no momento da criação do nó, 
        # não sabemos quem será o nó anterior.
        self.anterior = None
        
        # 'proximo' é uma referência ao próximo nó na lista duplamente ligada.
        # Assim como 'anterior', é inicialmente definido como None, pois no momento 
        # da criação do nó, não sabemos quem será o próximo nó.
        self.proximo = None


# Este trecho define a estrutura básica de uma lista duplamente ligada.

# Definição da classe 'ListaDuplamenteLigada', que representa uma lista 
# composta de nós que possuem referências para o nó anterior e para o próximo nó.
class ListaDuplamenteLigada:
    
    # O construtor da classe 'ListaDuplamenteLigada' é utilizado para inicializar 
    # uma nova lista vazia.
    def __init__(self):
        
        # 'cabeca' é uma referência ao primeiro nó (ou nó cabeça) da lista duplamente ligada.
        # Ao criar uma nova lista, a cabeça é inicialmente definida como None, 
        # indicando que a lista está vazia.
        self.cabeca = None
        
        # 'cauda' é uma referência ao último nó (ou nó cauda) da lista duplamente ligada.
        # Semelhante à 'cabeca', 'cauda' também é inicialmente definida como None 
        # quando a lista é criada, indicando que a lista está vazia.
        self.cauda = None


    # Neste segmento, estamos definindo um método para inserir um nó no final de uma 
    # lista duplamente ligada.

    # Método 'inserir_no_final' para adicionar um nó ao final da lista.
    def inserir_no_final(self, dado):
        
        # Criamos um novo nó com o dado fornecido.
        # Neste ponto, 'anterior' e 'proximo' do novo nó são ambos None.
        novo_no = No(dado)
        
        # Verificamos se a lista está vazia (a 'cabeca' é None).
        if not self.cabeca:
            
            # Se a lista estiver vazia, o 'novo_no' se torna tanto a 'cabeca' 
            # quanto a 'cauda' da lista.
            self.cabeca = novo_no
            
            # Atualizamos a referência 'cauda' para apontar para o 'novo_no'.
            self.cauda = novo_no
            
        # Caso a lista não esteja vazia (já tem nós):
        else:
            
            # O nó anterior ao 'novo_no' é o nó atualmente apontado pela 'cauda'.
            novo_no.anterior = self.cauda
            
            # O próximo nó da atual 'cauda' (que é o último nó da lista antes da inserção) 
            # agora aponta para o 'novo_no'.
            self.cauda.proximo = novo_no
            
            # Atualizamos a 'cauda' da lista para ser o 'novo_no', já que ele é o novo 
            # último elemento.
            self.cauda = novo_no


    # Neste segmento, estamos definindo um método para inserir um nó no início de uma 
    # lista duplamente ligada.

    # Método 'inserir_no_inicio' para adicionar um nó ao começo da lista.
    def inserir_no_inicio(self, dado):
        
        # Criamos um novo nó com o dado fornecido.
        # Neste ponto, 'anterior' e 'proximo' do novo nó são ambos None.
        novo_no = No(dado)
        
        # Verificamos se a lista está vazia (a 'cabeca' é None).
        if not self.cabeca:
            
            # Se a lista estiver vazia, o 'novo_no' se torna tanto a 'cabeca' 
            # quanto a 'cauda' da lista.
            self.cabeca = novo_no
            self.cauda = novo_no
            
        # Caso a lista não esteja vazia (já tem nós):
        else:
            
            # O nó seguinte ao 'novo_no' é o atualmente apontado pela 'cabeca'.
            novo_no.proximo = self.cabeca
            
            # O nó anterior da atual 'cabeca' (que é o primeiro nó da lista antes da inserção) 
            # agora aponta para o 'novo_no'.
            self.cabeca.anterior = novo_no
            
            # Atualizamos a 'cabeca' da lista para ser o 'novo_no', já que ele é o novo 
            # primeiro elemento.
            self.cabeca = novo_no


    # Neste segmento, estamos definindo um método para imprimir todos os nós de uma 
    # lista duplamente ligada do início ao fim.

    # Método 'imprimir_lista' para exibir os elementos da lista do início ao fim.
    def imprimir_lista(self):
        
        # Começamos com o primeiro nó (cabeca) da lista.
        no_atual = self.cabeca
        
        # Continuamos imprimindo e movendo para o próximo nó até chegarmos ao final da lista.
        # O loop vai executar enquanto 'no_atual' não for None.
        while no_atual:
            
            # Aqui, imprimimos o dado contido no nó atual.
            # Usamos 'end=' <-> '' para formatar a saída, mostrando que os nós são bidirecionais.
            print(no_atual.dado, end=' <-> ')
            
            # Movemos para o próximo nó na lista.
            no_atual = no_atual.proximo
        
        # Após imprimir todos os nós, imprimimos "None" para indicar o final da lista.
        print("None")


# Neste segmento, estamos inicializando uma lista duplamente ligada e inserindo elementos 
# nela. Após isso, imprimimos a lista.

# Primeiro, criamos uma instância da classe 'ListaDuplamenteLigada', o que nos dá uma lista vazia.
lista = ListaDuplamenteLigada()

# Usando o método 'inserir_no_final', inserimos o número 1 no final da lista. 
# Como a lista estava vazia, este se torna o único elemento da lista (tanto a 'cabeca' 
# quanto a 'cauda' apontam para este elemento).
lista.inserir_no_final(1)

# Da mesma forma, inserimos o número 2 no final da lista. 
# O novo nó é adicionado após o nó anterior e se torna a nova 'cauda' da lista.
lista.inserir_no_final(2)

# Continuamos inserindo, desta vez o número 3.
lista.inserir_no_final(3)

# Aqui, em vez de adicionar no final, usamos 'inserir_no_inicio' para adicionar o número 0 no início da lista. 
# Este novo nó se torna a 'cabeca' da lista.
lista.inserir_no_inicio(0)

# Continuamos inserindo, desta vez o número 4.
lista.inserir_no_final(4)

# Por fim, chamamos o método 'imprimir_lista' para visualizar os elementos da lista duplamente ligada.
# Como inserimos os números na ordem 1, 2, 3 e depois 0 no início, a saída será: 0 <-> 1 <-> 2 <-> 3 <-> None
lista.imprimir_lista()




"""
Neste exemplo:

    A classe No representa um nó na lista duplamente ligada. Ele tem três 
    atributos: dado, que armazena o valor do nó; anterior, que aponta para o 
    nó anterior na lista; e proximo, que aponta para o próximo nó.

    A classe ListaDuplamenteLigada representa a lista duplamente ligada. Ela tem 
    dois atributos: cabeca, que aponta para o primeiro nó da lista, e cauda, que 
    aponta para o último nó.

    O método inserir_no_final adiciona um nó ao final da lista.

    O método inserir_no_inicio adiciona um nó no início da lista.

    O método imprimir_lista imprime todos os elementos da lista, seguindo as 
    ligações entre os nós, do início ao fim.
"""
print()
