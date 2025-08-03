"""
Crie um algoritmo que faça reservas de passagens de um ônibus com 10 lugares, 
o sistema deve mostrar 4 opções:

1. Exibir mapa de lugares
2. Reservar lugar
3. Cancelar reserva
4. Sair

- Na venda de passagens o sistema deve perguntar "Escolha uma opção:"
- Quando reservar o sistema deve exibir "Lugar reservado com sucesso."
- Caso a pessoa escolher um assento ocupado o sistema deve informar "Lugar indisponível."
- Quando for cancelar uma reserva mostrar "Lugar reserva cancelada com sucesso."
- Se tentar reservar um lugar que não existe, mostrar "Lugar inválido".
"""

class Onibus:
    
    #Método de inicialização da classe
    def __init__(self, capacidade):
        
        #Recebe a capacidade do ônibus como parâmetro
        self.capacidade = capacidade #Armazena a capacidade do ônibus
        self.lugares = [0] * capacidade #Cria uma lista de lugares vazios  do tamanho da capacidade
        
    #Método para reservar
    def reservar_lugar(self, num_lugar):
        
        
        #verifica se o número do lugar é invalido
        #Se for inválido (menor que 1 ou maior que a capacidade)
        if num_lugar < 1 or num_lugar > self.capacidade:
            
            return "\nLugar Inválido!"
        
        #Verifica se o lugar está disponivel (representado por 0 na lista de lugares)
        if self.lugares[num_lugar - 1] == 0:
            
            #Se estiver disponivel. reserva o lugar
            #Atualiza o valor correspondente na lista para 1
            self.lugares[num_lugar - 1] = 1
            
            return f"\nLugar {num_lugar} reservado com sucesso."
        
        else:
            
            return f"\nLugar {num_lugar} indisponível."
        
    def cancelar_reserva(self, num_lugar):
        
        #verifica se o número do lugar é invalido
        #Se for inválido (menor que 1 ou maior que a capacidade)
        if num_lugar < 1 or num_lugar > self.capacidade:
            
            return "\nLugar Inválido!"
        
        # Verifica se o lugar está reservado (representado por 1 na lista de lugares)
        if self.lugares[num_lugar - 1] == 1:
            
            #Se estiver reservado
            #Atualiza o valor correspondente na lista para 0
            self.lugares[num_lugar - 1] = 0
            
            return f"\nLugar {num_lugar} reservada cancelada com sucesso."
        
        else:
            
            return f"\nLugar {num_lugar} não está reservado."
        
        
    
    #Método para exibir o mapa de lugares do ônibus
    def exibir_mapa(self):
    
        #Loop que itera pelos indices dos lugares de 2 em 2
        for i in range(0, self.capacidade, 2):
            
            lugar_esquerda = i + 1 #Número do lugar da esquerda
            lugar_direita = i + 2 #Número do lugar da direita
            
            #Verifica se o lugar da esquerda está reservado (Representado por 1 na lista de lugares)
            status_esquerda = "X" if self.lugares[i] == 1 else " "
            
            # Verifica se o lugar da direita está dentro da capacidade do ônibus e se está reservado
            # Se ambos os critérios forem atendidos, atribui "X" ao status_direita, caso contrário, atribui um espaço em branco
            status_direita = "X" if lugar_direita <= self.capacidade and self.lugares[i + 1] == 1 else " "
            
            print(f"Lugar {lugar_esquerda}: [{status_esquerda}]   Lugar {lugar_direita}: [{status_direita}]")
        
def exibir_menu():
    
    print("\n------- Menu ------")
    print("1. Exibir mapa de lugares")
    print("2. Reservar lugar")
    print("3. Cancelar reserva")
    print("4. Sair")
    
onibus = Onibus(20)

escolha = 0

while escolha != 4:
    
    #Chamo a função do menu
    exibir_menu()
    
    #Pego o número que o usuário digitar
    escolha = int(input("Escolha uma opção: "))
    
    if escolha == 1:
        
        print("\nMapa de Lugares:")
        
        onibus.exibir_mapa()
        
    elif escolha == 2:
        
        num_lugar = int(input("Digite o número do lugar que deseja reservar: "))
        
        print(onibus.reservar_lugar(num_lugar))
    
    elif escolha == 3:
        
        num_lugar = int(input("Digite o número do lugar que deseja cancelar a reservar: "))
        
        print(onibus.cancelar_reserva(num_lugar))
               
        
    elif escolha == 4:
        
        print("Programa encerrado com sucesso!")
        
    else:
        
        print("Opção inválida. Por favor, escolha novamente.")