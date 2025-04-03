"""
Exercício Simulando a Rotina de uma Pessoa

Objetivo:
Neste exercício, você irá implementar uma classe chamada Pessoa que 
simula algumas atividades do dia a dia de um indivíduo. A classe deve conter 
métodos que representem diferentes ações, como acordar, comer, dirigir e dormir. 

Além disso, a classe deve manter o controle dos estados do indivíduo para evitar 
ações incompatíveis (por exemplo, não se pode dirigir enquanto come).

Requisitos:

    1. A classe deve ter um construtor que aceite o nome da pessoa como 
    parâmetro e inicialize os estados "acordado", "comendo" e "dirigindo" como False.

    2. Implemente métodos para as seguintes ações:
        acordar(): Faz a pessoa acordar, se já não estiver acordada.
        comer(): Permite que a pessoa coma, desde que não esteja dirigindo ou dormindo.
        parar_de_comer(): Faz a pessoa parar de comer, se estiver comendo.
        dirigir(): Permite que a pessoa dirija, desde que não esteja comendo ou dormindo.
        parar_de_dirigir(): Faz a pessoa parar de dirigir, se estiver dirigindo.
        dormir(): Permite que a pessoa durma, desde que não esteja comendo ou dirigindo.

    3. Cada método deve imprimir mensagens adequadas para indicar o que a pessoa 
    está fazendo ou por que uma ação não pode ser realizada.

    4. Teste a classe criando um objeto e chamando vários métodos em sequência, simulando 
    um dia na vida da pessoa.
"""


#Solução

# Define uma classe chamada "Pessoa"
class Pessoa:
    
    """
    1. A classe deve ter um construtor que aceite o nome da pessoa como 
    parâmetro e inicialize os estados "acordado", "comendo" e "dirigindo" como False.
    """
  
    # O construtor da classe, inicializa um novo objeto Pessoa com o nome fornecido
    def __init__(self, nome):
        self.nome = nome  # Define o nome da pessoa como o nome fornecido
        self.acordado = False  # Inicialmente define o estado "acordado" como Falso
        self.comendo = False  # Inicialmente define o estado "comendo" como Falso
        self.dirigindo = False  # Inicialmente define o estado "dirigindo" como Falso
    
    """
    2. Implemente métodos para as seguintes ações:
        acordar(): Faz a pessoa acordar, se já não estiver acordada.
        comer(): Permite que a pessoa coma, desde que não esteja dirigindo ou dormindo.
        parar_de_comer(): Faz a pessoa parar de comer, se estiver comendo.
        dirigir(): Permite que a pessoa dirija, desde que não esteja comendo ou dormindo.
        parar_de_dirigir(): Faz a pessoa parar de dirigir, se estiver dirigindo.
        dormir(): Permite que a pessoa durma, desde que não esteja comendo ou dirigindo.
    """
    
    # Método para fazer a pessoa acordar
    def acordar(self):
        
        # Verifica se a pessoa já está acordada
        if self.acordado:
            
            # Se sim, imprime que a pessoa já está acordada
            print(f"{self.nome} já está acordado.")
            
        else:
            
            # Se não, muda o estado "acordado" para Verdadeiro
            self.acordado = True
            
            # E imprime que a pessoa acordou
            print(f"{self.nome} acordou.")
            
    # Método para fazer a pessoa comer
    def comer(self):
        
        # Verifica se a pessoa está dirigindo
        if self.dirigindo:
            
            # Se sim, imprime que não pode comer enquanto dirige
            print(f"{self.nome} não pode comer enquanto dirige.")
            
        # Verifica se a pessoa está dormindo
        elif not self.acordado:
            
            # Se sim, imprime que não pode comer enquanto dorme
            print(f"{self.nome} não pode comer enquanto está dormindo.")
            
        # Verifica se a pessoa já está comendo
        elif self.comendo:
            
            # Se sim, imprime que a pessoa já está comendo
            print(f"{self.nome} já está comendo.")
            
        else:
            
            # Se todas as condições acima não forem verdadeiras, então a pessoa pode comer
            self.comendo = True
            
            # Imprime que a pessoa começou a comer
            print(f"{self.nome} começou a comer.")
            
    # Método para fazer a pessoa parar de comer
    def parar_de_comer(self):
        
        # Verifica se a pessoa não está comendo
        if not self.comendo:
            
            # Se sim, imprime que a pessoa não está comendo
            print(f"{self.nome} não está comendo no momento.")
            
        else:
            
            # Se a pessoa estiver comendo, então ela pode parar de comer
            self.comendo = False
            
            # Imprime que a pessoa parou de comer
            print(f"{self.nome} terminou de comer.")
            
    # Método para fazer a pessoa dirigir
    def dirigir(self):
        
        # Verifica se a pessoa está dormindo
        if not self.acordado:
            
            # Se sim, imprime que não pode dirigir
            print(f"{self.nome} não pode dirigir enquanto está dormindo.")
            
        # Verifica se a pessoa está comendo
        elif self.comendo:
            
            # Se sim, imprime que não deve dirigir enquanto come
            print(f"{self.nome} não deve dirigir enquanto come.")
            
        # Verifica se a pessoa já está dirigindo
        elif self.dirigindo:
            
            # Se sim, imprime que a pessoa já está dirigindo
            print(f"{self.nome} já está dirigindo.")
            
        else:
            
            # Se nenhuma das condições acima for verdadeira, a pessoa pode dirigir
            self.dirigindo = True
            
            # Imprime que a pessoa começou a dirigir
            print(f"{self.nome} começou a dirigir.")
            
    # Método para fazer a pessoa parar de dirigir
    def parar_de_dirigir(self):
        
        # Verifica se a pessoa não está dirigindo
        if not self.dirigindo:
            
            # Se sim, imprime que a pessoa não está dirigindo
            print(f"{self.nome} não está dirigindo no momento.")
            
        else:
            
            # Se a pessoa estiver dirigindo, então ela pode parar
            self.dirigindo = False
            
            # Imprime que a pessoa parou de dirigir
            print(f"{self.nome} parou de dirigir.")

            
    # Método para fazer a pessoa dormir
    def dormir(self):
        
        # Verifica se a pessoa está dirigindo
        if self.dirigindo:
            
            # Se sim, imprime que não pode dormir enquanto dirige
            print(f"{self.nome} não pode dormir enquanto dirige.")
            
        # Verifica se a pessoa está comendo
        elif self.comendo:
            
            # Se sim, imprime que não pode dormir enquanto come
            print(f"{self.nome} não pode dormir enquanto come.")
            
        # Verifica se a pessoa já está dormindo
        elif not self.acordado:
            
            # Se sim, imprime que a pessoa já está dormindo
            print(f"{self.nome} já está dormindo.")
            
        else:
            
            # Se nenhuma das condições acima for verdadeira, a pessoa pode dormir
            print(f"{self.nome} foi dormir.")
            
            # Define o estado "acordado" como Falso
            self.acordado = False
            
            # Define o estado "comendo" como Falso
            self.comendo = False
            
            # Aqui, não redefinimos 'self.dirigindo' para manter seu estado atual
            
            
# Criando um objeto "joao" da classe "Pessoa" e passando "João" como nome para o construtor
joao = Pessoa("João")

"""
4. Teste a classe criando um objeto e chamando vários métodos em sequência, simulando 
    um dia na vida da pessoa.
"""

# Tentando fazer João acordar
joao.acordar()  # Ação de acordar é executada, João agora está acordado
joao.acordar()  # Já está acordado, então uma mensagem informando isso é impressa

# Fazendo João comer
joao.comer()  # Ação de comer é executada, João agora está comendo

# Tentando fazer João comer novamente
joao.comer()  # Já está comendo, então uma mensagem informando isso é impressa

# Tentando fazer João parar de comer
joao.parar_de_comer()  # Ação de parar de comer é executada, João agora parou de comer
joao.parar_de_comer()  # Não está comendo, então uma mensagem informando isso é impressa

# Fazendo João dirigir
joao.dirigir()  # Ação de dirigir é executada, João agora está dirigindo

# Tentando fazer João dormir
joao.dormir()  # Não pode dormir enquanto dirige, então uma mensagem informando isso é impressa

# Tentando fazer João comer enquanto dirige
joao.comer()  # Não pode comer enquanto dirige, então uma mensagem informando isso é impressa

# Tentando fazer João dirigir novamente
joao.dirigir()  # Já está dirigindo, então uma mensagem informando isso é impressa

# Fazendo João parar de dirigir
joao.parar_de_dirigir()  # Ação de parar de dirigir é executada, João agora parou de dirigir

# Fazendo João comer
joao.comer()  # Ação de comer é executada, João agora está comendo

# Tentando fazer João dormir enquanto come
joao.dormir()  # Não pode dormir enquanto come, então uma mensagem informando isso é impressa

# Tentando fazer João dirigir enquanto come
joao.dirigir()  # Não pode dirigir enquanto come, então uma mensagem informando isso é impressa

# Tentando fazer João parar de comer quando não está comendo
joao.parar_de_comer()  # Ação de parar de comer é executada, João agora parou de comer

# Tentando fazer João dormir
joao.dormir()  # Ação de dormir é executada, João agora está dormindo

# Tentando fazer João comer enquanto dorme
joao.comer()  # Não pode comer enquanto dorme, então uma mensagem informando isso é impressa

# Tentando fazer João dormir quando já está dormindo
joao.dormir()  # Já está dormindo, então uma mensagem informando isso é impressa

# Tentando fazer João dirigir enquanto dorme
joao.dirigir()  # Não pode dirigir enquanto dorme, então uma mensagem informando isso é impressa
print("Acordado: ",joao.acordado)
print("comendo", joao.comendo)
print("dormindo ", joao.dirigindo)
acordar= not joao.acordado
print("Acordado: ", acordar)