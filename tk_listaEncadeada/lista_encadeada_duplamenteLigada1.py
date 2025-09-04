"""
Exemplo 2 de Lista Encadeada Duplamente Ligada: Cada nó aponta para o 
próximo e para o nó anterior na lista.
"""

# Aqui estamos definindo uma classe chamada 'No'. Esta classe servirá como a 
#estrutura básica de um nó em uma lista duplamente ligada.

class No:
    
    # O método __init__ é um construtor especial em Python. 
    # Ele é invocado automaticamente quando criamos uma instância da classe. 
    # Neste caso, quando criamos um novo 'No', precisamos passar um 'dado' que o 
    # nó irá armazenar.
    def __init__(self, dado):
        
        # O 'dado' é uma variável que armazenará a informação ou valor que queremos 
        # manter neste nó.
        # Por exemplo, pode ser um número, uma string, etc.
        self.dado = dado
        
        # 'anterior' é uma referência que apontará para o nó anterior na lista duplamente ligada.
        # Para um novo nó, por padrão, não há nó anterior, por isso é definido como None.
        self.anterior = None
        
        # 'proximo' é uma referência que apontará para o próximo nó na lista duplamente ligada.
        # Semelhante ao 'anterior', para um novo nó, por padrão, não há próximo nó, por isso é 
        # definido como None.
        self.proximo = None


# Aqui estamos definindo uma classe chamada 'ListaDuplamenteLigada'. 
# Esta classe representa uma lista duplamente ligada, uma estrutura de dados em 
# que cada elemento tem uma referência para o elemento anterior e próximo na lista.

class ListaDuplamenteLigada:

    # O método __init__ é o construtor da classe. É invocado automaticamente quando uma
    # nova instância da 'ListaDuplamenteLigada' é criada.
    def __init__(self):
        
        # 'cabeca' é uma referência ao primeiro nó (ou elemento) da lista duplamente ligada. 
        # Quando a lista é inicialmente criada, ela está vazia, portanto 'cabeca' é definida
        # como None.
        self.cabeca = None
        
        # 'cauda' é uma referência ao último nó (ou elemento) da lista duplamente ligada. 
        # Similar à 'cabeca', quando a lista é inicialmente criada e ainda não tem 
        # elementos, 'cauda' é definida como None.
        self.cauda = None


    # Este método é responsável por inserir um novo nó no final da lista duplamente ligada.
    def inserir_no_final(self, dado):

        # Primeiro, criamos um novo nó com o dado fornecido.
        # 'dado' é o valor que queremos armazenar no novo nó.
        # 'anterior' e 'proximo' são inicializados como None no construtor do No.
        novo_no = No(dado)

        # Verificamos se a lista está vazia (se a cabeça é None).
        if not self.cabeca:

            # Se a lista estiver vazia, o novo nó se tornará tanto a 'cabeca' 
            # quanto a 'cauda' da lista.
            self.cabeca = novo_no
            self.cauda = novo_no

        else:
            # Se a lista não estiver vazia:

            # O próximo do nó atualmente na 'cauda' é definido para o novo nó.
            # Isso conecta o último nó da lista ao novo nó.
            self.cauda.proximo = novo_no

            # O 'anterior' do novo nó é definido para a 'cauda' atual.
            # Isso faz com que o novo nó aponte de volta para o nó anterior.
            novo_no.anterior = self.cauda

            # Por fim, definimos a 'cauda' da lista para o novo nó, já que é o novo
            # último nó da lista.
            self.cauda = novo_no


    # Este método é responsável por imprimir todos os nós da lista duplamente 
    # ligada, desde a cabeça até a cauda.
    def imprimir_lista(self):

        # Começamos a impressão a partir do nó cabeça.
        no_atual = self.cabeca

        # Continuamos imprimindo e avançando para o próximo nó até atingirmos 
        # o final da lista.
        while no_atual:

            # Imprime o dado contido no nó atual seguido por '<->', que indica uma 
            # ligação bidirecional.
            print(no_atual.dado, end=' <-> ')

            # Avança para o próximo nó da lista.
            no_atual = no_atual.proximo

        # Após imprimir todos os nós, imprimimos "None" para indicar o final da lista.
        print("None")
        

        
# Aqui, estamos criando uma nova instância da classe ListaDuplamenteLigada.
# A lista inicialmente está vazia, com a cabeça e a cauda definidas como None.
lista = ListaDuplamenteLigada()


# Este é um loop infinito. A ideia é continuar solicitando ao usuário uma 
# entrada até que o usuário decida sair.
while True:
    
    # Solicita ao usuário que insira uma letra ou a palavra "sair" para encerrar o loop.
    letra = input("Digite uma letra (ou 'sair' para encerrar): ")
    
    # Verifica se a entrada do usuário é "sair" (considerando ambos os casos de 
    # letras maiúsculas e minúsculas).
    if letra.lower() == 'sair':
        
        # Se o usuário digitar "sair", o loop é encerrado.
        break
    
    # Se o usuário não digitar "sair", a letra inserida é adicionada ao final da 
    # lista duplamente ligada.
    lista.inserir_no_final(letra)
    
    # Após inserir a letra na lista, a lista completa é impressa para fornecer 
    # feedback visual ao usuário.
    lista.imprimir_lista()


"""
Neste exemplo:

    A função input solicita ao usuário que insira uma letra.
    Se o usuário digitar "sair", o loop termina.
    Caso contrário, a letra é inserida no final da lista.
    A lista atualizada é então impressa para mostrar sua estrutura.

Dessa forma, você pode ver em tempo real como a lista duplamente encadeada 
evolui à medida que insere novos elementos.
"""
print()