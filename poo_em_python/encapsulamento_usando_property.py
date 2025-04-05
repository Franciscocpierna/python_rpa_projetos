"""

3. Pilares da POO

    Encapsulamento: Protegendo os dados de uma classe.
        Propriedades (usando o decorador @property).


Em Python, podemos usar o decorador @property para criar uma 
propriedade que atua como um atributo, mas que na verdade é acessada 
através de um método. Isso é útil quando queremos executar alguma lógica extra
ao obter ou definir o valor de um atributo.

Vamos criar uma classe Retângulo como exemplo. 

Nesta classe, vamos ter os atributos largura e altura, e uma propriedade 
área que será calculada usando esses atributos.
"""

# Iniciando a definição da classe chamada 'Retangulo'
class Retangulo:
    
    # Método construtor (__init__) para a classe Retangulo
    # Este método é chamado automaticamente quando um novo objeto da classe é criado
    # Ele recebe dois parâmetros: largura e altura, que serão usados para inicializar 
    # os atributos
    def __init__(self, largura, altura):
        
        # Atributo protegido '_largura' é inicializado com o valor do argumento 'largura'
        # O uso de um único sublinhado indica que este é um atributo 
        # protegido (não estritamente privado)
        self._largura = largura
        
        # Atributo protegido '_altura' é inicializado com o valor do argumento 'altura'
        # Similar ao '_largura', este também é um atributo protegido
        self._altura = altura
        
    # Método para obter o valor do atributo '_largura'
    # Este método age como um 'getter' para o atributo protegido '_largura'
    
    @property  # O decorador @property faz com que este método possa ser acessado 
               # como se fosse um atributo, ou seja, sem precisar 
               # de parênteses quando chamado.
    def largura(self):
        
        # Retorna o valor atual do atributo protegido '_largura'
        # Isso permite acesso somente leitura ao atributo '_largura' de fora da classe
        return self._largura
    
    
    # Método que age como um 'setter' para o atributo protegido '_largura'
    # O decorador @largura.setter indica que este método é um setter para a 
    # propriedade previamente definida 'largura'
    @largura.setter  
    def largura(self, valor):
        
        # Verifica se o valor fornecido é maior que zero
        # Isso é importante para manter a integridade dos dados, já que a largura 
        # de um retângulo não pode ser zero ou negativa
        if valor > 0:
            
            # Atualiza o atributo protegido '_largura' com o novo valor
            # Isso permite modificar o valor de '_largura' de fora da classe de forma controlada
            self._largura = valor
            
        else:
            
            # Exibe uma mensagem de erro caso o valor fornecido seja menor ou igual a zero
            # Isso fornece um feedback ao usuário sobre por que a operação falhou
            print("Largura deve ser maior que zero.")
            
            
    # Método que age como um 'getter' para o atributo protegido '_altura'
    # O decorador @property torna este método acessível como se fosse um atributo, ou seja, 
    # sem necessidade de parênteses
    @property
    def altura(self):
        
        # Retorna o valor atual do atributo protegido '_altura'
        # Isso permite um acesso somente leitura ao atributo '_altura' de fora da classe
        return self._altura  

    
    # Método que age como um 'setter' para o atributo protegido '_altura'
    # O decorador @altura.setter indica que este método é um setter para a propriedade 
    # previamente definida 'altura'
    @altura.setter  
    def altura(self, valor):
        
        # Verifica se o valor fornecido é maior que zero
        # Essa validação é importante para garantir que a altura do retângulo seja 
        # sempre positiva
        if valor > 0:
            
            # Atualiza o atributo protegido '_altura' com o novo valor fornecido
            # Isso permite modificar o valor de '_altura' de fora da classe, mas de forma 
            # controlada
            self._altura = valor
            
        else:
            
            # Exibe uma mensagem de erro caso o valor fornecido seja menor ou igual a zero
            # Isso serve como um feedback ao usuário para entender o motivo pelo qual a 
            # operação não foi bem-sucedida
            print("Altura deve ser maior que zero.")     
    
    
            
    # Método para calcular e retornar a área do retângulo
    # O decorador @property permite que esse método seja acessado como se fosse um atributo 
    # da classe, ou seja, sem parênteses
    @property  
    def area(self):
        
        # Calcula a área do retângulo multiplicando a largura pela altura
        # Retorna o resultado dessa multiplicação
        # Isso oferece uma forma conveniente de obter a área do retângulo diretamente, 
        # como se fosse um atributo
        return self._largura * self._altura  
  

"""
Neste código, @property e @<nome>.setter são decoradores que tornam 
os métodos acessíveis como se fossem atributos da classe. Isso permite 
que você use lógica adicional para validação ou cálculos, fornecendo 
uma interface de programação mais fácil e segura.
"""

# Instancia um novo objeto da classe Retangulo com a largura de 5 e a altura de 6
# Isso cria um novo retângulo chamado 'r' e inicializa seus atributos
r = Retangulo(5, 6)

# Usa a propriedade 'area' para calcular e exibir a área do retângulo
# Observe que estamos usando 'area' como um atributo, não como um método (graças ao decorador @property)
# A saída esperada aqui é "Área: 30" (5 x 6 = 30)
print("Área:", r.area)

# Usa o setter da propriedade 'largura' para atualizar a largura do retângulo para 7
# Novamente, estamos usando 'largura' como se fosse um atributo, permitindo um acesso mais simples e intuitivo
r.largura = 7

# Exibe a nova área do retângulo, agora com a largura atualizada para 7
# A saída esperada é "Nova área: 42" (7 x 6 = 42)
print("Nova área:", r.area)  

# Tenta definir uma largura inválida para o retângulo usando o setter da propriedade 'largura'
# Como o valor é negativo, o setter deve emitir uma mensagem de erro indicando que a largura deve ser maior que zero
r.largura = -5  # Deverá exibir "Largura deve ser maior que zero."


"""
Neste exemplo, largura e altura são propriedades que nos permitem 
acessar e modificar os atributos _largura e _altura, respectivamente, 
enquanto realizamos a verificação de que esses valores são positivos. 

A propriedade area nos permite calcular a área do retângulo de forma 
transparente, sem necessidade de chamar um método.
"""
print()      

"""
Exercício: Termômetro Digital

Você vai criar uma classe Termometro que representará um termômetro 
digital simples.

Requisitos:

    1. O termômetro deve ter um atributo protegido _temperatura que 
        armazena a temperatura atual em graus Celsius.
    
    2. Implemente um método getter usando @property para a temperatura.
    
    3. Implemente um método setter para a temperatura que verifica se o 
        valor é uma temperatura razoável para a atmosfera terrestre (digamos, entre -100°C e 100°C).

Exemplo de Uso:

t = Termometro()
t.temperatura = 25
print(t.temperatura)  # Deve imprimir 25

t.temperatura = 200  # Deve imprimir "Temperatura fora do alcance"
print(t.temperatura)  # Deve imprimir 25, pois a temperatura anterior não foi alterada


Sua tarefa é implementar essa classe Termometro e garantir que ela funcione como especificado.
"""

#Solução

# Definindo a classe Termometro para representar um termômetro digital simples
class Termometro:
    
    """
    1. O termômetro deve ter um atributo protegido _temperatura que 
        armazena a temperatura atual em graus Celsius.
    """
    # Método construtor para inicializar a instância da classe
    def __init__(self):
        
        # Inicializando um atributo protegido '_temperatura' com o valor 0
        # Este atributo armazena a temperatura atual em graus Celsius
        self._temperatura = 0  

    """
    2. Implemente um método getter usando @property para a temperatura.
    """
    # Utilizando o decorador @property para indicar que o método a seguir
    # será o 'getter' para o atributo temperatura
    @property
    def temperatura(self):
        
        # Este método retorna o valor atual do atributo protegido '_temperatura'
        return self._temperatura
    
    """
    3. Implemente um método setter para a temperatura que verifica se o 
        valor é uma temperatura razoável para a atmosfera terrestre (digamos, entre -100°C e 100°C).
    """

    # Utilizando o decorador @temperatura.setter para indicar que o método a seguir 
    # será o 'setter' para o atributo temperatura
    @temperatura.setter
    def temperatura(self, valor):
        
        # Este bloco de código verifica se o valor fornecido para a temperatura 
        # está dentro do intervalo de -100 a 100 graus Celsius
        if -100 <= valor <= 100:
            
            # Se o valor estiver dentro do intervalo, atualizamos o atributo 
            # protegido '_temperatura' com o novo valor
            self._temperatura = valor  
        else:
            
            # Se o valor estiver fora do intervalo permitido, imprimimos uma mensagem de erro
            print("Temperatura fora do alcance")
            

# Testando a classe Termometro
t = Termometro()
t.temperatura = 25  # Configurando a temperatura para 25°C
print(t.temperatura)  # Deve imprimir 25

t.temperatura = 200  # Tentando definir uma temperatura fora do alcance
print(t.temperatura)  # Deve imprimir 25, pois a tentativa anterior deveria ter falhado e a temperatura não foi alterada