"""
Exercício para decidir se um cliente deve receber um aumento no limite 
do cartão de crédito. Vamos usar um modelo de Regressão Linear 
para fazer a classificação.

Dados para Treinamento

    - Idade:                                          [20,    22,    23,    25,    26,    28,    32,    33,    35,    37,    39,    40,    42,    45,     47,     48,     50,     51,     55,     60]
    - Salário Anual (em R$):                          [30000, 40000, 45000, 50000, 52000, 55000, 60000, 65000, 70000, 75000, 85000, 90000, 95000, 100000, 105000, 110000, 120000, 125000, 130000, 140000]
    - Histórico de Crédito (1 para bom, 0 para ruim): [0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     1,     1,     1,     1,      1,      1,      1,      1,      1,      1]
    - Aumento Aprovado (1 para sim, 0 para não):      [0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     1,     1,     1,     1,      1,      1,      1,      1,      1,      1]


"""

# Importando a biblioteca NumPy para manipulação numérica de dados.
import numpy as np

# Importando a classe LinearRegression do módulo sklearn.linear_model.
# Essa classe é usada para implementar o algoritmo de Regressão Linear.
from sklearn.linear_model import LinearRegression


"""
O método .reshape(-1, 1) é usado para remodelar a dimensão do 
array NumPy.

    - O primeiro argumento -1 significa "não especificado": ele
            será automaticamente calculado.
    - O segundo argumento 1 diz que queremos que cada item esteja
            em sua própria sublista.

Em outras palavras, o .reshape(-1, 1) transforma um array unidimensional 
em um array bidimensional, onde cada elemento do array original agora se 
torna um elemento em uma sublista do novo array.
"""
idade = np.array([20, 22, 23, 25, 26, 28, 32, 33, 35, 37, 39, 40, 42, 45, 47, 48, 50, 51, 55, 60]).reshape(-1, 1)
salario_anual = np.array([30000, 40000, 45000, 50000, 52000, 55000, 60000, 65000, 70000, 75000, 85000, 90000, 95000, 100000, 105000, 110000, 120000, 125000, 130000, 140000]).reshape(-1, 1)
historico_credito = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]).reshape(-1, 1)

# Juntando todas as características em uma matriz
X = np.hstack([idade, salario_anual, historico_credito])

# Rótulos para as amostras (1 para aumento aprovado, 0 para não aprovado)
y = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

# Treinando o modelo
modelo = LinearRegression()
modelo.fit(X, y)


# Definição da função menu_interativo para interagir com o usuário
def menu_interativo():
    
    # O loop while True mantém o menu em execução até que o usuário escolha sair
    while True:
        
        # Mostrando as opções disponíveis para o usuário
        print("\nEscolha uma opção:")
        print("1. Verificar aumento de limite")
        print("2. Sair")
        
        # Coletando a escolha do usuário
        escolha = input("Digite o número da sua escolha: ")
        
        # Verificando se o usuário escolheu a primeira opção
        if escolha == '1':
            
            # Solicitando informações adicionais do usuário
            idade = int(input("Digite sua idade: "))
            salario = int(input("Digite seu salário anual em R$: "))
            historico = int(input("Digite 1 para histórico de crédito bom ou 0 para ruim: "))
            
            # Preparando os dados para a previsão em um array NumPy
            dados_predicao = np.array([[idade, salario, historico]])
            
            # Utilizando o modelo treinado para fazer uma previsão
            aumento_aprovado = modelo.predict(dados_predicao)
            
            # Verificando o resultado da previsão e decidindo se o aumento de
            # limite é aprovado ou não
            # Aqui, estou usando um limiar de 0.5 para tomar a decisão
            if aumento_aprovado[0] > 0.5:
                print("\nAumento de limite aprovado.")
            else:
                print("\nAumento de limite não aprovado.")
        
        # Verificando se o usuário escolheu a segunda opção para sair
        elif escolha == '2':
            print("Saindo...")
            break  # Saindo do loop

        # Caso o usuário digite uma opção inválida
        else:
            print("Escolha inválida. Tente novamente.")
            

# Chamando a função para testar o modelo
menu_interativo()

"""
Este é um exemplo simples de como um modelo de aprendizado de máquina 
pode ser usado para tomar decisões de negócios, como aprovar ou não um
aumento de limite de cartão de crédito com base em várias características
do cliente. 

Note que este é um exemplo básico e, na prática, modelos mais sofisticados 
e um conjunto de dados mais amplo seriam usados.


Dados para Treinamento

    - Idade:                                          [20,    22,    23,    25,    26,    28,    32,    33,    35,    37,    39,    40,    42,    45,     47,     48,     50,     51,     55,     60]
    - Salário Anual (em R$):                          [30000, 40000, 45000, 50000, 52000, 55000, 60000, 65000, 70000, 75000, 85000, 90000, 95000, 100000, 105000, 110000, 120000, 125000, 130000, 140000]
    - Histórico de Crédito (1 para bom, 0 para ruim): [0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     1,     1,     1,     1,      1,      1,      1,      1,      1,      1]
    - Aumento Aprovado (1 para sim, 0 para não):      [0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     1,     1,     1,     1,      1,      1,      1,      1,      1,      1]

"""
print()