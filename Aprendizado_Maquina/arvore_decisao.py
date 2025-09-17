"""
Vamos abordar um exemplo bem simples de aprendizado de máquina
usando Python. Utilizaremos é a Árvore de Decisão. Ele é usado tanto para
tarefas de classificação quanto de regressão e é muito intuitivo
de entender. Vou demonstrar como usar uma Árvore de Decisão para
classificar frutas como "Maça" ou "Laranja" com base em seu peso
e textura.
"""

# Código com Árvore de Decisão

# Importar bibliotecas necessárias
from sklearn.tree import DecisionTreeClassifier
import numpy as np


# Preparar os dados
# Temos algumas frutas medidas em termos de peso e textura
# Peso e Textura (1 para suave e 0 para áspero)
dados_frutas = np.array([[140, 1], [130, 1], [150, 0], [170, 0]])

# Rótulos (0 para maça e 1 para laranja)
rotulos_frutas = np.array([0, 0, 1, 1])


# Treinar o modelo

# Criar um classificador de Árvore de Decisão
classificador_arvore = DecisionTreeClassifier()

# Treinar o classificador com os dados
classificador_arvore.fit(dados_frutas, rotulos_frutas)

# Fazer previsões
# Temos uma fruta nova com peso 145g e textura áspera (0)
fruta_nova = np.array([[145, 0]])

# Usar o modelo para prever a classe da nova fruta
previsao = classificador_arvore.predict(fruta_nova)

# Mapear as classes numéricas para descrições textuais
mapeamento_classes = {0: 'Maçã', 1: 'Laranja'}

# Obter a descrição textual da previsão
descricao_previsao = mapeamento_classes[previsao[0]]

print(f"A fruta com peso {fruta_nova[0][0]}g e textura {'suave' if fruta_nova[0][1] == 1 else 'áspera'} é provavelmente uma {descricao_previsao}.")


# Características da laranja para teste
# Suponhamos que a laranja tenha peso de 160g e textura áspera (0)
laranja_teste = np.array([[160, 0]])

# Usar o modelo para prever a classe da laranja de teste
previsao_laranja = classificador_arvore.predict(laranja_teste)

# Obter a descrição textual da previsão da laranja
descricao_previsao_laranja = mapeamento_classes[previsao_laranja[0]]

print(f"A fruta com peso {laranja_teste[0][0]}g e textura {'suave' if laranja_teste[0][1] == 1 else 'áspera'} é provavelmente uma {descricao_previsao_laranja}.")
