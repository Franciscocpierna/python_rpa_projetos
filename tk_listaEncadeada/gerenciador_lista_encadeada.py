"""
Exercício Gerenciador de Lista Encadeada

Imagine que você está desenvolvendo um sistema de gerenciamento 
de informações para uma empresa. Para essa tarefa, foi proposto o 
uso de uma estrutura de dados do tipo Lista Encadeada. Seu objetivo é implementar 
as operações básicas que permitam:

    1. Adicionar elementos na lista.
    2. Editar elementos existentes.
    3. Remover elementos da lista.
    4. Filtrar e visualizar elementos com base em um critério específico.
    5. Visualizar todos os elementos da lista.

Crie um menu interativo que permita ao usuário realizar todas essas operações facilmente.

    1 - Adicionar elemento
    2 - Editar elemento
    3 - Remover elemento
    4 - Filtrar elementos
    5 - Mostrar lista
    6 - Sair

"""

# Definindo a classe 'No', que representará um nó em 
# nossa lista encadeada.
class No:
    
    # O construtor da classe 'No' recebe um único 
    # argumento: o dado que o nó armazenará.
    def __init__(self, dado):
        
        # Atribuímos o dado recebido ao atributo 'dado' do nó.
        self.dado = dado
        
        # Inicialmente, o nó não aponta para outro nó, 
        # então seu atributo 'proximo' é None.
        self.proximo = None
        


# Definindo a classe 'ListaEncadeada', que representará 
# a lista encadeada em si.
class ListaEncadeada:
    
    # O construtor da classe 'ListaEncadeada' não recebe argumentos.
    def __init__(self):
        
        # Inicialmente, a lista está vazia, então o 
        # atributo 'cabeca', que representa o primeiro nó 
        # da lista, é None.
        self.cabeca = None
        
    # Definindo a função 'adicionar' para adicionar um novo nó no final da lista encadeada.
    def adicionar(self, dado):
        
        # Criamos um novo nó com o dado fornecido.
        novo_no = No(dado)

        # Se a cabeça (primeiro nó) da lista encadeada for None
        # (ou seja, a lista estiver vazia),
        if not self.cabeca:
            
            # definimos o novo nó como a cabeça da lista e saímos da função.
            self.cabeca = novo_no
            return

        # Se a lista já tiver elementos, começamos a partir da cabeça da lista.
        temp = self.cabeca

        # Percorremos a lista até encontrarmos o último nó (aquele que 
        # não aponta para outro nó).
        while temp.proximo:
            temp = temp.proximo

        # Adicionamos o novo nó ao final da lista, fazendo o último 
        # nó atual apontar para ele.
        temp.proximo = novo_no
        
    # Definindo a função 'editar' para modificar o valor de um nó específico na lista encadeada.
    def editar(self, antigo_dado, novo_dado):
        
        # Começamos a busca a partir da cabeça da lista.
        temp = self.cabeca

        # Percorremos cada nó da lista.
        while temp:
            
            # Verificamos se o dado do nó atual é igual ao dado antigo que queremos modificar.
            if temp.dado == antigo_dado:
                
                # Se encontrarmos, atualizamos o dado desse nó para o novo dado.
                temp.dado = novo_dado
                
                # Retornamos True, indicando que a operação foi bem-sucedida.
                return True

            # Se o dado do nó atual não for o que estamos procurando, 
            # movemos para o próximo nó na lista.
            temp = temp.proximo

        # Se terminarmos de percorrer a lista e não encontrarmos o dado antigo, 
        # retornamos False, indicando que a operação falhou.
        return False
    
    # Definindo a função 'remover' para eliminar um nó com um dado 
    # específico da lista encadeada.
    def remover(self, dado):

        # Começamos verificando a cabeça da lista.
        temp = self.cabeca

        # Se a lista não estiver vazia e o dado da cabeça for o que queremos remover...
        if temp and temp.dado == dado:
            
            # ... então, atualizamos a cabeça para apontar para o 
            # próximo nó, removendo efetivamente o nó atual.
            self.cabeca = temp.proximo
            
            # Retornamos True, indicando que a operação foi bem-sucedida.
            return True

        # Se o dado da cabeça não for o que estamos procurando, 
        # começamos a verificar os próximos nós.
        while temp and temp.proximo:
            
            # Se o dado do próximo nó for o que queremos remover...
            if temp.proximo.dado == dado:
                
                # ... então, fazemos o nó atual (temp) apontar para o 
                # nó depois do próximo, 
                # removendo efetivamente o próximo nó.
                temp.proximo = temp.proximo.proximo
                
                # Retornamos True, indicando que a operação foi bem-sucedida.
                return True

            # Se o dado do próximo nó não for o que estamos procurando,
            # movemos para o próximo nó na lista.
            temp = temp.proximo

        # Se terminarmos de percorrer a lista e não encontrarmos o dado,
        # retornamos False, indicando que a operação falhou.
        return False
    
    # Definindo a função 'filtrar' que permite buscar todos os nós que contêm 
    # um determinado filtro (substring) em seus dados.
    def filtrar(self, filtro):

        # Inicializando 'temp' para o primeiro nó (cabeça) da lista encadeada.
        temp = self.cabeca

        # Percorremos cada nó da lista até o final, ou seja, enquanto 'temp' não for None.
        while temp:

            # Checamos se o filtro (substring) está contido no dado do nó atual.
            # O operador 'in' é usado para verificar se uma substring está contida em outra string.
            if filtro in temp.dado:

                # Se o filtro estiver contido no dado do nó, imprimimos o dado desse nó.
                print(temp.dado)

            # Movemos para o próximo nó da lista.
            temp = temp.proximo
    
        
    # Definindo a função 'imprimir' que permite visualizar todos os 
    # nós da lista encadeada.
    def imprimir(self):

        # Inicializando 'temp' para o primeiro nó (cabeça) da lista encadeada.
        temp = self.cabeca

        # Percorrendo a lista encadeada enquanto 'temp' não for None (até chegar ao 
        # final da lista).
        while temp:

            # Imprimindo o dado atual do nó, seguido da seta '->'.
            # O parâmetro 'end' é usado para evitar a quebra de linha após a impressão, 
            # assim os dados são impressos na mesma linha.
            print(temp.dado, end=' -> ')

            # Movendo para o próximo nó da lista.
            temp = temp.proximo

        # Após percorrer toda a lista e imprimir todos os nós, imprimimos "None" para 
        # indicar o fim da lista.
        print("None")
        
        

# Verifica se este script está sendo executado como o script principal.
if __name__ == "__main__":

    # Instancia um objeto da classe ListaEncadeada chamado 'lista'.
    lista = ListaEncadeada()

    # Inicia um loop infinito para exibir o menu continuamente.
    while True:

        # Imprime as opções do menu.
        print("\nMenu:")
        print("1 - Adicionar elemento")
        print("2 - Editar elemento")
        print("3 - Remover elemento")
        print("4 - Filtrar elementos")
        print("5 - Mostrar lista")
        print("6 - Sair")

        # Solicita ao usuário que escolha uma opção.
        escolha = input("Escolha uma opção: ")

        # Verifica se a escolha do usuário foi "1".
        if escolha == "1":

            # Solicita ao usuário que insira um elemento.
            elemento = input("Digite o elemento a ser adicionado: ")

            # Adiciona o elemento inserido pelo usuário à lista encadeada.
            lista.adicionar(elemento)

        # Verifica se a escolha do usuário foi "2".
        elif escolha == "2":

            # Solicita ao usuário que informe o elemento atual que deseja editar.
            antigo_elemento = input("Digite o elemento a ser editado: ")

            # Solicita ao usuário que insira o novo valor para esse elemento.
            novo_elemento = input("Digite o novo valor para o elemento: ")

            # Chama a função 'editar' para tentar atualizar o elemento na lista.
            # Se a edição for bem-sucedida, imprime uma mensagem de sucesso.
            # Caso contrário, imprime uma mensagem informando que o elemento não foi encontrado.
            if lista.editar(antigo_elemento, novo_elemento):
                print("Elemento editado com sucesso!")
            else:
                print("Elemento não encontrado.")

        # Verifica se a escolha do usuário foi "3".
        elif escolha == "3":

            # Solicita ao usuário que insira o elemento que deseja remover.
            elemento = input("Digite o elemento a ser removido: ")

            # Chama a função 'remover' para tentar deletar o elemento da lista.
            # Se a remoção for bem-sucedida, imprime uma mensagem de sucesso.
            # Caso contrário, imprime uma mensagem informando que o elemento não foi encontrado.
            if lista.remover(elemento):
                print("Elemento removido com sucesso!")
            else:
                print("Elemento não encontrado.")

        # Verifica se a escolha do usuário foi "4".
        elif escolha == "4":

            # Solicita ao usuário que insira o filtro para a busca.
            filtro = input("Digite o filtro de busca: ")

            # Chama a função 'filtrar' para exibir os elementos que correspondem ao filtro.
            lista.filtrar(filtro)

        # Verifica se a escolha do usuário foi "5".
        elif escolha == "5":

            # Chama a função 'imprimir' para exibir todos os elementos da lista.
            lista.imprimir()

        # Verifica se a escolha do usuário foi "6".
        elif escolha == "6":

            # Imprime uma mensagem informando que o programa está saindo e encerra o loop.
            print("Saindo...")
            break

        # Se nenhuma das opções anteriores foi escolhida, informa ao usuário que a 
        # opção é inválida.
        else:
            print("Opção inválida. Tente novamente.")