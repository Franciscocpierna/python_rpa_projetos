# 1. Classes e Objetos

# Vamos criar uma classe Livro que representa um livro em nossa biblioteca.
# Definindo uma classe chamada Livro
class Livro:
    
    # O construtor da classe com três parâmetros: título, autor e ano
    
    """
        def:
            Esta é uma palavra-chave em Python usada para definir uma função.

    __init__:
        Este é um método especial ou um "método mágico" em Python. Ele é o construtor da 
        classe. Sempre que você cria uma instância de uma classe (ou seja, um objeto da classe), 
        este método é automaticamente chamado.
        
        A principal utilidade do método __init__ é inicializar os atributos do objeto recém-criado.

        (self, titulo, autor, ano): Estes são os parâmetros do método __init__.

        self: É uma referência ao objeto atual ou à instância da classe. Em 
        Python, é uma convenção chamá-lo de "self", mas tecnicamente, você 
        poderia dar a ele qualquer nome que quiser (embora isso possa ser confuso). Quando 
        você cria uma instância de uma classe e chama um de seus métodos, Python 
        automaticamente passa essa instância específica como o primeiro argumento para 
        o método. Por isso, você precisa ter self como o primeiro parâmetro de todos os 
        métodos de instância, para que eles possam acessar e modificar os atributos ou 
        chamar outros métodos da mesma instância.

        titulo, autor, ano: São parâmetros adicionais que você passa quando cria uma 
        instância da classe Livro. Eles são usados para inicializar os atributos correspondentes 
        do objeto. No contexto do código fornecido, são usados para armazenar informações sobre 
        o título, o autor e o ano de publicação de um livro.
    """
    def __init__(self, titulo, autor, ano):
        
        # Atribuindo o valor do parâmetro título à variável de instância titulo
        self.titulo = titulo
        
        # Atribuindo o valor do parâmetro autor à variável de instância autor
        self.autor = autor
        
        # Atribuindo o valor do parâmetro ano à variável de instância ano
        self.ano = ano

# Instanciando (criando) um objeto da classe Livro e passando os valores "1984", "George Orwell" e 1949 
# como argumentos
     # Definindo um método chamado descricao: Este método retorna uma descrição formatada do livro.
    # Métodos são funções que pertencem a um objeto.
    def descricao(self):
        
        # Retornando uma string formatada que descreve o livro.
        # O método usa os atributos da instância (titulo, autor, ano) para criar essa descrição.
        return f"'{self.titulo}' por {self.autor}, publicado em {self.ano}"

meu_livro = Livro("1984", "George Orwell", 1949)

#No código acima, Livro é uma classe que tem um construtor __init__. 
#Usando a classe Livro, criamos um objeto meu_livro que representa o
#livro "1984" escrito por "George Orwell" e publicado em 1949.


#2. Atributos

#A classe Livro tem três atributos: titulo, autor e ano. Estes 
# são definidos e inicializados no construtor __init__.

#Acessando os atributos do objeto meu_livro:

print(meu_livro.titulo)  # Saída: 1984
print(meu_livro.autor)   # Saída: George Orwell
print(meu_livro.ano)     # Saída: 1949

# Instanciando e chamando o método
# Criando um novo objeto 'meu_livro' da classe Livro
# Nós passamos três argumentos: "1984" para o título, "George Orwell" 
# para o autor e 1949 para o ano.
meu_livro = Livro("1984", "George Orwell", 1949)

# Chamando o método 'descricao' do objeto 'meu_livro'
# Isso irá executar o método 'descricao' definido na classe Livro e imprimir a 
# descrição do livro.
print(meu_livro.descricao())  # Saída: '1984' por George Orwell, publicado em 1949
print(meu_livro) #<__main__.Livro object at 0x000002B7F0E14B90>

class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca      # Define o atributo marca do carro com o valor fornecido
        self.modelo = modelo    # Define o atributo modelo do carro com o valor fornecido
        self.cor = cor          # Define o atributo cor do carro com o valor fornecido
        self.velocidade = 0     # Inicializa o atributo velocidade atual do carro com 0
# Método que aumenta a velocidade do carro em 10 km/h
    def acelerar(self):
        
        # Incrementa a velocidade atual em 10 km/h
        # self.velocidade = self.velocidade + 10
        self.velocidade += 10
        
        # Exibe a velocidade atual do carro
        print(f"Velocidade atual: {self.velocidade} km/h")
        
    # Método que diminui a velocidade do carro em 10 km/h
    def frear(self):
        
        # Decrementa a velocidade atual em 10 km/h
        # self.velocidade = self.velocidade - 10
        self.velocidade -= 10
        
        # Garante que a velocidade não se torne negativa
        if self.velocidade < 0:
            self.velocidade = 0
        
        # Exibe a velocidade atual do carro
        print(f"Velocidade atual: {self.velocidade} km/h")
        
    # Método que exibe as informações básicas do carro
    def exibir_info(self):
        
        # Exibe a marca, modelo e cor do carro
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}")
        
        
# Instanciando objetos da classe Carro
carro1 = Carro("Toyota", "Corolla", "Branco")

carro1.exibir_info()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.frear()
carro1.frear()
carro1.frear()
carro1.frear()
carro1.frear()
carro1.frear()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.frear()

# Instanciando objetos da classe Carro
carro2 = Carro("Ford", "Fiesta", "Azul")

print("\n -------- \n")

carro2.exibir_info()
carro2.acelerar()
carro2.acelerar()
carro2.frear()

'''
Introdução à POO
O que é Programação Orientada a Objetos (POO)


Programação Orientada a Objetos (POO) é um paradigma de programação que utiliza objetos e classes para organizar o código fonte. Este paradigma foi criado com o objetivo de combinar dados e funcionalidades em entidades autônomas chamadas "objetos". Estes objetos são instâncias de "classes", que podem ser vistas como modelos ou protótipos para a criação de objetos. A POO oferece uma abstração mais natural e reutilizável do código, permitindo uma melhor organização, escalabilidade e manutenção.



Como a POO se diferencia da programação procedural


Abstração: Enquanto o paradigma procedural foca em rotinas e procedimentos, a POO foca em objetos que contêm tanto estado (dados) quanto comportamento (métodos).

Encapsulamento: Em POO, os dados e métodos que operam esses dados são agrupados em uma única entidade, permitindo que o estado do objeto seja modificado apenas através de métodos específicos.

Herança: A POO permite a criação de novas classes baseadas em classes existentes. Isso facilita a reutilização de código e pode reduzir a complexidade através da herança de funcionalidades.

Polimorfismo: Permite que objetos de diferentes classes sejam tratados como objetos de uma classe comum, tornando o código mais extensível e fácil de manter.



Vantagens da POO


Reutilização de Código: A herança e o polimorfismo facilitam a reutilização de código.

Manutenibilidade: O encapsulamento e a abstração tornam o código mais fácil de entender e manter.

Extensibilidade: É mais fácil adicionar novas funcionalidades a um sistema orientado a objetos sem alterar o código existente, graças ao conceito de polimorfismo.

Modelagem Natural: A POO fornece uma representação mais natural e intuitiva de entidades do mundo real, tornando o código mais compreensível.

Testabilidade: A encapsulação permite que você isole partes do seu sistema, tornando mais fácil o processo de testes unitários.

'''

