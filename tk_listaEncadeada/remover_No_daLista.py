"""
Estruturas de Dados Lineares
    
        Listas
        
            Deleção: Remover um nó da lista.
                
                    Do início
                    Do final
                    Com base em um valor específico
                    
Vamos criar um exemplo que contém operações de deleção para uma lista 
encadeada simples. A seguir, as operações para remover um nó:

    Do início da lista
    Do final da lista
    Com base em um valor específico
"""

# Definindo a classe "No" que representa um nó em uma lista encadeada.
class No:
    
    # O construtor da classe "__init__" é chamado quando um novo objeto No é criado.
    # Ele recebe um parâmetro "dado" que representa o valor armazenado neste nó.
    def __init__(self, dado):
        
        # O atributo "dado" deste nó recebe o valor passado como parâmetro.
        self.dado = dado
        
        # O atributo "proximo" é inicializado como None, indicando que
        # este nó não está ligado a outro nó inicialmente.
        self.proximo = None

# Definindo a classe "ListaEncadeada" que representa a própria lista encadeada.
class ListaEncadeada:
    
    # O construtor da classe "__init__" é chamado quando um novo objeto 
    # ListaEncadeada é criado.
    def __init__(self):
        
        # O atributo "cabeca" da lista é inicializado como None, indicando 
        # que a lista está vazia.
        self.cabeca = None
        
        
    # Definindo um método chamado "deletar_do_inicio" na classe ListaEncadeada.
    def deletar_do_inicio(self):
        
        # Verificando se a lista está vazia, ou seja, se a cabeça (self.cabeca) está 
        # definida como None.
        if not self.cabeca:
            
            # Se a lista estiver vazia, exibimos uma mensagem informando que não 
            # há nada para deletar.
            print("Lista vazia. Não há o que deletar.")
            
            # Retornamos imediatamente para encerrar a função sem fazer mais nada.
            return
        
        # Se a lista não estiver vazia, atualizamos a cabeça (self.cabeca) para apontar 
        # para o próximo nó na lista.
        self.cabeca = self.cabeca.proximo
        
    
    # Definindo um método chamado "deletar_do_final" na classe ListaEncadeada.
    def deletar_do_final(self):
        
        # Verificando se a lista está vazia, ou seja, se a cabeça (self.cabeca) está 
        # definida como None.
        if not self.cabeca:
            
            # Se a lista estiver vazia, exibimos uma mensagem informando que não 
            # há nada para deletar.
            print("Lista vazia. Não há o que deletar.")
            
            # Retornamos imediatamente para encerrar a função sem fazer mais nada.
            return
        
        # Verificando se há apenas um elemento na lista (a cabeça aponta diretamente 
        # para esse elemento).
        if not self.cabeca.proximo:
            
            # Se houver apenas um elemento, removemos esse elemento, definindo a cabeça como None.
            self.cabeca = None
            
            # Retornamos imediatamente para encerrar a função.
            return
        
        # Se houver mais de um elemento na lista, precisamos encontrar o penúltimo elemento.
        # Criamos uma variável temporária "temp" para percorrer a lista a partir da cabeça.
        temp = self.cabeca
        
        # Entramos em um loop que percorre a lista até que "temp" seja o penúltimo elemento.
        while temp.proximo.proximo:
            
            temp = temp.proximo
            
        # Quando encontramos o penúltimo elemento, definimos o próximo dele como None para remover o último elemento.
        temp.proximo = None
        
        
    # Definindo um método chamado "deletar_por_valor" na classe ListaEncadeada.
    def deletar_por_valor(self, chave):
        
        # Verificando se a lista está vazia, ou seja, se a cabeça (self.cabeca) está 
        # definida como None.
        if not self.cabeca:
            
            # Se a lista estiver vazia, exibimos uma mensagem informando que não há 
            # nada para deletar.
            print("Lista vazia. Não há o que deletar.")
            
            # Retornamos imediatamente para encerrar a função sem fazer mais nada.
            return
        
        # Verificando se o valor a ser deletado está na cabeça da lista.
        if self.cabeca.dado == chave:
            
            # Se estiver na cabeça, removemos a cabeça e atualizamos a cabeça 
            # para o próximo elemento da lista.
            self.cabeca = self.cabeca.proximo
            
            # Retornamos imediatamente para encerrar a função.
            return
        
        # Se o valor não estiver na cabeça, criamos uma variável 
        # temporária "temp" para percorrer a lista a partir da cabeça.
        temp = self.cabeca
        
        # Entramos em um loop que percorre a lista até encontrar o nó 
        # que contém o valor desejado ou até o final da lista.
        while temp.proximo and temp.proximo.dado != chave:
            
            temp = temp.proximo
            
        # Se chegarmos ao final da lista sem encontrar o valor, exibimos 
        # uma mensagem informando que o valor não foi encontrado.
        if not temp.proximo:
            
            print(f"O valor {chave} não foi encontrado na lista.")
            
            # Retornamos imediatamente para encerrar a função.
            return
        
        # Se encontrarmos o nó com o valor desejado, ajustamos 
        # as referências para remover o nó da lista.
        temp.proximo = temp.proximo.proximo
        
    
    # Definindo um método chamado "imprimir_lista" na classe ListaEncadeada.
    def imprimir_lista(self):
        
        # Criamos uma variável temporária "temp" e inicializamos com a cabeça da lista.
        temp = self.cabeca
        
        # Entramos em um loop que percorre a lista a partir da cabeça até o último elemento.
        while temp:
            
            # Imprimimos o valor de dados (temp.dado) do nó atual, seguido por uma seta "->".
            print(temp.dado, end=' -> ')
            
            # Atualizamos "temp" para apontar para o próximo nó na lista.
            temp = temp.proximo
            
        # Quando chegamos ao final da lista (temp é None), imprimimos "None" para indicar o fim da lista.
        print("None")
        
        
# Verificando se este script está sendo executado como um programa independente.
if __name__ == "__main__":
    
    # Criando uma instância da classe ListaEncadeada chamada "lista".
    lista = ListaEncadeada()

    # Suponhamos que você tenha uma lista com valores e depois deseja deletá-los
    # Para este exemplo, vamos inserir alguns valores na lista para ilustrar a deleção

    # Inserindo valores na lista encadeada.
    lista.cabeca = No("A")
    lista.cabeca.proximo = No("B")
    lista.cabeca.proximo.proximo = No("C")
    
    # Imprimindo a lista encadeada após a inserção: "A -> B -> C -> None"
    lista.imprimir_lista()

    # Deletando o elemento do início da lista.
    lista.deletar_do_inicio()
    
    # Imprimindo a lista após a deleção do início: "B -> C -> None"
    lista.imprimir_lista()

    # Deletando o elemento do final da lista.
    lista.deletar_do_final()
    
    # Imprimindo a lista após a deleção do final: "B -> None"
    lista.imprimir_lista()

    # Inserindo um novo valor "C" na lista.
    lista.cabeca.proximo = No("C")

    # Deletando o elemento com valor "B" da lista.
    lista.deletar_por_valor("B")

    # Imprimindo a lista após a deleção por valor: "C -> None"
    lista.imprimir_lista()
    
    # Inserindo valores na lista encadeada.
    lista.cabeca = No("A")
    lista.cabeca.proximo = No("B")
    lista.cabeca.proximo.proximo = No("C")
    lista.cabeca.proximo.proximo.proximo = No("D")
    lista.cabeca.proximo.proximo.proximo.proximo = No("E")
    
    # Imprimindo a lista após a deleção por valor: "C -> None"
    lista.imprimir_lista()
    
    # Deletando o elemento com valor "B" da lista.
    lista.deletar_por_valor("D")
    
    # Imprimindo a lista após a deleção por valor: "C -> None"
    lista.imprimir_lista()