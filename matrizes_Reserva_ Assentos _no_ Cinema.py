"""
Exercício: Reserva de Assentos no Cinema usando Matrizes

Você foi contratado para criar um sistema simples de reserva de 
assentos para um pequeno cinema. O cinema tem 5 fileiras e 10 assentos 
em cada fileira, totalizando 50 assentos.

Cada assento pode estar disponível, reservado ou ocupado.

Especificações:

    Inicie com todos os assentos disponíveis.
    - O usuário pode escolher entre ver a disposição dos assentos, 
    reservar um assento ou sair.
    
    - A disposição dos assentos deve mostrar "D" para assentos 
    disponíveis, "R" para assentos reservados e "O" para assentos ocupados.
    
    - Para reservar um assento, o usuário deve inserir a fileira e o número do assento.
    
    - Uma vez que um assento é reservado, ele não pode ser selecionado por outro usuário.

Dica: Use uma matriz 5x10 para representar o cinema, onde cada elemento é uma 
string que indica o status do assento.
"""

#Solução

# Inicializa uma lista vazia para a matriz do cinema
cinema = []

# Loop externo para percorrer as fileiras
for i in range(5):
    
    # Inicializa uma lista vazia para a fileira atual
    fileira = []
    
    # Loop interno para percorrer os assentos dentro de uma fileira
    for j in range(10):
        
        # Adiciona um assento disponível ('D') à fileira atual
        fileira.append('D')
    
    # Adiciona a fileira completa à matriz do cinema
    cinema.append(fileira)
    
    
# Inicia um loop infinito para o menu de opções
while True:
    
    # Imprime o menu de opções
    print("\nMenu:")
    print("1. Ver disposição dos assentos")
    print("2. Reservar um assento")
    print("3. Sair")
    
    # Solicita ao usuário que escolha uma opção
    escolha = input("Escolha uma opção: ")

    # Se o usuário escolher a opção 1
    if escolha == '1':
        
        # Inicia um loop para percorrer cada fileira da matriz do cinema
        for fileira in cinema:
            
            # Inicia um loop interno para percorrer cada assento na fileira atual
            for assento in fileira:
                
                # Imprime o status do assento (por exemplo, 'D' para disponível ou 'R' para reservado) sem quebrar a linha
                print(assento, end=" ")
                
            # Imprime uma quebra de linha após imprimir todos os assentos de uma fileira completa
            print()

    # Se o usuário escolher a opção 2
    elif escolha == '2':
        
        # Solicita ao usuário que escolha a fileira e o assento que deseja reservar
        fileira = int(input("Digite o número da fileira / Linha (0-4): "))
        assento = int(input("Digite o número do assento / Coluna (0-9): "))

        # Verifica se o assento escolhido está disponível
        if cinema[fileira][assento] == 'D':
            
            # Se estiver disponível, marca o assento como reservado (R = Reservado)
            cinema[fileira][assento] = 'R'
            print("Assento reservado com sucesso!")
            
        else:
            # Se o assento já estiver reservado, informa ao usuário
            print("Assento já está reservado ou ocupado.")

    # Se o usuário escolher a opção 3
    elif escolha == '3':
        
        # Agradece ao usuário e encerra o programa
        print("Obrigado por usar nosso sistema!")
        break
        
    # Se o usuário escolher uma opção inválida
    else:
        
        print("Opção inválida!")
    

print()