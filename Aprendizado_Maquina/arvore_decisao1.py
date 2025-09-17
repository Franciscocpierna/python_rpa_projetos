
# 1. Importar bibliotecas necessárias

# Importar a classe CountVectorizer do módulo sklearn.feature_extraction.text
# Esta classe é usada para converter uma coleção de documentos de
# texto em uma matriz de contagens de tokens.
from sklearn.feature_extraction.text import CountVectorizer

# Importar a classe MultinomialNB do módulo sklearn.naive_bayes
# Esta classe é uma implementação do algoritmo Naive Bayes para 
# classificação multinomial.
from sklearn.naive_bayes import MultinomialNB

# Importar a função make_pipeline do módulo sklearn.pipeline
# Essa função é usada para criar um pipeline que pode executar várias 
# etapas consecutivas em um conjunto de dados.
from sklearn.pipeline import make_pipeline


# 2. Preparar os dados

# Criar uma lista de palavras chamada 'palavras'. 
# Esta lista contém as palavras que serão usadas para treinar o modelo de classificação.
palavras = ["maça", "banana", "uva", "cachorro", "gato", "carro"]

# Criar uma lista de rótulos chamada 'rotulos'. 
# Cada rótulo corresponde a uma palavra na lista 'palavras'. 
# Aqui, o número 1 representa "Fruta" e o número 0 representa "Não é uma fruta".
rotulos = [1, 1, 1, 0, 0, 0]  # 1 para Fruta, 0 para Não é uma fruta


# 3. Transformar palavras em vetores numéricos
# Isso será feito automaticamente pela pipeline


# 4. Treinar o modelo

# Criar um pipeline usando a função 'make_pipeline'.
# O pipeline realizará duas tarefas principais em sequência:
# 1. Transformar as palavras em vetores numéricos usando CountVectorizer.
# 2. Treinar um classificador Naive Bayes usando MultinomialNB.
modelo = make_pipeline(CountVectorizer(), MultinomialNB())

# Treinar o modelo utilizando o método 'fit'.
# O método 'fit' faz duas coisas aqui devido ao pipeline:
# 1. Ele primeiro transforma a lista de palavras em vetores numéricos.
# 2. Depois, treina o classificador Naive Bayes usando esses vetores 
# e os rótulos correspondentes.
modelo.fit(palavras, rotulos)


# 5. Fazer previsões

# Criar uma lista que contém uma nova palavra para a qual queremos fazer uma previsão.
# A lista é chamada 'nova_palavra' e contém a palavra "laranja".
nova_palavra = ["banana"]

# Usar o método 'predict' do modelo treinado para fazer uma previsão para a nova palavra.
# O método 'predict' retorna uma lista de previsões, uma para cada exemplo fornecido.
# Aqui, como temos apenas uma palavra, a lista terá um único elemento.
previsao = modelo.predict(nova_palavra)

# Imprimir a previsão.
# Usamos uma expressão condicional para imprimir "Fruta" se a previsão for 1, e "Não é uma fruta" se for 0.
print("Previsão:", "Fruta" if previsao[0] == 1 else "Não é uma fruta")