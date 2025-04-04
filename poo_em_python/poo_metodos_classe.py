print(" Definindo e chamando métodos de uma classe")
class Termostato:
    
    # Método inicializador da classe Termostato
    def __init__(self, temperatura_atual=20):
        
        # Inicializa o atributo 'temperatura_atual' com o valor fornecido ou 20 graus por padrão
        self.temperatura_atual = temperatura_atual  

    # Método para aumentar a temperatura
    def aumentar_temperatura(self, valor):
        
        # Adiciona o valor fornecido ao atributo 'temperatura_atual'
        self.temperatura_atual += valor  
        
        # Imprime a nova temperatura após o aumento
        print(f"Temperatura aumentada em {valor}°. Nova temperatura: {self.temperatura_atual}°.")  
        
    # Método para diminuir a temperatura
    def diminuir_temperatura(self, valor):
        
        # Subtrai o valor fornecido do atributo 'temperatura_atual'
        self.temperatura_atual -= valor  
        
        # Imprime a nova temperatura após a diminuição
        print(f"Temperatura diminuída em {valor}°. Nova temperatura: {self.temperatura_atual}°.")  
        
    # Método para configurar (definir) a temperatura
    def configurar_temperatura(self, nova_temperatura):
        
        # Define a 'temperatura_atual' para o novo valor fornecido
        self.temperatura_atual = nova_temperatura  
        
        # Imprime a temperatura após ser reconfigurada
        print(f"Temperatura configurada para {nova_temperatura}°.")
        
    # Método para exibir a temperatura atual
    def mostrar_temperatura(self):
        
        # Imprime o valor atual do atributo 'temperatura_atual'
        print(f"Temperatura atual: {self.temperatura_atual}°.")
        

#2. Interagindo com o Termostato:

# Instanciando um termostato
meu_termostato = Termostato()

# Usando métodos para interagir com o termostato
meu_termostato.aumentar_temperatura(5)  # Aumenta a temperatura em 5°

meu_termostato.diminuir_temperatura(5)  # Aumenta a temperatura em 5°

meu_termostato.configurar_temperatura(10)  # Configura diretamente a temperatura para 10°

meu_termostato.mostrar_temperatura()  # Mostra a temperatura atual (deveria ser 10°)

meu_termostato.aumentar_temperatura(50)  # Aumenta a temperatura em 50°

meu_termostato.diminuir_temperatura(25)  # Aumenta a temperatura em 25°

meu_termostato.configurar_temperatura(15)

meu_termostato.mostrar_temperatura()

