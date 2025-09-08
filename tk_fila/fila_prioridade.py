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


"""
Exercício: Implementação de Fila de Prioridades

Objetivo: Implementar uma fila de prioridades em que 
os elementos são removidos com base em uma chave de prioridade.

Contexto: Em muitos sistemas, algumas tarefas ou ações têm prioridades 
diferentes. Por exemplo, em um sistema de atendimento ao cliente, certos 
tickets podem ter prioridade alta devido à urgência do problema, enquanto 
outros podem ser de baixa prioridade. Uma fila de prioridades pode ajudar a 
gerenciar essas tarefas efetivamente.

Instruções:

    1. Implemente uma classe chamada FilaDePrioridades.
    2. A classe deve ter as seguintes operações:
    
        - enqueue(prioridade, elemento): Adicione um elemento à fila de 
            prioridades. O parâmetro prioridade é um número (pode ser inteiro 
            ou flutuante) que define a prioridade do elemento. O parâmetro elemento 
            é o dado a ser armazenado na fila.
        
        - dequeue(): Remova e retorne o elemento com a mais alta 
            prioridade (o menor valor de prioridade). Se a fila estiver 
            vazia, retorne uma mensagem indicando isso.
            
        - peek(): Veja o elemento com a mais alta prioridade sem removê-lo. 
            Se a fila estiver vazia, retorne uma mensagem indicando isso.
            
        - isEmpty(): Retorne True se a fila estiver vazia e False caso 
            contrário.
        
        - getSize(): Retorne o número de elementos na fila.
    
    3. Depois de implementar a classe, crie uma instância da fila de prioridades 
        e execute as seguintes ações:
        
        - Adicione três elementos à fila com diferentes prioridades.
        - Veja o elemento de mais alta prioridade sem removê-lo.
        - Remova o elemento de mais alta prioridade.
        - Veja o tamanho da fila.
        
"""

# Solução

# Importamos o módulo heapq. 
# Ele fornece funções para transformar listas em heaps e implementar filas de prioridades. 
# Heaps são estruturas binárias que permitem fácil recuperação e deleção do menor elemento.
import heapq

# 1. Implemente uma classe chamada FilaDePrioridades.
# Esta classe representa nossa estrutura de dados de fila de prioridades.

class FilaDePrioridades:
    
    # O construtor da classe.
    # Quando uma nova instância da FilaDePrioridades é criada, este método é chamado.
    def __init__(self):
        
        # Dentro do construtor, inicializamos a variável de instância self.fila como uma lista vazia.
        # Esta lista será usada para armazenar os elementos da fila de prioridades.
        self.fila = []
    
    """
    2. A classe deve ter as seguintes operações:
    
        - enqueue(prioridade, elemento): Adicione um elemento à fila de 
            prioridades. O parâmetro prioridade é um número (pode ser inteiro 
            ou flutuante) que define a prioridade do elemento. O parâmetro elemento 
            é o dado a ser armazenado na fila.
        
        - dequeue(): Remova e retorne o elemento com a mais alta 
            prioridade (o menor valor de prioridade). Se a fila estiver 
            vazia, retorne uma mensagem indicando isso.
            
        - peek(): Veja o elemento com a mais alta prioridade sem removê-lo. 
            Se a fila estiver vazia, retorne uma mensagem indicando isso.
            
        - isEmpty(): Retorne True se a fila estiver vazia e False caso 
            contrário.
        
        - getSize(): Retorne o número de elementos na fila.
    """
    
    # Método para adicionar um elemento à fila de prioridades.
    # Este método aceita dois argumentos: 
    # 1. prioridade - que indica a prioridade do elemento,
    # 2. elemento - que é o item real que você deseja armazenar na fila.
    def enqueue(self, prioridade, elemento):
        
        # A função heapq.heappush é usada para adicionar um item ao heap.
        # Em uma fila de prioridades, o heap garante que o item com a menor prioridade 
        # (número menor) esteja sempre na frente.
        # Portanto, ao adicionar um item, passamos a lista (self.fila) e uma tupla contendo a prioridade e o elemento.
        heapq.heappush(self.fila, (prioridade, elemento))
        
        
    # Método para remover e retornar o elemento com a mais alta prioridade da fila.
    def dequeue(self):
        
        # Primeiro, verificamos se a fila não está vazia usando o método auxiliar self.isEmpty().
        if not self.isEmpty():
            
            # Se a fila não estiver vazia, usamos heapq.heappop para remover e retornar o elemento 
            # com a menor prioridade (que será o primeiro elemento na lista, devido à natureza do heap).
            # Como cada item na fila é uma tupla (prioridade, elemento), 
            # usamos [1] para retornar apenas o elemento, sem a prioridade.
            return heapq.heappop(self.fila)[1]  
        
        else:
            
            # Se a fila estiver vazia, retornamos uma mensagem indicando isso.
            return "A fila está vazia!"
        
    
    # Método para verificar se a fila está vazia.
    # Retorna True se a fila estiver vazia e False caso contrário.
    def isEmpty(self):
        
        # Verificamos se o tamanho da fila é 0. 
        # len(self.fila) retorna o número de itens na fila.
        # Se o tamanho for 0, isso significa que a fila está vazia.
        return len(self.fila) == 0
    
    
    # Método para visualizar (ou espiar) o elemento com a mais alta prioridade da fila, 
    # sem realmente removê-lo.
    def peek(self):
        
        # Primeiro, verificamos se a fila não está vazia usando o método auxiliar self.isEmpty().
        if not self.isEmpty():
            
            # Se a fila não estiver vazia, acessamos o primeiro elemento usando self.fila[0]. 
            # Como cada item na fila é uma tupla (prioridade, elemento), 
            # usamos [1] para retornar apenas o elemento, sem a prioridade.
            return self.fila[0][1]
        
        else:
            
            # Se a fila estiver vazia, retornamos uma mensagem indicando isso.
            return "A fila está vazia!"
        
        
   # Método para obter o número de elementos presentes na fila.
    def getSize(self):
        
        # Retornamos o tamanho da fila usando a função len().
        # Isso nos dará o número de itens atualmente presentes na fila.
        return len(self.fila)
    
# Testando a classe


"""
3. Depois de implementar a classe, crie uma instância da fila de prioridades 
        e execute as seguintes ações:
        
        - Adicione três elementos à fila com diferentes prioridades.
        - Veja o elemento de mais alta prioridade sem removê-lo.
        - Remova o elemento de mais alta prioridade.
        - Veja o tamanho da fila.
"""

# Instancie um objeto da classe FilaDePrioridades.
fila_p = FilaDePrioridades()

# Adicione três tarefas à fila de prioridades.
# A função enqueue aceita dois argumentos: prioridade e elemento.
# As tarefas são adicionadas com suas respectivas prioridades. 
# A prioridade 1 é mais alta do que 2, e 2 é mais alta do que 3.
fila_p.enqueue(3, "Tarefa normal 1")
fila_p.enqueue(1, "Tarefa urgente 1")
fila_p.enqueue(2, "Tarefa importante 1")

# Use o método peek para visualizar o elemento com a mais alta prioridade na fila, 
# sem realmente removê-lo. Neste caso, seria "Tarefa urgente 1" 
# porque foi adicionado com a prioridade mais alta (1).
print("Elemento com a mais alta prioridade na fila:", fila_p.peek())

# Use o método dequeue para remover e retornar o elemento com a mais alta prioridade.
# Neste caso, "Tarefa urgente 1" é removido e retornado porque tem a prioridade mais alta.
print("Remover e retornar o elemento com a mais alta prioridade:", fila_p.dequeue())  


# Use o método getSize para verificar quantos elementos ainda estão presentes na fila.
# Após a remoção da "Tarefa urgente 1", ainda devem restar duas tarefas na fila.
print("Verificar quantos elementos ainda estão presentes:", fila_p.getSize())

# Vamos adicionar mais alguns elementos para testes adicionais
fila_p.enqueue(1, "Tarefa urgente 2")
fila_p.enqueue(3, "Tarefa normal 2")

# Veja qual é o próximo elemento com a mais alta prioridade sem removê-lo.
print("Elemento com a mais alta prioridade após adicionar mais tarefas:", fila_p.peek())  # Esperado: Tarefa urgente 2

# Remova o elemento com a mais alta prioridade novamente.
print("Remover e retornar o elemento com a mais alta prioridade após adicionar mais tarefas:", fila_p.dequeue())  # Esperado: Tarefa urgente 2

# Verifique o tamanho da fila após a remoção.
print("Tamanho da fila após remover tarefas adicionais:", fila_p.getSize())  # Esperado: 3

# Vamos verificar se o método isEmpty retorna False quando a fila não está vazia
print("A fila está vazia?", fila_p.isEmpty())  # Esperado: False

# Remova todos os elementos restantes
fila_p.dequeue()
fila_p.dequeue()
fila_p.dequeue()

# Verifique se o método isEmpty retorna True quando a fila está vazia
print("A fila está vazia após remover todos os elementos?", fila_p.isEmpty())  # Esperado: True