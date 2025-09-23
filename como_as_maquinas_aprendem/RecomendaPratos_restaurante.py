"""
Exercício: Sistema de Recomendação de Pratos em um Restaurante

Em um projeto de ciência de dados, você foi contratado para desenvolver
um sistema de recomendação de pratos para um restaurante. O restaurante 
oferece uma variedade de pratos, incluindo opções vegetarianas, pratos 
de carne e frutos do mar. Além disso, os pratos variam em nível de apimentado 
e tempo de preparo.

O objetivo é criar um programa que recomende um prato com base nas preferências
do cliente. Para isso, você decidiu utilizar o algoritmo Naive Bayes para treinar 
um modelo de classificação.

Requisitos:

    - O programa deve usar o algoritmo Naive Bayes para treinar um modelo com 
        base em um conjunto de dados fornecido. O conjunto de dados inclui 
        informações sobre o tipo de comida, nível de apimentado e tempo de 
        preparo para cada prato.

    - Utilize a biblioteca Tkinter para criar uma interface gráfica que permita
        ao usuário selecionar suas preferências em relação ao tipo de comida, nível 
        de apimentado e tempo de preparo.

    - O programa deve então usar o modelo treinado para recomendar um prato que se 
        alinhe às preferências do usuário.

    - Mostre a recomendação em um rótulo na interface gráfica.

Conjunto de dados de exemplo:

O conjunto de dados dados_restaurante é fornecido no formato:
[Tipo de Comida, Nível de Apimentado, Tempo de Preparo, Nome do Prato]
[Tipo de Comida, Nível de Apimentado, Tempo de Preparo, Nome do Prato]

"""

# Importando a classe GaussianNB da biblioteca scikit-learn.
# GaussianNB é um classificador baseado em Naive Bayes.
from sklearn.naive_bayes import GaussianNB

# Importando a biblioteca Tkinter para criar a interface gráfica.
# Tkinter é uma biblioteca padrão do Python para desenvolvimento de interfaces gráficas.
import tkinter as tk

# Importando 'ttk' do Tkinter, que é um conjunto de widgets temáticos
# para Tkinter, oferecendo uma aparência mais moderna para os elementos da interface.
from tkinter import ttk


# Dados de treinamento
dados_restaurante = [
    [1, 1, 1, 'Salada'],
    [2, 2, 2, 'Bife'],
    [3, 3, 3, 'Camarão Apimentado'],
    [1, 2, 3, 'Vegetariano Especial'],
    [2, 1, 1, 'Frango Grelhado'],
    [3, 1, 2, 'Sopa de Frutos do Mar'],
    [1, 3, 2, 'Chilli Vegetariano'],
    [2, 3, 1, 'Costelas'],
    [3, 2, 2, 'Moqueca'],
    [2, 1, 3, 'Lasanha'],
    [3, 1, 3, 'Sushi'],
    [1, 2, 1, 'Wrap de Frango'],
    [2, 2, 1, 'Pizza'],
    [3, 3, 1, 'Curry Indiano'],
    [1, 1, 3, 'Smoothie de Frutas'],
    [3, 1, 1, 'Ramen'],
    [1, 3, 3, 'Falafel'],
    [2, 3, 3, 'Goulash'],
    [3, 2, 1, 'Tacos'],
    [1, 1, 2, 'Yogurte Grego']
]

# Criando a variável 'X' que contém todos os atributos de cada
# linha em 'dados_restaurante', exceto o último elemento.
# O último elemento em cada linha é o rótulo ou a classe (nome 
# do prato), que não queremos incluir em 'X'.
X = [linha[:-1] for linha in dados_restaurante]

# Criando a variável 'y' que contém apenas o último elemento de 
# cada linha em 'dados_restaurante'.
# Estes são os rótulos ou classes (nomes dos pratos) que queremos prever.
y = [linha[-1] for linha in dados_restaurante]


# Instanciando o classificador Gaussian Naive Bayes e 
# armazenando-o na variável 'modelo_nb'.
modelo_nb = GaussianNB()

# Utilizando o método 'fit' para treinar o modelo.
# 'X' é a matriz de atributos e 'y' é o vetor de rótulos.
modelo_nb.fit(X, y)


# Definindo a função 'recomendar_prato' para fazer a recomendação
# de pratos com base nas preferências do usuário.
def recomendar_prato():
    
    # Obtendo o valor da variável Tkinter 'var_tipo_comida', que
    # contém o tipo de comida selecionado pelo usuário.
    tipo_comida = var_tipo_comida.get()
    
    # Obtendo o valor da variável Tkinter 'var_nivel_apimentado', que
    # contém o nível de apimentado escolhido pelo usuário.
    nivel_apimentado = var_nivel_apimentado.get()
    
    # Obtendo o valor da variável Tkinter 'var_tempo_preparo', que 
    # contém o tempo de preparo escolhido pelo usuário.
    tempo_preparo = var_tempo_preparo.get()
    
    
    # Utilizando o método 'predict' do modelo para fazer uma previsão com base nos valores obtidos.
    # Os valores são agrupados em uma lista de listas, como o método 'predict' espera receber.
    predicao = modelo_nb.predict([[tipo_comida, nivel_apimentado, tempo_preparo]])
    
    # Atualizando o texto do rótulo Tkinter 'rotulo_recomendacao' para mostrar o prato recomendado.
    rotulo_recomendacao['text'] = f"Prato Recomendado: {predicao[0]}"
    
    

# Inicializando a janela Tkinter e armazenando-a na variável 'janela'.
janela = tk.Tk()

# Configurando o título da janela para "Recomendação de Pratos".
janela.title("Recomendação de Pratos")

# Inicializando variáveis Tkinter para armazenar as escolhas do usuário.
# Essas variáveis são do tipo IntVar, que podem armazenar valores inteiros.
var_tipo_comida = tk.IntVar()
var_nivel_apimentado = tk.IntVar()
var_tempo_preparo = tk.IntVar()


# Criando um frame principal usando o ttk (themed Tkinter) para uma aparência mais agradável.
# O frame terá um padding de 10 pixels.
frame_principal = ttk.Frame(janela, padding="10")

# Posicionando o frame principal na grade da janela.
# Ele será colocado na primeira linha (row=0) e na primeira coluna (column=0).
# As opções sticky=(tk.W, tk.E, tk.N, tk.S) fazem o frame se expandir nas
# direções Oeste, Leste, Norte e Sul, respectivamente.
frame_principal.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))


# Criando um rótulo (Label) para "Tipo de Comida" e posicionando-o na grade.
# O rótulo será colocado na primeira linha (row=1) e na primeira coluna (column=0) do frame principal.
# A opção 'sticky=tk.W' faz o texto do rótulo alinhar à esquerda (Oeste).
# A opção 'pady=5' adiciona um padding vertical de 5 pixels acima e abaixo do rótulo.
ttk.Label(frame_principal, text="Tipo de Comida:").grid(row=1, column=0, sticky=tk.W, pady=5)


# Criando um botão de opção (Radiobutton) para a opção "Vegetariana".
# O botão de opção será vinculado à variável Tkinter 'var_tipo_comida' e terá o valor 1.
# O botão será colocado na primeira linha (row=1) e na segunda coluna (column=1) do frame principal.
ttk.Radiobutton(frame_principal, text="Vegetariana", variable=var_tipo_comida, value=1).grid(row=1, column=1)

# Criando um botão de opção (Radiobutton) para a opção "Carne".
# O botão de opção será vinculado à variável Tkinter 'var_tipo_comida' e terá o valor 2.
# O botão será colocado na primeira linha (row=1) e na terceira coluna (column=2) do frame principal.
ttk.Radiobutton(frame_principal, text="Carne", variable=var_tipo_comida, value=2).grid(row=1, column=2)

# Criando um botão de opção (Radiobutton) para a opção "Frutos do Mar".
# O botão de opção será vinculado à variável Tkinter 'var_tipo_comida' e terá o valor 3.
# O botão será colocado na primeira linha (row=1) e na quarta coluna (column=3) do frame principal.
ttk.Radiobutton(frame_principal, text="Frutos do Mar", variable=var_tipo_comida, value=3).grid(row=1, column=3)


# Criando um rótulo (Label) com o texto "Nível de Apimentado:".
# Este rótulo é colocado na linha 2 (row=2) e na coluna 0 (column=0) do frame principal.
# A opção 'sticky=tk.W' alinha o texto do rótulo à esquerda (Oeste).
# A opção 'pady=5' adiciona um padding vertical de 5 pixels acima e abaixo do rótulo.
ttk.Label(frame_principal, text="Nível de Apimentado:").grid(row=2, column=0, sticky=tk.W, pady=5)

# Criando um botão de opção (Radiobutton) com o texto "Baixo".
# Este botão de opção está vinculado à variável Tkinter 'var_nivel_apimentado' e tem um valor de 1.
# É colocado na linha 2 (row=2) e na coluna 1 (column=1) do frame principal.
ttk.Radiobutton(frame_principal, text="Baixo", variable=var_nivel_apimentado, value=1).grid(row=2, column=1)

# Criando um botão de opção (Radiobutton) com o texto "Médio".
# Este botão de opção está vinculado à variável Tkinter 'var_nivel_apimentado' e tem um valor de 2.
# É colocado na linha 2 (row=2) e na coluna 2 (column=2) do frame principal.
ttk.Radiobutton(frame_principal, text="Médio", variable=var_nivel_apimentado, value=2).grid(row=2, column=2)

# Criando um botão de opção (Radiobutton) com o texto "Alto".
# Este botão de opção está vinculado à variável Tkinter 'var_nivel_apimentado' e tem um valor de 3.
# É colocado na linha 2 (row=2) e na coluna 3 (column=3) do frame principal.
ttk.Radiobutton(frame_principal, text="Alto", variable=var_nivel_apimentado, value=3).grid(row=2, column=3)


# Criando um rótulo (Label) com o texto "Tempo de Preparo:".
# Este rótulo é colocado na linha 3 (row=3) e na coluna 0 (column=0) do frame principal.
# A opção 'sticky=tk.W' alinha o texto do rótulo à esquerda (Oeste).
# A opção 'pady=5' adiciona um padding vertical de 5 pixels acima e abaixo do rótulo.
ttk.Label(frame_principal, text="Tempo de Preparo:").grid(row=3, column=0, sticky=tk.W, pady=5)

# Criando um botão de opção (Radiobutton) com o texto "Rápido".
# Este botão de opção está vinculado à variável Tkinter 'var_tempo_preparo' e tem um valor de 1.
# É colocado na linha 3 (row=3) e na coluna 1 (column=1) do frame principal.
ttk.Radiobutton(frame_principal, text="Rápido", variable=var_tempo_preparo, value=1).grid(row=3, column=1)

# Criando um botão de opção (Radiobutton) com o texto "Médio".
# Este botão de opção está vinculado à variável Tkinter 'var_tempo_preparo' e tem um valor de 2.
# É colocado na linha 3 (row=3) e na coluna 2 (column=2) do frame principal.
ttk.Radiobutton(frame_principal, text="Médio", variable=var_tempo_preparo, value=2).grid(row=3, column=2)

# Criando um botão de opção (Radiobutton) com o texto "Demorado".
# Este botão de opção está vinculado à variável Tkinter 'var_tempo_preparo' e tem um valor de 3.
# É colocado na linha 3 (row=3) e na coluna 3 (column=3) do frame principal.
ttk.Radiobutton(frame_principal, text="Demorado", variable=var_tempo_preparo, value=3).grid(row=3, column=3)


# Criando um botão (Button) com o texto "Recomendar".
# Este botão está configurado para chamar a função 'recomendar_prato' quando clicado.
# O botão é colocado na linha 4 (row=4) e abrange 4 colunas (columnspan=4) no frame principal.
# A opção 'pady=10' adiciona um padding vertical de 10 pixels acima e abaixo do botão.
ttk.Button(frame_principal, text="Recomendar", command=recomendar_prato).grid(row=4, column=0, columnspan=4, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

# Criando um rótulo (Label) sem texto inicial (text="").
# Este rótulo será usado para mostrar a recomendação do prato.
# O rótulo é colocado na linha 5 (row=5) e abrange 4 colunas (columnspan=4) no frame principal.
# A opção 'wraplength=300' permite que o texto dentro do rótulo seja quebrado em várias linhas se tiver mais de 300 pixels de largura.
# A opção 'pady=10' adiciona um padding vertical de 10 pixels acima e abaixo do rótulo.
rotulo_recomendacao = ttk.Label(frame_principal, text="", wraplength=300)
rotulo_recomendacao.grid(row=5, column=0, columnspan=4, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

# Iniciando o loop principal da aplicação Tkinter.
# Esta linha mantém a janela aberta e lida com todos os eventos da interface do usuário.
janela.mainloop()
