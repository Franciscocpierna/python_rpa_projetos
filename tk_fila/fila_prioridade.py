"""
Filas
        
        Variações e Tipos Especiais

            Fila de Prioridades: Elementos são removidos da fila com base 
            em uma chave de prioridade.
                

Uma fila de prioridades é uma estrutura de dados especializada onde
o elemento com a mais alta (ou mais baixa, dependendo da implementação) 
prioridade é removido da fila antes dos outros elementos. Em Python, o 
módulo heapq fornece funções para implementar filas de prioridades usando 
listas.

Vamos criar uma implementação simples de uma fila de prioridades onde os 
elementos são tuplas. A primeira posição da tupla é o valor da prioridade 
e a segunda é o elemento em si. Assim, a fila será organizada com base nos 
valores de prioridade.
"""

# Exemplo Prático: Fila de Prioridades

# Importamos a biblioteca 'heapq', que fornece funções para trabalhar com heaps binários. 
# Heaps são frequentemente usados para implementar filas de prioridade.
import heapq

# Definição da classe FilaDePrioridades.
class FilaDePrioridades:

    # Método de inicialização da classe.
    # Quando um objeto dessa classe é instanciado, este método é chamado.
    def __init__(self):
        
        # Inicializamos a propriedade 'fila' como uma lista vazia.
        # Esta lista armazenará os elementos da fila de prioridades.
        self.fila = []
        
    # Método para adicionar um elemento à fila de prioridades.
    def enqueue(self, prioridade, elemento):
        
        # Usamos a função 'heappush' da biblioteca 'heapq' para inserir o elemento na fila.
        # A função garante que o elemento seja inserido na posição correta do heap (ou fila de prioridades) 
        # com base na sua prioridade.
        # A prioridade e o elemento são passados como uma tupla, onde 'prioridade' é o primeiro elemento 
        # e 'elemento' é o segundo.
        # Isso garante que ao adicionar ou remover itens do heap, eles serão ordenados com base na prioridade.
        heapq.heappush(self.fila, (prioridade, elemento))
        
        
    # Método para remover e retornar o elemento com a maior prioridade.
    # Como estamos usando um min-heap com a biblioteca 'heapq', o elemento 
    # com a menor prioridade será removido primeiro.
    def dequeue(self):
        
        # Verificamos se a fila não está vazia.
        if not self.isEmpty():
            
            # Se não estiver vazia, usamos a função 'heappop' da biblioteca 'heapq' 
            # para remover e retornar o elemento com a menor prioridade (primeiro elemento do heap).
            # Como estamos armazenando o elemento e sua prioridade como uma tupla, 
            # e queremos retornar apenas o elemento (e não sua prioridade), 
            # acessamos o segundo item da tupla usando '[1]'.
            return heapq.heappop(self.fila)[1]
        
        else:
            
            # Se a fila estiver vazia, retornamos uma mensagem indicando isso.
            return "A fila está vazia!"
    
    # Método para verificar se a fila está vazia.
    # Retorna True se a fila estiver vazia e False caso contrário.
    def isEmpty(self):
        
        # Comparamos o tamanho da fila com 0.
        # Se o tamanho da fila for 0, significa que está vazia.
        return len(self.fila) == 0
    
    
    # Método para obter o número de elementos na fila.
    # Retorna o tamanho da fila.
    def getSize(self):
        
        # Usamos a função 'len' para obter o número de elementos na lista 'fila'.
        return len(self.fila)


# Testando a classe

# Criamos uma instância da classe FilaDePrioridades.
# Isso nos dá uma fila de prioridades vazia que podemos usar.
fila_p = FilaDePrioridades()

# Usamos o método enqueue para adicionar tarefas à fila de prioridades.
# A prioridade é dada pelo primeiro argumento e a tarefa pelo segundo.
# Quanto menor o número, maior é a prioridade.
# Portanto, a tarefa "Tarefa urgente 1" com prioridade 1 tem a maior prioridade.
fila_p.enqueue(3, "Tarefa normal 1")  # Tarefa com prioridade média.
fila_p.enqueue(1, "Tarefa urgente 1")  # Tarefa com a maior prioridade.
fila_p.enqueue(2, "Tarefa importante 1")  # Tarefa com prioridade entre as outras.
fila_p.enqueue(3, "Tarefa normal 2")  # Outra tarefa com prioridade média.
fila_p.enqueue(1, "Tarefa urgente 2")  # Outra tarefa com a maior prioridade.
fila_p.enqueue(2, "Tarefa importante 2")  # Outra tarefa com prioridade entre as outras.

# Usamos o método dequeue para remover e imprimir tarefas da fila de prioridades.
# As tarefas são removidas em ordem de prioridade.
# Como estamos usando um min-heap, a tarefa com a menor prioridade (número mais baixo) é removida primeiro.
print(fila_p.dequeue())  # Esperado: Tarefa urgente 1 (pois tem prioridade 1, que é a mais alta).
print(fila_p.dequeue())  # Esperado: Tarefa urgente 2 (pois também tem prioridade 1).
print(fila_p.dequeue())  # Esperado: Tarefa importante 1 (poi2, a prós tem prioridade xima mais alta após as tarefas urgentes).
print(fila_p.dequeue())  # Esperado: Tarefa importante 2 (pois também tem prioridade 2).
print(fila_p.dequeue())  # Esperado: Tarefa normal 1 (pois tem prioridade 3, que é a mais baixa das restantes).
print(fila_p.dequeue())  # Esperado: Tarefa normal 2 (pois também tem prioridade 3).