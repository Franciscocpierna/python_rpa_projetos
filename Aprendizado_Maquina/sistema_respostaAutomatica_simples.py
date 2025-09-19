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

# Define um conjunto de treinamento com perguntas frequentes
perguntas_treino = ["Qual é o seu nome?", "Como você está?", "O que você faz?", "Você gosta de programar?"]

# Define as respostas correspondentes para cada pergunta no conjunto de treinamento
respostas_treino = ["Meu nome é Celso.", "Estou funcionando bem, obrigado!", "Eu respondo a perguntas.", "Sim, eu adoro programar!"]



# Inicializa o transformador TF-IDF (Term Frequency-Inverse Document Frequency)
vectorizer = TfidfVectorizer()


# Cria um pipeline que primeiro aplica o transformador TF-IDF e, 
# em seguida, aplica o classificador Naive Bayes
modelo = make_pipeline(vectorizer, MultinomialNB())


# Treina o modelo usando as perguntas como entrada e os índices das respostas como saída
# np.arange(len(respostas_treino)) cria um array de índices [0, 1, 2, ...]
modelo.fit(perguntas_treino, np.arange(len(respostas_treino)))


# Função chamada 'responder_pergunta' destinada a encontrar e exibir a 
# resposta mais adequada para uma pergunta inserida.
def responder_pergunta():
    
    # Obter o conteúdo do widget 'entrada_pergunta' do Tkinter e armazená-lo 
    # na variável 'pergunta'.
    pergunta = entrada_pergunta.get()
    
    # Verificar se a variável 'pergunta' contém algum texto.
    if pergunta:
        
        # Utilizar o modelo treinado para prever a resposta mais adequada.
        # O resultado é o índice da resposta no array de respostas do treinamento.
        idx = modelo.predict([pergunta])[0]
        
        # Utilizar o método 'predict_proba' para obter as probabilidades associadas às previsões.
        # Em seguida, obter a máxima dessas probabilidades usando np.max().
        prob = np.max(modelo.predict_proba([pergunta]))
        
        # Definir um limiar de confiança (neste caso, 0.3).
        # Se a probabilidade máxima for maior que esse limiar, então a resposta é 
        # considerada válida.
        if prob > 0.3:
            
            # Definir o texto do widget 'lbl_resposta' para mostrar a resposta correspondente.
            lbl_resposta['text'] = f"Resposta: {respostas_treino[idx]}"
            
        else:
            # Se a probabilidade máxima for menor que o limiar, exibir uma mensagem 
            # indicando que a resposta não foi encontrada.
            lbl_resposta['text'] = "Resposta não encontrada."
    
    
# Criar uma nova janela Tkinter e armazená-la na variável 'janela'.
janela = tk.Tk()

# Definir as dimensões da janela para 600x300 pixels.
janela.geometry("600x300")

# Definir o título da janela como "Sistema de Resposta Automática".
janela.title("Sistema de Resposta Automática")

# Adicionar Widgets à Janela

# Adicionar um rótulo (Label) com o texto "Faça uma pergunta:".
lbl_instrucao = tk.Label(janela, 
                         text="Faça uma pergunta:",
                         font=("Arial 16"))

# Posicionar o rótulo na janela com um padding vertical de 10 pixels.
lbl_instrucao.pack(pady=10)

# Adicionar uma caixa de entrada (Entry) onde o usuário pode digitar uma pergunta.
# Definir a largura da caixa de entrada como 50 caracteres.
entrada_pergunta = tk.Entry(janela, 
                            width=50,
                            font=("Arial 16"))

# Posicionar a caixa de entrada na janela com um padding vertical de 5 pixels.
entrada_pergunta.pack(pady=5)

# Adicionar um botão (Button) com o texto "Responder".
# Associar o comando 'responder_pergunta' ao botão para que seja executado 
# quando o botão for clicado.
btn_responder = tk.Button(janela, 
                          text="Responder", 
                          command=responder_pergunta,
                          font=("Arial 16"))

# Posicionar o botão na janela com um padding vertical de 10 pixels.
btn_responder.pack(pady=10)

# Adicionar um rótulo (Label) onde a resposta será exibida.
# Inicialmente, o texto deste rótulo está vazio e a fonte é Arial tamanho 16.
lbl_resposta = tk.Label(janela, 
                        text="", 
                        font=("Arial", 16))

# Posicionar o rótulo na janela com um padding vertical de 10 pixels.
lbl_resposta.pack(pady=10)

# Iniciar o loop principal do Tkinter para manter a janela aberta.
janela.mainloop()