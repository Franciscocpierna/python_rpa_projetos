"""
Aprendizado Supervisionado

O algoritmo aprende a partir de um conjunto de dados rotulado, 
ou seja, cada exemplo de treinamento é associado a um rótulo. 

O objetivo é aprender um mapeamento dos dados de entrada para 
os rótulos de saída.

Vamos considerar algumas características comuns que frequentemente 
diferenciam um e-mail de spam de um e-mail legítimo:

    - Número de palavras: A quantidade de palavras no e-mail.
    
    - Contém a palavra 'grátis': Se o e-mail contém a 
        palavra "grátis" (1 para 'Sim', 0 para 'Não').
    
    - Contém a palavra 'oferta': Se o e-mail contém a palavra 
        "oferta" (1 para 'Sim', 0 para 'Não').
        
    - Links externos: O número de links externos no e-mail.

A etiqueta ainda será É Spam (1 para 'Sim', 0 para 'Não').
"""

# Importa a classe GaussianNB do módulo sklearn.naive_bayes
# Esta classe é usada para implementar o algoritmo Naive Bayes.
from sklearn.naive_bayes import GaussianNB

# Importa a biblioteca pandas para manipulação e análise de dados.
import pandas as pd


# Define uma função chamada 'extrair_caracteristicas' que aceita um argumento 'email_texto'.
# Essa função é responsável por extrair várias características do texto de um e-mail.
def extrair_caracteristicas(email_texto):
    
    # Conta o número de palavras no texto do e-mail.
    # O método 'split()' divide o texto em uma lista de palavras e 
    # 'len()' conta o número de elementos na lista.
    numero_palavras = len(email_texto.split())
    
    
    # Verifica se a palavra "grátis" está presente no texto do e-mail.
    # A função 'lower()' é usada para tornar a busca insensível a maiúsculas e minúsculas.
    # Se a palavra "grátis" estiver presente, 'contem_gratis' será 1, caso contrário, será 0.
    contem_gratis = 1 if "grátis" in email_texto.lower() else 0
    
    
    # Verifica se a palavra "oferta" está presente no texto do e-mail.
    # A função 'lower()' é usada para tornar a busca insensível a maiúsculas e minúsculas.
    # Se a palavra "oferta" estiver presente, 'contem_oferta' será 1, caso contrário, será 0.
    contem_oferta = 1 if "oferta" in email_texto.lower() else 0
    
    
    # Conta a quantidade de ocorrências da string "http" no texto do e-mail.
    # Isso serve como uma aproximação para contar o número de links externos no e-mail.
    # A função 'lower()' é usada para tornar a busca insensível a maiúsculas e minúsculas.
    qtd_links = email_texto.lower().count("http")
    
    
    # Retorna uma lista com as características extraídas:
    # número de palavras, presença da palavra "grátis", presença da palavra "oferta" e quantidade de links.
    return [numero_palavras, contem_gratis, contem_oferta, qtd_links]


# Dados para treinamento do modelo
# 0 - Não é SPAM
# 1 - É SPAM

#Não é SPAM
# 100 palavras
# 0 - Grátis
# 0 - Oferta
# 1 - Links
dados_treino = {
    'Numero_Palavras': [90, 150, 50, 100, 50, 75],
    'Contem_Gratis': [0, 1, 0, 1, 0, 1],
    'Contem_Oferta': [0, 1, 1, 0, 0, 1],
    'Qtd_Links': [1, 3, 2, 4, 0, 5],
    'Eh_Spam': [0, 1, 1, 1, 0, 1]
}

# Dados de treino são colocados no DataFrame 'df_treino'
# Esses dados são usados para treinar o modelo Naive Bayes
df_treino = pd.DataFrame(dados_treino)

#display(df_treino)
print(df_treino)


# Separa as colunas de características e a coluna de 
# etiquetas (labels) em duas variáveis diferentes, X_treino e y_treino.
# X_treino contém as características que serão usadas para treinar o modelo.
# y_treino contém as etiquetas que indicam se cada linha é spam (1) ou não spam (0).
X_treino = df_treino[['Numero_Palavras', 'Contem_Gratis', 'Contem_Oferta', 'Qtd_Links']]
y_treino = df_treino['Eh_Spam']


# Cria uma instância da classe GaussianNB, que implementa o algoritmo Naive Bayes
modelo_nb = GaussianNB()

# Treina o modelo Naive Bayes usando os dados em X_treino para as
# características e y_treino para as etiquetas.
# O método 'fit' ajusta o modelo aos dados fornecidos.
modelo_nb.fit(X_treino, y_treino)


#email_exemplo = "Olá, este é um email para te desejar uma boa noite!"
email_exemplo = "Olá, compre nosso produto amostra grátis e está em Oferta hoje, aproveite nossa promoção pelo link https://www.google.com/  e link https://www.google.com/"

# Simula um e-mail inserido pelo usuário para teste.
# Neste caso, é um e-mail simples que deseja uma "boa noite".
# email_exemplo = "Olá, este é um email para te desejar uma boa noite!."

# Utiliza a função 'extrair_caracteristicas' para obter as
# características deste e-mail de exemplo.
caracteristicas = extrair_caracteristicas(email_exemplo)


# Exibe as características extraídas na tela.
print(f"\nCaracteristicas extraídas")
print(f"Número de Palavras: {caracteristicas[0]}")
print(f"Contém 'Grátis': {caracteristicas[1]}")
print(f"Contém 'Oferta': {caracteristicas[2]}")
print(f"Quantidade de Links': {caracteristicas[3]}")

# Prepara as características para serem usadas no modelo, colocando-as em um DataFrame.
caracteristicas_df = pd.DataFrame([caracteristicas], columns=['Numero_Palavras', 'Contem_Gratis', 'Contem_Oferta', 'Qtd_Links'])