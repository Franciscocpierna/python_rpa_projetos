"""
Exercício: Urna Eletrônica com Matrizes

Imagine que estamos conduzindo uma eleição para escolher o representante 
estudantil de uma universidade. Existem três candidatos concorrendo e, para 
simplificar, cada aluno pode votar apenas uma vez.

Seu objetivo é criar um programa que simule uma urna eletrônica 
simples usando matrizes.

Especificações:

    - A matriz terá 2 colunas: a primeira para armazenar o nome do 
    candidato e a segunda para armazenar a quantidade de votos.
    
    - O usuário deve inserir o nome do candidato em quem deseja votar. 
    Se o voto for para um candidato não listado, ele será considerado nulo.
    
    - Depois que todos os votos forem inseridos, o programa deve imprimir 
    o nome de cada candidato, o número total de votos que receberam e o vencedor da eleição.

Dica: Para simplificar, considere que o número total de eleitores é fixo, digamos 10.
"""

#Solução

# Inicializa uma matriz com os nomes dos candidatos e seus respectivos votos
urna = [["Alice", 0], ["Bob", 0], ["Charlie", 0]]

# Simula a votação de 4 eleitores
for i in range(4):
    
    # Solicita ao eleitor o nome do candidato em quem deseja votar
    voto = input("Digite o nome do candidato em quem deseja votar (Alice, Bob ou Charlie): ")

    # Inicializa uma flag para verificar se o voto foi válido
    encontrado = False
    
    # Percorre a lista de candidatos
    for candidato in urna:
        
        # Se o nome do candidato corresponder ao voto do eleitor
        if candidato[0] == voto:
            
            # Incrementa o número de votos do candidato
            # candidato[1] = candidato[1] + 1
            candidato[1] += 1
            
            # Atualiza a flag indicando que o voto foi válido
            encontrado = True
            break

    # Se o voto não foi válido (candidato não encontrado)
    if not encontrado:
        print("Voto nulo.")
        

# Imprime os resultados da votação
print("\nResultados:")

# Inicializa variáveis para identificar o candidato com o maior número de votos
votos_maximos = -1
vencedor = ""

# Inicia um loop para percorrer a lista de candidatos
for candidato in urna:
    
    # Imprime o nome do candidato e o número de votos que ele recebeu
    print(f"{candidato[0]}: {candidato[1]} votos")

    # Verifica se o número de votos do candidato atual é maior do que o número máximo de votos registrado até agora
    if candidato[1] > votos_maximos:
        
        # Se o candidato atual tem mais votos, atualiza o número máximo de votos
        votos_maximos = candidato[1]
        
        # Define o candidato atual como o vencedor até o momento
        vencedor = candidato[0]


# Imprime o nome do vencedor e o número de votos que ele recebeu
print(f"\nO vencedor é {vencedor} com {votos_maximos} votos!")