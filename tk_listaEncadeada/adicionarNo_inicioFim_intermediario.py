"""
Estruturas de Dados Lineares
    
        Listas
        
            Operações Básicas

                Inserção: Adicionar um novo nó à lista.
                
                    No início
                    No final
                    Após um nó específico
"""

# Definição da classe No, que representa um elemento da lista encadeada.
class No:
    
    # O construtor da classe No inicializa o nó com o dado fornecido e um 
    # ponteiro para o próximo nó como None.
    def __init__(self, dado):
        
        self.dado = dado  # Armazena o dado passado para o nó
        self.proximo = None  # Define o próximo nó. Inicialmente, é definido como None.

# Definição da classe ListaEncadeada que representa a estrutura da lista.
class ListaEncadeada:
    
    # O construtor da classe ListaEncadeada inicializa a cabeça da lista como None.
    def __init__(self):
        
        self.cabeca = None  # Define a cabeça (ou primeiro nó) da lista. Inicialmente, é definido como None.
        
    # Método para inserção de um novo nó no início da lista encadeada.
    def inserir_no_inicio(self, dado):
        
        # Criação de um novo nó com o dado fornecido.
        novo_no = No(dado)
        
        # O ponteiro 'proximo' do novo nó é ajustado para apontar para a 
        # cabeça atual da lista.
        # Isso significa que o novo nó será inserido antes do nó atual 
        # que é a cabeça da lista.
        novo_no.proximo = self.cabeca
        
        # A cabeça da lista é atualizada para ser o novo nó.
        # Isso efetivamente coloca o novo nó no início da lista.
        self.cabeca = novo_no
        
    # Método para inserção de um novo nó no final da lista encadeada.
    def inserir_no_final(self, dado):
        
        # Criação de um novo nó com o dado fornecido.
        novo_no = No(dado)
        
        # Verifica se a lista está vazia (ou seja, se não tem cabeça).
        if not self.cabeca:
            
            # Se a lista estiver vazia, simplesmente designamos o novo 
            # nó como a cabeça da lista.
            self.cabeca = novo_no
            
            return  # Finalizamos o método já que o novo nó foi adicionado.

        # Se a lista não estiver vazia, usamos uma variável temporária 
        # para percorrer a lista.
        temp = self.cabeca

        # Continuamos percorrendo a lista até chegar ao último nó (aquele que 
        # não tem um próximo).
        while temp.proximo:
            temp = temp.proximo
        
        # Agora que estamos no último nó, apontamos seu 'proximo' para o novo nó.
        # Isso efetivamente adiciona o novo nó ao final da lista.
        temp.proximo = novo_no
        
    
    # Método para inserção de um novo nó após um nó específico.
    def inserir_apos_no(self, no_anterior, dado):
        
        # Verifica se o nó anterior fornecido é None (ou seja, não 
        # foi fornecido ou é inválido).
        if not no_anterior:
            
            # Se o nó anterior não for válido, exibe uma mensagem e termina o método.
            print("O nó anterior fornecido não está presente.")
            return
        
        # Cria um novo nó com o dado fornecido.
        novo_no = No(dado)
        
        # O 'proximo' do novo nó é agora o mesmo que o 'proximo' do nó anterior.
        # Isso é feito para manter a continuidade da lista.
        novo_no.proximo = no_anterior.proximo
        
        # Agora, o 'proximo' do nó anterior aponta para o novo nó, inserindo efetivamente
        # o novo nó após o nó anterior.
        no_anterior.proximo = novo_no
        
    
    # Método para imprimir todos os elementos da lista encadeada.
    def imprimir_lista(self):
        
        # Inicializa um ponteiro temporário com a cabeça da lista.
        temp = self.cabeca
        
        # Enquanto o ponteiro temporário não for None (ou seja, enquanto 
        # houver nós na lista)...
        while temp:
            
            # Imprime o dado armazenado no nó atual.
            print(temp.dado, end=' -> ')
            
            # Move o ponteiro temporário para o próximo nó da lista.
            temp = temp.proximo
        
        # Após imprimir todos os nós, imprime "None" para indicar o fim da lista.
        print("None")
        

# Testando as funcionalidades da lista encadeada.

# Criando uma nova lista encadeada vazia.
lista = ListaEncadeada()

# Inserindo no início da lista.
lista.inserir_no_inicio("C")  # O único nó da lista será C.
lista.imprimir_lista()  # Esperamos ver: C -> None

# Inserindo "B" no início, então "B" se tornará a nova cabeça e "C" será o segundo nó.
lista.inserir_no_inicio("B")
lista.imprimir_lista()  # Esperamos ver: B -> C -> None

# Inserindo "A" no início, então "A" será a cabeça, "B" o segundo nó e "C" o terceiro.
lista.inserir_no_inicio("A")
lista.imprimir_lista()  # Esperamos ver: A -> B -> C -> None

# Inserindo no final da lista.
# "D" será acrescentado depois do último nó, que é "C".
lista.inserir_no_final("D")
lista.imprimir_lista()  # Esperamos ver: A -> B -> C -> D -> None

# Inserindo após um nó específico.
# Primeiro, encontramos o nó que contém "B" (que é o segundo nó, logo após a cabeça).
no_B = lista.cabeca.proximo

# Inserindo "X" logo após o nó "B".
lista.inserir_apos_no(no_B, "X")
lista.imprimir_lista()  # Esperamos ver: A -> B -> X -> C -> D -> None