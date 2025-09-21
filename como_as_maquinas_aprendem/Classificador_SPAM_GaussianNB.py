# Importa as classes Tk, Label, Button, Text, Scrollbar e INSERT do módulo tkinter.
# Essas classes serão usadas para criar a interface gráfica do usuário (GUI).
from tkinter import Tk, Label, Button, Text, Scrollbar, INSERT

# Importa a classe GaussianNB do módulo sklearn.naive_bayes.
# Esta classe é usada para implementar o algoritmo Naive Bayes.
from sklearn.naive_bayes import GaussianNB

# Importa a biblioteca pandas para manipulação e análise de dados.
# Será usada para criar e manipular o DataFrame.
import pandas as pd

# Importa a biblioteca re para trabalhar com expressões regulares.
# Será usada para extrair características específicas dos e-mails.
import re


# Define uma função chamada 'extrair_caracteristicas' que aceita uma variável 'email_texto'.
def extrair_caracteristicas(email_texto):
    
    # Conta o número de palavras no texto do e-mail. 
    # 'split()' divide o texto em uma lista de palavras e
    # 'len()' conta o número de itens na lista.
    numero_palavras = len(email_texto.split())
    
    # Usa expressão regular para verificar se a palavra 'grátis' está no texto do e-mail.
    # 're.search()' retorna um objeto de correspondência se encontrar uma ocorrência.
    # '\b' indica a borda da palavra, garantindo que palavras como 'agráde' não sejam contadas.
    # 're.IGNORECASE' torna a busca insensível a maiúsculas e minúsculas.
    contem_gratis = 1 if re.search(r'\bgrátis\b', email_texto, re.IGNORECASE) else 0
    
    # Similar ao 'contem_gratis', mas verifica a presença da palavra 'oferta'.
    contem_oferta = 1 if re.search(r'\boferta\b', email_texto, re.IGNORECASE) else 0
    
    # Conta o número de URLs no texto do e-mail usando expressão regular.
    # 're.findall()' retorna todas as ocorrências da expressão regular no texto.
    # A expressão regular usada é uma expressão comum para encontrar URLs.
    qtd_links = len(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', email_texto))
    
    
    # Retorna uma lista contendo as características extraídas: 
    # número de palavras, presença da palavra 'grátis', presença da
    # palavra 'oferta' e quantidade de links.
    return [numero_palavras, contem_gratis, contem_oferta, qtd_links]

    

# Define uma classe chamada 'App' para criar a interface gráfica do usuário.
class App:
    
    # Método construtor '__init__' que é executado quando uma instância da classe é criada.
    # 'raiz' é o argumento que representa a janela principal da interface gráfica.
    def __init__(self, raiz):
        
        # Atribui o argumento 'raiz' ao atributo 'self.raiz' da classe.
        self.raiz = raiz
        
        # Define o título da janela como "Classificador de SPAM".
        raiz.title("Classificador de SPAM")
        
        # Cria uma caixa de texto onde o usuário pode digitar o e-mail a ser classificado.
        # O texto será ajustado automaticamente ('wrap=word') e a caixa terá dimensões de 50x20.
        self.caixa_texto = Text(raiz, wrap='word', width=50, height=20)
        
        # Adiciona a caixa de texto à janela principal.
        self.caixa_texto.pack()        
        
        # Cria uma barra de rolagem vertical para a caixa de texto.
        self.barra_rolagem = Scrollbar(raiz, command=self.caixa_texto.yview)
        
        # Adiciona a barra de rolagem à direita da janela principal.
        self.barra_rolagem.pack(side='right', fill='y')
                
        # Configura a barra de rolagem para funcionar com a caixa de texto.
        self.caixa_texto.config(yscrollcommand=self.barra_rolagem.set)
        
        
        # Cria um botão chamado "Classificar" que, quando pressionado, chama o método 'classificar_spam'.
        self.botao_classificar = Button(raiz, text="Classificar", command=self.classificar_spam)
        
        # Adiciona o botão à janela principal.
        self.botao_classificar.pack()
        
        
        # Cria um label (rótulo de texto) para exibir as características extraídas do e-mail.
        # Inicialmente, o texto do label está vazio.
        self.label_caracteristicas = Label(raiz, text="", font=("Arial 20"))
        
        # Adiciona o label à janela principal.
        self.label_caracteristicas.pack()
        
        
        # Cria outro label para exibir o resultado da classificação (se é SPAM ou não).
        # Inicialmente, o texto do label está vazio.
        self.label_resultado = Label(raiz, text="", font=("Arial 20"))
        
        # Adiciona o label à janela principal.
        self.label_resultado.pack()
        
        
    # Define uma função de nome 'classificar_spam' dentro da classe App.
    # Essa função será chamada quando o usuário clicar no botão "Classificar".
    def classificar_spam(self):

        # Obtém o conteúdo da caixa de texto, do início ("1.0") ao fim ('end-1c').
        # O conteúdo obtido é armazenado na variável 'email_digitado'.
        email_digitado = self.caixa_texto.get("1.0", 'end-1c')
        
        
        # Chama a função 'extrair_caracteristicas' para obter as características do e-mail.
        # As características são armazenadas na variável 'caracteristicas'.
        caracteristicas = extrair_caracteristicas(email_digitado)

        # Atualiza o conteúdo do Label 'label_caracteristicas' para 
        # mostrar as características extraídas.
        # Utiliza formatação de string para inserir as características no texto.
        self.label_caracteristicas.config(text=f"Características extraídas:\nNúmero de Palavras: {caracteristicas[0]}\nContém 'Grátis': {caracteristicas[1]}\nContém 'Oferta': {caracteristicas[2]}\nQuantidade de Links: {caracteristicas[3]}")
        
        
        # Cria um DataFrame do Pandas para armazenar as características em 
        # um formato que o modelo possa usar.
        # O DataFrame tem colunas nomeadas para corresponder às características.
        caracteristicas_df = pd.DataFrame([caracteristicas], columns=['Numero_Palavras', 'Contem_Gratis', 'Contem_Oferta', 'Qtd_Links'])
    
        # Usa o modelo Naive Bayes (modelo_nb) para fazer a previsão com base nas características.
        # A previsão é armazenada na variável 'previsao'.
        previsao = modelo_nb.predict(caracteristicas_df)

        # Verifica o resultado da previsão para atualizar o Label 'label_resultado'.
        # Se a previsão for 1 (SPAM), atualiza o Label para mostrar que o e-mail é SPAM.
        # Se for 0 (não é SPAM), mostra que o e-mail é seguro.
        if previsao[0] == 1:
            self.label_resultado.config(text="O e-mail é considerado SPAM.")
        else:
            self.label_resultado.config(text="O e-mail é considerado seguro (não é SPAM).")
            
            
# Dados para treinamento do modelo
dados_treino = {
    'Numero_Palavras': [90, 150, 50, 100, 50, 75],
    'Contem_Gratis': [0, 1, 0, 1, 0, 1],
    'Contem_Oferta': [0, 1, 1, 0, 0, 1],
    'Qtd_Links': [1, 3, 2, 4, 0, 5],
    'Eh_Spam': [0, 1, 1, 1, 0, 1]
}


# Converte o dicionário 'dados_treino' em um DataFrame do Pandas.
# Isso é feito para facilitar a manipulação e análise dos dados.
df_treino = pd.DataFrame(dados_treino)

# Separa as colunas de características e a coluna de etiquetas (labels) em duas
# variáveis diferentes, X_treino e y_treino.
# X_treino contém as características que serão usadas para treinar o modelo.
# y_treino contém as etiquetas que indicam se cada linha é spam (1) ou não spam (0).
X_treino = df_treino[['Numero_Palavras', 'Contem_Gratis', 'Contem_Oferta', 'Qtd_Links']]
y_treino = df_treino['Eh_Spam']

# Cria uma instância da classe GaussianNB, que é uma implementação do algoritmo Naive Bayes.
# GaussianNB é importado da biblioteca scikit-learn.
modelo_nb = GaussianNB()

# Treina o modelo Naive Bayes usando os dados em X_treino para as 
# características e y_treino para as etiquetas.
# O método 'fit' ajusta o modelo aos dados fornecidos.
modelo_nb.fit(X_treino, y_treino)


# Inicializa a interface gráfica Tkinter.
# Tk é uma classe do módulo Tkinter que cria uma janela raiz.
raiz = Tk()

# Cria uma instância da classe 'App', que contém todos os
# widgets (caixas de texto, botões, etc.)
# e a lógica para a interface gráfica.
app = App(raiz)

# Entra no loop principal da interface gráfica.
# O método 'mainloop' mantém a janela aberta e responde a eventos do usuário.
raiz.mainloop()


"""
Características do Modelo de E-mail Spam

    Numero_de_Palavras: 500 (Um e-mail muito longo pode ser suspeito)
    Palavra_Gratis: 1 (Contém a palavra "grátis")
    Palavra_Oferta: 1 (Contém a palavra "oferta")
    Links_Externos: 5 (Contém muitos links externos, que podem levar a sites maliciosos)

Texto do E-mail (Modelo)

#-------------------------------------------

Assunto: Oferta Imperdível! Ganhe um iPhone GRÁTIS!

Olá Leonardo,

Você foi selecionado para uma oferta incrível! Clique no link abaixo 
para ganhar um iPhone absolutamente GRÁTIS!

https://www.google.com/

Mas espere, tem mais! Temos também ofertas exclusivas para você!

https://www.google.com/

Não perca essa oportunidade única!

https://www.google.com/

Atenciosamente,
Equipe de Marketing

#-------------------------




Características do Modelo de E-mail Não-Spam

    Numero_de_Palavras: 100 (O e-mail não é muito longo)
    Palavra_Gratis: 0 (Não contém a palavra "grátis")
    Palavra_Oferta: 0 (Não contém a palavra "oferta")
    Links_Externos: 1 (Contém apenas um link externo, que é menos suspeito)

Texto do E-mail (Modelo)


Assunto: Atualização Sobre o Projeto

Olá Cesar,

Espero que esteja tudo bem.

Estou escrevendo para atualizá-lo sobre o status do nosso projeto atual. Fizemos um progresso significativo desde a nossa última reunião e estou ansioso para discutir os detalhes na próxima semana.

Para mais informações, você pode visitar a nossa página de atualizações do projeto:
https://www.google.com/

Agradeço o seu tempo e esforço contínuos neste projeto.

Atenciosamente,



"""
print()