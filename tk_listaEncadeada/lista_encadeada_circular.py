"""
Estruturas de Dados Lineares
    
        Listas
        
            Lista encadeada
            
                Lista Encadeada Circular Simplesmente Ligada: O último nó 
                da lista aponta para o primeiro nó.


Uma lista encadeada circular simplesmente ligada é similar à lista encadeada 
simples, com a diferença de que o último nó da lista aponta para o primeiro, 
formando um ciclo.

Vamos criar uma lista que insere elementos e, depois de inserir, 
imprimirá os n+1 primeiros elementos (onde n é o número de elementos 
na lista), para demonstrar claramente que após o último elemento, 
retornamos ao primeiro:

Vamos começar do zero com um novo exemplo:
"""

# Definindo a estrutura básica de um nó para a lista circular
class No:
    
    # O construtor da classe No é usado para inicializar um novo nó
    def __init__(self, dado):
        
        # O atributo 'dado' armazena o valor que queremos inserir na lista
        self.dado = dado
        
        # O atributo 'proximo' é uma referência ao próximo nó na lista.
        # Inicialmente, é definido como None até que o nó seja conectado a outro nó na lista.
        self.proximo = None

# Definindo a estrutura básica da lista circular
class ListaCircular:
    
    # O construtor da classe ListaCircular é usado para inicializar uma nova lista circular
    def __init__(self):
        
        # O atributo 'cabeca' é uma referência ao primeiro nó da lista.
        # Quando uma lista é inicialmente criada, ela está vazia, então 'cabeca' 
        # é definida como None.
        self.cabeca = None


    # Método para inserir um novo nó na lista circular
    def inserir(self, dado):

        # Criamos um novo nó com o dado fornecido
        novo_no = No(dado)

        # Verificamos se a lista está vazia (se a cabeça é None)
        if not self.cabeca:

            # Se a lista estiver vazia, definimos o novo nó como a cabeça da lista
            self.cabeca = novo_no

            # E o ponteiro 'proximo' do novo nó apontará para ele mesmo,
            # já que é o único elemento na lista e a lista é circular
            novo_no.proximo = self.cabeca

        # Se a lista já tiver elementos
        else:

            # Inicializamos uma variável temporária com a cabeça da lista 
            # para não perder a referência ao início da lista
            temp = self.cabeca

            # Percorremos a lista até encontrar o último nó (aquele cujo 'proximo' 
            # aponta para a cabeça)
            while temp.proximo != self.cabeca:
                temp = temp.proximo

            # Após encontrar o último nó, fazemos ele apontar para o novo nó
            temp.proximo = novo_no

            # E, por ser uma lista circular, fazemos o 'proximo' do novo nó apontar
            # para a cabeça da lista
            novo_no.proximo = self.cabeca
    
    # Método para imprimir os elementos da lista circular
    def imprimir_lista(self):

        # Começamos pela cabeça da lista
        no_atual = self.cabeca

        # Inicializamos um contador para controlar o número de nós que foram impressos
        cont = 0

        # Chamamos a função 'tamanho' para saber quantos elementos existem na lista
        # e adicionamos 1 para imprimir a cabeça novamente e mostrar que a lista é circular
        n = self.tamanho() + 1

        # Continuamos imprimindo enquanto o contador for menor que o total de nós + 1
        while cont < n:

            # Imprimimos o dado do nó atual
            print(no_atual.dado, end=' -> ')

            # Movemos para o próximo nó na lista
            no_atual = no_atual.proximo

            # Incrementamos o contador
            cont += 1

        # Ao final, imprimimos '...' para indicar que a lista é circular e, se continuássemos, 
        # os elementos se repetiriam em loop
        print("...")
        
    # Método para calcular o tamanho da lista circular
    def tamanho(self):

        # Inicializamos o contador com 1, porque começaremos contando a partir da cabeça da lista
        cont = 1

        # Começamos pela cabeça da lista
        no_atual = self.cabeca

        # Continuamos contando enquanto o próximo nó não for a cabeça da lista
        # Quando o próximo nó for a cabeça, saberemos que a lista deu a volta completa, 
        # então podemos parar a contagem
        while no_atual.proximo != self.cabeca:

            # Incrementamos o contador
            cont += 1

            # Movemos para o próximo nó da lista
            no_atual = no_atual.proximo

        # Ao final, retornamos o total de nós contados
        return cont
        
        
# Inicialização e teste da Lista Circular

# Criando uma instância da Lista Circular
lista = ListaCircular()

# Inserindo o elemento "A" na lista
lista.inserir("A")

# Depois de inserir "A", a lista terá um único nó apontando para si mesmo.
# Por isso, a saída esperada é: A -> A -> ... indicando que a lista está em loop
lista.imprimir_lista()  # Saída esperada: A -> A -> ...

# Agora inserimos o elemento "B" na lista
lista.inserir("B")

# Depois de inserir "B", a lista terá dois nós: "A" e "B", e o último nó (B) apontará de volta para "A"
# Por isso, a saída esperada é: A -> B -> A -> ... indicando que a lista está em loop a partir de "A"
lista.imprimir_lista()  # Saída esperada: A -> B -> A -> ...

# Inserindo o elemento "C" na lista
lista.inserir("C")

# Com a inserção do "C", a lista terá três nós: "A", "B" e "C", e o último nó (C) apontará de volta para "A"
# Por isso, a saída esperada é: A -> B -> C -> A -> ... indicando que a lista está em loop a partir de "A"
lista.imprimir_lista()  # Saída esperada: A -> B -> C -> A -> ...

"""
Dessa forma, após inserir 3 elementos na lista ("A", "B" e "C"), ao 
imprimir, verá o início da lista após o terceiro elemento, demonstrando 
a circularidade.
"""
print()
