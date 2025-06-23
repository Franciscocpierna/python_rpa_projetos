# Importa as bibliotecas necessárias para a aplicação

# Importa o módulo tkinter para criar a interface gráfica
import tkinter as tk

# Importa messagebox para mostrar alertas
from tkinter import messagebox

# Importa random para geração de caracteres aleatórios
import random

# Importa string para acessar conjuntos predefinidos de caracteres
import string


# Define a função para gerar uma senha personalizada 
        # baseada em opções selecionadas pelo usuário.
def gerar_senha():
    
    try:
        
        # Tenta obter o comprimento da senha desejado a partir do
        # campo de entrada, convertendo o valor para inteiro.
        comprimento = int(entrada_comprimento.get())
        
    except ValueError:
        
        # Se a conversão falhar devido a um valor não numérico, 
                # mostra uma mensagem de alerta ao usuário.
        messagebox.showwarning("Entrada inválida", "Por favor, insira um número válido para a quantidade de dígitos.")
        
        # Encerra a execução da função para evitar mais 
                # processamento sem um valor válido de comprimento.
        return

    # Obtém os valores booleanos das variáveis associadas às 
            # opções de caracteres (maiúsculas, minúsculas, números, especiais).
    incluir_maiusculas = var_maiusculas.get()
    incluir_minusculas = var_minusculas.get()
    incluir_numeros = var_numeros.get()
    incluir_especiais = var_especiais.get()
    
    # Verifica se pelo menos uma categoria de caracteres 
            # foi selecionada para incluir na senha.
    if not (incluir_maiusculas or incluir_minusculas or incluir_numeros or incluir_especiais):
        
        # Se nenhuma opção foi selecionada, mostra uma 
                # mensagem de alerta ao usuário.
        messagebox.showwarning("Opção inválida", "Selecione pelo menos uma opção de caracteres.")
        
        # Encerra a função para evitar a geração de uma 
                # senha vazia ou inválida.
        return
    
    # Inicializa uma string vazia para acumular todos os
            # caracteres possíveis que podem aparecer na senha.
    caracteres = ""
    
    # Inicializa uma lista vazia para armazenar os
            # caracteres selecionados aleatoriamente para a senha.
    senha = []


    # Verifica se o usuário selecionou incluir letras maiúsculas na senha.
    if incluir_maiusculas:
        
        # Se sim, adiciona todas as letras maiúsculas (A-Z) à 
                # string de caracteres possíveis.
        caracteres += string.ascii_uppercase
        
        # Seleciona aleatoriamente uma letra maiúscula e a adiciona à lista
                # inicial de caracteres da senha, garantindo a presença
                # de pelo menos uma letra maiúscula.
        senha.append(random.choice(string.ascii_uppercase))
    
    # Verifica se o usuário selecionou incluir letras minúsculas na senha.
    if incluir_minusculas:
        
        # Se sim, adiciona todas as letras minúsculas (a-z) à
                # string de caracteres possíveis.
        caracteres += string.ascii_lowercase
        
        # Seleciona aleatoriamente uma letra minúscula e a adiciona à
                # lista inicial de caracteres da senha, garantindo a
                # presença de pelo menos uma letra minúscula.
        senha.append(random.choice(string.ascii_lowercase))
    
    # Verifica se o usuário selecionou incluir números na senha.
    if incluir_numeros:
        
        # Se sim, adiciona todos os dígitos numéricos (0-9) à
                # string de caracteres possíveis.
        caracteres += string.digits
        
        # Seleciona aleatoriamente um número e o adiciona à lista inicial de
                # caracteres da senha, garantindo a presença de pelo menos um dígito.
        senha.append(random.choice(string.digits))
    
    # Verifica se o usuário selecionou incluir caracteres especiais na senha.
    if incluir_especiais:
        
        # Se sim, adiciona todos os caracteres de pontuação
                # disponíveis (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~) à
                # string de caracteres possíveis.
        caracteres += string.punctuation
        
        # Seleciona aleatoriamente um caractere especial e o adiciona à
                # lista inicial de caracteres da senha, garantindo a
                # presença de pelo menos um caractere especial.
        senha.append(random.choice(string.punctuation))
    
    # Verifica se após as seleções anteriores, a string de
                # caracteres possíveis está vazia.
    if len(caracteres) == 0:
        
        # Se a string estiver vazia, isso significa que nenhuma
                # categoria de caracteres foi selecionada.
        # Exibe uma mensagem de alerta ao usuário, informando sobre a
                # necessidade de selecionar pelo menos uma categoria.
        messagebox.showwarning("Opção inválida", "Selecione pelo menos uma opção de caracteres.")
        
        # Encerra a função para evitar a continuação do processo de
                # geração da senha sem caracteres válidos.
        return


    # Continua adicionando caracteres à senha até que seu
                # comprimento atinja o valor especificado pelo usuário.
    while len(senha) < comprimento:
        
        # Escolhe um caractere aleatoriamente da string de
                # caracteres possíveis e o adiciona à lista de senha.
        # Isso continua até que a senha tenha o número de
                # caracteres definido pelo usuário em 'comprimento'.
        senha.append(random.choice(caracteres))
    
    # Embaralha a lista de caracteres da senha para aumentar a
                # segurança e a imprevisibilidade.
    # O embaralhamento é importante porque os primeiros caracteres
                # foram escolhidos de cada conjunto de caracteres incluído,
    # portanto, misturá-los reduz a previsibilidade de sua posição inicial.
    random.shuffle(senha)
    
    # Converte a lista de caracteres embaralhados de 
            # volta para uma string.
    # Usa 'join' para concatenar os elementos da lista 'senha', 
            # criando uma única string.
    # Isso garante que a senha seja tratada como uma 
            # sequência contínua de caracteres.
    senha = "".join(senha[:comprimento])
    
    # Limpa qualquer conteúdo anterior que possa estar presente no
                # campo de entrada 'entrada_senha'.
    # O método 'delete' remove todo o conteúdo do campo de entrada, do
                # início (0) até o fim (tk.END), garantindo que não
                # haja vestígios de senhas anteriores.
    entrada_senha.delete(0, tk.END)
    
    # Insere a senha gerada e embaralhada no campo de entrada
                # 'entrada_senha' para exibição ao usuário.
    # O método 'insert' é usado para colocar a nova senha na
                # posição inicial do campo de entrada, tornando-a visível ao usuário.
    entrada_senha.insert(0, senha)


        
# Configuração da janela principal
# Cria a janela principal da aplicação utilizando a 
        # classe Tk do módulo tkinter.
janela_principal = tk.Tk()

# Define o título da janela principal que aparecerá na 
        # barra de título da janela do aplicativo.
janela_principal.title("Gerador de Senhas")

# Configura a cor de fundo da janela para branco. Isto é 
        # aplicado a toda a janela principal e será a cor de fundo 
        # padrão para todos os widgets que não definirem sua 
        # própria cor de fundo.
janela_principal.configure(bg="white")

# Centralizar a janela
# Define a largura da janela principal em pixels. Aqui, a 
        # largura é definida como 400 pixels.
largura_janela = 400

# Define a altura da janela principal em pixels. Aqui, a 
        # altura é definida como 400 pixels.
altura_janela = 400

# Obtém a largura total da tela do dispositivo onde a aplicação 
        # está sendo executada. Esta medida é usada para 
        # ajudar a centralizar a janela.
largura_tela = janela_principal.winfo_screenwidth()

# Obtém a altura total da tela do dispositivo onde a aplicação 
        # está sendo executada. Esta medida é usada para ajudar 
        # a centralizar a janela.
altura_tela = janela_principal.winfo_screenheight()

# Calcula a posição horizontal (X) para a janela, de modo que 
        # ela fique centralizada na tela. O cálculo envolve subtrair 
        # metade da largura da janela de metade da largura da tela.
posicao_x = (largura_tela // 2) - (largura_janela // 2)

# Calcula a posição vertical (Y) para a janela, de modo que ela fique 
        # centralizada na tela. O cálculo envolve subtrair metade 
        # da altura da janela de metade da altura da tela.
posicao_y = (altura_tela // 2) - (altura_janela // 2)

# Aplica as medidas de largura, altura e as posições X e Y 
        # calculadas para definir a geometria da janela principal. 
# O formato é "larguraxaltura+X+Y", que especifica a largura, 
        # altura e posição exatas da janela na tela.
janela_principal.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")


# Frame para as opções de caracteres
# Cria um LabelFrame dentro da janela principal, que é um 
        # container com um rótulo opcional.
# Este LabelFrame agrupa visualmente e organiza as 
        # opções de caracteres da senha.
frame_opcoes = tk.LabelFrame(janela_principal, 
                             text="Opções de Caracteres", 
                             padx=10, 
                             pady=10, 
                             bg="white")

# Configura o padding interno do frame em 10 pixels tanto na 
        # vertical (pady) quanto na horizontal (padx) para 
        # melhor espaçamento entre os widgets internos.
# Empacota o frame dentro da janela principal, com espaçamento 
        # externo de 20 pixels em todas as direções (pady e padx),
# estica o frame para preencher o espaço disponível na direção 
        # horizontal e vertical (fill="both") e permite que o 
        # frame expanda (expand="yes")
# para ocupar qualquer espaço extra disponível na janela.
frame_opcoes.pack(pady=20, padx=20, fill="both", expand="yes")

# Variáveis de controle para os checkboxes, usadas para armazenar e 
        # rastrear o estado (selecionado ou não) de cada opção de caracteres.
var_maiusculas = tk.BooleanVar()  # Variável booleana para letras maiúsculas.
var_minusculas = tk.BooleanVar()  # Variável booleana para letras minúsculas.
var_numeros = tk.BooleanVar()     # Variável booleana para números.
var_especiais = tk.BooleanVar()   # Variável booleana para caracteres especiais.

# Checkboxes para seleção das opções de caracteres
# Cria um checkbox para a opção de incluir letras maiúsculas na senha.
check_maiusculas = tk.Checkbutton(frame_opcoes, 
                                  text="Incluir Letras Maiúsculas", 
                                  variable=var_maiusculas, 
                                  bg="white")

# Configura o checkbox com a variável de 
        # controle var_maiusculas e define o 
        # fundo como branco.
# Posiciona o checkbox na primeira linha e primeira coluna,
        # alinhado à esquerda (west).
check_maiusculas.grid(row=0, column=0, sticky="w")  

# Cria um checkbox para a opção de incluir letras minúsculas.
check_minusculas = tk.Checkbutton(frame_opcoes, 
                                  text="Incluir Letras Minúsculas", 
                                  variable=var_minusculas, 
                                  bg="white")

# Configura o checkbox com a variável de controle 
        # var_minusculas e define o fundo como branco.
# Posiciona na segunda linha, alinhado à esquerda.
check_minusculas.grid(row=1, column=0, sticky="w")  

# Cria um checkbox para a opção de incluir números.
check_numeros = tk.Checkbutton(frame_opcoes, 
                               text="Incluir Números", 
                               variable=var_numeros, 
                               bg="white")

# Configura o checkbox com a variável de controle 
        # var_numeros e define o fundo como branco.
# Posiciona na terceira linha, alinhado à esquerda.
check_numeros.grid(row=2, column=0, sticky="w")  

# Cria um checkbox para a opção de incluir caracteres especiais.
check_especiais = tk.Checkbutton(frame_opcoes, 
                                 text="Incluir Caracteres Especiais", 
                                 variable=var_especiais, 
                                 bg="white")

# Configura o checkbox com a variável de controle 
        # var_especiais e define o fundo como branco.
# Posiciona na quarta linha, alinhado à esquerda.
check_especiais.grid(row=3, column=0, sticky="w")  


# Criação e configuração do frame para a entrada do 
        # comprimento da senha.
frame_comprimento = tk.Frame(janela_principal, bg="white")

# Cria um novo frame dentro da janela principal para 
        # organizar visualmente a entrada relacionada ao 
        # comprimento da senha. Configura o fundo para branco.
frame_comprimento.pack(pady=10)

# Empacota o frame no layout da janela principal, adicionando 
        # um espaçamento vertical (pady) de 10 pixels acima e 
        # abaixo do frame para separá-lo visualmente dos elementos adjacentes.

# Criação do rótulo para a entrada do comprimento da senha.
label_comprimento = tk.Label(frame_comprimento, 
                             text="Quantidade de Dígitos:", 
                             bg="white")

# Cria um rótulo dentro do frame_comprimento, especificando 
        # "Quantidade de Dígitos:" como texto para informar 
        # ao usuário o propósito da entrada adjacente.
label_comprimento.pack(side="left", padx=5)

# Empacota o rótulo no lado esquerdo do frame_comprimento, 
        # adicionando um espaçamento horizontal (padx) de 5 pixels à 
        # esquerda do rótulo para um alinhamento apropriado.

# Criação da entrada para definir o comprimento da senha.
entrada_comprimento = tk.Entry(frame_comprimento, width=5)

# Cria um campo de entrada dentro do frame_comprimento para 
        # permitir ao usuário especificar o número desejado de 
        # dígitos para a senha. Limita a largura a 5 caracteres, 
        # adequado para a entrada de números.
entrada_comprimento.pack(side="left", padx=5)

# Empacota a entrada ao lado do rótulo no lado esquerdo, 
        # adicionando um espaçamento horizontal (padx) de 5 pixels 
        # para separá-la adequadamente do rótulo e manter a organização visual.


# Botão para gerar a senha
# Cria um botão na janela principal que, quando clicado, 
        # aciona a função 'gerar_senha'.
botao_gerar = tk.Button(janela_principal, 
                        text="Gerar Senha", 
                        command=gerar_senha)

# O botão é empacotado no layout da janela principal com um 
        # espaçamento vertical (pady) de 20 pixels acima e 
        # abaixo para separá-lo visualmente de outros elementos.
botao_gerar.pack(pady=20)

# Entrada para exibir a senha gerada
# Cria um frame na janela principal para organizar os elementos 
        # relacionados à exibição da senha gerada.
frame_senha = tk.Frame(janela_principal, bg="white")

# Define a cor de fundo do frame como branca para manter a 
        # consistência com o tema geral da interface.
frame_senha.pack(pady=10)

# O frame é empacotado com um espaçamento vertical (pady) de 10 pixels 
        # acima e abaixo, ajudando na organização e separação 
        # visual dos elementos.

# Rótulo para a senha gerada
# Cria um rótulo dentro do frame_senha para identificar 
        # claramente onde a senha gerada será exibida.
label_senha = tk.Label(frame_senha, 
                       text="Senha Gerada:", 
                       bg="white")

# Configura o rótulo com texto "Senha Gerada:", fundo branco 
        # para manter o design uniforme.
label_senha.pack(side="left", padx=5)

# Empacota o rótulo no lado esquerdo do frame_senha, adicionando um 
        # espaçamento horizontal (padx) de 5 pixels para um 
        # alinhamento adequado e espaço visual.

# Campo de entrada para mostrar a senha gerada
# Cria um campo de entrada no frame_senha para exibir a senha que será gerada.
entrada_senha = tk.Entry(frame_senha, 
                         width=50, 
                         font=('Helvetica', 14))

# Define a largura do campo de entrada para 50 caracteres e 
        # ajusta a fonte para Helvetica tamanho 14 para
        # melhor legibilidade.
entrada_senha.pack(side="left", padx=5)

# Empacota o campo de entrada ao lado do rótulo, no lado esquerdo, com 
        # um espaçamento horizontal (padx) de 5 pixels para 
        # separação adequada.

# Inicia o loop principal da interface gráfica, mantendo a 
        # janela aberta e responsiva a interações do usuário.
janela_principal.mainloop()