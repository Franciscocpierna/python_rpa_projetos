# Importa o módulo tkinter para criar interfaces gráficas.
import tkinter as tk

# Importa a submódulo messagebox para exibir caixas de diálogo.
from tkinter import messagebox

# Importa o módulo random para gerar números aleatórios.
import random

# Define a função para gerar dígitos verificadores de um CPF.
def gerar_digito_verificador(nove_digitos):
    
    # Inicializa uma variável soma para acumular os
            # resultados das multiplicações.
    soma = 0
    
    # Itera sobre cada dígito e seu índice na lista de
            # nove dígitos iniciais do CPF.
    for i, num in enumerate(nove_digitos):
        
        # Multiplica cada dígito pelo seu peso (decrescente
                # de 10 a 2) e adiciona à soma.
        soma += int(num) * (10 - i)
        
    # Calcula o primeiro dígito verificador como o
            # resto da divisão da soma por 11.
    digito1 = soma % 11
    
    # Se o resto da divisão for menor que 2, o dígito é 0;
            # caso contrário, subtrai-se o resto de 11.
    digito1 = 0 if digito1 < 2 else 11 - digito1
    
    # Reinicia a variável soma para calcular o
            # segundo dígito verificador.
    soma = 0
    
    # Adiciona o primeiro dígito verificador
            # calculado à lista de dígitos.
    nove_digitos.append(str(digito1))
    
    # Itera sobre a lista agora com dez dígitos,
            # incluindo o primeiro dígito verificador.
    for i, num in enumerate(nove_digitos):
        
        # Multiplica cada dígito pelo seu novo
                # peso (decrescente de 11 a 2) e adiciona à soma.
        soma += int(num) * (11 - i)
        
    # Calcula o segundo dígito verificador como o
            # resto da divisão da soma por 11.
    digito2 = soma % 11
    
    # Se o resto da divisão for menor que 2, o dígito é 0;
            # caso contrário, subtrai-se o resto de 11.
    digito2 = 0 if digito2 < 2 else 11 - digito2

    # Retorna os dois dígitos verificadores como uma tupla.
    return digito1, digito2


# Define a função gerar_cpf para criar um
        # número de CPF completo.
def gerar_cpf():
    
    # Gera uma lista de nove dígitos aleatórios, onde 
            # cada dígito é convertido para uma string.
    # A função random.randint(0, 9) é chamada nove 
            # vezes (uma para cada dígito do CPF base).
    nove_digitos = [str(random.randint(0, 9)) for _ in range(9)]

    # Chama a função gerar_digito_verificador passando a 
            # lista de nove dígitos para calcular os 
            # dois dígitos verificadores.
    digito1, digito2 = gerar_digito_verificador(nove_digitos)

    # Concatena os nove dígitos originais com os dois 
            # dígitos verificadores para formar o número 
            # completo do CPF.
    # Usa a função join para converter a lista de strings em 
            # uma única string e adiciona os dígitos verificadores.
    cpf = "".join(nove_digitos[:9]) + str(digito1) + str(digito2)

    # Limpa qualquer valor anterior no campo de entrada 'entrada_cpf' 
            # para garantir que não haja sobrescrição ou erro visual.
    # O método delete remove todo o conteúdo do campo de 
            # entrada desde o índice 0 até o final do campo (tk.END).
    entrada_cpf.delete(0, tk.END)

    # Insere o CPF formatado no campo de entrada. 
            # A função formatar_cpf é chamada com o 
            # CPF completo como argumento.
    # A função formatar_cpf retorna o CPF formatado na 
            # máscara padrão brasileira 000.000.000-00, 
            # que é então inserido no campo de entrada.
    entrada_cpf.insert(0, formatar_cpf(cpf))


# Define a função formatar_cpf que aceita um argumento 'cpf', 
        # que é a string de dígitos do CPF.
def formatar_cpf(cpf):
    
    # Retorna o CPF formatado usando string interpolation.
    # f-string é usada para inserir os dígitos do CPF 
            # nas posições corretas da máscara de formatação.
    # cpf[:3] extrai os três primeiros dígitos do CPF.
    # cpf[3:6] extrai os dígitos do CPF da 
            # posição 3 até a posição 5.
    # cpf[6:9] extrai os dígitos do CPF da 
            # posição 6 até a posição 8.
    # cpf[9:] extrai os dois últimos dígitos do 
            # CPF, que são os dígitos verificadores.
    # Os dígitos são separados por pontos (.) e 
            # um hífen (-) antes dos
    # dois últimos dígitos, conforme o formato 
            # padrão de CPF no Brasil.
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    

# Define a função que mostra as regras 
            # para o cálculo de CPF.
def mostrar_regras():
    
    # Cria uma nova janela toplevel que 
            # será uma janela filha da janela principal.
    regras_janela = tk.Toplevel(janela_principal)
    
    # Configura o título da janela de regras.
    regras_janela.title("Regras do Cálculo do CPF")
    
    # Define a cor de fundo da janela de 
            # regras como branco.
    regras_janela.configure(bg="white")
    
    # Configurações para centralizar a 
            # janela de regras na tela.
    # Define a largura da janela de regras 
            # como 1200 pixels.
    largura_janela_regras = 1200
    
    # Define a altura da janela de regras como 400 pixels.
    altura_janela_regras = 400
    
    # Obtém a largura da tela onde a 
            # janela será exibida.
    largura_tela_regras = regras_janela.winfo_screenwidth()
    
    # Obtém a altura da tela onde a 
            # janela será exibida.
    altura_tela_regras = regras_janela.winfo_screenheight()
    
    # Calcula a posição horizontal para 
            # centralizar a janela na tela.
    posicao_x_regras = (largura_tela_regras // 2) - (largura_janela_regras // 2)
    
    # Calcula a posição vertical para centralizar a 
            # janela na tela.
    posicao_y_regras = (altura_tela_regras // 2) - (altura_janela_regras // 2)
    
    # Aplica as dimensões e posição calculadas para 
            # definir a geometria da janela.
    regras_janela.geometry(f"{largura_janela_regras}x{altura_janela_regras}+{posicao_x_regras}+{posicao_y_regras}")

    # Texto explicativo sobre as regras de 
            # cálculo do CPF.
    texto_regras = (
        "O CPF (Cadastro de Pessoas Físicas) é composto por 11 dígitos.\n\n"
        "Os nove primeiros dígitos são a base do CPF. A partir deles, calculam-se os dois dígitos verificadores.\n\n"
        "Cálculo do primeiro dígito verificador:\n"
        "1. Multiplique os 9 primeiros dígitos pela sequência decrescente de 10 a 2.\n"
        "2. Some os resultados das multiplicações.\n"
        "3. Calcule o resto da divisão da soma por 11.\n"
        "4. Se o resto for menor que 2, o primeiro dígito verificador é 0. Caso contrário, subtraia o resto de 11 para obter o primeiro dígito verificador.\n\n"
        "Cálculo do segundo dígito verificador:\n"
        "1. Inclua o primeiro dígito verificador aos 9 primeiros dígitos, totalizando 10 dígitos.\n"
        "2. Multiplique os 10 dígitos pela sequência decrescente de 11 a 2.\n"
        "3. Some os resultados das multiplicações.\n"
        "4. Calcule o resto da divisão da soma por 11.\n"
        "5. Se o resto for menor que 2, o segundo dígito verificador é 0. Caso contrário, subtraia o resto de 11 para obter o segundo dígito verificador."
    )

    # Cria um rótulo (Label) que contém o texto das regras, 
            # configurando o alinhamento, cor de 
            # fundo, padding e fonte.
    # Cria uma instância de tk.Label, que é um widget 
            # usado para exibir texto ou imagens.
    # regras_janela é o widget pai onde o Label será 
            # colocado, vinculando o Label à janela de regras.
    # text=texto_regras define o conteúdo do texto que 
            # será exibido pelo Label, que é uma string 
            # multilinha contendo as regras detalhadas 
            # de cálculo do CPF.
    # justify="left" configura o alinhamento do texto 
            # dentro do Label para ser alinhado à esquerda, 
            # facilitando a leitura de múltiplas linhas.
    # bg="white" define a cor de fundo (background) do 
            # Label como branco, mantendo consistência 
            # com o tema da interface gráfica.
    # padx=10 e pady=10 configuram o "padding" interno ao 
            # redor do texto dentro do Label em 10 pixels 
            # tanto na horizontal (x) quanto na vertical (y).
    # Isso ajuda a evitar que o texto fique muito próximo das 
            # bordas do Label, melhorando a legibilidade.
    # font=('Helvetica', 12) define a fonte do texto no Label 
            # como Helvetica de tamanho 12, escolha que 
            # oferece boa legibilidade.
    label_regras = tk.Label(regras_janela, 
                            text=texto_regras, 
                            justify="left", 
                            bg="white", 
                            padx=10, 
                            pady=10, 
                            font=('Helvetica', 12))
    
    # Adiciona o rótulo à janela de regras e ajusta para 
            # preencher todo o espaço disponível, 
            # expandindo conforme necessário.
    # pack() é um gerenciador de geometria que 
            # organiza os widgets em blocos antes de 
            # colocá-los no widget pai.
    # fill="both" indica que o widget (Label) deve 
            # expandir para preencher todo o espaço 
            # disponível tanto na horizontal (x) quanto 
            # na vertical (y).
    # Isso garante que o texto ocupe toda a área do Label, 
            # que se ajustará ao tamanho do texto e ao 
            # espaço disponível na janela.
    # expand=True faz com que o Label expanda para ocupar 
            # qualquer espaço extra no widget pai, garantindo 
            # que use todo o espaço que possa estar disponível.
    # Esse comportamento é útil para manter o layout responsivo e 
            # adaptável a diferentes tamanhos de janela.
    label_regras.pack(fill="both", 
                      expand=True)


# Configuração da janela principal
# Cria uma nova instância da classe Tk, que serve 
        # como a janela principal para a aplicação de 
        # interface gráfica.
janela_principal = tk.Tk()

# Define o título da janela principal, que aparece 
        # na barra de título da janela.
janela_principal.title("Gerador de CPF")

# Configura a cor de fundo da janela principal para 
        # branco. Isso define a cor de fundo de todos os 
        # widgets que não têm uma cor de fundo 
        # explicitamente definida.
janela_principal.configure(bg="white")

# Centralizar a janela
# Obtém a largura pretendida para a janela principal. 
        # Esta é a largura que a janela terá 
        # quando for exibida.
largura_janela = 400

# Obtém a altura pretendida para a janela principal. 
        # Esta é a altura que a janela terá 
        # quando for exibida.
altura_janela = 150

# Utiliza o método winfo_screenwidth para obter a 
        # largura total da tela onde a janela será 
        # exibida. Este valor é necessário para 
        # centralizar a janela.
largura_tela = janela_principal.winfo_screenwidth()

# Utiliza o método winfo_screenheight para obter a 
        # altura total da tela onde a janela será exibida. 
        # Este valor é necessário para centralizar a janela.
altura_tela = janela_principal.winfo_screenheight()

# Calcula a posição horizontal (X) para a janela. Isso é 
        # feito subtraindo metade da largura da janela de 
        # metade da largura da tela, centralizando-a 
        # horizontalmente.
posicao_x = (largura_tela // 2) - (largura_janela // 2)

# Calcula a posição vertical (Y) para a janela. 
        # Isso é feito subtraindo metade da altura da 
        # janela de metade da altura da tela, 
        # centralizando-a verticalmente.
posicao_y = (altura_tela // 2) - (altura_janela // 2)

# Aplica a largura, altura e posições X e Y calculadas 
        # para definir a geometria da janela principal.
# O formato do argumento é "larguraxaltura+X+Y", o que 
        # define as dimensões e a posição da janela na tela.
janela_principal.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")


# Configuração do grid
# Configura a coluna 0 da janela_principal para 
        # que ela tenha um "peso" flexível.
# O peso determina como o espaço adicional é 
        # distribuído entre as colunas. Um peso maior 
        # faz com que a coluna expanda mais do que 
        # colunas com pesos menores.
janela_principal.grid_columnconfigure(0, weight=1)

# Configura a linha 0 da janela_principal de maneira 
        # similar à coluna, permitindo que ela expanda e 
        # ocupe espaço adicional na janela.
# Isso garante que os elementos dentro dessa linha e 
        # coluna possam crescer para preencher o espaço 
        # disponível conforme a janela é redimensionada.
janela_principal.grid_rowconfigure(0, weight=1)

# Frame principal
# Cria um novo frame (container para outros widgets) 
        # dentro da janela_principal.
# Este frame serve como o principal contêiner para 
        # outros widgets e é configurado com fundo branco.
frame_principal = tk.Frame(janela_principal, bg="white")


# Posiciona o frame_principal na linha 0, coluna 0 
        # do grid da janela_principal.
# O argumento 'sticky="nsew"' faz com que o frame_principal se 
        # expanda e adira ao norte (n), sul (s), 
        # leste (e) e oeste (w) do espaço de grid.
# Isso significa que o frame irá expandir para 
        # preencher todo o espaço da célula de grid em que está localizado.
frame_principal.grid(row=0, 
                     column=0, 
                     sticky="nsew")

# Frame para os botões
# Cria outro frame dentro de frame_principal, 
        # especificamente para conter os botões.
# Este frame também tem o fundo configurado como 
        # branco, mantendo a consistência visual da aplicação.
frame_botoes = tk.Frame(frame_principal, bg="white")

# Usa o gerenciador de layout 'pack' para adicionar o 
        # frame_botoes ao frame_principal.
# O 'pady=20' adiciona um espaçamento vertical de 
        # 20 pixels acima e abaixo do frame_botoes, 
        # criando um espaço visual entre os botões e 
        # outros elementos.
frame_botoes.pack(pady=20)

# Botão para gerar o CPF
# Cria um botão no frame 'frame_botoes'. Este botão é 
        # usado para iniciar a geração de um CPF 
        # quando clicado.
botao_gerar = tk.Button(frame_botoes, 
                        text="Gerar CPF", 
                        command=gerar_cpf, 
                        font=('Helvetica', 12))

# Posiciona o botão 'botao_gerar' na linha 0, 
        # coluna 0 do grid dentro de 'frame_botoes'.
# O 'padx=10' adiciona um espaçamento horizontal de 
        # 10 pixels em ambos os lados do botão, 
        # separando-o visualmente de outros 
        # elementos ou bordas.
botao_gerar.grid(row=0, column=0, padx=10)


# Botão para mostrar regras
# Cria um segundo botão no mesmo frame para 
        # mostrar as regras de cálculo do CPF.
botao_regras = tk.Button(frame_botoes, 
                         text="Regras", 
                         command=mostrar_regras, 
                         font=('Helvetica', 12))

# Posiciona o botão 'botao_regras' ao lado do 
        # botão 'botao_gerar', na linha 0, 
        # coluna 1 do grid.
# Semelhante ao botão anterior, 'padx=10' adiciona 
        # espaçamento horizontal.
botao_regras.grid(row=0, column=1, padx=10)

# Entrada para exibir o CPF gerado
# Cria um novo frame dentro de 'frame_principal' 
        # para conter o campo de entrada e seu rótulo.
frame_cpf = tk.Frame(frame_principal, bg="white")

# Posiciona 'frame_cpf' dentro de 'frame_principal' 
        # usando o método 'pack' com 'pady=20',
# que adiciona espaçamento vertical de 20 pixels 
        # acima e abaixo do frame para separação visual.
frame_cpf.pack(pady=20)

# Cria um rótulo dentro de 'frame_cpf' para identificar o 
        # campo de entrada onde o CPF gerado será exibido.
label_cpf = tk.Label(frame_cpf, 
                     text="CPF Gerado:", 
                     bg="white", 
                     font=('Helvetica', 12))

# Posiciona o rótulo 'label_cpf' no lado esquerdo do 
        # 'frame_cpf' usando 'pack' com 'padx=5',
# que adiciona 5 pixels de espaçamento horizontal a 
        # partir da borda esquerda.
label_cpf.pack(side="left", padx=5)

# Cria um campo de entrada para exibir o CPF gerado.
entrada_cpf = tk.Entry(frame_cpf, width=20, font=('Helvetica', 14))

# Posiciona o campo de entrada ao lado do rótulo 
        # 'label_cpf', também no lado esquerdo de 'frame_cpf'.
# 'padx=5' é usado novamente para adicionar espaçamento 
        # horizontal, garantindo que o campo de entrada 
        # não fique muito próximo ao rótulo.
entrada_cpf.pack(side="left", padx=5)

# Inicia o loop principal da interface gráfica, que 
        # mantém a janela aberta e responde a 
        # eventos, como cliques de botão.
janela_principal.mainloop()