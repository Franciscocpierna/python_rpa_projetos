"""
Exercício: Sistema de Recomendação de Filmes com Naive Bayes

Contexto:

Você é um desenvolvedor em uma startup que está trabalhando em um 
aplicativo de streaming de filmes. A empresa quer implementar um sistema
de recomendação de filmes para melhorar a experiência do usuário. Seu
objetivo é criar um sistema de recomendação que aprende com o feedback 
dos usuários.

Requisitos:

    - Utilize o algoritmo Naive Bayes para desenvolver um modelo de 
        recomendação de filmes. O conjunto de dados fornecido no código 
        inclui uma lista de filmes e seus respectivos 
        gêneros (Ficção Científica, Drama, Ação, etc.).

    - Implemente uma interface gráfica usando a biblioteca Tkinter. A interface deve:
        - Mostrar ao usuário um filme e seu gênero.
        - Ter botões "Sim" e "Não" para o usuário indicar se gostou ou
            não do filme exibido.

    - Com base no feedback do usuário, o sistema deve adaptar suas 
        recomendações. Se o usuário gostou de um filme de um determinado 
        gênero, outros filmes desse gênero deverão ser priorizados nas 
        recomendações futuras.

    - Após receber o feedback de 5 filmes, o sistema deve ser capaz de 
        mostrar uma lista de recomendações finais baseada nos gêneros que o 
        usuário mais gostou. Esta lista deve ser exibida em uma nova janela Tkinter.

    - Use uma caixa de mensagem para informar o usuário caso não seja possível
        determinar suas preferências de gênero.
"""

# Importando a biblioteca Tkinter para criar a interface gráfica do usuário.
import tkinter as tk

# Importando a classe messagebox do Tkinter para exibir caixas de diálogo.
from tkinter import messagebox

# Importando a biblioteca random para gerar números aleatórios.
import random

# Importando a biblioteca NumPy para manipulação de arrays e matrizes.
import numpy as np

# Importando o classificador Naive Bayes Multinomial do 
# scikit-learn para aprendizado de máquina.
from sklearn.naive_bayes import MultinomialNB


# Definindo uma função chamada 'codificar_genero' que leva um argumento 'genero'.
# Essa função codifica os gêneros de filmes como números inteiros.
# Por exemplo, se temos gêneros como ['Ação', 'Drama'], 'Ação' seria 
# codificado como 0 e 'Drama' como 1.
def codificar_genero(genero):
    
    # Utilizando o método .index() para encontrar o índice do gênero na lista 'generos'.
    # O índice serve como a codificação numérica do gênero.
    return generos.index(genero)


# Dicionario filmes de filmes e gêneros
dicionario_filmes = {
    'A Origem': 'Ficção Científica',
    'Matrix': 'Ficção Científica',
    'Interestelar': 'Ficção Científica',
    'Blade Runner': 'Ficção Científica',
    'Ex Machina': 'Ficção Científica',
    'Avatar': 'Ficção Científica',
    'Elysium': 'Ficção Científica',
    'De Volta Para o Futuro': 'Ficção Científica',
    'Duna': 'Ficção Científica',
    'Star Wars': 'Ficção Científica',
    'O Quinto Elemento': 'Ficção Científica',
    'Guerra nas Estrelas': 'Ficção Científica',
    'O Exterminador do Futuro': 'Ficção Científica',
    '2001: Uma Odisseia no Espaço': 'Ficção Científica',
    'Alien, o Oitavo Passageiro': 'Ficção Científica',
    'Distrito 9': 'Ficção Científica',
    'O Hospedeiro': 'Ficção Científica',
    'Planeta dos Macacos': 'Ficção Científica',
    'O Vingador do Futuro': 'Ficção Científica',
    'Eu Sou a Lenda': 'Ficção Científica',
    'O Poderoso Chefão': 'Drama',
    'Forrest Gump': 'Drama',
    'Coringa': 'Drama',
    'Gladiador': 'Drama',
    'O Resgate do Soldado Ryan': 'Drama',
    'Um Sonho de Liberdade': 'Drama',
    'Cidade de Deus': 'Drama',
    'A Lista de Schindler': 'Drama',
    'Clube da Luta': 'Drama',
    'Cisne Negro': 'Drama',
    'O Menino do Pijama Listrado': 'Drama',
    'À Espera de Um Milagre': 'Drama',
    'O Pianista': 'Drama',
    'O Lobo de Wall Street': 'Drama',
    '12 Homens e Uma Sentença': 'Drama',
    'O Silêncio dos Inocentes': 'Drama',
    'O Grande Gatsby': 'Drama',
    'Amnésia': 'Drama',
    'O Discurso do Rei': 'Drama',
    'Menina de Ouro': 'Drama',
    'Vingadores': 'Ação',
    'John Wick': 'Ação',
    'Homem de Ferro': 'Ação',
    'Missão Impossível': 'Ação',
    'Mad Max: Estrada da Fúria': 'Ação',
    'Duro de Matar': 'Ação',
    'Gladiador': 'Ação',
    'O Cavaleiro das Trevas': 'Ação',
    'Kill Bill': 'Ação',
    'Velozes e Furiosos': 'Ação',
    '007: Cassino Royale': 'Ação',
    'O Exterminador do Futuro': 'Ação',
    'Pantera Negra': 'Ação',
    'O Livro de Eli': 'Ação',
    'Homem-Aranha': 'Ação',
    'Star Wars: O Despertar da Força': 'Ação',
    'Capitão América': 'Ação',
    'Invasão a Casa Branca': 'Ação',
    'Guardiões da Galáxia': 'Ação',
    'Transformers': 'Ação',
    'O Senhor dos Anéis': 'Fantasia',
    'Harry Potter': 'Fantasia',
    'As Crônicas de Nárnia': 'Fantasia',
    'Pantera Negra': 'Fantasia',
    'Alice no País das Maravilhas': 'Fantasia',
    'Piratas do Caribe': 'Fantasia',
    'Labirinto do Fauno': 'Fantasia',
    'Stardust': 'Fantasia',
    'Avatar': 'Fantasia',
    'Coraline': 'Fantasia',
    'O Mágico de Oz': 'Fantasia',
    'Viagem ao Centro da Terra': 'Fantasia',
    'O Hobbit': 'Fantasia',
    'Malévola': 'Fantasia',
    'Beleza Oculta': 'Fantasia',
    'Enrolados': 'Fantasia',
    'A Bela e a Fera': 'Fantasia',
    'Frozen': 'Fantasia',
    'Shrek': 'Fantasia',
    'Moana': 'Fantasia',
    'O Rei Leão': 'Animação',
    'Toy Story': 'Animação',
    'Shrek': 'Animação',
    'Meu Amigo Totoro': 'Animação',
    'Procurando Nemo': 'Animação',
    'Monstros S.A.': 'Animação',
    'Wall-E': 'Animação',
    'Divertida Mente': 'Animação',
    'Frozen': 'Animação',
    'A Viagem de Chihiro': 'Animação',
    'Como Treinar o Seu Dragão': 'Animação',
    'Kung Fu Panda': 'Animação',
    'Moana': 'Animação',
    'Zootopia': 'Animação',
    'Os Incríveis': 'Animação',
    'Coco': 'Animação',
    'Aladdin': 'Animação',
    'Ratatouille': 'Animação',
    'Coraline': 'Animação',
    'Viva - A Vida é uma Festa': 'Animação',
    'O Auto da Compadecida': 'Comédia',
    'Minha Mãe é uma Peça': 'Comédia',
    'Se Beber, Não Case!': 'Comédia',
    'Superbad': 'Comédia',
    'Quem Vai Ficar com Mary?': 'Comédia',
    'American Pie': 'Comédia',
    'Trovão Tropical': 'Comédia',
    'Anchorman': 'Comédia',
    'Zoolander': 'Comédia',
    'O Virgem de 40 Anos': 'Comédia',
    'Todo Mundo em Pânico': 'Comédia',
    'As Branquelas': 'Comédia',
    'Meu Malvado Favorito': 'Comédia',
    'Shrek 2': 'Comédia',
    'Legalmente Loira': 'Comédia',
    'Debi & Lóide': 'Comédia',
    'MIB - Homens de Preto': 'Comédia',
    'Click': 'Comédia',
    'Escola de Rock': 'Comédia',
    'O Diabo Veste Prada': 'Comédia'
}


# Criando uma lista única de gêneros de filmes.
# A função set() é usada para remover quaisquer gêneros 
# duplicados na lista de valores do dicionário 'dicionario_filmes'.
# Depois, a função list() transforma o conjunto em uma lista novamente.
# Isso é útil para ter uma lista única de gêneros que será usada 
# mais tarde para codificação.
generos = list(set(dicionario_filmes.values()))


# Inicializa uma lista vazia para armazenar os gêneros codificados dos filmes.
generos_codificados = []

# Itera sobre todas as chaves (nomes dos filmes) no dicionário 'dicionario_filmes'.
for filme in dicionario_filmes.keys():
    
    # Usa a função 'codificar_genero' para obter o valor numérico do gênero do filme.
    genero_codificado = codificar_genero(dicionario_filmes[filme])
    
    # Adiciona o valor numérico à lista 'generos_codificados'.
    generos_codificados.append(genero_codificado)

# Converte a lista 'generos_codificados' em um array NumPy e remodela para ter uma única coluna.
dados_treino = np.array(generos_codificados).reshape(-1, 1)


"""
    usa a função np.random.randint() para gerar um array de rótulos aleatórios 
    que são 0 ou 1.

    - O primeiro argumento 0 é o valor mínimo do intervalo para os números aleatórios.
    
    - O segundo argumento 2 é o valor máximo do intervalo para os números aleatórios, 
        mas note que este é exclusivo. Ou seja, o número gerado estará no
        intervalo [0,2), o que significa que ele pode ser 0 ou 1, mas não 2.
        
    - O terceiro argumento size=len(dicionario_filmes) define o tamanho do array 
        de rótulos a ser igual ao número de filmes em dicionario_filmes
"""
rotulos_treino = np.random.randint(0, 2, size=len(dicionario_filmes))

# Inicializando o modelo Naive Bayes Multinomial do scikit-learn.
# Este é um classificador que será treinado para recomendar filmes com base nos gêneros.
modelo_nb = MultinomialNB()

# Treinando o modelo usando os dados e rótulos preparados.
# O método .fit() é responsável pelo treinamento do modelo.
modelo_nb.fit(dados_treino, rotulos_treino)

# Função para recomendar um filme com base nos filmes que o usuário já viu.
# A função recebe como argumento a lista 'filmes_vistos', que contém os 
# filmes já vistos pelo usuário.
filmes_vistos = []
generos_gostados = {}

# Função para recomendar um filme
def recomendar_filme(filmes_vistos):
    
    # Inicializa uma lista vazia para armazenar os filmes que 
    # o usuário ainda não viu.
    filmes_nao_vistos = []

    # Itera sobre todas as chaves (nomes dos filmes) no dicionário 'dicionario_filmes'.
    for filme in dicionario_filmes.keys():

        # Verifica se o filme atual já foi visto pelo usuário.
        if filme not in filmes_vistos:

            # Se o filme não foi visto, adiciona-o à lista 'filmes_nao_vistos'.
            filmes_nao_vistos.append(filme)
            
    
    # Inicializando uma lista vazia para armazenar os gêneros codificados
    # dos filmes que o usuário ainda não viu.
    generos_codificados = []

    # Utilizando um loop 'for' para percorrer todos os filmes que o usuário ainda não viu.
    for filme in filmes_nao_vistos:
        
        # Usando a função 'codificar_genero' para obter o código numérico 
        # correspondente ao gênero do filme.
        genero_codificado = codificar_genero(dicionario_filmes[filme])

        # Adicionando o gênero codificado à lista 'generos_codificados'.
        generos_codificados.append(genero_codificado)
        
    
    # Convertendo a lista 'generos_codificados' em um array NumPy.
    # Utilizamos .reshape(-1, 1) para garantir que o array seja bidimensional,
    # com uma coluna e um número de linhas determinado automaticamente.
    # Isso é feito para atender aos requisitos do método .predict().
    generos_codificados_array = np.array(generos_codificados).reshape(-1, 1)
    
    # Utilizando o método .predict() do modelo Naive Bayes para fazer previsões.
    # As previsões são armazenadas no array 'predicoes'.
    predicoes = modelo_nb.predict(generos_codificados_array)
    
    # Inicializa uma lista vazia para armazenar os filmes recomendados.
    filmes_recomendados = []

    # Enumera sobre o array de predicoes para obter tanto o índice 'i' quanto
    # a previsão 'pred' para cada elemento.
    for i, pred in enumerate(predicoes):

        # Verifica se a previsão é igual a 1, o que significa que o modelo 
        # acredita que o usuário vai gostar deste filme.
        if pred == 1:

            # Se a previsão é 1, adiciona o filme correspondente da 
            # lista 'filmes_nao_vistos' à lista 'filmes_recomendados'.
            filmes_recomendados.append(filmes_nao_vistos[i])
            
    
    # Se a lista 'filmes_recomendados' estiver vazia (ou seja, o modelo não 
    # prevê que o usuário gostará de nenhum filme não visto),
    # um filme é escolhido aleatoriamente da lista 'filmes_nao_vistos'.
    if not filmes_recomendados:
        return random.choice(filmes_nao_vistos)
    
    
    # Se a lista 'filmes_recomendados' contiver um ou mais filmes, um
    # filme é escolhido aleatoriamente dessa lista para ser recomendado.
    return random.choice(filmes_recomendados)


# Define a função para mostrar as recomendações finais ao usuário.
def mostrar_recomendacoes_finais():

    # Verifica se o dicionário 'generos_gostados' tem algum conteúdo.
    # Se estiver vazio, significa que o usuário ainda não deu feedback suficiente.
    if generos_gostados:

        # Ordena os gêneros com base no número de vezes que o usuário disse que gostou.
        # A ordenação é feita em ordem decrescente para pegar os gêneros mais gostados primeiro.
        # Apenas os dois gêneros mais gostados são considerados ([:2]).
        generos_favoritos = sorted(generos_gostados, key=generos_gostados.get, reverse=True)[:2]

        # Inicializa um dicionário que terá os gêneros favoritos como chaves e listas vazias como valores.
        # As listas vazias serão preenchidas com filmes desses gêneros favoritos.
        recomendacoes_finais = {genero: [] for genero in generos_favoritos}
    
        
        # Itera sobre todos os filmes e seus gêneros na lista 'dicionario_filmes'.
        for filme, genero in dicionario_filmes.items():

            # Verifica se o gênero do filme atual está entre os gêneros favoritos do usuário.
            if genero in generos_favoritos:

                # Se o gênero do filme está entre os favoritos, adiciona o filme à lista de recomendações finais.
                recomendacoes_finais[genero].append(filme)
                
        
        # Cria uma nova janela Tkinter para exibir as recomendações ao usuário.
        nova_janela = tk.Toplevel(root)
        nova_janela.title("Recomendações de Filmes")
        nova_janela.geometry("500x400")  # Define o tamanho da nova janela como 500x400 pixels.

        # Cria um objeto Canvas, que é uma área onde os widgets podem ser colocados.
        tela = tk.Canvas(nova_janela)

        # Cria uma barra de rolagem vertical e associa seu movimento ao canvas através do comando 'yview'.
        barra_rolagem = tk.Scrollbar(nova_janela, orient="vertical", command=tela.yview)      
        
        # Cria um quadro rolável que será inserido dentro do canvas.
        quadro_rolavel = tk.Frame(tela)

        # Vincula o evento <Configure> ao quadro_rolavel. Este evento é disparado quando o widget é redimensionado.
        # A função lambda atualiza a área de rolagem do Canvas para incluir todos os elementos dentro dele.
        # Isso permite que a barra de rolagem saiba até onde ela pode rolar.
        quadro_rolavel.bind(
            "<Configure>",
            lambda e: tela.configure(scrollregion=tela.bbox("all"))
        )
        
        # Cria uma "janela" dentro do Canvas (tela) para abrigar o quadro_rolavel.
        # O quadro_rolavel será ancorado no canto superior esquerdo (Northwest) dessa "janela".
        tela.create_window((0, 0), window=quadro_rolavel, anchor="nw")
        
        
        # Configura o comando de rolagem vertical do Canvas (tela) para ser controlado pela barra_rolagem.
        # Isso faz com que a barra de rolagem e o Canvas estejam sincronizados.
        tela.configure(yscrollcommand=barra_rolagem.set)
        
        
        # Adiciona um rótulo (Label) ao quadro_rolavel com um texto informativo.
        # O texto é "Recomendações baseadas nos gêneros que você gostou:", e o tamanho da fonte é 14.
        # O método pack com pady=10 adiciona um preenchimento vertical de 10 pixels acima e abaixo do rótulo.
        tk.Label(quadro_rolavel, text="Recomendações baseadas nos gêneros que você gostou:", font=("Arial", 14)).pack(pady=10)

        
        # Itera pelos gêneros e filmes nas recomendações finais.
        # "recomendacoes_finais" é um dicionário onde a chave é o gênero e o valor é uma lista de filmes desse gênero.
        for genero, filmes in recomendacoes_finais.items():

            # Cria um novo quadro (Frame) para cada gênero dentro do quadro_rolavel.
            # Os parâmetros padx e pady adicionam preenchimento horizontal e vertical ao quadro.
            quadro = tk.Frame(quadro_rolavel, padx=10, pady=5)
            quadro.pack(pady=10)  # pady=10 adiciona um preenchimento vertical de 10 pixels acima e abaixo do quadro.

            # Adiciona um rótulo (Label) ao quadro para exibir o nome do gênero.
            # O texto será o nome do gênero e a fonte será Arial, tamanho 12 e em negrito.
            # O fundo do rótulo será cinza claro (#eee).
            tk.Label(quadro, text=genero, font=("Arial", 12, "bold"), bg="#eee").pack(fill="x")      
            
            # Itera pela lista de filmes do gênero atual.
            for filme in filmes:
                
                # Adiciona um rótulo (Label) para cada filme dentro do quadro do gênero.
                # O texto será o nome do filme e o wraplength=400 quebra o texto se ele exceder 400 pixels.
                tk.Label(quadro, text=filme, wraplength=400).pack(pady=2, padx=5)  # pady=2 e padx=5 adicionam preenchimento ao redor do rótulo.

        # Configura o layout dos widgets.
        # O Canvas (tela) e a barra de rolagem serão exibidos lado a lado.
        tela.pack(side="left", fill="both", expand=True)  # O Canvas (tela) expandirá para preencher todo o espaço disponível.
        barra_rolagem.pack(side="right", fill="y")  # A barra de rolagem preencherá apenas na direção vertical (y).
        
    else:
        
        # Se não foi possível determinar os gêneros de que o usuário gosta, mostra uma mensagem de informação.
        messagebox.showinfo("Recomendações", "Não foi possível determinar suas preferências de gênero. Tente avaliar mais filmes.")
        

# Função para lidar com o feedback do usuário sobre se ele gostou
# ou não de um filme.
def feedback(filme, gostou):
    
    # Usa as variáveis globais filmes_vistos e generos_gostados para 
    # manter o estado entre as chamadas da função.
    global filmes_vistos, generos_gostados
    
    # Se o usuário gostou do filme, atualize o dicionário generos_gostados.
    if gostou:
        
        # Pega o gênero do filme da dicionario_filmes.
        genero = dicionario_filmes[filme]
        
        # Atualiza a contagem de gêneros gostados. Se o gênero não estiver
        # no dicionário, ele será adicionado com o valor 1.
        generos_gostados[genero] = generos_gostados.get(genero, 0) + 1
        
        
    # Adiciona o filme à lista de filmes_vistos independentemente de o
    # usuário ter gostado ou não.
    filmes_vistos.append(filme)

    # Se o usuário viu menos de 5 filmes, continue recomendando.
    if len(filmes_vistos) < 5:

        # Chama a função recomendar_filme para obter uma nova recomendação 
        # com base nos filmes já vistos.
        novo_filme = recomendar_filme(filmes_vistos)

        # Pega o gênero do novo filme recomendado.
        genero_novo_filme = dicionario_filmes[novo_filme]

        # Atualiza o texto do rótulo lbl_filme na interface gráfica para
        # mostrar o novo filme e seu gênero.
        lbl_filme.config(text=f"Gostou do filme {novo_filme} ({genero_novo_filme})?")

        # Atualiza os botões 'Sim' e 'Não' para chamar esta função de feedback 
        # novamente, mas agora para o novo filme.
        btn_sim.config(command=lambda: feedback(novo_filme, True))
        btn_nao.config(command=lambda: feedback(novo_filme, False))

    else:

        # Se o usuário já viu 5 filmes, mostre as recomendações finais.
        mostrar_recomendacoes_finais()
        
        
        
# Interface gráfica
# Inicializa a janela principal do Tkinter.
root = tk.Tk()

# Define o título da janela.
root.title("Sistema de Recomendação de Filmes")

# Define o tamanho da janela: 500 pixels de largura 
# por 200 pixels de altura.
root.geometry("500x200")

# Cria um frame (quadro) para conter o rótulo (Label) que
# mostrará o nome do filme.
frame_lbl = tk.Frame(root, pady=20)

# Adiciona o frame ao layout da janela principal, ocupando 
# todo o espaço horizontal disponível.
frame_lbl.pack(fill="both")

# Cria um rótulo (Label) para exibir o nome do filme, com
# a fonte Arial tamanho 14.
lbl_filme = tk.Label(frame_lbl, 
                     font=("Arial", 14))

# Adiciona o rótulo ao frame.
lbl_filme.pack()


# Cria um frame para conter os botões "Sim" e "Não".
frame_btn = tk.Frame(root, pady=20)

# Adiciona o frame ao layout da janela principal, ocupando 
# todo o espaço horizontal disponível.
frame_btn.pack(fill="both")

# Cria o botão "Sim" com várias propriedades estilísticas e funcionais.
btn_sim = tk.Button(frame_btn,  # O botão será colocado dentro do frame 'frame_btn'.
                    text="Sim",  # O texto exibido no botão será "Sim".
                    width=20,    # O botão terá uma largura de 20 unidades.
                    height=2,    # O botão terá uma altura de 2 unidades.
                    bg="#4CAF50",  # A cor de fundo do botão será verde (#4CAF50).
                    fg="white",  # A cor do texto será branca.
                    font=("Arial", 12))  # A fonte do texto será Arial tamanho 12.

# Adiciona o botão "Sim" ao frame 'frame_btn', alinhando-o à esquerda
# e adicionando um padding de 10 pixels na horizontal.
btn_sim.pack(side=tk.LEFT, padx=10)


# Cria o botão "Não", semelhante ao botão "Sim", mas com cores e texto diferentes.
btn_nao = tk.Button(frame_btn,  
                    text="Não",  # O texto exibido no botão será "Não".
                    width=20,    # O botão terá uma largura de 20 unidades.
                    height=2,    # O botão terá uma altura de 2 unidades.
                    bg="#f44336",  # A cor de fundo será vermelha (#f44336).
                    fg="white",  # A cor do texto será branca.
                    font=("Arial", 12))  # A fonte do texto será Arial tamanho 12.

# Adiciona o botão "Não" ao frame 'frame_btn', alinhando-o à direita e 
# adicionando um padding de 10 pixels na horizontal.
btn_nao.pack(side=tk.RIGHT, padx=10)


# Chama a função 'recomendar_filme' para obter um filme inicial para o usuário.
filme_inicial = recomendar_filme(filmes_vistos)

# Consulta o dicionário 'dicionario_filmes' para encontrar o gênero do filme inicial.
genero_filme_inicial = dicionario_filmes[filme_inicial]

# Atualiza o texto do rótulo 'lbl_filme' para incluir o nome e o gênero do filme inicial.
lbl_filme.config(text=f"Gostou do filme {filme_inicial} ({genero_filme_inicial})?")

# Configura o botão "Sim" para que, quando clicado, chame a 
# função 'feedback' com o filme inicial e o valor True (indicando que o
# usuário gostou do filme).
btn_sim.config(command=lambda: feedback(filme_inicial, True))

# Configura o botão "Não" para que, quando clicado, chame a 
# função 'feedback' com o filme inicial e o valor False (indicando que o usuário 
# não gostou do filme).
btn_nao.config(command=lambda: feedback(filme_inicial, False))


# Inicia o loop principal da interface gráfica.
root.mainloop()

