
"""
 Filas
        
            Conceitos Básicos

                Definição e Estrutura: Compreender o que é uma fila e como ela é organizada.
                First In, First Out (FIFO): Entender o princípio básico que rege as operações de uma fila.


Filas (Queues)

Uma fila é outra estrutura de dados linear, mas, diferentemente das pilhas, os 
elementos em uma fila são processados na ordem em que são adicionados. O lugar onde 
os novos elementos são adicionados é chamado de "final" (ou "rear"), e o lugar de 
onde os elementos são removidos é chamado de "início" (ou "front").

Imagine uma fila de pessoas esperando para comprar ingressos para um show. A primeira
pessoa que chega à fila será a primeira a comprar o ingresso e, consequentemente, a 
primeira a sair da fila.

Em Python, as filas podem ser implementadas de várias maneiras, incluindo listas e o 
módulo collections.deque. No entanto, usar listas para filas pode não ser eficiente, 
especialmente para operações no início da lista, portanto, deque é frequentemente 
preferido.
"""

# Importando a classe 'deque' do módulo 'collections'. 
# 'deque' é uma estrutura de dados de fila de dupla ponta, 
# mas neste exemplo, estamos usando apenas como uma fila simples.
from collections import deque

# Inicializando uma nova fila vazia.
fila = deque()

# Adicionando 'pessoa1' ao final da fila.
fila.append('pessoa1')

# Adicionando 'pessoa2' também ao final da fila. 
# Agora, 'pessoa1' é o primeiro da fila e 'pessoa2' é o segundo.
fila.append('pessoa2')

# Imprimindo a fila para visualização. 
# Neste ponto, a fila contém 'pessoa1' e 'pessoa2' em ordem.
print(fila)  # Saída: deque(['pessoa1', 'pessoa2'])

"""
First In, First Out (FIFO):

O conceito de "First In, First Out" (FIFO) rege as operações de uma 
fila. Isso significa que o primeiro elemento que foi adicionado à fila será o 
primeiro a ser removido.

Usando o exemplo da fila de pessoas novamente, se "pessoa1" se juntar à fila 
primeiro, seguida por "pessoa2" e depois "pessoa3", então "pessoa1" será a primeira 
a ser atendida e a sair da fila.

Aqui está como você pode implementar operações FIFO usando deque em Python:
"""

# Importando a classe 'deque' do módulo 'collections'. 
# 'deque' pode ser usado como uma fila de dupla ponta,

# mas neste exemplo, estamos usando apenas como uma fila simples.
from collections import deque

# Inicializando uma nova fila vazia.
fila = deque()

# Adicionando 'pessoa1' ao final da fila.
fila.append('pessoa1')  

# Adicionando 'pessoa2' ao final da fila.
fila.append('pessoa2')

# Adicionando 'pessoa3' ao final da fila.
fila.append('pessoa3')

# Imprimindo a fila para visualização. Neste ponto, a fila contém 
# 'pessoa1', 'pessoa2' e 'pessoa3' em ordem.
print(fila)  # Saída: deque(['pessoa1', 'pessoa2', 'pessoa3'])

# Removendo e retornando o elemento do início da fila, que neste caso é 'pessoa1'.
primeira_pessoa = fila.popleft()

# Imprimindo o nome da primeira pessoa, que foi removida da fila.
print(primeira_pessoa)  # Saída: 'pessoa1'

# Imprimindo a fila após a remoção de 'pessoa1'. 
# Agora a fila contém 'pessoa2' e 'pessoa3'.
print(fila)  # Saída: deque(['pessoa2', 'pessoa3'])

"""
As principais operações associadas às filas são enqueue (para adicionar 
um elemento ao final da fila) e dequeue (para remover o elemento do início). 
Em Python, usando deque, o método append pode ser usado para enqueue e o método 
popleft pode ser usado para dequeue.

Lembre-se de que, embora deque seja uma boa escolha para implementar filas, 
Python também oferece o módulo queue que fornece várias implementações de 
fila (como Simple Queue, Lifo Queue e PriorityQueue).
"""
print()




"""
 Filas
        
            Operações Fundamentais

                Enqueue: Adicionar um elemento ao final da fila.
                Dequeue: Remover e retornar o elemento da frente da fila.
                Front: Ver o elemento da frente sem removê-lo.
                Rear/Back: Ver o último elemento sem removê-lo.
                isEmpty: Verificar se a fila está vazia.
                getSize: Obter o número de elementos na fila.
"""

# Vamos criar uma implementação simples de fila em Python usando collections.deque.

# Importando a classe 'deque' do módulo 'collections'. 'deque' é uma 
# estrutura de dados que pode ser usada como uma fila ou uma pilha.
from collections import deque

# Definindo uma nova classe chamada 'Fila'.
class Fila:
    
    # Método construtor da classe. Este método é chamado automaticamente 
    # quando criamos uma nova instância da classe.
    def __init__(self):
        
        # Inicializando a propriedade 'fila' com uma instância vazia de 'deque'.
        # Isso servirá como nossa estrutura de fila.
        self.fila = deque()
    
    # Método para adicionar um elemento à fila. Em termos técnicos de fila, 
    # isso é comumente chamado de 'enqueue' (enfileirar).
    def enqueue(self, elemento):
        
        # Usando o método 'append' do 'deque' para adicionar o 'elemento' 
        # fornecido ao final da fila.
        self.fila.append(elemento)
        
    # Método para remover e retornar o primeiro elemento 
    # da fila. Em termos técnicos 
    # de fila, isso é comumente chamado de 'dequeue' (desenfileirar).
    def dequeue(self):
        
        # Verificando se a fila não está vazia usando o método 'isEmpty'.
        if not self.isEmpty():
            
            # Se a fila não estiver vazia, usamos o método 'popleft' do 'deque' 
            # para remover e retornar o primeiro elemento da fila.
            return self.fila.popleft()
        
        else:
        
            # Se a fila estiver vazia, retornamos uma mensagem informando isso.
            return "A fila está vazia!"
        
        
    # Método para verificar se a fila está vazia. Ele é usado internamente 
    # no método 'dequeue' acima.
    def isEmpty(self):
        
        # Retorna True se o tamanho da fila for 0 (ou seja, está vazia); 
        # caso contrário, retorna False.
        return len(self.fila) == 0
    
    
        
    # Método para visualizar o primeiro elemento da fila sem removê-lo.
    def front(self):
        
        # Usando o método 'isEmpty' para verificar se a fila não está vazia.
        if not self.isEmpty():
            
            # Se a fila não estiver vazia, retorna o primeiro elemento. Em Python,
            # 'self.fila[0]' nos dá o primeiro elemento de uma lista ou deque.
            return self.fila[0]
        
        else:
        
            # Se a fila estiver vazia, retornamos uma mensagem informando isso.
            return "A fila está vazia!"
        
        
    # Método para visualizar o último elemento da fila sem removê-lo.
    def rear(self):
        
        # Novamente, verificamos se a fila não está vazia.
        if not self.isEmpty():
            
            # Se a fila não estiver vazia, retorna o último elemento. Em Python,
            # 'self.fila[-1]' nos dá o último elemento de uma lista ou deque.
            return self.fila[-1]
        
        else:
        
            # Se a fila estiver vazia, retornamos uma mensagem informando isso.
            return "A fila está vazia!"
        
    
    # Método para obter o número total de elementos na fila.
    def getSize(self):
        
        # Usamos a função 'len' para contar o número de elementos no deque
        # e retornamos esse valor.
        return len(self.fila)

    
# Iniciando a seção de testes da classe Fila

# Criando uma instância da classe Fila.
# Isso nos dará uma fila vazia pronta para ser usada.
fila = Fila()

# Verificando se a fila recém-criada está vazia. Como acabamos de criá-la e não adicionamos 
# nenhum elemento ainda, a expectativa é que ela esteja vazia, por isso o resultado deve ser True.
print(fila.isEmpty())  # Saída esperada: True

# Adicionando o elemento "elemento1" ao final da fila.
fila.enqueue("elemento1")

# Adicionando o elemento "elemento2" ao final da fila.
fila.enqueue("elemento2")

# Adicionando o elemento "elemento3" ao final da fila.
fila.enqueue("elemento3")

# Verificando e imprimindo o elemento da frente da fila, que é "elemento1", 
# mas sem removê-lo.
print(fila.front())  # Saída esperada: elemento1


# Verificando e imprimindo o último elemento da fila, que é "elemento3", 
# mas sem removê-lo.
print(fila.rear())   # Saída esperada: elemento3


# Imprimindo o número total de elementos na fila. Como adicionamos 3 elementos, 
# o tamanho da fila deve ser 3.
print(fila.getSize())  # Saída esperada: 3

# Removendo e imprimindo o elemento da frente da fila, que é "elemento1". 
# Após essa operação, "elemento1" não estará mais na fila.
print(fila.dequeue())  # Saída esperada: elemento1

# Imprimindo novamente o número total de elementos na fila. 
# Como "elemento1" foi removido, agora a fila contém apenas 2 elementos.
print(fila.getSize())  # Saída esperada: 2

# Verificando e imprimindo o elemento da frente da fila, que é "elemento2", 
# mas sem removê-lo.
print(fila.front())  # Saída esperada: elemento2