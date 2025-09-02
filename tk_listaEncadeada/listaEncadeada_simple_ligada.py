"""
Estruturas de Dados

    Estruturas de Dados Lineares
    
        Listas
        
            Lista encadeada
            
                Lista Encadeada Simplesmente Ligada: Cada nó aponta para o próximo nó na lista.
                Lista Encadeada Duplamente Ligada: Cada nó aponta para o próximo e para o nó anterior na lista.
                Lista Encadeada Circular Simplesmente Ligada: O último nó da lista aponta para o primeiro nó.
                Lista Encadeada Circular Duplamente Ligada: Semelhante à circular simplesmente ligada, mas cada nó também tem um ponteiro para o nó anterior.

            Operações Básicas

                Inserção: Adicionar um novo nó à lista.
                
                    No início
                    No final
                    Após um nó específico
                    
                Deleção: Remover um nó da lista.
                
                    Do início
                    Do final
                    Com base em um valor específico
                    
                Busca: Encontrar um nó com um valor específico.
                Acesso: Acessar elementos em uma posição específica.
                Tamanho: Encontrar o tamanho da lista.

            
        Pilhas
            
            Conceitos Básicos

                Definição e Estrutura: Entender o que é uma pilha e como ela é organizada.
                Last In, First Out (LIFO): Compreensão do princípio fundamental que rege as operações de uma pilha.

            Operações Fundamentais

                Push: Adicionar um elemento ao topo da pilha.
                Pop: Remover e retornar o elemento do topo da pilha.
                Peek/Top: Ver o elemento do topo sem removê-lo.
                isEmpty: Verificar se a pilha está vazia.
                getSize: Obter o número de elementos na pilha.

            
            
        Filas
        
            Conceitos Básicos

                Definição e Estrutura: Compreender o que é uma fila e como ela é organizada.
                First In, First Out (FIFO): Entender o princípio básico que rege as operações de uma fila.

            Operações Fundamentais

                Enqueue: Adicionar um elemento ao final da fila.
                Dequeue: Remover e retornar o elemento da frente da fila.
                Front: Ver o elemento da frente sem removê-lo.
                Rear/Back: Ver o último elemento sem removê-lo.
                isEmpty: Verificar se a fila está vazia.
                getSize: Obter o número de elementos na fila.

            Variações e Tipos Especiais

                Fila de Prioridades: Elementos são removidos da fila com base em uma chave de prioridade.
                Deque (Double-Ended Queue): Estruturas que podem ser manipuladas em ambas as extremidades.
                Filas Duplamente Terminadas (Double-Ended Queues)
                Fila Bloqueadora: Usada em programação concorrente, onde as operações de enfileiramento e desenfileiramento podem ser bloqueadas.

 
"""
print()
"""
Estruturas de Dados Lineares
        
        Listas
            
            Lista encadeada
            
                Lista Encadeada Simplesmente Ligada: Cada nó aponta para o próximo nó na lista.
            
Lista encadeada

As listas encadeadas são estruturas de dados lineares onde cada 
elemento é uma parte separada que contém dados e um link para o 
próximo elemento na sequência. Uma lista encadeada é frequentemente 
usada quando você quer ter a capacidade de inserir e remover elementos 
de qualquer ponto na lista sem realocar ou mover outros elementos. Isso 
é diferente das listas (arrays) em Python, que são dinâmicos, mas ainda 
assim precisam realocar às vezes para realizar inserções e remoções.

Uma lista encadeada simplesmente ligada é uma estrutura de dados 
composta por nós onde cada nó contém um dado e uma referência 
(ou apontador) para o próximo nó na sequência. 

Abaixo está um exemplo prático em Python para demonstrar uma lista 
encadeada simplesmente ligada:
"""

# Definição da estrutura básica de um nó

class No:
    
    # O construtor inicializa um nó com um dado e um ponteiro para 
    # o próximo nó como None (nulo)
    def __init__(self, dado):
        
        # Valor do nó
        self.dado = dado
        
        # Referência para o próximo nó na lista; começa como None
        self.proximo = None

# Aqui estamos definindo uma nova classe chamada 'ListaEncadeada'. Esta classe 
# representará nossa lista encadeada.
class ListaEncadeada:
    
    # Este é o construtor da classe. Ele é chamado automaticamente quando criamos
    # uma nova instância da classe.
    def __init__(self):
        
        # 'self.cabeca' é um atributo da classe que representa o primeiro nó (ou elemento) da lista encadeada.
        # Ao criar uma nova lista, ela estará vazia, então 'self.cabeca' é inicializado como 'None'.
        # 'None' em Python é um valor especial que indica a ausência de valor ou nulidade.
        self.cabeca = None
        
    # Este método é parte da classe ListaEncadeada e sua função é adicionar 
    # um novo nó no final da lista encadeada.
    def inserir_no_final(self, dado):

        # Criamos uma nova instância da classe No, passando o 'dado' como argumento.
        # Isso resulta na criação de um novo nó com o valor fornecido e onde o 
        # atributo 'proximo' é inicialmente 'None'.
        novo_no = No(dado)

        # Verificamos se a lista encadeada está vazia. Fazemos isso ao verificar 
        # se o atributo 'cabeca' é 'None'.
        if self.cabeca is None:

            # Se a lista estiver vazia (a cabeça é None), o novo nó se torna a cabeça da lista.
            # Isso significa que o novo nó é agora o primeiro (e único) elemento da lista.
            self.cabeca = novo_no
            return
        
        # Se chegarmos até aqui, significa que a lista não está vazia.
        # Então, começamos na cabeça da lista e navegamos através dos nós até encontrar o último nó.
        ultimo_no = self.cabeca
        
        # Continuamos movendo para o próximo nó até encontrarmos um nó que 
        # não tenha um próximo nó (último nó)
        while ultimo_no.proximo:
            
            ultimo_no = ultimo_no.proximo
            
            
        # Configuramos o próximo nó do último nó para o novo nó, efetivamente 
        # adicionando o novo nó ao final da lista
        ultimo_no.proximo = novo_no
        
        
    # Método que pertence à classe ListaEncadeada. Ele é responsável por 
    # imprimir todos os elementos da lista encadeada.
    def imprimir_lista(self):

        # 'no_atual' é uma variável temporária utilizada para percorrer a lista. 
        # Ela começa apontando para a "cabeça" da lista, que é o primeiro nó.
        no_atual = self.cabeca

        # A estrutura de repetição 'while' é usada para percorrer a lista. Ela 
        # continuará enquanto 'no_atual' estiver apontando para um nó (ou seja, não for None).
        while no_atual:

            # Imprime o valor (dado) do nó atual. 'end=' -> '' é usado para que 
            # o próximo print não comece em uma nova linha.
            print(no_atual.dado, end=' -> ')

            # Move 'no_atual' para o próximo nó na lista. Se o nó atual for o 
            # último nó, 'no_atual.proximo' será None e o loop 'while' terminará.
            no_atual = no_atual.proximo

        # Após percorrer toda a lista, imprimimos "None" para indicar o final da lista encadeada. 
        # É uma convenção comum para mostrar que a lista terminou e não há mais nós a seguir.
        print("None")
        
        
# Criação de uma nova instância da classe ListaEncadeada.
# Neste ponto, a lista está vazia (sua cabeça é 'None').
lista = ListaEncadeada()

# Adicionando o valor '1' ao final da lista encadeada.
# Como a lista está vazia, o valor '1' se tornará o primeiro elemento (ou cabeça) da lista.
lista.inserir_no_final(1)

# Adicionando o valor '2' ao final da lista encadeada.
# Neste ponto, o valor '1' já está na lista, então '2' será inserido após ele.
lista.inserir_no_final(2)

# Adicionando o valor '3' ao final da lista encadeada.
# Agora, '3' será inserido após os valores '1' e '2'.
lista.inserir_no_final(3)

# Adicionando o valor '4' ao final da lista encadeada.
# '4' será o último elemento inserido, vindo após '1', '2', e '3'.
lista.inserir_no_final(4)

# Chamando o método 'imprimir_lista' da instância 'lista'.
# Este método imprimirá todos os elementos da lista em sequência, 
# seguidos por uma seta (->), indicando a ligação para o próximo nó.
# Como '4' é o último elemento, após ele, será impresso 'None' para indicar o final da lista.
lista.imprimir_lista()  # Saída esperada: 1 -> 2 -> 3 -> 4 -> None


"""
A classe No define um nó da lista encadeada. Ela tem dois membros: dado, 
que armazena o dado do nó, e proximo, que é uma referência para o próximo 
nó na lista.

A classe ListaEncadeada define a lista encadeada. Ela tem um membro chamado 
cabeca que aponta para o primeiro nó da lista.

O método inserir_no_final insere um novo elemento no final da lista.

O método imprimir_lista imprime todos os elementos da lista, seguindo as 
ligações entre os nós.
"""
print()