"""
Filas
        
        Variações e Tipos Especiais
        
            Deque (Double-Ended Queue): Estruturas que podem ser 
            manipuladas em ambas as extremidades.
                

Um deque (pronuncia-se "deck" e é abreviação de "double-ended queue") é uma 
estrutura de dados abstrata que generaliza uma fila, para a qual as adições e 
remoções de itens podem ser realizadas nas extremidades dianteira e traseira. 

Em Python, a biblioteca collections fornece a implementação de deque que suporta 
a adição e remoção eficiente de elementos de ambas as extremidades em tempo 
aproximado constante.

Exemplo Prático: Deque (Double-Ended Queue)

Vamos criar um pequeno programa para demonstrar as operações fundamentais de um deque:
"""

# Importamos a classe deque do módulo collections. 
# deque é uma estrutura de dados tipo lista de dupla extremidade que suporta 
# operações de adicionar e remover em ambas as extremidades em O(1).
from collections import deque

# Definimos uma classe chamada DequeDemo.
class DequeDemo:
    
    # Este é o método construtor da classe. Ele é chamado automaticamente 
    # quando uma nova instância da classe é criada.
    def __init__(self):
        
        # Aqui, inicializamos uma instância vazia do deque e a armazenamos 
        # como uma variável de instância chamada dq. 
        # Isso significa que cada instância da classe DequeDemo terá seu próprio deque.
        self.dq = deque()
        
    
    # Este é um método para adicionar um elemento à frente do deque.
    # Ele pega um único argumento - o elemento que você deseja adicionar.
    def addFront(self, elemento):
        
        # Usamos o método appendleft do deque para adicionar o elemento à frente.
        # Isso efetivamente coloca o novo elemento no início do deque.
        self.dq.appendleft(elemento)
        
        
    # Este é um método para adicionar um elemento à traseira do deque.
    # Semelhante ao método addFront, ele pega um único argumento.
    def addRear(self, elemento):
        
        # Aqui, usamos o método append do deque para adicionar o elemento ao final.
        # Isso coloca o novo elemento no final do deque.
        self.dq.append(elemento)
        
        
    # Este é um método para remover e retornar o elemento da frente do deque.
    def removeFront(self):
        
        # Aqui, verificamos se o deque está vazio usando o método auxiliar isEmpty.
        # O método isEmpty retorna True se o deque estiver vazio e False caso contrário.
        if not self.isEmpty():
            
            # Se o deque não estiver vazio, usamos o método popleft do deque para 
            # remover e retornar o elemento da frente.
            return self.dq.popleft()
        
        else:
            
            # Se o deque estiver vazio, retornamos uma mensagem indicando que o deque está vazio.
            return "O deque está vazio!"
        
        
    # Este é um método para remover e retornar o elemento da traseira do deque.
    def removeRear(self):
        
        # Mais uma vez, verificamos primeiro se o deque está vazio
        if not self.isEmpty():
            
            # Se o deque não estiver vazio, usamos o método pop do deque para 
            # remover e retornar o último elemento (ou elemento da traseira).
            return self.dq.pop()
        
        else:
            
            # Se o deque estiver vazio, retornamos a mesma mensagem me antes
            return "O deque está vazio!"
        
        
    # Este é um método para ver o elemento da frente do deque sem removê-lo.
    def peekFront(self):
        
        # Verificamos se o deque está vazio.
        if not self.isEmpty():
            
            # Se não estiver vazio, retornamos o primeiro elemento do deque 
            # sem removê-lo. O índice [0] é usado para acessar o primeiro elemento.
            return self.dq[0]
        
        else:
            
            # Se estiver vazio, retornamos a mensagem indicativa.
            return "O deque está vazio!"
        
    
    # Este é um método para ver o elemento da traseira do deque sem removê-lo.
    def peekRear(self):
        
        # Primeiro, verificamos se o deque está vazio usando o método auxiliar isEmpty.
        # Este método retorna True se o deque estiver vazio e False caso contrário.
        if not self.isEmpty():
            
            # Se o deque não estiver vazio, retornamos o último elemento 
            # (ou elemento da traseira) sem removê-lo. O índice [-1] é 
            # usado para acessar o último elemento da sequência em Python.
            return self.dq[-1]
        
        else:
            
            # Se o deque estiver vazio, retornamos uma mensagem indicando essa condição.
            return "O deque está vazio!"
        
    # Este método verifica se o deque está vazio.
    def isEmpty(self):
        
        # Utilizamos a função len() para obter o número de elementos no deque.
        # Se esse número for 0, significa que o deque está vazio e o método 
        # retornará True. Caso contrário, retornará False.
        return len(self.dq) == 0
    
    
    # Este é um método para obter o número total de elementos atualmente no deque.
    def size(self):
        
        # Utilizamos a função len() para obter e retornar o número de elementos no deque.
        return len(self.dq)
    
    
# Testando a classe

# Cria uma instância do DequeDemo, inicializando um deque vazio.
demo = DequeDemo()

# Adiciona o elemento "Frente 1" à frente do deque.
demo.addFront("Frente 1")

# Adiciona o elemento "Traseira 1" à traseira do deque.
demo.addRear("Traseira 1")

# Adiciona o elemento "Frente 2" à frente do deque. 
# Portanto, ele se torna o novo elemento da frente.
demo.addFront("Frente 2")

# Adiciona o elemento "Traseira 2" à traseira do deque.
demo.addRear("Traseira 2")

# Verifica e imprime o elemento da frente do deque.
print(demo.peekFront())  # Esperado: Frente 2

# Verifica e imprime o elemento da traseira do deque.
print(demo.peekRear())   # Esperado: Traseira 2


# Remove e retorna o elemento da frente do deque.
print(demo.removeFront())  # Esperado: Frente 2


# Remove e retorna o elemento da traseira do deque.
print(demo.removeRear())   # Esperado: Traseira 2

# Estado atual do deque após remoção é ["Frente 1", "Traseira 1"]


# Verifica e imprime novamente o elemento da frente.
print(demo.peekFront())  # Esperado: Frente 1


# Verifica e imprime novamente o elemento da traseira.
print(demo.peekRear())   # Esperado: Traseira 1


# Imprime o tamanho atual do deque.
print(demo.size())  # Esperado: 2


# Verificando se o deque está vazio.
print("O deque está vazio?", demo.isEmpty())  # Esperado: False, porque ainda existem elementos no deque.

# Removendo todos os elementos restantes.
print(demo.removeFront())  # Esperado: Frente 1
print(demo.removeRear())   # Esperado: Traseira 1

# Verificando se o deque está agora vazio após remover todos os elementos.
print("O deque está vazio?", demo.isEmpty())  # Esperado: True