"""
Exercício: Sistema de Recomendação de Calçados com K-NN

Você está trabalhando como desenvolvedor em uma loja de calçados e
recebeu a tarefa de criar um sistema de recomendação de calçados para
os clientes. O objetivo é oferecer uma experiência de compra 
personalizada, considerando as preferências do cliente em termos de 
conforto, estilo e durabilidade.

Para este projeto, você optou por utilizar o algoritmo K-Nearest Neighbors (K-NN) 
para criar um modelo de recomendação.

Requisitos:

    - Utilize o algoritmo K-Nearest Neighbors para treinar um modelo de
        recomendação com base em um conjunto de dados de calçados. O 
        conjunto de dados já foi fornecido no código e contém informações 
        sobre conforto, estilo e durabilidade para diferentes tipos de 
        calçados: Esportivo, Formal e Casual.

    - Implemente uma interface gráfica usando a biblioteca Tkinter que permita
        ao usuário ajustar suas preferências usando escalas (de 1 a 5) para 
        conforto, estilo e durabilidade.

    - Depois que o usuário ajustar suas preferências, ele deve ser capaz de 
        clicar em um botão "Recomendar" para obter uma recomendação de tipo de 
        calçado que melhor atenda às suas necessidades.

    Mostre a recomendação em um rótulo na interface gráfica.
"""

# Importa a classe KNeighborsClassifier da biblioteca scikit-learn para usar o algoritmo k-NN.
from sklearn.neighbors import KNeighborsClassifier

# Importa a biblioteca NumPy para realizar operações numéricas.
import numpy as np

# Importa a biblioteca Tkinter para criar a interface gráfica.
import tkinter as tk

# Importa ttk e StringVar do módulo tkinter.
# ttk é usado para widgets temáticos que oferecem uma aparência mais agradável.
# StringVar é uma classe Tkinter usada para manipular variáveis de string.
from tkinter import ttk, StringVar


# Função para fazer a recomendação de um calçado com 
# base nas preferências do usuário.
def recomendar_calcado():
    
    # Obtém o valor da escala de conforto escolhida pelo usuário através
    # da variável Tkinter 'var_conforto'.
    conforto_usuario = var_conforto.get()
    
    # Obtém o valor da escala de estilo escolhida pelo usuário através da
    # variável Tkinter 'var_estilo'.
    estilo_usuario = var_estilo.get()
    
    # Obtém o valor da escala de durabilidade escolhida pelo usuário através 
    # da variável Tkinter 'var_durabilidade'.
    durabilidade_usuario = var_durabilidade.get()
    
    # Utiliza o modelo de aprendizado de máquina (k-NN) para fazer 
    # uma previsão com base nos três parâmetros.
    # Os valores são convertidos em um array NumPy e passados para o
    # método 'predict' do modelo.
    # O resultado é armazenado na variável 'recomendacao'.
    recomendacao = modelo.predict(np.array([[conforto_usuario, estilo_usuario, durabilidade_usuario]]))
    
    # Atualiza o rótulo da interface gráfica para mostrar a recomendação.
    # Utiliza f-string para inserir o tipo de calçado recomendado (obtido de 'recomendacao[0]') na string.
    rotulo_recomendacao.config(text=f"Com base nas suas preferências, recomendamos um calçado do tipo: {recomendacao[0]}")
    
    
# Criar base de dados fictícia
dados_calcados = [
    [5, 1, 3, 'Esportivo'],
    [4, 2, 4, 'Esportivo'],
    [4, 1, 5, 'Esportivo'],
    [5, 2, 3, 'Esportivo'],
    [2, 5, 2, 'Formal'],
    [1, 5, 3, 'Formal'],
    [2, 4, 3, 'Formal'],
    [1, 4, 4, 'Formal'],
    [3, 3, 5, 'Casual'],
    [2, 4, 4, 'Casual'],
    [3, 4, 5, 'Casual'],
    [4, 3, 4, 'Casual'],
]


# Convertendo a lista 'dados_calcados' em um array NumPy 
# para facilitar a manipulação.
dados_calcados = np.array(dados_calcados)

# A variável 'X' recebe todas as linhas do array e todas as colunas exceto a última.
# O método 'astype(int)' é usado para garantir que todos os elementos sejam inteiros.
X = dados_calcados[:, :-1].astype(int)

# A variável 'y' recebe todas as linhas do array e apenas a última coluna.
# Estes são os rótulos ou as categorias dos calçados ('Esportivo', 'Formal', etc.).
y = dados_calcados[:, -1]

# Criando um objeto da classe KNeighborsClassifier com 3 vizinhos mais próximos
modelo = KNeighborsClassifier(n_neighbors=3)

# Treinando o modelo k-NN com os dados 'X' e os rótulos 'y'.
modelo.fit(X, y)


# Criando a janela principal da aplicação Tkinter.
janela = tk.Tk()

# Configurando o título da janela para "Recomendação de Calçados".
janela.title("Recomendação de Calçados")

# Inicializando variáveis Tkinter para armazenar as escolhas do usuário.
# Essas variáveis serão usadas para capturar as preferências do usuário
# em relação a conforto, estilo e durabilidade.
var_conforto = tk.IntVar()
var_estilo = tk.IntVar()
var_durabilidade = tk.IntVar()


# Criando um frame (quadro) principal que conterá outros widgets.
# O padding é configurado para "10" para fornecer um espaçamento ao redor do frame.
frame_principal = ttk.Frame(janela, padding="10")

# Posicionando o frame na primeira linha e primeira coluna da janela principal.
# O frame é "grudado" nas quatro direções (Norte, Sul, Leste, Oeste) para
# preencher todo o espaço disponível.
frame_principal.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))



# Criando um rótulo (Label) para servir como título na interface gráfica.
# Este rótulo é adicionado ao frame_principal e exibirá o texto "Selecione suas preferências".
# A fonte usada é Arial com tamanho 16.
ttk.Label(frame_principal, 
          text="Selecione suas preferências", 
          font=("Arial", 16)).grid(row=0, column=0, columnspan=3, pady=10)


# Criando um rótulo para a escala de conforto.
# Este rótulo também é adicionado ao frame_principal e exibirá o texto "Conforto:".
# Ele é posicionado à esquerda (sticky=tk.W) e tem um pequeno espaçamento vertical (pady=5).
ttk.Label(frame_principal, 
          text="Conforto:",
          font=("Arial", 16)).grid(row=1, column=0, sticky=tk.W, pady=5)


# Criando uma escala (Slider) para a seleção de conforto.
# A escala vai de 1 a 5 (from_=1, to=5), é horizontal (orient=tk.HORIZONTAL) e tem resolução de 1.
# A variável Tkinter var_conforto é usada para armazenar o valor selecionado pelo usuário.
escala_conforto = tk.Scale(frame_principal, 
                           from_=1, 
                           to=5, 
                           orient=tk.HORIZONTAL, 
                           resolution=1, 
                           variable=var_conforto,
                           font=("Arial", 16))

# Posicionando a escala de conforto na interface.
# Ela é colocada na primeira linha (row=1), na segunda coluna (column=1).
# A escala é alinhada à direita (sticky=tk.E) e tem um pequeno espaçamento vertical (pady=5).
escala_conforto.grid(row=1, column=1, sticky=tk.E, pady=5)

#------------------------------------------------------

# Criando um rótulo (Label) para a escala de estilo.
# Este rótulo é adicionado ao frame_principal e exibirá o texto "Estilo:".
# Ele é posicionado à esquerda (sticky=tk.W) e tem um pequeno espaçamento vertical (pady=5).
ttk.Label(frame_principal, 
          text="Estilo:",
          font=("Arial", 16)).grid(row=2, column=0, sticky=tk.W, pady=5)

# Criando uma escala (Slider) para a seleção de estilo.
# A escala vai de 1 a 5 (from_=1, to=5), é horizontal (orient=tk.HORIZONTAL) e tem resolução de 1.
# A variável Tkinter var_estilo é usada para armazenar o valor selecionado pelo usuário.
escala_estilo = tk.Scale(frame_principal, 
                         from_=1, 
                         to=5, 
                         orient=tk.HORIZONTAL, 
                         resolution=1, 
                         variable=var_estilo,
                         font=("Arial", 16))

# Posicionando a escala de estilo na interface.
# Ela é colocada na terceira linha (row=2), na segunda coluna (column=1).
# A escala é alinhada à direita (sticky=tk.E) e tem um pequeno espaçamento vertical (pady=5).
escala_estilo.grid(row=2, column=1, sticky=tk.E, pady=5)


#------------------------------------------------------

# Criando um rótulo (Label) para a escala de durabilidade.
# Este rótulo é adicionado ao frame_principal e exibirá o texto "Durabilidade:".
# Ele é posicionado à esquerda (sticky=tk.W) e tem um pequeno espaçamento vertical (pady=5).
ttk.Label(frame_principal, 
          text="Durabilidade:",
          font=("Arial", 16)).grid(row=3, column=0, sticky=tk.W, pady=5)

# Criando uma escala (Slider) para a seleção de durabilidade.
# A escala vai de 1 a 5 (from_=1, to=5), é horizontal (orient=tk.HORIZONTAL) e tem resolução de 1.
# A variável Tkinter var_durabilidade é usada para armazenar o valor selecionado pelo usuário.
escala_durabilidade = tk.Scale(frame_principal, 
                               from_=1, 
                               to=5, 
                               orient=tk.HORIZONTAL, 
                               resolution=1, 
                               variable=var_durabilidade,
                               font=("Arial", 16))

# Posicionando a escala de durabilidade na interface.
# Ela é colocada na quarta linha (row=3), na segunda coluna (column=1).
# A escala é alinhada à direita (sticky=tk.E) e tem um pequeno espaçamento vertical (pady=5).
escala_durabilidade.grid(row=3, column=1, sticky=tk.E, pady=5)


#------------------------------------------------


# Criando um botão (Button) para disparar a função de recomendação.
# Este botão é adicionado ao frame_principal e tem o texto "Recomendar".
# A função recomendar_calcado() será chamada quando o botão for pressionado.
botao_recomendar = ttk.Button(frame_principal, 
                              text="Recomendar",
                              command=recomendar_calcado)

# Posicionando o botão na interface.
# Ele é colocado na quinta linha (row=4) e ocupa 3 colunas (columnspan=3).
# Tem um espaçamento vertical de 10 pixels (pady=10).
botao_recomendar.grid(row=4, column=0, columnspan=3, pady=10)


# Criando um rótulo (Label) para exibir as recomendações.
# Este rótulo é adicionado ao frame_principal e inicialmente não tem texto ("").
# O parâmetro wraplength=300 faz com que o texto seja quebrado após 300 pixels.
rotulo_recomendacao = ttk.Label(frame_principal, 
                                text="Teste",
                                font="Arial 16",
                                wraplength=300)

# Posicionando o rótulo na interface.
# Ele é colocado na sexta linha (row=5) e ocupa 3 colunas (columnspan=3).
# Tem um espaçamento vertical de 10 pixels (pady=10).
rotulo_recomendacao.grid(row=5, column=0, columnspan=3, pady=10)

# Iniciar a janela
janela.mainloop()