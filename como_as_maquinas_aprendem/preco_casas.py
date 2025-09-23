"""
Exercicio Previsão do Preço de Casas com Aprendizado de Máquina

O objetivo é criar um modelo de aprendizado de máquina 
que possa prever o preço de casas com base em diversas características
como área total, número de quartos e número de banheiros. 

Além disso, você deve implementar um menu interativo que permita 
ao usuário entrar com os valores dessas características para obter
uma previsão do preço.

Requisitos:

    - Utilize a biblioteca scikit-learn para criar um modelo de Regressão Linear.

    - Utilize NumPy para manipular os arrays de dados.

    - Treine o modelo usando o seguinte conjunto de dados de exemplo:
    
            Área Total (m²): [50,60,100,150]
            Número de Quartos: [1,2,3,4]
            Número de Banheiros: [1,1,2,3]
            Preço da Casa (R$): [200000,300000,500000,750000]

            Área Total (m²):    [50,     60,     100,    150,    120,   130,     170,   80]
            Número de Quartos:  [1,      2,      3,      4,      3,     2,       4,     2]
            Número de Banheiros:[1,      1,      2,      3,      2,     1,       3,     1]

            Preço da Casa (R$): [200000, 300000, 500000, 750000, 600000, 550000, 800000, 400000]

    Implemente uma função chamada menu_interativo que:
        - Exibe um menu com as opções: "Prever o preço de uma casa" e "Sair".
        - Lê a escolha do usuário.
        - Se o usuário escolher prever o preço, o programa deve pedir as 
            características da casa (área total, número de quartos e número 
            de banheiros) e, em seguida, exibir o preço previsto.
        - Se o usuário escolher sair, o programa deve terminar.
        
Dicas:

    - Use a função fit da classe LinearRegression para treinar o modelo.
    - Use a função predict para fazer previsões.
    - Para ler um número com casas decimais e separador de milhar, você pode usar
        a biblioteca locale.
"""


# Importando a biblioteca NumPy para manipulação numérica de dados.
import numpy as np

# Importando a classe LinearRegression do módulo sklearn.linear_model.
# Essa classe é usada para implementar o algoritmo de Regressão Linear.
from sklearn.linear_model import LinearRegression

# Importando a biblioteca 'locale' para configurações de localidade.
# Isso será usado para formatar números de acordo com as configurações brasileiras.
import locale

# Configurando o locale para o padrão brasileiro 'pt_BR.UTF-8'.
# Isso afetará a formatação de números, datas e moedas.
# No caso deste código, será usado principalmente para formatação de números.
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

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
# Dados para treinamento
area_total = np.array([50, 60, 100, 150, 120, 130, 170, 80]).reshape(-1, 1)
num_quartos = np.array([1, 2, 3, 4, 3, 2, 4, 2]).reshape(-1, 1)
num_banheiros = np.array([1, 1, 2, 3, 2, 1, 3, 1]).reshape(-1, 1)

preco_casa = np.array([200000, 300000, 500000, 750000, 600000, 550000, 800000, 400000])

# Exibindo os novos dados
# (Note que essa linha é um comentário e não faz nada no código.
# Você pode querer usar print ou outras formas de saída para
# realmente exibir os dados)
area_total, num_quartos, num_banheiros, preco_casa

# Combinando as matrizes de características (area_total, num_quartos
# e num_banheiros) horizontalmente
# para criar uma única matriz de características 'X'.
# A função np.hstack() empilha matrizes horizontalmente.
X = np.hstack([area_total, num_quartos, num_banheiros])

# Definindo 'y' como a matriz de preços das casas.
# Esta é a variável que queremos prever com nosso modelo.
y = preco_casa

# Criando uma instância da classe LinearRegression para
# representar nosso modelo.
modelo = LinearRegression()

# Treinando o modelo de Regressão Linear usando os dados 
# em 'X' para as características
# e 'y' para os preços das casas.
# O método 'fit()' ajusta o modelo aos dados fornecidos.
modelo.fit(X, y)


# Definindo uma função chamada 'menu_interativo' para gerenciar as interações do usuário
def menu_interativo():
    
    # Loop infinito para manter o menu rodando até que o usuário decida sair
    while True:
        
        # Exibindo opções do menu para o usuário
        print("\nEscolha uma opção:")
        print("1. Prever o preço de uma casa")
        print("2. Sair")
        
        # Coletando a escolha do usuário
        escolha = input("Digite o número da sua escolha: ")
        
        # Verificando se a escolha do usuário é '1' para prever o preço de uma casa
        if escolha == '1':
            
            # Coletando dados da casa do usuário
            area = locale.atof(input("Digite a área total da casa em metros quadrados: "))
            quartos = int(input("Digite o número de quartos: "))
            banheiros = int(input("Digite o número de banheiros: "))
            
            # Preparando os dados para a previsão:
            # Criamos um array NumPy com os valores de 'area', 'quartos' e 'banheiros'.
            # Esse array é bidimensional porque o método 'predict' espera um array bidimensional.
            # Cada subarray (neste caso, temos apenas um) representa um conjunto de características de uma casa.
            dados_predicao = np.array([[area, quartos, banheiros]])

            # Fazendo a previsão do preço da casa usando o modelo treinado:
            # Usamos o método 'predict' do objeto 'modelo', que é uma instância da classe LinearRegression.
            # O método 'predict' faz uma previsão com base nas características fornecidas ('dados_predicao')
            # e retorna um array NumPy com os preços previstos.
            # Como estamos prevendo o preço de apenas uma casa, pegamos o primeiro elemento do array de saída.
            preco_predito = modelo.predict(dados_predicao)

            # Exibindo o preço previsto da casa:
            # Usamos uma f-string para formatar a saída.
            # O preço previsto é arredondado para duas casas decimais.
            # Utilizamos ':,.2f' para formatar o número, adicionando separadores de milhar e limitando a duas casas decimais.
            print(f"\nO preço previsto para a casa é R$ {preco_predito[0]:,.2f}")

        
        # Verificando se a escolha do usuário é '2' para sair do programa
        elif escolha == '2':
            
            print("Saindo...")
            break  # Saindo do loop infinito e encerrando o programa

        # Caso a escolha do usuário não seja nem '1' nem '2'
        else:
            
            print("Escolha inválida. Tente novamente.")

# Chamando a função
menu_interativo()   


"""
Área Total (m²):    [50,     60,     100,    150,    120,   130,     170,   80]
Número de Quartos:  [1,      2,      3,      4,      3,     2,       4,     2]
Número de Banheiros:[1,      1,      2,      3,      2,     1,       3,     1]

Preço da Casa (R$): [200000, 300000, 500000, 750000, 600000, 550000, 800000, 400000]
"""
print()
            