"""
Estruturas de Dados Lineares
    
        Listas
        
            Busca: Encontrar um nó com um valor específico.
            
Vamos criar um exemplo prático onde você terá uma lista encadeada 
e uma função que permitirá buscar um nó com um valor específico.

Neste exemplo, quando um valor é buscado na lista encadeada, o programa 
retornará uma mensagem informando se o valor foi encontrado ou não.
"""

# Definição da classe 'No', que servirá como elemento individual da lista encadeada.
class No:
    
    # Método construtor (__init__) é chamado quando uma instância da classe 'No' é criada.
    def __init__(self, dado):
        
        # 'dado' é uma variável passada para o construtor e representa o valor do nó.
        self.dado = dado
        
        # 'proximo' é uma referência ao próximo 'No' na lista encadeada.
        # Inicialmente, é definido como 'None' porque não sabemos qual será o próximo 'No' ainda.
        self.proximo = None

# Definição da classe 'ListaEncadeada', que será a estrutura da nossa lista encadeada.
class ListaEncadeada:
    
    # Método construtor (__init__) é chamado quando uma instância da 
    # classe 'ListaEncadeada' é criada.
    def __init__(self):
        
        # 'cabeca' é uma referência ao primeiro nó (ou elemento) da lista encadeada.
        # Inicialmente, a lista está vazia, portanto, 'cabeca' é definido como 'None'.
        self.cabeca = None
        
    # Método 'buscar' da classe 'ListaEncadeada'. Ele é usado para verificar se um 
    # determinado valor (ou chave) existe na lista encadeada.
    def buscar(self, chave):

        # 'temp' é uma variável temporária que inicialmente aponta para a cabeça da 
        # lista (ou seja, o primeiro elemento).
        # Usaremos 'temp' para percorrer a lista encadeada.
        temp = self.cabeca

        # Este loop 'while' continuará enquanto 'temp' não for 'None'. 
        # Basicamente, ele percorrerá cada nó na lista até que o final da lista seja 
        # alcançado (quando 'temp' se torna 'None').
        while temp:

            # Aqui, verificamos se o 'dado' do nó atual (apontado por 'temp') é igual ao 
            # valor da 'chave' que estamos procurando.
            if temp.dado == chave:
                
                # Se for igual, retornamos 'True' para indicar que o valor foi encontrado 
                # na lista.
                return True

            # Se o 'dado' do nó atual não for o que estamos procurando, movemos para o 
            # próximo nó na lista.
            temp = temp.proximo

        # Se o loop terminar e não tivermos retornado 'True' (ou seja, não encontramos 
        # a chave), retornamos 'False' para indicar que o valor não está presente na lista.
        return False
    
    # Método 'inserir_no_final' da classe 'ListaEncadeada'. Ele é usado para 
    # adicionar um novo nó com um dado específico ao final da lista encadeada.
    def inserir_no_final(self, dado):

        # Criamos um novo nó com o dado fornecido. 'novo_no' é uma instância da 
        # classe 'No' e conterá o dado que queremos inserir.
        novo_no = No(dado)

        # Verificamos se a lista está vazia (ou seja, a cabeça da lista é 'None').
        if not self.cabeca:
            
            # Se a lista estiver vazia, fazemos o novo nó ser a cabeça da lista.
            # Em outras palavras, inserimos o novo nó no início da lista.
            self.cabeca = novo_no
            
            # E então, retornamos do método já que nossa tarefa está completa.
            return

        # Se a lista não estiver vazia, precisamos encontrar o último nó 
        # para adicionar o novo nó após ele.
        # Para isso, começamos pela cabeça da lista e usamos a variável 
        # temporária 'temp' para percorrer a lista.
        temp = self.cabeca

        # Este loop 'while' nos permite avançar pela lista até encontrarmos o último nó.
        # Continuará enquanto o próximo nó da variável 'temp' não for 'None' (o que indica o final da lista).
        while temp.proximo:
            
            # Move 'temp' para o próximo nó na lista.
            temp = temp.proximo

        # Uma vez que o loop 'while' termina, 'temp' estará apontando para o último nó da lista.
        # Configuramos o próximo nó de 'temp' para ser o 'novo_no', efetivamente 
        # adicionando 'novo_no' ao final da lista.
        temp.proximo = novo_no


    # Método 'imprimir_lista' da classe 'ListaEncadeada'. Ele é usado para imprimir 
    # todos os dados dos nós da lista encadeada em ordem.
    def imprimir_lista(self):

        # Inicializamos a variável 'temp' com a cabeça da lista. Isso nos permitirá 
        # percorrer a lista começando pelo primeiro nó.
        temp = self.cabeca

        # Este loop 'while' nos permite avançar pela lista e imprimir o dado de cada 
        # nó até chegarmos ao final da lista.
        # Continuará enquanto 'temp' não for 'None', ou seja, enquanto houver nós para percorrer.
        while temp:
            
            # Imprime o dado do nó atual seguido de ' -> '. O argumento 'end' evita 
            # que o 'print' vá para a próxima linha após imprimir.
            print(temp.dado, end=' -> ')
            
            # Move 'temp' para o próximo nó na lista. Isso nos permite avançar pelo 
            # loop e percorrer todos os nós.
            temp = temp.proximo

        # Após o loop, imprimimos 'None' para indicar o final da lista encadeada. 
        # Em uma lista encadeada, o último nó aponta para 'None', por isso é uma 
        # representação apropriada para o final da lista.
        print("None")


# Verifica se este script está sendo executado como o principal (e não importado em outro lugar). 
# Isso é comum em scripts Python para garantir que certos blocos de código só sejam 
# executados quando o script é executado diretamente.
if __name__ == "__main__":

    # Cria uma instância da classe 'ListaEncadeada', inicializando uma nova lista vazia.
    lista = ListaEncadeada()

    # Inserindo alguns valores na lista encadeada para fins de teste.
    lista.inserir_no_final("A")  # Insere "A" no final da lista.
    lista.inserir_no_final("B")  # Insere "B" no final da lista, após "A".
    lista.inserir_no_final("C")  # Insere "C" no final da lista, após "B".

    # Imprime a lista encadeada. O resultado esperado é: A -> B -> C -> None
    lista.imprimir_lista()
    
    # Define um valor que queremos buscar na lista encadeada.
    valor_busca = "B"

    # Usa o método 'buscar' da classe 'ListaEncadeada' para verificar se o 
    # valor "B" está presente na lista.
    if lista.buscar(valor_busca):
        
        # Se o valor foi encontrado na lista, imprime a mensagem confirmando.
        print(f"Valor {valor_busca} encontrado na lista!")
        
    else:
        
        # Se o valor não foi encontrado na lista, imprime a mensagem informando 
        # que ele não está presente.
        print(f"Valor {valor_busca} não está presente na lista.")    
