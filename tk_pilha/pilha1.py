"""
Exercício: Simulação de Livros em uma Biblioteca

Imagine uma mesa em uma biblioteca onde os estudantes colocam os 
livros que já leram. A mesa foi projetada de forma que só pode conter 
uma pilha de livros. Cada vez que um estudante lê um livro, ele o coloca 
no topo da pilha. E cada vez que um bibliotecário precisa guardar um 
livro de volta na estante, ele sempre pega o livro do topo da pilha.

Tarefas:

    1. Crie uma classe PilhaDeLivros:
    
        - A classe deve ter uma lista privada _livros 
            que inicialmente está vazia.
        
        - Deve ter métodos para adicionar_livro, 
                                remover_livro, 
                                ver_topo, 
                                esta_vazia e quantidade.

    2. Simule o seguinte cenário usando a classe PilhaDeLivros:

        a. Cinco estudantes leram, em sequência, os 
            livros: "Livro A", "Livro B", "Livro C", "Livro D" e "Livro E". 
            Eles colocam cada livro na pilha após a leitura.

        b. Um bibliotecário vem e precisa guardar três livros de volta na 
            estante. Ele pega os livros do topo da pilha. Quais são os livros 
            que ele guardou?

        c. Dois estudantes vêm e colocam os livros "Livro F" e "Livro G" na 
            pilha, respectivamente.

        d. Outro bibliotecário vem e pega dois livros do topo para guardá-los. Quais 
            são os livros?

    Perguntas para reflexão:
    
        - Qual foi o último livro lido pelos estudantes e qual foi o primeiro a 
              ser guardado pelos bibliotecários?
        
        - Qual é o estado final da pilha após todas as ações?
        
        - Baseado nesse exercício, você pode explicar o conceito 
              de Last In, First Out (LIFO)?

Objetivo:

Este exercício ajuda a entender o conceito fundamental do LIFO, onde 
o último item adicionado à pilha é o primeiro a ser removido dela. Ao 
simular o cenário com livros em uma biblioteca, podem visualizar e 
compreender melhor a natureza da pilha e suas operações.
"""

# Solução

"""
1. Crie uma classe PilhaDeLivros:
    
        - A classe deve ter uma lista privada _livros 
            que inicialmente está vazia.
        
        - Deve ter métodos para adicionar_livro, 
                                remover_livro, 
                                ver_topo, 
                                esta_vazia e quantidade.
""" 

# Define uma nova classe chamada "PilhaDeLivros"
class PilhaDeLivros:
    
        # Método construtor para inicializar uma nova instância da classe
        def __init__(self):

            """
            - A classe deve ter uma lista privada _livros 
                que inicialmente está vazia.
            """

            # Define um atributo privado chamado '_livros' para a classe
            # Este atributo é uma lista que vai armazenar os livros na pilha
            # O prefixo de sublinhado (_) indica que é uma convenção em Python
            # para denotar que este atributo deve ser tratado como "privado"
            # ou seja, não deve ser acessado diretamente fora da classe
            self._livros = []


            """
            - Deve ter métodos para adicionar_livro, 
                                        remover_livro, 
                                        ver_topo, 
                                        esta_vazia e quantidade.
            """

        # Define um método chamado 'adicionar_livro' para a classe PilhaDeLivros
        def adicionar_livro(self, livro):
            
            # Utiliza o método 'append' da lista para adicionar o livro passado como 
            # argumento ao final da lista '_livros', que simula o topo da pilha.
            self._livros.append(livro)
            
        # Define um método chamado 'remover_livro' para a classe PilhaDeLivros
        def remover_livro(self):
           
            # Verifica se a pilha (lista '_livros') está vazia usando o método 'esta_vazia' 
            # (que ainda não foi definido neste código, mas assume-se que esteja presente na classe)
            if not self.esta_vazia():
                
                # Se a pilha não estiver vazia, utiliza o método 'pop' da lista para remover 
                # e retornar o último item da lista '_livros', que simula o topo da pilha.
                return self._livros.pop()
            
            else:
                
                # Se a pilha estiver vazia, retorna None, indicando que não há livro para remover.
                return None
            
        # Define um método chamado 'ver_topo' para a classe PilhaDeLivros
        def ver_topo(self):
            
            # Verifica se a pilha (lista '_livros') está vazia usando o método 'esta_vazia'
            if not self.esta_vazia():
                
                # Se a pilha não estiver vazia, retorna o último livro da lista '_livros'
                # (ou seja, o livro no topo da pilha) usando a indexação '-1'
                return self._livros[-1]
            
            else:
                
                # Se a pilha estiver vazia, retorna None, indicando que não há livro no topo.
                return None

            
        # Define um método chamado 'esta_vazia' para a classe PilhaDeLivros
        def esta_vazia(self):
            
            # Retorna True se o comprimento da lista '_livros' for 0 (indicando que a pilha está vazia)
            # e False caso contrário
            return len(self._livros) == 0
        
        
        # Define um método chamado 'quantidade' para a classe PilhaDeLivros
        def quantidade(self):
            
            # Retorna o número de livros na pilha (ou seja, o comprimento da lista '_livros')
            return len(self._livros)
        

"""
2. Simule o seguinte cenário usando a classe PilhaDeLivros:

        a. Cinco estudantes leram, em sequência, os 
            livros: "Livro A", "Livro B", "Livro C", "Livro D" e "Livro E". 
            Eles colocam cada livro na pilha após a leitura.

        b. Um bibliotecário vem e precisa guardar três livros de volta na 
            estante. Ele pega os livros do topo da pilha. Quais são os livros 
            que ele guardou?

        c. Dois estudantes vêm e colocam os livros "Livro F" e "Livro G" na 
            pilha, respectivamente.

        d. Outro bibliotecário vem e pega dois livros do topo para guardá-los. Quais 
            são os livros?
"""

"""
a. Cinco estudantes leram, em sequência, os 
            livros: "Livro A", "Livro B", "Livro C", "Livro D" e "Livro E". 
            Eles colocam cada livro na pilha após a leitura.
"""

# Cria uma nova instância da classe PilhaDeLivros e armazena-a na variável chamada 'pilha'
pilha = PilhaDeLivros()

# Usa o método 'adicionar_livro' da instância 'pilha' para adicionar "Livro A" ao topo da pilha de livros
pilha.adicionar_livro("Livro A")

# Novamente, usa o método 'adicionar_livro' para adicionar "Livro B" ao topo da pilha
# Agora, "Livro B" está no topo e "Livro A" fica logo abaixo dele
pilha.adicionar_livro("Livro B")

# Continua a adicionar livros à pilha. Cada novo livro é colocado no topo, 
# acima dos livros anteriormente adicionados
pilha.adicionar_livro("Livro C")

# Adiciona "Livro D" ao topo da pilha
pilha.adicionar_livro("Livro D")

# Adiciona "Livro E" ao topo da pilha. Agora, a ordem da pilha, de baixo para 
# cima, é: A, B, C, D, E
pilha.adicionar_livro("Livro E")


"""
b. Um bibliotecário vem e precisa guardar três livros de volta na 
            estante. Ele pega os livros do topo da pilha. Quais são os livros 
            que ele guardou?
"""

# livros_guardados1 = [pilha.remover_livro() for _ in range(3)]

# Inicializa uma lista vazia chamada 'livros_guardados1'. 
# Esta lista será usada para armazenar os livros que o bibliotecário irá guardar.
livros_guardados1 = []

# O loop 'for' irá rodar 3 vezes porque queremos que o bibliotecário guarde 3 livros.
for _ in range(3):

    # Dentro do loop, o método 'remover_livro' é chamado na instância 'pilha'.
    # Isso irá remover o livro do topo da pilha (devido ao comportamento LIFO da pilha) 
    # e o valor retornado (o livro removido) é armazenado na variável 'livro'.
    livro = pilha.remover_livro()

    # O livro removido é então adicionado à lista 'livros_guardados1' usando o método 'append'.
    livros_guardados1.append(livro)

# Após o loop terminar, a lista 'livros_guardados1' contém os 3 livros que o bibliotecário guardou.
# Estes são impressos na tela.
print("O bibliotecário guardou:", livros_guardados1)


"""
c. Dois estudantes vêm e colocam os livros "Livro F" e "Livro G" na 
            pilha, respectivamente.
"""

# Aqui, estamos chamando o método 'adicionar_livro' na instância 'pilha' e 
# passando o argumento "Livro F".
# Isso irá adicionar "Livro F" no topo da pilha. 
# Lembre-se, a pilha tem um comportamento LIFO (Last In, First Out), então o 
# último livro adicionado
# fica no topo e será o primeiro a ser removido.
pilha.adicionar_livro("Livro F")

# Agora, estamos adicionando "Livro G" ao topo da pilha da mesma maneira.
# Como "Livro G" é adicionado após "Livro F", ele agora será o livro no topo da pilha.
pilha.adicionar_livro("Livro G")


"""
d. Outro bibliotecário vem e pega dois livros do topo para guardá-los. Quais 
            são os livros?
"""
# livros_guardados2 = [pilha.remover_livro() for _ in range(2)]

# Aqui, estamos inicializando uma lista vazia chamada 'livros_guardados2'. 
# Esta lista será usada para armazenar os livros que o segundo bibliotecário guarda.
livros_guardados2 = []

# O 'for' loop irá rodar exatamente 2 vezes. Isto é indicado por 'range(2)'.
# Para cada iteração (rodada) deste loop, nós faremos as seguintes ações:
for _ in range(2):
    
    # Aqui, estamos chamando o método 'remover_livro' na instância 'pilha'.
    # Isso removerá e retornará o livro do topo da pilha.
    livro = pilha.remover_livro()

    # Agora, estamos adicionando o livro retornado (ou seja, o livro removido do topo da pilha)
    # à lista 'livros_guardados2'.
    livros_guardados2.append(livro)

# Após o loop terminar (ou seja, após 2 livros serem removidos da pilha e adicionados à lista),
# nós imprimimos os livros que o segundo bibliotecário guardou.
print("O segundo bibliotecário guardou:", livros_guardados2)

# Perguntas para reflexão:

"""
    Qual foi o último livro lido pelos estudantes e qual foi o primeiro a 
    ser guardado pelos bibliotecários?

        Resposta: O último livro lido pelos estudantes foi o "Livro G". O primeiro 
        livro a ser guardado pelos bibliotecários foi o "Livro E" (pois é o último 
        adicionado e o primeiro a ser removido devido ao princípio LIFO).

    Qual é o estado final da pilha após todas as ações?

        Resposta: Após todas as ações, os livros remanescentes na pilha, do 
        topo para a base, são: ["Livro A", "Livro B"].

    Baseado nesse exercício, você pode explicar o conceito de Last In, First Out (LIFO)?

        Resposta: Sim. Last In, First Out (LIFO) significa que o último item inserido 
        em uma pilha será o primeiro a ser removido dela. No cenário, o último livro 
        que os estudantes leram e colocaram no topo da pilha foi sempre o primeiro 
        a ser guardado pelos bibliotecários. Isso demonstra claramente o princípio 
        LIFO em ação, onde a última ação de "inserção" (adicionar um livro) tem sua 
        correspondente ação de "remoção" (remover um livro) ocorrendo antes de qualquer 
        ação de inserção anterior.
"""
print()