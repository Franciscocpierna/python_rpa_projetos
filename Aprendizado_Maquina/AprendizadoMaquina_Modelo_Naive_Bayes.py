"""
Criar um Classificador de Frutas utilizando Tkinter e Naive Bayes

Objetivo

Neste exercício, você irá criar um aplicativo de desktop simples usando Tkinter que 
será capaz de classificar palavras como "Fruta" ou "Não é uma fruta". Você também 
usará o algoritmo Naive Bayes para treinar um modelo de classificação de texto.

Requisitos

    Interface Gráfica: Use Tkinter para criar a interface do usuário que deve incluir:
    
        - Um campo de entrada para inserir a palavra a ser classificada.
        - Dois botões de opção para especificar se a palavra inserida é uma fruta ou não.
        - Um botão para adicionar a palavra ao conjunto de treinamento.
        - Um botão para verificar se a palavra inserida é uma fruta ou não.
        - Uma etiqueta para mostrar o resultado da classificação ou outras mensagens ao usuário.

    Modelo de Machine Learning: Use a biblioteca scikit-learn para criar um modelo 
    Naive Bayes que seja treinado com as palavras inseridas pelo usuário.

    Persistência de Dados: Salve as palavras e seus rótulos correspondentes em um 
    arquivo de texto para que possam ser carregados cada vez que o programa é iniciado.

    Verificação de Palavra: Se a palavra inserida não estiver no conjunto de treinamento, 
    informe ao usuário que a palavra não pode ser classificada e precisa ser adicionada ao 
    conjunto de treinamento primeiro.

    Estilização Opcional: Melhore a aparência da sua aplicação usando diferentes fontes, cores
    ou widgets Tkinter adicionais.

Diretrizes

    Utilize o algoritmo Naive Bayes para classificação.
    
    Trate erros e exceções, como por exemplo, quando o arquivo de texto que armazena 
    as palavras não existir ou estiver corrompido.
    
    Siga as melhores práticas de codificação e estruture seu código de forma limpa e eficiente.


"""

# Importando as bibliotecas necessárias

# Importar a biblioteca tkinter como tk.
# tkinter é uma biblioteca padrão do Python para criar interfaces gráficas do usuário (GUI).
import tkinter as tk

# Importar ttk do tkinter.
# ttk (themed tkinter) é um conjunto de widgets estendidos que são estilizados
# para se parecer melhor com o sistema operacional.
from tkinter import ttk

# Importar CountVectorizer da biblioteca sklearn.feature_extraction.text.
# CountVectorizer é uma técnica de processamento de linguagem natural para converter texto em vetores numéricos.
from sklearn.feature_extraction.text import CountVectorizer

# Importar MultinomialNB da biblioteca sklearn.naive_bayes.
# MultinomialNB é uma implementação do algoritmo Naive Bayes para classificação de texto.
from sklearn.naive_bayes import MultinomialNB

# Importar make_pipeline da biblioteca sklearn.pipeline.
# make_pipeline é uma função que ajuda a criar um pipeline de aprendizado de máquina, 
# permitindo que você encadeie múltiplas etapas de processamento e modelagem juntas.
from sklearn.pipeline import make_pipeline

# Importar a biblioteca os.
# A biblioteca os fornece uma maneira de interagir com o sistema operacional, 
# como verificar a existência de arquivos ou criar diretórios.
import os


# Função para carregar palavras e rótulos do arquivo
def carregar_dados():
    
    # Inicializar listas vazias para armazenar as palavras e os rótulos.
    palavras = []
    rotulos = []
    
    # Verificar se o arquivo de dados existe no caminho especificado usando os.path.exists.
    if os.path.exists(r'C:\python_projetos\python_rpa_projetos\Aprendizado_Maquina\palavras.txt'):
        
        # Abrir o arquivo em modo de leitura ('r').
        with open(r'C:\python_projetos\python_rpa_projetos\Aprendizado_Maquina\palavras.txt', 'r',  encoding='UTF-8') as f:
            
            # Ler cada linha do arquivo.
            for linha in f:
                
                try:
                    
                    # Remover espaços em branco e quebras de linha da linha com strip(),
                    # e então dividir a linha em palavra e rótulo usando split(',').
                    palavra, rotulo = linha.strip().split(',')
                    
                    # Adicionar a palavra e o rótulo às listas correspondentes.
                    palavras.append(palavra)
                    rotulos.append(int(rotulo))  # Converter o rótulo para um inteiro.
                    
                except ValueError:
                    
                    # Caso a linha não possa ser dividida em uma palavra e um rótulo,
                    # capturar a exceção e imprimir uma mensagem de erro.
                    print(f"Erro ao processar a linha: {linha.strip()}")
    
    # Retornar as listas de palavras e rótulos.
    return palavras, rotulos


# Função para salvar palavras e rótulos no arquivo
def salvar_dados(palavras, rotulos):
    
    # Abrir o arquivo especificado em modo de escrita ('w').
    # O modo 'w' sobrescreverá o arquivo se ele já existir ou criará um novo arquivo se ele não existir.
    with open(r'C:\python_projetos\python_rpa_projetos\Aprendizado_Maquina\palavras.txt', 'w') as f:
        
        # Iterar sobre as listas de palavras e rótulos simultaneamente usando a função zip.
        # A função zip agrupa o i-ésimo elemento de cada uma das listas de entrada, 
        # permitindo que os elementos correspondentes sejam processados juntos.
        for palavra, rotulo in zip(palavras, rotulos):
            
            # Escrever a palavra e o rótulo na mesma linha do arquivo, separados por uma vírgula.
            # O método write é usado para escrever uma string no arquivo.
            # A palavra e o rótulo são formatados como uma string, com a palavra e o 
            # rótulo separados por uma vírgula e seguidos por uma quebra de linha ('\n').
            f.write(f"{palavra},{rotulo}\n")
         
    

# Função para treinar o modelo de classificação Naive Bayes
def treinar_modelo(palavras, rotulos):
    
    # Criar um pipeline de aprendizado de máquina usando a função make_pipeline.
    # O pipeline contém duas etapas: 
    # 1. CountVectorizer para transformar as palavras em vetores numéricos.
    # 2. MultinomialNB para aplicar o algoritmo de classificação Naive Bayes.
    modelo = make_pipeline(CountVectorizer(), MultinomialNB())
    
    # Treinar o modelo usando o método fit.
    # O método fit toma dois argumentos:
    # 1. palavras: a lista de palavras que serve como entrada (features).
    # 2. rotulos: a lista de rótulos que serve como saída (labels).
    # O método ajusta o modelo aos dados fornecidos.
    modelo.fit(palavras, rotulos)
    
    # Retornar o modelo treinado para ser usado para previsões futuras.
    return modelo


# Inicializar palavras e rótulos chamando a função carregar_dados.
# carregar_dados é uma função definida anteriormente que lê um arquivo e retorna duas listas:
# 1. palavras: uma lista de palavras extraídas do arquivo.
# 2. rotulos: uma lista de rótulos correspondentes extraídos do arquivo.
palavras, rotulos = carregar_dados()


# Verificar se as listas de palavras e rótulos não estão vazias
# A expressão "if palavras and rotulos:" verifica se ambas as listas são não vazias.
# Se ambas as listas contiverem pelo menos um elemento, a expressão será avaliada como True.
if palavras and rotulos:
    
    # Treinar o modelo inicial chamando a função treinar_modelo.
    # A função treinar_modelo foi definida anteriormente e toma duas listas como argumentos:
    # 1. palavras: a lista de palavras que servirá como entrada (features).
    # 2. rotulos: a lista de rótulos que servirá como saída (labels).
    # A função retorna um modelo treinado que é armazenado na variável 'modelo'.
    modelo = treinar_modelo(palavras, rotulos)
    
else:
    
    # Se qualquer uma das listas (palavras ou rótulos) estiver vazia, imprimir uma mensagem de erro.
    # Isso serve como um aviso de que o modelo de aprendizado de máquina não pode ser treinado sem dados.
    print("O conjunto de treinamento está vazio. Adicione algumas palavras e rótulos primeiro.")


    
# Função para adicionar uma nova palavra e seu rótulo correspondente ao modelo
def adicionar_palavra():
    
    # Declarar 'modelo', 'palavras' e 'rotulos' como variáveis globais
    # para que possamos modificá-las dentro desta função
    global modelo  
    global palavras, rotulos  
    
    # Obter a nova palavra e o novo rótulo dos widgets de entrada do Tkinter
    nova_palavra = entrada_palavra.get()  # Obter o texto da caixa de entrada chamada 'entrada_palavra'
    novo_rotulo = var_rotulo.get()  # Obter o valor do widget de botão de opção, que está armazenado na variável 'var_rotulo'
    
    # Verificar se uma nova palavra foi inserida e se o novo rótulo é 0 ou 1
    if nova_palavra and (novo_rotulo == 0 or novo_rotulo == 1):
        
        # Verificar se a nova palavra já existe na lista de palavras
        if nova_palavra not in palavras:
            
            # Adicionar a nova palavra (convertida para minúsculas) e o novo rótulo às listas correspondentes
            palavras.append(nova_palavra.lower())
            rotulos.append(novo_rotulo)
            
            # Salvar as listas atualizadas em um arquivo usando a função 'salvar_dados'
            salvar_dados(palavras, rotulos)
            
            # Retreinar o modelo com os novos dados
            modelo = treinar_modelo(palavras, rotulos)
            
            # Atualizar a etiqueta de resultado para informar que a nova palavra foi adicionada e o modelo foi atualizado
            lbl_resultado['text'] = f"A palavra '{nova_palavra}' foi adicionada e o modelo foi atualizado."
        
        else:
            
            # Se a nova palavra já existir na lista de palavras, atualizar a etiqueta de resultado para indicar isso
            lbl_resultado['text'] = f"A palavra '{nova_palavra}' já está no conjunto de treinamento."
   
        
    
# Função para verificar e classificar uma palavra usando o modelo treinado
def verificar_palavra():
    
    # Declarar 'modelo', 'palavras' e 'rotulos' como variáveis globais
    # para que possamos acessá-las e modificá-las dentro desta função
    global modelo  
    global palavras, rotulos  
    
    # Recarregar os dados do arquivo e retreinar o modelo
    # Usamos a função carregar_dados para ler palavras e rótulos de um arquivo
    # e a função treinar_modelo para treinar o modelo com esses novos dados
    palavras, rotulos = carregar_dados()
    modelo = treinar_modelo(palavras, rotulos)
    
    # Obter a palavra de consulta da caixa de entrada do Tkinter e converter para minúsculas
    consulta_palavra = entrada_palavra.get().lower()
    
    # Verificar se a palavra de consulta está presente no conjunto de treinamento
    if consulta_palavra in palavras:
    
        # Se a palavra estiver presente, usar o modelo para prever seu rótulo
        previsao = modelo.predict([consulta_palavra])
        
        # Atualizar a etiqueta de resultado com a previsão feita pelo modelo
        lbl_resultado['text'] = f"Previsão para '{consulta_palavra}': {'é uma Fruta' if previsao[0] == 1 else 'Não é uma fruta'}"
    
    else:
        
        # Se a palavra de consulta não estiver no conjunto de treinamento, informar ao usuário
        lbl_resultado['text'] = f"Palavra '{consulta_palavra}' não encontrada."


# Importa o módulo tkinter e o renomeia como tk
import tkinter as tk

# Cria uma nova janela principal
janela = tk.Tk()

# Define a geometria da janela (largura x altura)
janela.geometry("900x300")

# Define o título da janela
janela.title("Classificador de frutas")

# Define uma fonte para o título da aplicação
fonte_titulo = ("Arial", 24)

# Define uma fonte para o texto na aplicação
fonte_texto = ("Arial", 16)

# Define uma cor de fundo para a janela (Hexadecimal: #f2f2f2, Nome: Silver)
cor_fundo = "#f2f2f2"  # Cor de fundo: Silver

# Define uma cor para os botões (Hexadecimal: #4CAF50, Nome: Green)
cor_botao = "#4CAF50"  # Cor do botão: Green

# Define uma cor para o texto nos botões (Hexadecimal: #ffffff, Nome: White)
cor_texto_botao = "#ffffff"  # Cor do texto do botão: White

# Configura a cor de fundo da janela
janela.configure(bg=cor_fundo)


# Adicionar widgets (elementos de interface do usuário) à janela

# Adicionar um rótulo para instruções
lbl_instrucao = tk.Label(janela, 
                         text="Insira uma palavra:", 
                         font=fonte_titulo, bg=cor_fundo)

 # Posicionar o rótulo na primeira linha e primeira coluna
lbl_instrucao.grid(row=0, column=0, padx=20, pady=20)


# Adicionar uma caixa de entrada para a palavra
entrada_palavra = tk.Entry(janela, 
                           font=fonte_texto)

# Posicionar a caixa de entrada ao lado do rótulo de instrução
entrada_palavra.grid(row=0, column=1, padx=20, pady=20)


# Adicionar botões de opção para escolher o rótulo da palavra (fruta ou não fruta)


var_rotulo = tk.IntVar()  # Variável para armazenar a escolha do usuário
var_rotulo.set(0)  # Definir o valor inicial como 0 (não é uma fruta)

# Criar e posicionar o primeiro botão de opção (Radiobutton)
r1 = tk.Radiobutton(janela, 
                    text="Não é uma fruta",  # Texto exibido ao lado do Radiobutton
                    variable=var_rotulo,      # Variável para armazenar o valor deste Radiobutton
                    value=0,                  # Valor atribuído à 'var_rotulo' quando este Radiobutton é selecionado
                    font=fonte_texto,         # Fonte e tamanho do texto
                    bg=cor_fundo)             # Cor de fundo do Radiobutton

# Posiciona o Radiobutton de opção na linha 1, coluna 0 
# com padding de 20 à direita/esquerda e 10 acima/abaixo
r1.grid(row=1, column=0, padx=20, pady=10)


# Criar e posicionar o primeiro botão de opção (Radiobutton)
r2 = tk.Radiobutton(janela, 
                    text="É uma fruta",  # Texto exibido ao lado do Radiobutton
                    variable=var_rotulo,      # Variável para armazenar o valor deste Radiobutton
                    value=1,                  # Valor atribuído à 'var_rotulo' quando este Radiobutton é selecionado
                    font=fonte_texto,         # Fonte e tamanho do texto
                    bg=cor_fundo)             # Cor de fundo do Radiobutton

# Posiciona o Radiobutton de opção na linha 1, coluna 0 
# com padding de 20 à direita/esquerda e 10 acima/abaixo
r2.grid(row=1, column=1, padx=20, pady=10)


# Criar e posicionar o botão para adicionar uma palavra
btn_adicionar = tk.Button(janela, 
                          text="Adicionar Palavra",  # Texto exibido no botão
                          command=adicionar_palavra, # Função a ser executada quando o botão é pressionado
                          bg=cor_botao,              # Cor de fundo do botão
                          fg=cor_texto_botao,        # Cor do texto do botão
                          font=fonte_texto)          # Fonte e tamanho do texto
# Posiciona o botão na linha 2, coluna 0
btn_adicionar.grid(row=2, column=0, padx=20, pady=20)


# Criar e posicionar o botão para verificar a classificação de uma palavra
btn_verificar = tk.Button(janela, 
                          text="Verificar Palavra", 
                          command=verificar_palavra, 
                          bg=cor_botao, 
                          fg=cor_texto_botao, 
                          font=fonte_texto)
# Posiciona o botão na linha 2, coluna 1
btn_verificar.grid(row=2, column=1, padx=20, pady=20)


# Criar e posicionar um rótulo (Label) para exibir os resultados
lbl_resultado = tk.Label(janela, 
                         text="",       # Texto inicial vazio
                         font=("Arial", 20),     # Fonte e tamanho do texto
                         bg=cor_fundo)           # Cor de fundo do rótulo

# Posiciona o rótulo na linha 3, abrangendo 2 colunas (columnspan=2)
lbl_resultado.grid(row=3, columnspan=2, padx=20, pady=20)

# Inicia o loop principal do Tkinter para manter a janela aberta
janela.mainloop()
