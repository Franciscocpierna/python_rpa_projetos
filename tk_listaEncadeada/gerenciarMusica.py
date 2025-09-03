"""
Exemplo Prático: Gerenciamento de Músicas em um Player

Imagine um player de música simples. O usuário pode adicionar 
músicas à sua lista de reprodução, pular para a próxima música ou 
voltar para a música anterior. Nesse cenário, uma lista encadeada é 
perfeita, pois a ordem de reprodução é importante, e o usuário pode 
desejar adicionar ou remover músicas de qualquer posição na lista.

Passos:

    Criar a estrutura do nó para armazenar informações da música.
    Criar a estrutura da lista encadeada para gerenciar a lista de reprodução.
    Fornecer operações como: adicionar música, pular música, voltar música e listar músicas.

Implementação:
"""

# Definindo a classe 'Musica' que representará um elemento em 
# uma lista encadeada dupla.
class Musica:
    
    # Construtor da classe 'Musica'. É chamado quando uma nova 
    # instância da classe é criada.
    def __init__(self, titulo, artista):
        
        # Inicializando a propriedade 'titulo' do objeto com o valor 
        # do título passado como argumento.
        self.titulo = titulo
        
        # Inicializando a propriedade 'artista' do objeto com o valor do artista 
        # passado como argumento.
        self.artista = artista
        
        # Inicializando a propriedade 'proximo' com None. Esta propriedade 
        # apontará para a próxima música em uma lista encadeada.
        # No momento da criação, não há uma "próxima" música definida, então é 
        # inicializada com 'None'.
        self.proximo = None
        
        # Inicializando a propriedade 'anterior' com None. Esta propriedade apontará 
        # para a música anterior em uma lista encadeada dupla.
        # No momento da criação, não há uma "anterior" música definida, então é 
        # inicializada com 'None'.
        self.anterior = None
        
        
# Definindo a classe 'Player' que representará um player de músicas com
# capacidade de reprodução em lista encadeada dupla.
class Player:
    
    # Construtor da classe 'Player'. É chamado quando uma nova instância da classe é criada.
    def __init__(self):
        
        # Inicializando a propriedade 'atual' com None. 
        # Esta propriedade apontará para a música atualmente selecionada no player. 
        # No momento da criação, nenhuma música foi adicionada, então é 
        # inicializada com 'None'.
        self.atual = None

    # Método para adicionar uma música à lista encadeada do player.
    def adicionar_musica(self, titulo, artista):
        
        # Criando uma nova instância da classe 'Musica' com o título e artista fornecidos.
        nova_musica = Musica(titulo, artista)
        
        # Verificando se a propriedade 'atual' está vazia (não há músicas 
        # adicionadas ao player).
        if not self.atual:
            
            # Se estiver vazia, definimos a 'nova_musica' como a música 'atual'.
            self.atual = nova_musica
            
        else:
            
            # Se já houver músicas adicionadas, começamos pela música atual.
            ultima_musica = self.atual
            
            # Continuamos avançando na lista encadeada até encontrarmos
            # a última música (aquela que não tem um 'proximo').
            while ultima_musica.proximo:
                
                ultima_musica = ultima_musica.proximo
            
            # Conectamos a 'nova_musica' à última música da lista encadeada.
            ultima_musica.proximo = nova_musica
            
            # Como é uma lista duplamente encadeada, definimos a música anterior da 'nova_musica' 
            # como sendo a 'ultima_musica'.
            nova_musica.anterior = ultima_musica
            
    # Método para pular (avançar) para a próxima música na lista encadeada de músicas.
    def pular_musica(self):

        # Verifica se há uma música atualmente definida (sendo reproduzida ou selecionada).
        if self.atual:
            
            # Se houver, imprime uma mensagem informando que está pulando a música atual.
            print(f"Pulando '{self.atual.titulo}' de {self.atual.artista}.")

            # Verifica se a música atual tem uma música seguinte (proximo) na lista encadeada.
            if self.atual.proximo:
                
                # Se houver, muda a música atual para a próxima música.
                self.atual = self.atual.proximo
                
            else:
                
                # Se não houver uma próxima música (significando que a música atual é a última da lista),
                # imprime uma mensagem informando que o usuário está na última música da lista.
                print("Você está na última música da lista!")
                
        else:
            
            # Se não houver uma música atualmente definida (lista vazia ou nenhuma música selecionada),
            # imprime uma mensagem informando que nenhuma música está sendo reproduzida.
            print("Nenhuma música está sendo reproduzida.")
            
            
    # Método para voltar (retroceder) para a música anterior na lista encadeada de músicas.
    def voltar_musica(self):

        # Verifica se há uma música atualmente definida (sendo reproduzida ou selecionada).
        if self.atual:
            
            # Se houver, imprime uma mensagem informando que está voltando da música atual.
            print(f"Voltando da música '{self.atual.titulo}' de {self.atual.artista}.")

            # Verifica se a música atual tem uma música anterior (anterior) na lista encadeada.
            if self.atual.anterior:
                
                # Se houver, muda a música atual para a música anterior.
                self.atual = self.atual.anterior
                
            else:
                
                # Se não houver uma música anterior (significando que a música atual é a primeira da lista),
                # imprime uma mensagem informando que o usuário está na primeira música da lista.
                print("Você está na primeira música da lista!")
                
        else:
            
            # Se não houver uma música atualmente definida (lista vazia ou nenhuma música selecionada),
            # imprime uma mensagem informando que nenhuma música está sendo reproduzida.
            print("Nenhuma música está sendo reproduzida.")
            
            
    # Método para listar todas as músicas a partir da música atual até o 
    # fim da lista encadeada.
    def listar_musicas(self):

        # Inicializa uma variável temporária 'temp' com a música atual.
        # Esta variável será usada para percorrer a lista encadeada.
        temp = self.atual

        # O loop 'while' irá iterar enquanto houver uma música na 
        # variável 'temp' (enquanto temp não for None).
        while temp:
            
            # Imprime os detalhes da música atualmente apontada pela variável 'temp'.
            print(f'Título: {temp.titulo}, Artista: {temp.artista}')

            # Move a variável 'temp' para a próxima música na lista encadeada.
            # Se 'temp.proximo' for None (não houver próxima música), o loop 
            # será encerrado.
            temp = temp.proximo
            
            
    # Método para exibir a música que está sendo tocada atualmente.
    def musica_atual(self):

        # Verifica se há uma música atualmente definida (se 'self.atual' não for None).
        if self.atual:

            # Imprime o título e o artista da música que está atualmente definida como 'atual'.
            print(f'Tocando agora: {self.atual.titulo} de {self.atual.artista}')

        else:
            
            # Caso não haja música definida como 'atual' (por exemplo, a lista de músicas pode estar vazia),
            # essa mensagem será exibida.
            print("Nenhuma música está sendo reproduzida.")


# Testando o player

# Criação de uma instância da classe Player chamada "player".
player = Player()

# Adiciona três músicas à instância "player" usando o método adicionar_musica.
player.adicionar_musica("Imagine", "John Lennon")  # Adiciona a música "Imagine" do "John Lennon" à lista.
player.adicionar_musica("Bohemian Rhapsody", "Queen")  # Adiciona a música "Bohemian Rhapsody" do "Queen" à lista.
player.adicionar_musica("Like a Rolling Stone", "Bob Dylan")  # Adiciona a música "Like a Rolling Stone" do "Bob Dylan" à lista.

# Imprime o título para indicar que as músicas na lista de reprodução serão listadas.
print("Músicas na lista de reprodução:")

# Chama o método listar_musicas para exibir todas as músicas presentes na lista de reprodução do player.
player.listar_musicas()

# Indica que a música atualmente em reprodução será exibida.
print("\nMúsica Atual")

# Chama o método musica_atual para exibir a música que está sendo tocada no momento.
player.musica_atual()

# Indica que uma ação para pular a música atual será realizada.
print("\nPular música")

# Chama o método pular_musica para avançar para a próxima música na lista de reprodução.
player.pular_musica()

# Novamente, indica que a música atualmente em reprodução será exibida.
print("\nMúsica Atual")

# Chama o método musica_atual para exibir a música que está sendo tocada agora (depois de pular a anterior).
player.musica_atual()

# Indica que uma ação para voltar à música anterior será realizada.
print("\nVoltar Música")

# Chama o método voltar_musica para retornar à música anterior na lista de reprodução.
player.voltar_musica()

# Mais uma vez, indica que a música atualmente em reprodução será exibida.
print("\nMúsica Atual")

# Chama o método musica_atual para exibir a música que está sendo tocada 
# agora (depois de voltar à anterior).
player.musica_atual()