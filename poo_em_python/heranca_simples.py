"""
3. Pilares da POO

Introdução à Herança

            1. Conceitos básicos e definição de herança.
            2. Como a herança promove o reuso de código e a organização da estrutura do programa.
            
            
1. Conceitos Básicos e Definição de Herança

Herança é um dos pilares da Programação Orientada a Objetos. Ela permite que
uma nova classe herde os atributos e métodos de uma classe existente. 

A classe que é herdada é chamada de "classe base" ou "classe pai", enquanto 
a classe que herda é conhecida como "classe derivada" ou "classe filha".


2. Como a herança promove o reuso de código e a organização da estrutura do programa.

A herança ajuda a evitar a duplicação de código, pois a classe filha herda 
todos os métodos e atributos da classe pai. Isso torna o código mais reutilizável 
e fácil de manter. Além disso, a herança também contribui para uma melhor organização 
do código, já que as relações entre as classes pai e filha podem ser entendidas intuitivamente.

"""
print()
"""
3. Pilares da POO

    Tipos de Herança

            1. Herança Simples: Uma classe derivada de uma única classe base.
            2. Herança Múltipla: Uma classe derivada de mais de uma classe base.
            
        
1. Herança Simples: Uma classe derivada de uma única classe base.

A herança simples é um conceito de programação orientada
a objetos onde uma classe herda atributos e métodos de uma única 
classe pai.

Vamos criar um exemplo simples de herança que representa diferentes 
papéis em uma escola: Pessoa, Estudante e Professor.

A classe Pessoa é a classe pai e contém atributos e métodos comuns 
a todas as pessoas em uma escola, como nome e idade. 

As classes Estudante e Professor herdam da classe Pessoa e adicionam 
atributos e métodos específicos para estudantes e professores, respectivamente.

Aqui está o código:
"""

# Classe base (ou classe pai) chamada Pessoa. 
# Ela servirá como o modelo genérico para criar outras classes relacionadas.
class Pessoa:
    
    # Método construtor da classe Pessoa para inicializar os atributos nome e idade.
    def __init__(self, nome, idade):
        
        # Atribui o valor do argumento 'nome' ao atributo 'nome' da instância.
        self.nome = nome
        
        # Atribui o valor do argumento 'idade' ao atributo 'idade' da instância.
        self.idade = idade

    # Método para exibir informações sobre a Pessoa.
    def exibir_info(self):
        
        # Imprime as informações da Pessoa.
        print(f"Nome: {self.nome}, Idade: {self.idade}")
        
# Classe derivada (ou classe filha) chamada Estudante, que herda atributos e métodos 
# da classe Pessoa.
class Estudante(Pessoa):
    
    # Método construtor da classe Estudante para inicializar os atributos nome, 
    # idade e matricula.
    def __init__(self, nome, idade, matricula):
        
        # Chama o método construtor da classe pai (Pessoa) explicitamente.
        Pessoa.__init__(self, nome, idade)  
        
        # Atributo específico para Estudante.
        self.matricula = matricula  

    # Método para simular a ação de estudar.
    def estudar(self):
        
        # Imprime a ação de estudar.
        print(f"{self.nome} está estudando.")
        

# Classe derivada (ou classe filha) chamada Professor, 
# que também herda atributos e métodos da classe Pessoa.
class Professor(Pessoa):
    
    # Método construtor para a classe Professor.
    def __init__(self, nome, idade, disciplina):
        
        # Chama o método construtor da classe pai (Pessoa) explicitamente.
        Pessoa.__init__(self, nome, idade)
        
        # Atributo específico para Professor.
        self.disciplina = disciplina

    # Método para simular a ação de ensinar.
    def ensinar(self):
        
        # Imprime a ação de ensinar.
        print(f"{self.nome} está ensinando {self.disciplina}.")
        
    
# Criação de objetos

# Cria um objeto da classe Pessoa com o nome "Maria" e idade 40.
# O construtor da classe Pessoa será chamado, e os atributos 'nome' e 'idade' da instância serão inicializados.
pessoa = Pessoa("Maria", 40)

# Cria um objeto da classe Estudante com o nome "João", idade 20, e matrícula "12345".
# O construtor da classe Estudante será chamado, inicializando os atributos 'nome', 'idade' e 'matricula'.
estudante = Estudante("João", 20, "12345")

# Cria um objeto da classe Professor com o nome "Carlos", idade 50, e disciplina "Matemática".
# O construtor da classe Professor será chamado, inicializando os atributos 'nome', 'idade' e 'disciplina'.
professor = Professor("Carlos", 50, "Matemática")

# Exibindo informações
pessoa.exibir_info()
estudante.exibir_info()  # Método herdado da classe Pessoa
estudante.estudar()  # Método específico da classe Estudante
professor.exibir_info()  # Método herdado da classe Pessoa
professor.ensinar()  # Método específico da classe Professor
"""
Exercício Herança Simples:

Crie uma classe Animal que tenha um método fazer_som(). 
Essa classe será a classe pai para outras duas classes: Cachorro e Gato. 

Ambas as classes filhas deverão ter seus próprios métodos fazer_som() que 
sobrescrevem o método da classe pai. Além disso, a classe Cachorro 
deve ter um método latir() e a classe Gato um método miar().

    1. A classe Animal deve ter um método fazer_som() que imprime "O animal faz um som".
    2. A classe Cachorro deve ter um método fazer_som() que imprime "O cachorro faz woof-woof".
    3. A classe Gato deve ter um método fazer_som() que imprime "O gato faz miau".
    4. A classe Cachorro deve ter um método adicional chamado latir() que imprime "Woof-woof".
    5. A classe Gato deve ter um método adicional chamado miar() que imprime "Miau".

Crie objetos das classes Cachorro e Gato e chame seus métodos para 
testar se tudo está funcionando como esperado.
"""

#Solução

# 1. A classe Animal deve ter um método fazer_som() que imprime "O animal faz um som".

# Definindo uma classe Animal que atuará como classe pai (ou classe base)
class Animal:
    
    # Definindo um método chamado fazer_som dentro da classe Animal
    def fazer_som(self):
        
        print("O animal faz um som")  # Imprime uma mensagem padrão para qualquer animal

#---------------------------------------------------------------------

# 2. A classe Cachorro deve ter um método fazer_som() que imprime "O cachorro faz woof-woof".

# Definindo uma classe Cachorro que herda da classe Animal
class Cachorro(Animal):
    
    # Sobrescrevendo o método fazer_som para a classe Cachorro
    def fazer_som(self):
        
        print("O cachorro faz woof-woof")  # Imprime um som específico para cachorros

    # 4. A classe Cachorro deve ter um método adicional chamado latir() que imprime "Woof-woof".
    
    # Definindo um método adicional específico para a classe Cachorro
    def latir(self):
        
        print("Woof-woof")  # Imprime o som de um cachorro latindo


#---------------------------------------------------------------------

# 3. A classe Gato deve ter um método fazer_som() que imprime "O gato faz miau".

# Definindo uma classe Gato que também herda da classe Animal
class Gato(Animal):
    
    # Sobrescrevendo o método fazer_som para a classe Gato
    def fazer_som(self):
        
        print("O gato faz miau")  # Imprime um som específico para gatos

    # 5. A classe Gato deve ter um método adicional chamado miar() que imprime "Miau".
    
    # Definindo um método adicional específico para a classe Gato
    def miar(self):
        
        print("Miau")  # Imprime o som de um gato miando

        
# Criando um objeto da classe Animal e testando o seu método fazer_som
animal = Animal()

# Deverá imprimir "O animal faz um som", pois estamos usando o método da classe Animal
animal.fazer_som()

# Criando um objeto da classe Cachorro e testando os seus métodos
cachorro = Cachorro()

# Deverá imprimir "O cachorro faz woof-woof", pois estamos usando o método sobrescrito na classe Cachorro
cachorro.fazer_som()

# Deverá imprimir "Woof-woof", usando o método específico da classe Cachorro
cachorro.latir()

# Criando um objeto da classe Gato e testando os seus métodos
gato = Gato()

# Deverá imprimir "O gato faz miau", pois estamos usando o método sobrescrito na classe Gato
gato.fazer_som()

# Deverá imprimir "Miau", usando o método específico da classe Gato
gato.miar()