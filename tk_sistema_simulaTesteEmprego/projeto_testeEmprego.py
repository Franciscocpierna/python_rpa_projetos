#Aula 2
# Importar as bibliotecas necessárias
import tkinter as tk  # Importa a biblioteca tkinter e a renomeia como tk
from tkinter import messagebox  # Importa a classe messagebox do módulo tkinter
from tkinter import scrolledtext  # Importa a classe scrolledtext do módulo tkinter
import os  # Importa o módulo os
import win32com.client as win32  # Importa o módulo win32com.client e o renomeia como win32
import openpyxl  # Importa o módulo openpyxl

#Definir a lista de perguntas
perguntas = [
    {
        "pergunta": "Qual é a forma correta de criar uma variável em Python?",
        "opcoes": ["a) var = 10", "b) 10 = var", "c) VAR = 10", "d) $var = 10"],
        "resposta": "a",
        "explicacao": "Em Python, a forma correta de criar uma variável é utilizando o nome da variável seguido pelo operador de atribuição (=) e o valor que será atribuído à variável."
    },
    {
        "pergunta": "Qual é o resultado da expressão 3 + 4 * 2?",
        "opcoes": ["a) 14", "b) 11", "c) 10", "d) 7"],
        "resposta": "b",
        "explicacao": "Em Python, a ordem de precedência dos operadores é levada em consideração. Neste caso, a multiplicação tem precedência sobre a adição, então a expressão é avaliada como 3 + (4 * 2) = 11."
    },
    {
        "pergunta": "Qual é o método utilizado para obter o tamanho de uma lista em Python?",
        "opcoes": ["a) len()", "b) size()", "c) count()", "d) get_size()"],
        "resposta": "a",
        "explicacao": "O método len() é utilizado para obter o tamanho de uma lista em Python. Ele retorna o número de elementos presentes na lista."
    },
    {
        "pergunta": "Qual é o operador de atribuição em Python?",
        "opcoes": ["a) =", "b) ==", "c) +=", "d) -="],
        "resposta": "a",
        "explicacao": "O operador de atribuição em Python é o sinal de igual (=). Ele é utilizado para atribuir um valor a uma variável."
    },
    {
        "pergunta": "Qual é o resultado da expressão 'hello' + 'world'?",
        "opcoes": ["a) hello", "b) world", "c) helloworld", "d) hello world"],
        "resposta": "c",
        "explicacao": "Quando se utiliza o operador de concatenação (+) com duas strings em Python, elas são concatenadas, ou seja, unidas. Neste caso, 'hello' + 'world' resulta em 'helloworld'."
    },
    {
        "pergunta": "Qual é a estrutura de repetição utilizada em Python para percorrer uma sequência?",
        "opcoes": ["a) while", "b) for", "c) repeat", "d) loop"],
        "resposta": "b",
        "explicacao": "A estrutura de repetição for é utilizada em Python para percorrer uma sequência, como uma lista, uma string, entre outros. Ela permite executar um bloco de código para cada elemento da sequência."
    },
    {
        "pergunta": "Qual é o método utilizado para imprimir um valor no console em Python?",
        "opcoes": ["a) print()", "b) input()", "c) display()", "d) show()"],
        "resposta": "a",
        "explicacao": "O método print() é utilizado para imprimir um valor no console em Python. Ele exibe o valor especificado como argumento na saída padrão."
    },
    {
        "pergunta": "Qual é o tipo de dado utilizado para armazenar uma sequência de caracteres em Python?",
        "opcoes": ["a) string", "b) number", "c) boolean", "d) list"],
        "resposta": "a",
        "explicacao": "O tipo de dado utilizado para armazenar uma sequência de caracteres em Python é chamado de string. Strings são representadas entre aspas simples ('') ou aspas duplas (\")."
    },
    {
        "pergunta": "Qual é o resultado da expressão 2 ** 3?",
        "opcoes": ["a) 6", "b) 8", "c) 2", "d) 23"],
        "resposta": "b",
        "explicacao": "O operador ** é utilizado em Python para realizar a exponenciação. Neste caso, 2 ** 3 é igual a 8, pois representa 2 elevado à potência de 3."
    },
    {
        "pergunta": "Qual é o operador utilizado para verificar se dois valores são iguais em Python?",
        "opcoes": ["a) =", "b) ==", "c) +=", "d) -="],
        "resposta": "b",
        "explicacao": "O operador de comparação utilizado para verificar se dois valores são iguais em Python é o operador ==. Ele retorna True se os valores forem iguais e False caso contrário."
    }
]

def iniciar_teste():
    
    # Permite acessar as variáveis nome_completo e email definidas fora da função
    global nome_completo, email
    
    # Obtém o nome completo e o email inseridos pelos usuários a partir dos campos de entrada na interface gráfica
    nome_completo = nome_entry.get()
    email = email_entry.get()
    
    #if - se
    if nome_completo.strip() == "" or email.strip() == "":
        
        # Mostra um aviso caso algum dos campos esteja vazio
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos antes de começar o teste.")

    else:
        
        # Se todos os campos estiverem preenchidos, destrói a tela inicial e exibe a primeira pergunta
        #Fecho o Frame da janela principal
        #Assim eu fecho o frame subindo as pergunta e opções
        tela_inicial.destroy()
        
        mostrar_pergunta()
        
def mostrar_pergunta():
    
    """
    pergunta_label: É a variável que representa o rótulo (label) onde a pergunta 
    será exibida. Presumivelmente, essa variável está vinculada a um rótulo na 
    interface gráfica.

    .config(): É um método para configurar as propriedades de um widget 
    da interface gráfica. Permite alterar várias opções, como texto, fonte, 
    cor etc., do widget especificado.

    text=perguntas[pergunta_atual]["pergunta"]: Estamos usando a opção text 
    do método config() para definir o texto que será exibido no rótulo (pergunta_label). 
    O texto é obtido a partir da lista de perguntas (perguntas), na posição 
    pergunta_atual, e acessando a chave "pergunta" do dicionário correspondente
    à pergunta atual.
    """
    pergunta_label.config(text=perguntas[pergunta_atual]["pergunta"])
    
    for i in range(len(opcao_buttons)):
        
        #Define o texto das opções de respostas nos botões
        """
        opcao_buttons[i]: É um elemento da lista opcao_buttons que representa 
        um botão de opção na interface gráfica. Presumivelmente, essa lista contém 
        vários botões de opção, e estamos acessando o elemento na posição i.

        .config(): É um método para configurar as propriedades de um widget da 
        interface gráfica. Permite alterar várias opções, como texto, fonte, cor 
        etc., do widget especificado.

        text=perguntas[pergunta_atual]["opcoes"][i]: Estamos usando a opção text 
        do método config() para definir o texto que será exibido no botão de opção 
        (opcao_buttons[i]). O texto é obtido a partir da lista de perguntas (perguntas), 
        na posição pergunta_atual, e acessando a chave "opcoes" do dicionário correspondente 
        à pergunta atual. Em seguida, acessamos o elemento na posição i da lista de opções 
        de resposta para essa pergunta.
        """
        opcao_buttons[i].config(text=perguntas[pergunta_atual]["opcoes"][i])
    
#Função para verficar a resposta dada pelo usuário
def verificar_resposta(resposta):
    
    print("Resposta")
                           
    

# Inicializar variáveis
pontuacao = 0  # Variável para armazenar a pontuação do usuário
pergunta_atual = 0  # Variável para acompanhar a pergunta atual exibida
respostas_usuarios = []  # Lista para armazenar as respostas dadas pelos usuários
nome_completo = ""  # Variável para armazenar o nome completo do usuário
email = ""  # Variável para armazenar o email do usuário

janela_principal = tk.Tk()  # Cria a janela principal
janela_principal.title("Avaliação de Python")  # Define o título da janela
janela_principal.attributes('-fullscreen', True)  # Define a janela em modo de tela cheia

largura_tela = janela_principal.winfo_screenwidth()  # Obtém a largura da tela
altura_tela = janela_principal.winfo_screenheight()  # Obtém a altura da tela

tela_inicial = tk.Frame(janela_principal)  # Cria um frame para a tela inicial
tela_inicial.pack(pady=altura_tela * 0.2)  # Posiciona o frame na janela principal com um espaçamento vertical

# Cria um rótulo para o nome completo
label_nome = tk.Label(tela_inicial, 
                      text="Nome Completo:", 
                      font=("Arial", 20))  
label_nome.pack()  # Posiciona o rótulo no frame

#Campo de entrada de dados
nome_entry = tk.Entry(tela_inicial, 
                      font=("Arial", 20))
nome_entry.pack()  # Posiciona o rótulo no frame

# Cria um rótulo para o nome completo
label_email = tk.Label(tela_inicial, 
                      text="Email:", 
                      font=("Arial", 20))  
label_email.pack()  # Posiciona o rótulo no frame

#Campo de entrada de dados
email_entry = tk.Entry(tela_inicial, 
                      font=("Arial", 20))
email_entry.pack()  # Posiciona o rótulo no frame

#Cria o botão
button_iniciar = tk.Button(tela_inicial, 
                          text="Inicial Teste",
                          font=("Arial", 20),
                          command = iniciar_teste)
button_iniciar.pack(pady=altura_tela * 0.05)  # Posiciona o button_iniciar no frame

# Cria um rótulo para exibir a pergunta
pergunta_label = tk.Label(janela_principal, 
                      text="", 
                      font=("Arial", 20))  
pergunta_label.pack(pady=altura_tela * 0.05)  # Posiciona o rótulo na janela_principal

#Lista vazia para armazenar os botões de opção
opcao_buttons = []

#Cria 4 botões
for posicao in range(4):
    
    opcao_button = tk.Button(janela_principal,
                            text="",
                            width = int(largura_tela * 0.4),
                            command = lambda posicao = posicao: verificar_resposta(chr(ord('a') + posicao)), #ord('a') calcula o deslocamento necessário para obter o índice correto na lista
                            font = ("Arial", 20))
    opcao_button.pack(pady=altura_tela * 0.01)  # Posiciona o botão na janela_principal
    opcao_buttons.append(opcao_button) #Adiciona o botão à lista de opções
    
#Cria o menu na janela principal
barra_menu = tk.Menu(janela_principal)
barra_menu.add_command(label="Sair",
                      command = janela_principal.destroy) # Aciona o camando para sair do sistema
janela_principal.config(menu=barra_menu) #Configura a barra de menu na janela_principal

#Inicial o loop que carrega sistema
janela_principal.mainloop()
