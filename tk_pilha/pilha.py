"""
Pilhas
            
        Conceitos Básicos

            Definição e Estrutura: Entender o que é uma pilha e como ela é organizada.
            

Pilhas: Pilhas são uma estrutura de dados linear que segue o princípio 
de Last In First Out (LIFO). Isso significa que o último elemento inserido 
na pilha será o primeiro a ser removido. As operações básicas associadas 
às pilhas são: push (adicionar um item ao topo) e pop (remover o item do topo).


Definição e Estrutura:


1 - Definição: 

Uma pilha é uma coleção ordenada de itens na qual a adição 
de novos itens e a remoção de itens existentes sempre ocorrem no mesmo 
final. Esse final é comumente referido como o "topo". O final oposto da 
pilha é conhecido como "base".


2 - Características:

A pilha é uma estrutura LIFO (Last In, First Out).

Somente o elemento no topo da pilha é acessível. Para acessar 
outros elementos, você teria que remover os que estão no topo primeiro.


3 - Operações Básicas:

push(): Adiciona um item ao topo da pilha.

pop(): Remove e retorna o item do topo da pilha.

peek() ou top(): Retorna o item do topo sem removê-lo.

is_empty(): Verifica se a pilha está vazia.

size(): Retorna o número de elementos na pilha.


Em Python, podemos implementar pilhas usando listas ou através da 
classe deque da biblioteca collections
"""
"""

Pilhas
            
        Conceitos Básicos

            Last In, First Out (LIFO): Compreensão do princípio 
            fundamental que rege as operações de uma pilha.

            
Vamos começar com uma analogia simples e, em seguida, 
apresentar um exemplo prático em Python.

Analogia:

Imagine uma pilha de pratos. Quando você adiciona (lava) um prato, 
você o coloca no topo da pilha. E quando você precisa pegar um 
prato (para usar), você sempre pega o do topo da pilha, que é o 
último prato que foi colocado lá. Portanto, o último prato que você 
colocou (Last In) é o primeiro que você pega (First Out).


Exemplo Prático em Python:

Vamos usar a implementação de pilha que fizemos anteriormente 
e demonstrar o princípio LIFO.
"""

# Define uma classe chamada 'Pilha'
class Pilha:
    
    # Construtor da classe, que é chamado quando um objeto desta classe é criado
    def __init__(self):
        
        # Cria uma lista vazia chamada 'pratos' para representar a pilha
        self.pratos = []
        
    # Método para adicionar (push) um elemento ao topo da pilha
    def adicionar(self, prato):
        
        # Usa o método 'append' da lista para adicionar 
        # o elemento ao final (topo da pilha)
        self.pratos.append(prato)

    # Método para remover (pop) o elemento do topo da pilha
    def remover(self):
        
        # Primeiro, verifica se a pilha não está vazia
        if not self.esta_vazia():
            
            # Usa o método 'pop' da lista para remover 
            # e retornar o elemento do final (topo da pilha)
            return self.pratos.pop()
        
        # Se a pilha estiver vazia, retorna None (ou seja, nada)
        return None

    # Método auxiliar para verificar se a pilha está vazia
    def esta_vazia(self):
        
        # Retorna True se a lista 'pratos' estiver 
        # vazia, caso contrário retorna False
        return len(self.pratos) == 0
    
    # Método para visualizar (não remover) o elemento do topo da pilha
    def ver_topo(self):
        
        # Primeiro, verifica se a pilha não está vazia
        if not self.esta_vazia():
            
            # Retorna o último elemento da lista 'pratos' (topo da pilha) 
            # usando índice -1
            return self.pratos[-1]
        
        # Se a pilha estiver vazia, retorna None (ou seja, nada)
        return None
    
    # Método para obter o número de elementos na pilha (tamanho da pilha)
    def quantidade(self):
        
        # Retorna o número de elementos na lista 'pratos' (tamanho da pilha)
        return len(self.pratos)
    
# Inicializa (cria) uma nova instância da classe Pilha, criando uma pilha vazia
minha_pilha = Pilha()

# Usa o método 'adicionar' da instância 'minha_pilha' para adicionar
# o "Prato 1" ao topo da pilha
minha_pilha.adicionar("Prato 1")

# Imprime uma mensagem para informar que o "Prato 1" foi adicionado à pilha
print("Adicionando: Prato 1")

# Usa o método 'adicionar' da instância 'minha_pilha' para adicionar 
# o "Prato 2" ao topo da pilha
minha_pilha.adicionar("Prato 2")

# Imprime uma mensagem para informar que o "Prato 2" foi adicionado à pilha
print("Adicionando: Prato 2")

# Usa o método 'adicionar' da instância 'minha_pilha' para adicionar 
# o "Prato 3" ao topo da pilha
minha_pilha.adicionar("Prato 3")

# Imprime uma mensagem para informar que o "Prato 3" foi adicionado à pilha
print("Adicionando: Prato 3")

# Usa o método 'ver_topo' para obter o item no topo da 
# pilha (neste caso, "Prato 3") e imprime-o
print("Topo da pilha:", minha_pilha.ver_topo())  # A saída esperada é "Prato 3"


# Usa o método 'remover' da instância 'minha_pilha' para remover o item no topo da pilha
prato_removido = minha_pilha.remover()

# Imprime uma mensagem informando qual prato foi removido da pilha
print("Removendo:", prato_removido)  # A saída esperada é "Prato 3"

# Repete o processo: remove o item do topo da pilha
prato_removido = minha_pilha.remover()

# Imprime uma mensagem informando qual prato foi removido da pilha
print("Removendo:", prato_removido)  # A saída esperada é "Prato 2"

# Usa o método 'adicionar' da instância 'minha_pilha' para adicionar o
# "Prato 4" ao topo da pilha
minha_pilha.adicionar("Prato 4")

# Imprime uma mensagem para informar que o "Prato 4" foi adicionado à pilha
print("Adicionando: Prato 4")

# Usa o método 'ver_topo' para obter o item no topo da 
# pilha (neste caso, "Prato 4") e imprime-o
print("Topo da pilha:", minha_pilha.ver_topo())  # A saída esperada é "Prato 4"

# Usa o método 'esta_vazia' para verificar se a pilha está vazia
if minha_pilha.esta_vazia():
    
    # Se o resultado for True, imprime que a pilha está vazia
    print("A pilha está vazia.")
    
else:
    
    # Se o resultado for False, imprime que a pilha tem pratos
    print("A pilha tem pratos.")

# Usa o método 'quantidade' para obter o número de itens na pilha
num_pratos = minha_pilha.quantidade()

# Imprime o número total de pratos presentes na pilha
print(f"A pilha tem {num_pratos} pratos.")
