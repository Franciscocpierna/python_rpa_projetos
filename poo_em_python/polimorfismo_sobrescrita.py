"""
3. Pilares da POO

    Polimorfismo: Permitindo que um objeto se comporte de diferentes maneiras.
        - Polimorfismo de sobrescrita (também conhecido como overriding)
        
Polimorfismo de sobrescrita (ou "overriding" em inglês) é uma característica 
de programação orientada a objetos onde uma subclasse fornece uma implementação 
específica para um método que já é definido em sua superclasse. Esse mecanismo 
permite que a subclasse herde características da superclasse mas também possa 
modificar comportamentos específicos.
"""

"""
Exemplo: Classe Animal e suas subclasses Cachorro e Gato

Neste exemplo, vamos criar uma classe Animal com um método som. Em seguida, 
vamos criar duas subclasses Cachorro e Gato que sobrescrevem o método som da 
superclasse.
"""

# Classe Animal: Esta é a superclasse que define um comportamento básico 
# comum a todos os animais.
class Animal:
    
    # Define um método chamado 'som' que imprime uma mensagem genérica indicando 
    # que o animal faz um som.
    def som(self):
        print("O animal faz um som")

# Classe Cachorro: Esta é uma subclasse de Animal, ou seja, herda todos os 
# métodos e atributos da classe Animal.
class Cachorro(Animal):
    
    # Sobrescreve o método 'som' da superclasse Animal. Isso significa que 
    # este método substituirá o método da superclasse quando chamado em um 
    # objeto da subclasse.
    def som(self):
        
        # Imprime uma mensagem específica que indica que o cachorro late, ao 
        # invés de fazer um "som genérico".
        print("O cachorro late")


# Classe Gato: Esta é outra subclasse de Animal, herdando os métodos e atributos da classe Animal.
class Gato(Animal):
    
    # Sobrescreve o método 'som' da superclasse Animal. Este método substituirá o método da superclasse quando chamado em um objeto da subclasse Gato.
    def som(self):
        # Imprime uma mensagem específica indicando que o gato mia, diferentemente de fazer um "som genérico".
        print("O gato mia")

# Cria um objeto da classe Animal e armazena na variável 'animal'.
animal = Animal()

# Chama o método 'som' no objeto 'animal'. Este método é herdado da classe Animal.
# A saída será "O animal faz um som" porque estamos usando um objeto da classe Animal.
animal.som()  # Saída: "O animal faz um som"

# Cria um objeto da classe Cachorro e armazena na variável 'cachorro'.
cachorro = Cachorro()

# Chama o método 'som' no objeto 'cachorro'. Este método foi sobrescrito na classe Cachorro.
# A saída será "O cachorro late" porque estamos usando um objeto da classe Cachorro.
cachorro.som()  # Saída: "O cachorro late"

# Cria um objeto da classe Gato e armazena na variável 'gato'.
gato = Gato()

# Chama o método 'som' no objeto 'gato'. Este método foi sobrescrito na classe Gato.
# A saída será "O gato mia" porque estamos usando um objeto da classe Gato.
gato.som()  # Saída: "O gato mia"

"""
Note como cada subclasse (Cachorro e Gato) fornece sua própria 
implementação do método som, sobrescrevendo o método som da superclasse 
Animal. Este é um exemplo clássico de polimorfismo de sobrescrita. Quando 
chamamos o método som em um objeto da subclasse, a implementação da subclasse 
é a que é executada, e não a da superclasse.
"""
print()
"""
Exercício: Polimorfismo de Sobrescrita com Classes de Veículos

O objetivo deste exercício é entender o polimorfismo de 
sobrescrita (overriding) através de um exemplo prático envolvendo 
diferentes tipos de veículos. Cada tipo de veículo pode ter uma forma 
específica de movimento, que é descrita pelo método mover.

    Passo 1: Implemente a Classe Veiculo

        Crie uma classe chamada Veiculo que terá um método chamado 
        mover. Este método imprimirá uma mensagem genérica sobre como 
        um veículo se move.
        
    Passo 2: Implemente as Subclasses Carro, Barco e Aviao

        Agora crie três subclasses: Carro, Barco e Aviao. Cada uma 
        dessas subclasses deve sobrescrever o método mover para fornecer 
        detalhes específicos sobre como cada tipo de veículo se move.
        
    Passo 3: Teste as Classes

        Depois de implementar as subclasses, crie instâncias 
        de cada uma e chame o método mover.
"""

#Solução:

"""
Passo 1: Implemente a Classe Veiculo

        Crie uma classe chamada Veiculo que terá um método chamado 
        mover. Este método imprimirá uma mensagem genérica sobre como 
        um veículo se move.
"""

# Classe Veiculo: Esta é uma classe geral que define o comportamento 
# básico de um veículo.
class Veiculo:
    
    # Define um método chamado 'mover', que imprimirá uma mensagem genérica
    # indicando que o veículo está se movendo.
    def mover(self):
        print("O veículo está se movendo")
        

"""
Passo 2: Implemente as Subclasses Carro, Barco e Aviao

        Agora crie três subclasses: Carro, Barco e Aviao. Cada uma 
        dessas subclasses deve sobrescrever o método mover para fornecer 
        detalhes específicos sobre como cada tipo de veículo se move.
"""

# Classe Carro: Esta é uma subclasse da classe Veiculo e herda os métodos e 
# atributos da classe Veiculo.
class Carro(Veiculo):
    
    # Sobrescreve o método 'mover' da superclasse Veiculo para fornecer um 
    # comportamento específico para Carro.
    def mover(self):
        
        # Imprime uma mensagem específica indicando que o carro está dirigindo na estrada.
        print("O carro está dirigindo na estrada")

# Classe Barco: Esta é outra subclasse da classe Veiculo e também herda 
# os métodos e atributos da classe Veiculo.
class Barco(Veiculo):
    
    # Sobrescreve o método 'mover' da superclasse Veiculo para fornecer um 
    # comportamento específico para Barco.
    def mover(self):
        
        # Imprime uma mensagem específica indicando que o barco está navegando no mar.
        print("O barco está navegando no mar")

# Classe Aviao: Esta é outra subclasse da classe Veiculo e, mais uma 
# vez, herda os métodos e atributos da classe Veiculo.
class Aviao(Veiculo):
    
    # Sobrescreve o método 'mover' da superclasse Veiculo para fornecer 
    # um comportamento específico para Aviao.
    def mover(self):
        
        # Imprime uma mensagem específica indicando que o avião está voando no céu.
        print("O avião está voando no céu")
        
        
"""
Passo 3: Teste as Classes

        Depois de implementar as subclasses, crie instâncias 
        de cada uma e chame o método mover.
"""

# Instanciando objetos de cada classe e subclasse
# Cria um objeto da classe Veiculo e armazena na variável 'veiculo'.
veiculo = Veiculo()

# Cria um objeto da classe Carro (subclasse de Veiculo) e armazena na variável 'carro'.
carro = Carro()

# Cria um objeto da classe Barco (subclasse de Veiculo) e armazena na variável 'barco'.
barco = Barco()

# Cria um objeto da classe Aviao (subclasse de Veiculo) e armazena na variável 'aviao'.
aviao = Aviao()

# Chamando o método mover para cada objeto
# Chama o método 'mover' no objeto 'veiculo'. Este método é herdado da classe Veiculo.
# A saída será "O veículo está se movendo" porque estamos usando um objeto da classe Veiculo.
veiculo.mover()  # Saída: "O veículo está se movendo"

# Chama o método 'mover' no objeto 'carro'. Este método foi sobrescrito na classe Carro.
# A saída será "O carro está dirigindo na estrada" porque estamos usando um objeto da classe Carro.
carro.mover()    # Saída: "O carro está dirigindo na estrada"

# Chama o método 'mover' no objeto 'barco'. Este método foi sobrescrito na classe Barco.
# A saída será "O barco está navegando no mar" porque estamos usando um objeto da classe Barco.
barco.mover()    # Saída: "O barco está navegando no mar"

# Chama o método 'mover' no objeto 'aviao'. Este método foi sobrescrito na classe Aviao.
# A saída será "O avião está voando no céu" porque estamos usando um objeto da classe Aviao.
aviao.mover()    # Saída: "O avião está voando no céu"


"""
Observe como o método mover foi sobrescrito em cada 
subclasse (Carro, Barco, Aviao) para fornecer uma implementação 
específica de como o veículo se move, demonstrando assim o 
conceito de polimorfismo de sobrescrita.
"""
print()