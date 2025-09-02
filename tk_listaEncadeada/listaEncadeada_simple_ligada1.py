"""
Podemos criar uma lista encadeada simplesmente ligada para armazenar palavras (ou textos). 

Vamos adaptar o exemplo anterior para trabalhar com strings:
"""

# Definição da estrutura básica de um nó para a lista encadeada.
# Esta classe será usada para representar cada elemento individual da lista encadeada.
class No:

    # O construtor da classe No. Ele é chamado sempre que um novo objeto No é criado.
    # Ele aceita um argumento 'texto', que será o dado armazenado no nó.
    def __init__(self, texto):
        
        # Atributo 'texto' do nó. Ele armazena o dado (neste caso, uma string) que 
        # é passado ao construtor.
        self.texto = texto
        
        # Atributo 'proximo' do nó. 
        # Ele serve como ponteiro para o próximo nó na lista encadeada.
        # Quando um novo nó é criado, ele não está ligado a nada ainda, então 
        # 'proximo' é definido como 'None'.
        self.proximo = None


# Definição da estrutura principal da lista encadeada.
# Esta classe servirá para gerenciar os nós, permitindo operações como inserção e remoção.
class ListaEncadeada:

    # O construtor da classe ListaEncadeada. 
    # É chamado sempre que um novo objeto ListaEncadeada é criado.
    def __init__(self):

        # Atributo 'cabeca' da lista encadeada. 
        # Representa o primeiro nó da lista. 
        # Inicialmente, a lista não tem nós, então a 'cabeca' é definida como 'None'.
        self.cabeca = None

    # Método para inserir um nó no final da lista encadeada.
    # Ele aceita um argumento 'texto', que será o dado armazenado no novo nó.
    def inserir_no_final(self, texto):

        # Cria um novo nó com o texto fornecido.
        novo_no = No(texto)

        # Verifica se a lista está vazia, ou seja, se a 'cabeca' é 'None'.
        if self.cabeca is None:

            # Se a lista estiver vazia, o novo nó é inserido na 'cabeca' da lista.
            self.cabeca = novo_no
            return

        # Se a lista não estiver vazia, começamos na 'cabeca' e navegamos até o final da lista.
        ultimo_no = self.cabeca

        # O loop continua enquanto o próximo nó existir, 
        # isso é, até que 'proximo' do 'ultimo_no' seja 'None', indicando o final da lista.
        while ultimo_no.proximo:
            ultimo_no = ultimo_no.proximo

        # Após sair do loop, 'ultimo_no' será o último nó da lista.
        # Então, vinculamos o 'proximo' do 'ultimo_no' ao 'novo_no', inserindo o 
        # 'novo_no' no final da lista.
        ultimo_no.proximo = novo_no


    # Método para exibir todos os elementos da lista encadeada.
    def imprimir_lista(self):

        # Define 'no_atual' como o primeiro nó da lista (ou seja, a 'cabeca').
        # Isso permite começar a impressão a partir do início da lista.
        no_atual = self.cabeca

        # O loop while percorre cada nó da lista até que chegue ao final (onde 
        # 'no_atual' será 'None').
        while no_atual:

            # Imprime o conteúdo (texto) do nó atual seguido pela seta '->' 
            # para indicar o apontamento para o próximo nó.
            print(no_atual.texto, end=' -> ')

            # Move para o próximo nó na lista.
            # Se já estivermos no último nó, 'no_atual.proximo' será 'None', encerrando o loop.
            no_atual = no_atual.proximo

        # Após imprimir todos os nós, imprimimos "None" para indicar o final da lista encadeada.
        print("None")


# Inicialização e manipulação da lista encadeada com textos.

# Cria uma nova instância da classe 'ListaEncadeada'.
# A esta altura, a lista está vazia, pois a 'cabeca' é definida como 'None' no construtor da classe.
lista = ListaEncadeada()

# Utiliza o método 'inserir_no_final' para adicionar o texto "Olá" à lista.
# Como a lista está vazia, "Olá" se torna o primeiro nó (ou cabeça) da lista.
lista.inserir_no_final("Olá")

# Adiciona o texto "mundo" após "Olá" na lista.
lista.inserir_no_final("mundo")

# Adiciona o texto "Python" após "mundo" na lista.
lista.inserir_no_final("Python")

# Continua inserindo mais textos à lista.
lista.inserir_no_final("é")
lista.inserir_no_final("incrível!")

# Usa o método 'imprimir_lista' para exibir todos os textos da lista em sequência.
# A função irá imprimir cada texto seguido por '->', indicando o encadeamento.
# Finalmente, a saída termina com "None" para indicar o fim da lista.
lista.imprimir_lista()  # Saída esperada: Olá -> mundo -> Python -> é -> incrível! -> None