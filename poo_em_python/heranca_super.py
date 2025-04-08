"""
Pilares da POO

    Herança: Criando novas classes a partir de classes existentes.
        Uso da função super().
        
        
A função super() em Python é usada para chamar um método da classe pai 
dentro da classe derivada. Isso é útil quando você quer estender ou modificar 
o comportamento de um método herdado sem substituí-lo completamente.

Vejamos um exemplo prático. Suponha que você tem uma classe Animal com um 
método falar(). Você quer criar uma classe Cachorro que herda de Animal e 
estende o método falar() para incluir um comportamento adicional.
"""


# Definindo uma classe chamada Animal, que servirá como a superclasse (classe pai).
class Animal:
    
    # Definindo um método chamado falar() dentro da classe Animal.
    def falar(self):
        
        # Quando o método falar() é chamado, ele imprime a string "O animal está falando".
        print("O animal está falando")

# Definindo uma classe chamada Cachorro, que herda da classe Animal (portanto, é uma subclasse).
class Cachorro(Animal):
    
    # Sobrescrevendo o método falar() da classe pai (Animal) na subclasse (Cachorro).
    def falar(self):
        
        # Chamando o método falar() da classe pai (Animal) usando super().
        # Isso é feito para que a subclasse também execute o comportamento da superclasse.
        super().falar()
        
        # Imprime uma string específica para a classe Cachorro.
        print("O cachorro diz: Au au")

# Criando uma instância da classe Animal e armazenando-a na variável 'animal'.
animal = Animal()

# Chamando o método falar() da classe Animal usando a instância 'animal'.
# Isso imprimirá "O animal está falando".
animal.falar()

# Criando uma instância da classe Cachorro e armazenando-a na variável 'cachorro'.
cachorro = Cachorro()

# Chamando o método falar() da classe Cachorro usando a instância 'cachorro'.
# Isso imprimirá "O animal está falando" e também "O cachorro diz: Au au" porque
# o método da superclasse também é chamado.
cachorro.falar()

# Saída:
# O animal está falando
# O cachorro diz: Au au

"""
No exemplo acima, o método falar() da classe Cachorro chama o 
método falar() da classe pai Animal usando super().falar(). 

Isso assegura que o comportamento da classe pai seja preservado, e 
então adiciona um comportamento adicional ("O cachorro diz: Au au").

Isso é particularmente útil em situações onde o método da classe pai é 
complexo e você não quer reescrevê-lo completamente na classe filha. 

Você simplesmente chama o método original com super() e adiciona o 
comportamento adicional que você precisa.
"""
print()
"""
Exercício: Estendendo a Classe Veiculo usando super()

Neste exercício, você trabalhará com uma classe Veiculo e uma 
subclasse Carro. O objetivo é usar a função super() para estender a 
funcionalidade da classe pai Veiculo na classe filha Carro.

    Passo 1: Defina a Classe Pai

        Crie uma classe chamada Veiculo que tenha um método 
        exibir_info() para exibir informações sobre o veículo.
        
    Passo 2: Defina a Classe Filha

        Agora crie uma classe Carro que herda de Veiculo. 
        Adicione um atributo adicional cor e use super() no método 
        exibir_info() para chamar o método da classe pai e adicionar 
        informações sobre a cor.
        
    Passo 3: Teste as Classes

        Finalmente, instancie objetos tanto para a classe Veiculo quanto 
        para a classe Carro, e chame o método exibir_info() em ambos.
"""

#Solução:

"""
Passo 1: Defina a Classe Pai

    Crie uma classe chamada Veiculo que tenha um método 
    exibir_info() para exibir informações sobre o veículo.
"""

# Definindo uma classe chamada Veiculo.
class Veiculo:
    
    # O método __init__ é um método especial que é executado quando 
    # uma nova instância da classe é criada.
    # Ele serve para inicializar os atributos da instância.
    def __init__(self, marca, modelo):
        
        # Inicializando o atributo 'marca' com o valor do parâmetro 'marca' 
        # passado durante a criação da instância.
        self.marca = marca
        
        # Inicializando o atributo 'modelo' com o valor do parâmetro 'modelo' 
        # passado durante a criação da instância.
        self.modelo = modelo
    
    # Definindo um método chamado exibir_info, que exibirá informações sobre o veículo.
    def exibir_info(self):
        
        # Utilizando uma string formatada para imprimir as informações do veículo.
        # O método acessa os atributos 'marca' e 'modelo' da instância atual (self) 
        # para exibir as informações.
        print(f"Veículo da marca {self.marca}, modelo {self.modelo}.")
        
"""
Passo 2: Defina a Classe Filha

        Agora crie uma classe Carro que herda de Veiculo. 
        Adicione um atributo adicional cor e use super() no método 
        exibir_info() para chamar o método da classe pai e adicionar 
        informações sobre a cor.
"""

# Definindo uma classe chamada Carro, que herda da classe Veiculo.
class Carro(Veiculo):
    
    # O método __init__ é o construtor e é chamado quando uma nova instância 
    # da classe Carro é criada.
    def __init__(self, marca, modelo, cor):
        
        # Chamando o método construtor da classe pai (Veiculo) usando super().
        # Isso inicializa os atributos 'marca' e 'modelo' da instância.
        super().__init__(marca, modelo)
        
        # Inicializando um novo atributo 'cor' específico para a classe Carro.
        self.cor = cor
    
    # Sobrescrevendo o método exibir_info da classe pai (Veiculo).
    def exibir_info(self):
        
        # Chamando o método exibir_info da classe pai (Veiculo) para 
        # imprimir as informações de 'marca' e 'modelo'.
        super().exibir_info()
        
        # Imprimindo informações adicionais específicas para a classe Carro, 
        # no caso, a cor do carro.
        print(f"Cor do carro: {self.cor}.")
        
        
"""
Passo 3: Teste as Classes

        Finalmente, instancie objetos tanto para a classe Veiculo quanto 
        para a classe Carro, e chame o método exibir_info() em ambos.
"""

# Criando uma instância da classe Veiculo chamada veiculo1.
# A marca é "Toyota" e o modelo é "Corolla".
veiculo1 = Veiculo("Toyota", "Corolla")

# Chamando o método exibir_info da instância veiculo1.
# Isso deve imprimir "Veículo da marca Toyota, modelo Corolla."
veiculo1.exibir_info()

# Criando uma instância da classe Carro chamada carro1.
# A marca é "Honda", o modelo é "Civic" e a cor é "Azul".
carro1 = Carro("Honda", "Civic", "Azul")

# Chamando o método exibir_info da instância carro1.
# Isso deve imprimir informações sobre a marca, o modelo e também sobre a cor do carro.
# Espera-se a saída:
# "Veículo da marca Honda, modelo Civic."
# "Cor do carro: Azul."
carro1.exibir_info()

# Deve exibir:
# Veículo da marca Honda, modelo Civic.
# Cor do carro: Azul.

"""
Neste exercício, você aprendeu a usar a função super() para chamar 
métodos da classe pai dentro de uma classe filha, permitindo que você 
estenda ou modifique o comportamento dos métodos herdados.
"""
print()