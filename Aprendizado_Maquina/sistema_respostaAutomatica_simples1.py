# Importa o módulo Tkinter para criar a interface gráfica
import tkinter as tk

# Importa a classe TfidfVectorizer para transformar texto em vetores numéricos
from sklearn.feature_extraction.text import TfidfVectorizer

# Importa a classe MultinomialNB para o modelo de classificação Naive Bayes multinomial
from sklearn.naive_bayes import MultinomialNB

# Importa a função make_pipeline para criar um pipeline de aprendizado de máquina
from sklearn.pipeline import make_pipeline

# Importa o módulo numpy como 'np' para manipulação de arrays
import numpy as np

# Importar o módulo os para interagir com o sistema operacional.
# Pode ser usado para verificar a existência de arquivos, entre outras coisas.
import os

# Importar a função 'distance' da biblioteca Levenshtein.
# Esta função calcula a distância de Levenshtein entre duas strings, que é uma 
# medida da diferença entre elas.
from Levenshtein import distance as levenshtein_distance


# Definir uma função chamada carregar_dados para ler perguntas e respostas de um arquivo.
def carregar_dados():
    
    # Inicializar listas vazias para armazenar perguntas e respostas.
    perguntas = []
    respostas = []
    
    # Definir o caminho do arquivo que contém as perguntas e respostas.
    # Você deve ajustar esse caminho para o local onde o arquivo está 
    # realmente armazenado em seu sistema.
    caminho_arquivo = r'C:\python_projetos\python_rpa_projetos\Aprendizado_Maquina\perguntas.txt'
    
    # Verificar se o arquivo existe.
    if os.path.exists(caminho_arquivo):
        
        # Abrir o arquivo para leitura.
        with open(caminho_arquivo, 'r', encoding='latin-1') as f:
            
            # Ler cada linha do arquivo.
            for linha in f:
                try:
                    
                    # Tentar dividir a linha pelo delimitador '|' para separar 
                    # a pergunta e a resposta.
                    pergunta, resposta = linha.strip().split('|')
                    
                    # Adicionar a pergunta e a resposta às respectivas listas.
                    perguntas.append(pergunta)
                    respostas.append(resposta)
                    
                except ValueError:
                    
                    # Se ocorrer um erro ao dividir a linha, imprimir uma mensagem de erro.
                    print(f"Erro ao processar a linha: {linha.strip()}")
                    
    # Retornar as listas de perguntas e respostas.
    return perguntas, respostas


# Definir uma função chamada 'corrigir_texto' que toma um 
# texto e um vocabulário como argumentos.
def corrigir_texto(texto, vocabulario):
    
    # Inicializar uma lista vazia chamada 'palavras_corrigidas' para armazenar 
    # palavras corrigidas.
    palavras_corrigidas = []
    
    # Dividir o texto em palavras e iterar sobre cada palavra.
    for palavra in texto.split():
        
        # Inicializar 'min_dist' com infinito. Esta variável manterá a menor 
        # distância de Levenshtein encontrada.
        min_dist = float("inf")
        
        # Inicializar 'palavra_correta' com a palavra original. Esta variável
        # será atualizada se encontrarmos uma palavra mais próxima no vocabulário.
        palavra_correta = palavra
        
        # Iterar sobre cada palavra no vocabulário para encontrar a palavra 
        # mais próxima da palavra original.
        for vocab in vocabulario:
            
            # Calcular a distância de Levenshtein entre a palavra original 
            # e a palavra do vocabulário.
            dist = levenshtein_distance(palavra, vocab)
            
            # Se a distância calculada for menor que 'min_dist', atualizamos
            # 'min_dist' e 'palavra_correta'.
            if dist < min_dist:
                min_dist = dist
                palavra_correta = vocab
                
        # Adicionar a palavra correta à lista 'palavras_corrigidas'.
        palavras_corrigidas.append(palavra_correta)
        
    # Juntar todas as palavras corrigidas em uma string e retorná-la.
    return " ".join(palavras_corrigidas)


# Inicializar as listas 'perguntas_treino' e 'respostas_treino' 
# chamando a função 'carregar_dados'.
perguntas_treino, respostas_treino = carregar_dados()

# Criar um conjunto chamado 'vocabulario' que contém todas as palavras 
# únicas presentes nas perguntas de treino.
# Isso é feito juntando todas as perguntas em uma única string e, em seguida, 
# dividindo-a em palavras e convertendo em um conjunto para remover duplicatas.
vocabulario = set(" ".join(perguntas_treino).split())


# Verificar se as listas 'perguntas_treino' e 'respostas_treino' não estão vazias.
if perguntas_treino and respostas_treino:
    
    # Instanciar o objeto 'TfidfVectorizer', que será responsável por converter o
    # texto em uma matriz TF-IDF.
    vectorizer = TfidfVectorizer()
    
    # Criar um pipeline que primeiro aplica a vetorização TF-IDF e, em seguida, 
    # treina um modelo Naive Bayes Multinomial.
    modelo = make_pipeline(vectorizer, MultinomialNB())
    
    # Treinar o modelo usando as perguntas como entradas e um array de índices como saídas.
    # O array de índices é criado usando 'np.arange' e tem o mesmo tamanho que 'respostas_treino'.
    modelo.fit(perguntas_treino, np.arange(len(respostas_treino)))
    
    
# Função para encontrar a resposta mais adequada a uma pergunta feita.
def responder_pergunta():
    
    # Verificar se as listas de treinamento de perguntas e respostas estão
    # vazias. Se estiverem, exibe uma mensagem e retorna.
    if not perguntas_treino or not respostas_treino:
        
        # Limpar qualquer texto anterior na caixa de resposta da interface gráfica.
        caixa_resposta.delete(1.0, tk.END)
        
        # Inserir a resposta prevista na caixa de resposta da interface gráfica.
        caixa_resposta.insert(tk.END, "O conjunto de treinamento está vazio")
        
    
    # Obter a pergunta da caixa de entrada da interface gráfica.
    pergunta = entrada_pergunta.get()
    
    # Corrigir possíveis erros na pergunta usando a função 'corrigir_texto' e
    # o vocabulário criado anteriormente.
    pergunta_corrigida = corrigir_texto(pergunta, vocabulario)
    
    # Imprimir a pergunta corrigida no console para fins de depuração.
    print(pergunta_corrigida)
    
    # Verificar se a pergunta corrigida não está vazia.
    if pergunta_corrigida:
        
        # Usar o modelo treinado para prever o índice da resposta mais
        # adequada para a pergunta.
        idx = modelo.predict([pergunta_corrigida])[0]
        
        # Obter a probabilidade máxima associada à classe prevista.
        prob = np.max(modelo.predict_proba([pergunta_corrigida]))
        
        # Imprimir a probabilidade no console para fins de depuração.
        print(f"Probabilidade: {prob}")
        
        # Limpar qualquer texto anterior na caixa de resposta da interface gráfica.
        caixa_resposta.delete(1.0, tk.END)
        
        # Inserir a resposta prevista na caixa de resposta da interface gráfica.
        caixa_resposta.insert(tk.END, f"Resposta: {respostas_treino[idx]}")
    

# Criar a janela Tkinter principal
janela = tk.Tk()

# Definir as dimensões da janela para 600x300 pixels
janela.geometry("700x350")

# Definir o título da janela como "Sistema de Resposta Automática"
janela.title("Sistema de Resposta Automática")

# Adicionar um rótulo com o texto "Faça uma pergunta:" para instruir o usuário
lbl_instrucao = tk.Label(janela, 
                         text="Faça uma pergunta:",
                        font=("Arial 16"))

# Posicionar o rótulo na janela com um padding vertical de 10 pixels
lbl_instrucao.pack(pady=10)

# Adicionar uma caixa de entrada para o usuário digitar sua pergunta
entrada_pergunta = tk.Entry(janela, 
                            width=50,
                            font=("Arial 16"))

# Posicionar a caixa de entrada na janela com um padding vertical de 5 pixels
entrada_pergunta.pack(pady=5)



# Adicionar um botão com o texto "Responder" que, quando clicado, chama a função responder_pergunta
btn_responder = tk.Button(janela, 
                          text="Responder", 
                          command=responder_pergunta,
                          font=("Arial 16"))

# Posicionar o botão na janela com um padding vertical de 10 pixels
btn_responder.pack(pady=10)

# Adicionar uma caixa de texto onde a resposta será exibida
caixa_resposta = tk.Text(janela, 
                         wrap=tk.WORD,  # Configurar a quebra de linha para ocorrer em palavras completas
                         width=50,      # Definir a largura da caixa de texto para 50 caracteres
                         height=10,     # Definir a altura da caixa de texto para 10 linhas
                        font=("Arial 16"))

# Posicionar a caixa de texto na janela com um padding vertical de 10 pixels
caixa_resposta.pack(pady=10)

# Iniciar o loop de eventos Tkinter para manter a janela aberta e responsiva
janela.mainloop()