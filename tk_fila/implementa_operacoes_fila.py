"""
Exercício: Implementação e Operações de Fila

Objetivo: Implementar uma fila e suas operações fundamentais.

Instruções:

    1. Crie uma classe chamada Fila.

    2. A classe deve conter as seguintes operações:
        - enqueue: Deve receber um elemento como argumento e adicioná-lo 
        ao final da fila.
        
        - dequeue: Deve remover e retornar o elemento da frente da fila. Se a 
        fila estiver vazia, deve retornar uma mensagem indicando que a fila está vazia.
        
        - front: Deve retornar o elemento da frente da fila sem removê-lo. Se a fila 
        estiver vazia, deve retornar uma mensagem indicando que a fila está vazia.
        
        - rear: Deve retornar o último elemento da fila sem removê-lo. Se a fila estiver 
        vazia, deve retornar uma mensagem indicando que a fila está vazia.        
        
        - isEmpty: Deve retornar True se a fila estiver vazia e False caso contrário.
        
        - getSize: Deve retornar o número de elementos presentes na fila.

    3. Depois de implementar a classe Fila, crie uma instância da fila e realize as 
    seguintes operações, imprimindo os resultados:
        - Verifique se a fila está vazia.
        - Adicione os elementos "A", "B" e "C" à fila.
        - Veja o elemento da frente.
        - Veja o último elemento.
        - Remova o elemento da frente.
        - Veja o elemento da frente novamente.
        - Verifique o tamanho da fila.
        - Remova todos os elementos da fila até que esteja vazia.
        
        
    
"""

# Resposta

# Primeiro, estamos importando a classe deque do módulo collections.
# A classe deque fornece uma implementação de fila de dupla extremidade 
# que pode ser usada tanto como pilha quanto como fila.
from collections import deque

# 1. Crie uma classe chamada Fila.

# Aqui começamos a definição da nossa classe chamada 'Fila'.
class Fila:
    
    # Este é o construtor da classe, chamado automaticamente toda vez que 
    # criamos uma nova instância (ou objeto) da classe Fila.
    def __init__(self):
        
        # Dentro do construtor, estamos inicializando um atributo chamado 'fila'.
        # Esse atributo irá armazenar todos os elementos da nossa fila.
        # Atribuímos a ele uma instância vazia de deque, o que significa que
        # nossa fila inicia sem nenhum elemento.
        self.fila = deque()
        
    """
    2. A classe deve conter as seguintes operações:
        - enqueue: Deve receber um elemento como argumento e adicioná-lo 
        ao final da fila.
        
        - dequeue: Deve remover e retornar o elemento da frente da fila. Se a 
        fila estiver vazia, deve retornar uma mensagem indicando que a fila está vazia.
        
        - front: Deve retornar o elemento da frente da fila sem removê-lo. Se a fila 
        estiver vazia, deve retornar uma mensagem indicando que a fila está vazia.
        
        - rear: Deve retornar o último elemento da fila sem removê-lo. Se a fila estiver 
        vazia, deve retornar uma mensagem indicando que a fila está vazia.        
        
        - isEmpty: Deve retornar True se a fila estiver vazia e False caso contrário.
        
        - getSize: Deve retornar o número de elementos presentes na fila.
    """
    
    # Esta é a função 'enqueue' da nossa classe.
    # Ela é responsável por adicionar um elemento ao final da fila.
    def enqueue(self, elemento):
        
        # Usando o método 'append' do objeto 'deque', 
        # adicionamos o elemento fornecido ao final da fila.
        self.fila.append(elemento)
    
    # Esta é a função 'dequeue' da nossa classe.
    # Ela é responsável por remover e retornar o elemento da frente da fila.
    def dequeue(self):
        
        # Antes de tentar remover um elemento, verificamos se a fila não está vazia.
        # Usamos a função 'isEmpty' (que será definida em breve) para isso.
        if not self.isEmpty():
            
            # Se a fila não estiver vazia, removemos e retornamos o primeiro elemento 
            # usando o método 'popleft' do objeto 'deque'.
            return self.fila.popleft()
        
        else:
            
            # Se a fila estiver vazia, retornamos uma mensagem informando isso.
            return "A fila está vazia!"
    
    # Esta é a função 'front' da nossa classe.
    # Ela é responsável por retornar (sem remover) o elemento da frente da fila.
    def front(self):
        
        # Novamente, antes de tentar acessar um elemento, verificamos se a fila não está vazia.
        if not self.isEmpty():
            
            # Se a fila não estiver vazia, retornamos o primeiro elemento.
            # Aqui usamos indexação (self.fila[0]) para obter o primeiro elemento.
            return self.fila[0]
        
        else:
            
            # Se a fila estiver vazia, retornamos uma mensagem informando isso.
            return "A fila está vazia!"

    
    # Esta é a função 'rear' da nossa classe.
    # Ela é responsável por retornar (sem remover) o último elemento da fila.
    def rear(self):
        
        # Primeiro, verificamos se a fila não está vazia usando a função 'isEmpty'.
        if not self.isEmpty():
            
            # Se a fila não estiver vazia, retornamos o último elemento.
            # Usamos indexação (self.fila[-1]) para obter o último elemento.
            return self.fila[-1]
        
        else:
            
            # Se a fila estiver vazia, retornamos uma mensagem informando isso.
            return "A fila está vazia!"
    
    # A função 'isEmpty' verifica se a fila está vazia ou não.
    def isEmpty(self):
        
        # Aqui, usamos a função len para obter o número de elementos na fila.
        # Se o tamanho da fila for 0, isso significa que a fila está vazia e a função retorna True.
        # Caso contrário, retorna False.
        return len(self.fila) == 0
    
    # A função 'getSize' retorna o número de elementos presentes na fila.
    def getSize(self):
        
        # Usamos a função len para obter e retornar o número de elementos na fila.
        return len(self.fila)
    

# Agora, vamos testar a nossa implementação:

"""
3. Depois de implementar a classe Fila, crie uma instância da fila e realize as seguintes operações, imprimindo os resultados:
        - Verifique se a fila está vazia.
        - Adicione os elementos "A", "B" e "C" à fila.
        - Veja o elemento da frente.
        - Veja o último elemento.
        - Remova o elemento da frente.
        - Veja o elemento da frente novamente.
        - Verifique o tamanho da fila.
        - Remova todos os elementos da fila até que esteja vazia.
"""

# Primeiro, criamos uma nova instância da classe 'Fila'.
fila = Fila()

# Verificamos se a fila está vazia.
# A função 'isEmpty()' da classe 'Fila' retorna True se a fila estiver vazia e False caso contrário.
print(fila.isEmpty())  # Esperado: True

# Adicionamos o elemento "A" ao final da fila.
fila.enqueue("A")
# Agora, a fila tem: A

# Adicionamos o elemento "B" ao final da fila.
fila.enqueue("B")
# Agora, a fila tem: A -> B

# Adicionamos o elemento "C" ao final da fila.
fila.enqueue("C")
# Agora, a fila tem: A -> B -> C

# Verificamos e imprimimos o elemento da frente da fila (sem removê-lo).
# Usamos a função 'front()' para isso.
print(fila.front())  # Esperado: A
# A fila ainda é: A -> B -> C

# Verificamos e imprimimos o último elemento da fila (sem removê-lo).
# Usamos a função 'rear()' para isso.
print(fila.rear())   # Esperado: C
# A fila ainda é: A -> B -> C

# Removemos o elemento da frente da fila e imprimimos esse elemento.
# Usamos a função 'dequeue()' para isso.
print(fila.dequeue())  # Esperado: A
# Agora, a fila tem: B -> C

# Verificamos e imprimimos o elemento da frente da fila novamente (sem removê-lo).
print(fila.front())  # Esperado: B
# A fila ainda é: B -> C

# Verificamos e imprimimos o número de elementos na fila.
# Usamos a função 'getSize()' para isso.
print(fila.getSize())  # Esperado: 2
# A fila ainda é: B -> C

# Removemos o próximo elemento da frente da fila e imprimimos esse elemento.
print(fila.dequeue())  # Esperado: B
# Agora, a fila tem: C

# Removemos o próximo (e último) elemento da frente da fila e imprimimos esse elemento.
print(fila.dequeue())  # Esperado: C
# Agora, a fila está vazia.

# Tentamos remover um elemento de uma fila vazia.
# A função 'dequeue()' deverá retornar uma mensagem indicando que a fila está vazia.
print(fila.dequeue())  # Esperado: A fila está vazia!

"""
Com essa solução, conseguimos implementar todas as operações 
fundamentais de uma fila e também testamos cada uma dessas 
operações conforme especificado no exercício.
"""
print()