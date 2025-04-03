"""
Exercício: Sistema de Reservas para um Evento

Objetivo: Compreender a definição e utilização de métodos dentro de classes em Python.

Descrição:

Crie uma classe chamada Evento que represente um evento com um número limitado de 
lugares. A classe deve permitir:

    1. Reservar um lugar.
    2. Cancelar uma reserva.

A classe Evento deve ter os seguintes métodos:

    - reservar(): Este método deve diminuir o número de lugares disponíveis em um.
    - cancelar(): Este método deve aumentar o número de lugares disponíveis em um.
    - lugares_disponiveis(): Este método deve retornar o número de lugares disponíveis.

Restrições:

    1. O evento tem uma capacidade inicial definida (por exemplo, 10 lugares).
    
    2. Se tentar reservar um lugar e todos estiverem ocupados, o sistema deve 
    informar que não há lugares disponíveis.
    
    3. Se tentar cancelar uma reserva e todos os lugares estiverem disponíveis, 
    o sistema deve informar que não há reservas para cancelar.

"""

#Solução

# Define a classe Evento
# Define a classe chamada 'Evento'.
class Evento:
    
    # Define o método inicializador '__init__' da classe Evento.
    # Este método é chamado automaticamente ao criar uma nova instância da classe.
    def __init__(self, capacidade=10):
        
        # Inicializa o atributo 'capacidade' da instância com o valor fornecido como argumento.
        # Se nenhum valor for fornecido, utiliza o valor padrão de 10.
        self.capacidade = capacidade  
        
        # Inicializa o atributo 'lugares_disponiveis' com o mesmo valor da 'capacidade' inicial.
        # Isso é feito porque inicialmente todos os lugares estão disponíveis.
        self.lugares_disponiveis = capacidade
        
    
    # Define o método 'reservar', que é usado para reservar um lugar no evento.
    def reservar(self):
        
        # Verifica se o número de 'lugares_disponiveis' é igual a zero.
        # Se for, isso significa que não há lugares disponíveis para reserva.
        if self.lugares_disponiveis == 0:  
            
            # Imprime uma mensagem informando o usuário que não há lugares disponíveis para reserva.
            print("Desculpe, não há lugares disponíveis para reserva.")
            
            # Retorna do método sem executar qualquer outra ação.
            return  
        
        # Diminui o atributo 'lugares_disponiveis' em 1 para representar a reserva de um lugar.
        self.lugares_disponiveis -= 1  
        
        # Imprime uma mensagem informando que a reserva foi realizada com sucesso.
        print("Lugar reservado com sucesso!")  
        
    
    # Define o método 'cancelar', que é usado para cancelar uma reserva existente.
    def cancelar(self):
        
        # Verifica se o número de 'lugares_disponiveis' é igual à 'capacidade' total.
        # Se for, isso significa que não há reservas para cancelar.
        if self.lugares_disponiveis == self.capacidade:  
            
            # Imprime uma mensagem informando que não há reservas para cancelar.
            print("Não há reservas para cancelar.")
            
            # Retorna do método sem executar qualquer outra ação.
            return  
        
        # Aumenta o atributo 'lugares_disponiveis' em 1 para representar o cancelamento de uma reserva.
        self.lugares_disponiveis += 1  
        
        # Imprime uma mensagem informando que a reserva foi cancelada com sucesso.
        print("Reserva cancelada com sucesso!")
        
        
    # Define o método 'mostrar_lugares_disponiveis', que é usado para mostrar o 
    # número de lugares disponíveis.
    def mostrar_lugares_disponiveis(self):
        
        # Retorna uma string formatada que inclui o número atual de 'lugares_disponiveis'.
        return f"Lugares disponíveis: {self.lugares_disponiveis}"
        
    
# Testando a classe
evento = Evento()

print(evento.mostrar_lugares_disponiveis()) #10

evento.reservar() #9
print(evento.mostrar_lugares_disponiveis())

evento.reservar() #8
print(evento.mostrar_lugares_disponiveis())

evento.cancelar() #9
print(evento.mostrar_lugares_disponiveis())

evento.cancelar() #10
print(evento.mostrar_lugares_disponiveis())

print()

# Reservando lugares para o evento
# Usando um loop for para repetir a ação de reserva 3 vezes
"""
    for: Esta é a palavra-chave que inicia um loop for em Python. O loop for é 
    usado para iterar sobre uma sequência (que pode ser uma lista, uma tupla, um 
    dicionário, um conjunto ou uma string).

    _: Este é um identificador (basicamente, uma variável) usado para armazenar o 
    valor de cada item na sequência à medida que o loop é executado. Em Python, é 
    comum usar o _ como um identificador quando você não planeja realmente usar o valor 
    dentro do loop. É uma convenção que indica "Eu não me importo com o valor atual, estou 
    apenas usando o loop para repetição".

    in: Esta é outra palavra-chave do loop for que define a sequência sobre a qual o loop irá iterar.

    range(3): A função range() retorna uma sequência de números, começando de 0 por padrão, e 
    parando antes de um número especificado. No caso de range(3), ela retornará a sequência [0, 1, 2].
"""
for _ in range(3):
    
    # Chamando o método 'reservar' da instância 'evento'
    evento.reservar()
    
print(evento.mostrar_lugares_disponiveis())


print()

# Cancelando algumas reservas para o evento
# Usando um loop for para repetir a ação de cancelamento 2 vezes
for _ in range(2):
    
    # Chamando o método 'cancelar' da instância 'evento'
    evento.cancelar()

# Imprimindo o número de lugares disponíveis após os 2 cancelamentos
print(evento.mostrar_lugares_disponiveis())