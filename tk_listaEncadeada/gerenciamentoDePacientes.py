"""
Exemplo Prático: Gerenciamento de Pacientes em um Consultório Médico

Considere um consultório médico onde os pacientes são atendidos 
por ordem de chegada (a não ser em casos de emergência). Uma lista 
encadeada é apropriada para gerenciar essa fila de espera, pois permite 
inserções e remoções eficientes.

Passos:

    1. Criar a estrutura do nó para armazenar informações do paciente.
    2. Criar a estrutura da lista encadeada para gerenciar a fila de pacientes.
    3. Fornecer operações como: registrar paciente, chamar próximo 
    paciente, e listar todos os pacientes.

Implementação:
"""

# Criando uma classe chamada Paciente.
class Paciente:
    
    # Método construtor da classe. Quando um objeto desta classe for criado, 
    # este método será chamado automaticamente.
    def __init__(self, nome, motivo):
        
        # Atributo 'nome' do objeto, que armazena o nome do paciente. 
        # O valor deste atributo é passado como argumento quando o objeto é criado.
        self.nome = nome
        
        # Atributo 'motivo' do objeto, que armazena o motivo da consulta ou hospitalização do paciente. 
        # O valor deste atributo é passado como argumento quando o objeto é criado.
        self.motivo = motivo
        
        # Atributo 'proximo' do objeto. Serve para referenciar o próximo objeto da 
        # lista encadeada (caso exista). 
        # Inicialmente, é definido como None, indicando que não há próximo paciente por padrão.
        self.proximo = None
        
# Criando uma classe chamada FilaDeEspera. A ideia por trás dessa classe é representar 
# uma fila de espera comum, 
# onde o primeiro paciente que entra é o primeiro a ser atendido (First In First Out - FIFO).
class FilaDeEspera:
    
    # Método construtor da classe. Ele é chamado automaticamente sempre que um objeto dessa classe é criado.
    def __init__(self):
        
        # Atributo 'primeiro' da fila de espera. Ele armazena uma referência para o primeiro paciente (objeto) na fila. 
        # Inicialmente, é definido como None, indicando que a fila está vazia e não há paciente esperando.
        self.primeiro = None
        
        # Atributo 'ultimo' da fila de espera. Ele armazena uma referência para o último paciente (objeto) na fila.
        # Assim como o 'primeiro', ele é inicialmente definido como None, indicando que a fila está vazia.
        self.ultimo = None


    # Definindo o método 'registrar_paciente' dentro da classe FilaDeEspera.
    # Esse método é responsável por adicionar um novo paciente à fila de espera.
    def registrar_paciente(self, nome, motivo):

        # Criando uma nova instância do objeto 'Paciente' com os valores de 'nome' e 'motivo' fornecidos como parâmetros.
        novo_paciente = Paciente(nome, motivo)

        # Verifica se a fila de espera está vazia (ou seja, o primeiro paciente não existe).
        if not self.primeiro:

            # Se a fila estiver vazia, o 'novo_paciente' se torna o primeiro da fila.
            self.primeiro = novo_paciente

            # Também definimos o 'novo_paciente' como o último da fila, pois ele é o único paciente na fila no momento.
            self.ultimo = self.primeiro

        else: # Caso em que já existem pacientes na fila.

            # O próximo paciente após o atual 'último' na fila é definido como o 'novo_paciente'.
            self.ultimo.proximo = novo_paciente

            # Atualizamos o 'ultimo' da fila para referenciar o 'novo_paciente', 
            # pois ele agora é o último paciente na fila de espera.
            self.ultimo = novo_paciente
            
    # Definindo o método 'chamar_proximo_paciente' dentro da classe FilaDeEspera.
    # Esse método é responsável por chamar o próximo paciente na fila de espera para ser atendido.
    def chamar_proximo_paciente(self):

        # Verifica se a fila de espera está vazia (ou seja, o primeiro paciente não existe).
        if not self.primeiro:

            # Se a fila estiver vazia, exibe uma mensagem informando que não há 
            # pacientes para serem atendidos.
            print("Não há pacientes na fila.")
            return  # Termina a execução do método.

        # Se a fila não estiver vazia, obtemos a referência para o primeiro 
        # paciente que está sendo chamado para atendimento.
        paciente_chamado = self.primeiro

        # Atualiza o 'primeiro' da fila para ser o próximo paciente depois do atual 'primeiro'.
        # Em outras palavras, removemos o paciente atual da frente da fila.
        self.primeiro = self.primeiro.proximo

        # Exibe uma mensagem informando o nome do paciente que foi chamado para atendimento.
        print(f"Paciente {paciente_chamado.nome} foi chamado para o atendimento!")
        
    # Definindo o método 'listar_pacientes' dentro da classe FilaDeEspera.
    # Esse método é responsável por listar todos os pacientes que estão 
    # na fila de espera.
    def listar_pacientes(self):

        # Iniciamos com o primeiro paciente da fila.
        # A variável 'temp' será usada para navegar pela fila, começando 
        # pelo primeiro paciente.
        temp = self.primeiro

        # Utilizamos um loop 'while' para percorrer todos os pacientes na fila.
        # O loop continua enquanto a variável 'temp' estiver apontando 
        # para um paciente (ou seja, enquanto 'temp' não for None).
        while temp:

            # Dentro do loop, imprimimos o nome e o motivo do paciente ao 
            # qual 'temp' está atualmente apontando.
            print(f'Nome: {temp.nome}, Motivo: {temp.motivo}')

            # Atualizamos a variável 'temp' para apontar para o próximo paciente na fila.
            # Fazemos isso para avançar na fila e, eventualmente, chegar ao final dela.
            temp = temp.proximo
            
            
# Iniciando o teste da classe FilaDeEspera.

# Criando uma instância da classe FilaDeEspera e armazenando-a na variável 'consultorio'.
# Agora temos um 'consultorio' que representa uma fila de espera vazia.
consultorio = FilaDeEspera()

# Utilizando o método 'registrar_paciente' para adicionar o paciente "João" 
# com o motivo "Dor de cabeça" à fila.
consultorio.registrar_paciente("João", "Dor de cabeça")

# Adicionando a paciente "Maria" com o motivo "Check-up anual" à fila de espera.
consultorio.registrar_paciente("Maria", "Check-up anual")

# Adicionando o paciente "Lucas" com o motivo "Febre" à fila de espera.
consultorio.registrar_paciente("Lucas", "Febre")

# Imprimindo uma mensagem para indicar que os pacientes na fila de espera 
# serão listados a seguir.
print("Pacientes na fila de espera:")

# Utilizando o método 'listar_pacientes' para exibir todos os pacientes
# atualmente na fila de espera.
consultorio.listar_pacientes()

# Utilizando o método 'chamar_proximo_paciente' para chamar o próximo paciente 
# na fila de espera para atendimento.
# Este método também irá remover esse paciente da fila.
consultorio.chamar_proximo_paciente()

print("\n")

# Imprimindo uma mensagem para indicar que os pacientes na fila de espera, após 
# o primeiro ser chamado, serão listados a seguir.
print("\nPacientes na fila de espera após o primeiro ser chamado:")

# Novamente, usando o método 'listar_pacientes' para exibir os pacientes 
# restantes na fila de espera.
consultorio.listar_pacientes()


# Chamando o próximo paciente na fila para atendimento.
consultorio.chamar_proximo_paciente()

print("\n")

# Novamente, usando o método 'listar_pacientes' para exibir os pacientes 
# restantes na fila de espera.
consultorio.listar_pacientes()

# Chamando o próximo paciente na fila para atendimento.
consultorio.chamar_proximo_paciente()