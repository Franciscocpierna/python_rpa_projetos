#pip install qrcode[pil] Pillow

# Importando o módulo tkinter para a criação de interfaces gráficas.
import tkinter as tk

# Importando componentes específicos de tkinter para 
        # mensagens e seleção de arquivos.
from tkinter import messagebox, filedialog

# Importando o módulo qrcode para a geração de QR Codes.
import qrcode

# Importando módulos da biblioteca PIL para 
        # trabalhar com imagens.
from PIL import Image, ImageTk

# Importando o módulo re para expressões regulares.
import re


# Definição da função gerar_qrcode, que será 
        # responsável por criar um QR Code.
def gerar_qrcode():
    
    # A função 'get' é usada para obter o texto digitado na 
            # área de texto do usuário. "1.0" significa que 
            # começamos do primeiro caractere do texto, e 'tk.END' 
            # indica que vamos até o final do texto inserido.
    # O método 'strip' é utilizado para remover espaços em 
            # branco desnecessários no início e no fim do texto.
    texto = entrada_texto.get("1.0", tk.END).strip()
    
    # Verificação se o campo de texto está vazio. Se estiver, 
            # uma mensagem de aviso é mostrada ao usuário.
    if not texto:
        
        messagebox.showwarning("Aviso", "Por favor, insira algum texto para gerar o QR Code.")
        return  # Termina a execução da função se não houver texto.

    
    # Criação de um objeto QR Code. Aqui são definidos 
            # alguns parâmetros:
    # - version=1: Define a versão do QR Code. A versão 1 
            # tem 21x21 módulos. Versões mais altas têm mais módulos.
    # - error_correction=qrcode.constants.ERROR_CORRECT_L: Define o nível 
            # de correção de erros. L permite cerca de 7% de correção de erro.
    # - box_size=10: Define o tamanho de cada caixa 
            # do QR Code em pixels.
    # - border=4: Define a largura da borda ao redor 
            # do QR Code em unidades de caixa.
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Adiciona os dados (texto) ao objeto QR Code que será 
            # convertido em um código.
    qr.add_data(texto)
    
    # O método 'make' é chamado com o argumento 'fit=True' 
            # para permitir que a biblioteca otimize automaticamente o 
            # tamanho do QR Code com base no texto inserido.
    qr.make(fit=True)
    
    # Geração da imagem do QR Code, definindo a cor de 
            # preenchimento (fill) e a cor de fundo (back_color).
    img = qr.make_image(fill='black', back_color='white')
    
    # Salvar a imagem gerada do QR Code no sistema de 
            # arquivos como 'qrcode.png'.
    img.save("qrcode.png")
    
    # Chamada da função 'exibir_qrcode' que atualiza a 
            # interface gráfica para mostrar a imagem do QR Code gerada.
    exibir_qrcode("qrcode.png")


# Definição da função exibir_qrcode, que recebe um 
            # parâmetro 'caminho_imagem'.
# Este parâmetro é uma string que indica o caminho do 
        # arquivo da imagem do QR Code que será exibida.
def exibir_qrcode(caminho_imagem):
    
    # Carrega a imagem do QR Code do disco usando a 
            # função 'open' do módulo Image.
    # A função 'open' é parte da biblioteca PIL (Python 
            # Imaging Library) e é usada para abrir arquivos de imagem.
    imagem = Image.open(caminho_imagem)
    
    # Redimensiona a imagem para um tamanho específico. 
            # Neste caso, para 200x200 pixels.
    # O método 'resize' recebe uma tupla com o novo tamanho e 
            # o algoritmo de redimensionamento a ser usado.
    # 'Image.LANCZOS' é um dos algoritmos de redimensionamento 
            # disponíveis que oferece uma alta qualidade de interpolação.
    imagem = imagem.resize((200, 200), Image.LANCZOS)
    
    # Converte a imagem PIL para um formato que o 
            # Tkinter possa usar.
    # 'ImageTk.PhotoImage' é uma classe que cria uma imagem 
            # compatível com Tkinter a partir de uma imagem PIL.
    imagem_tk = ImageTk.PhotoImage(imagem)
    
    # Configura o 'label_imagem' para usar a imagem Tkinter recém-criada.
    # 'label_imagem' é uma variável global que se refere a um 
            # widget de etiqueta (label) na interface gráfica 
            # onde a imagem do QR Code é exibida.
    # O método 'config' é usado para configurar várias opções de 
            # widgets no Tkinter, como a imagem mostrada no label.
    label_imagem.config(image=imagem_tk)
    
    # Armazena uma referência da imagem Tkinter no próprio 
            # widget de label.
    # Isso é necessário porque o Tkinter não mantém uma 
            # referência interna às imagens configuradas em seus widgets,
            # e a imagem pode ser coletada como lixo (deletada da 
            # memória) se não for mantida uma referência 
            # ativa em algum lugar no código.
    label_imagem.image = imagem_tk


# Definição da função 'sanitize_filename', que recebe um 
            # parâmetro 'text'.
# Esta função é usada para limpar o texto que será 
        # utilizado como nome de arquivo, removendo 
        # caracteres indesejados.
def sanitize_filename(text):
    
    # A função utiliza a função 'sub' do módulo 're' (regular 
            # expressions) para substituir caracteres.
    # O primeiro argumento de 'sub' é um padrão de expressão 
            # regular que identifica quais caracteres devem ser substituídos.
    # r'[^a-zA-Z0-9_\-]' é uma expressão regular que 
            # corresponde a qualquer caractere que NÃO seja:
    # - Letra maiúscula (A-Z)
    # - Letra minúscula (a-z)
    # - Número (0-9)
    # - Sublinhado (_)
    # - Hífen (-)
    # O '^' dentro dos colchetes inverte o conjunto, então 
            # estamos definindo um conjunto de caracteres 
            # permitidos e dizendo "tudo que não é isso deve ser substituído".
    # O segundo argumento é o caractere '_' que será usado para 
            # substituir qualquer caractere que não seja permitido.
    # O último argumento é o 'text', o texto que será processado.
    # A função 'sub' irá percorrer o texto fornecido, substituir 
            # cada caractere que não esteja no conjunto permitido 
            # por um sublinhado,
            # e retornará a nova string resultante.
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', text)



# Definição da função 'baixar_qrcode'. Esta função não recebe 
            # argumentos e é responsável por gerar e permitir o 
        # download de um QR Code.
def baixar_qrcode():
    
    # A função 'get' do widget 'entrada_texto' é utilizada para 
            # recuperar o texto inserido pelo usuário na interface gráfica.
    # O "1.0" indica que a leitura do texto deve começar do 
            # primeiro caractere da primeira linha,
    # e 'tk.END' indica que a leitura deve continuar até o 
            # final do texto, incluindo todos os caracteres.
    # O método 'strip' é aplicado ao texto obtido para remover 
            # espaços em branco extras no início e no fim do texto.
    texto = entrada_texto.get("1.0", tk.END).strip()
    
    # Verifica se o campo de texto está vazio após a remoção dos 
            # espaços. Se estiver, exibe uma mensagem de aviso.
    # A função 'showwarning' do módulo 'messagebox' é usada para 
            # exibir uma janela de aviso com uma mensagem específica.
    if not texto:
        messagebox.showwarning("Aviso", "Por favor, insira algum texto para gerar o QR Code.")
        return  # Interrompe a execução da função se o campo de texto estiver vazio.

    # Criação de um objeto QR Code utilizando a biblioteca 'qrcode'.
    # Aqui são especificados alguns parâmetros para a geração do QR Code:
    # - version=1: Define a versão do QR Code, que influencia o 
            # tamanho e a quantidade de dados que ele pode armazenar.
    # - error_correction=qrcode.constants.ERROR_CORRECT_L: Estabelece o 
            # nível de correção de erros do QR Code. 'L' permite 
            # cerca de 7% de correção.
    # - box_size=10: Define o tamanho de cada "caixa" no QR Code em pixels.
    # - border=4: Define a largura da borda ao redor do QR Code, 
            # medida em unidades de caixas.
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Adiciona os dados recuperados do campo de 
            # texto ao objeto QR Code.
    qr.add_data(texto)
    
    # Finaliza a construção do QR Code com o método 'make', 
            # ajustando-o para caber nos dados fornecidos 
            # com o parâmetro 'fit=True'.
    qr.make(fit=True)
    
    # Gera a imagem do QR Code configurando as cores de 
            # preenchimento e de fundo.
    # 'fill='black'' define a cor dos pixels do QR Code para preto,
    # e 'back_color='white'' define a cor de fundo para branco.
    img = qr.make_image(fill='black', back_color='white')

    # Sanitização do nome do arquivo para garantir que o nome é 
            # seguro e compatível com o sistema de arquivos.
    # 'sanitize_filename(texto)' chama a função que substitui 
            # caracteres não permitidos no nome do arquivo por sublinhados.
    # '[:50]' limita o comprimento do nome do arquivo a 50 
            # caracteres para evitar erros devido a nomes de 
            # arquivo excessivamente longos.
    nome_arquivo = sanitize_filename(texto)[:50]
    
    # Abre uma janela para o usuário escolher onde deseja salvar o 
            # arquivo. Esta janela é criada pelo método 'asksaveasfilename'.
    # 'initialfile=nome_arquivo' define o nome inicial do arquivo na 
            # janela de diálogo, baseado no texto inserido pelo 
            # usuário, mas sanitizado e limitado.
    # 'defaultextension=".png"' garante que, se o usuário não 
            # especificar uma extensão, o arquivo será salvo com a extensão .png.
    # 'filetypes=[("PNG files", "*.png")]' limita o tipo de 
            # arquivo que o usuário pode salvar a arquivos PNG.
    caminho_arquivo = filedialog.asksaveasfilename(
        initialfile=nome_arquivo,
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")]
    )
    
    # Verifica se um caminho de arquivo foi selecionado. Se 
            # nenhum caminho for escolhido (usuário fechou a 
            # janela ou cancelou), o código abaixo não será executado.
    if caminho_arquivo:
        
        # Salva a imagem do QR Code no local especificado pelo usuário.
        img.save(caminho_arquivo)
        
        # Exibe uma mensagem de informação indicando que o QR Code 
                # foi salvo com sucesso no local escolhido.
        messagebox.showinfo("Sucesso", f"O QR Code foi salvo em {caminho_arquivo}")



# Configuração da janela principal:
# 'tk.Tk()' cria uma nova instância de janela principal para a 
        # aplicação usando a biblioteca Tkinter. 
# Esta instância é armazenada na variável 'janela_principal' e 
        # será a base para adicionar outros componentes gráficos.
janela_principal = tk.Tk()

# Define o título da janela principal.
# 'title("Gerador de QR Code")' configura o texto que 
        # aparece na barra de título da janela principal, 
# ajudando os usuários a identificar qual aplicativo está 
        # sendo executado ou a função da janela.
janela_principal.title("Gerador de QR Code")

# Configura a cor de fundo da janela principal.
# 'configure(bg="white")' define a cor de fundo da 
        # janela como branca. 
# O parâmetro 'bg' refere-se à "background", que é a 
        # cor de fundo. Aqui, escolhe-se branco para um 
        # visual limpo e simples.
janela_principal.configure(bg="white")


# Definição das dimensões da janela principal.
# 'largura_janela' e 'altura_janela' são variáveis que 
        # armazenam os valores de largura e altura da 
        # janela, respectivamente.
largura_janela = 600  # Largura da janela definida como 600 pixels.
altura_janela = 400   # Altura da janela definida como 400 pixels.

# Obtenção das dimensões da tela do monitor onde a 
        # janela será exibida.
# 'winfo_screenwidth()' e 'winfo_screenheight()' são 
        # métodos do objeto 'janela_principal' que 
        # retornam a largura e a altura da tela, respectivamente.
largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()

# Cálculo da posição inicial da janela para que ela 
        # apareça centralizada na tela.
# O cálculo usa divisão inteira (//) para encontrar o 
        # ponto central tanto da largura quanto da 
        # altura da tela, e então subtrai metade das 
        # dimensões da janela para garantir que o 
        # centro da janela alinhe com o centro da tela.
posicao_x = (largura_tela // 2) - (largura_janela // 2)
posicao_y = (altura_tela // 2) - (altura_janela // 2)

# Configuração da geometria da janela principal.
# O método 'geometry' aceita uma string que 
        # especifica a largura, a altura e as posições x e y da janela.
# A sintaxe "{largura}x{altura}+{posicao_x}+{posicao_y}" é 
        # usada para definir esses valores.
janela_principal.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")


# Criação de um frame dentro da janela principal para 
        # organizar a entrada de texto.
# 'tk.Frame' cria um contêiner na janela principal 
        # que pode conter outros widgets.
# 'bg="white"' define a cor de fundo do frame como branca.
frame_entrada = tk.Frame(janela_principal, bg="white")

# Posicionamento do frame dentro da janela usando o método 'pack'.
# 'pady=10' adiciona um espaçamento vertical de 10 
        # pixels acima e abaixo do frame para evitar 
        # que ele fique muito próximo de outros componentes.
frame_entrada.pack(pady=10)

# Criação de um label, ou rótulo, que indica ao 
        # usuário onde inserir o texto.
# 'tk.Label' cria um widget de texto que pode exibir 
        # informações ou títulos dentro de contêineres como frames.
# 'text="Texto para QR Code:"' define o texto a ser 
        # exibido no label.
# A combinação de 'bg="white"' e 'font=('Helvetica', 12)' 
        # define o fundo como branco e usa a fonte 
        # Helvetica tamanho 12 para o texto.
label_entrada = tk.Label(frame_entrada, 
                         text="Texto para QR Code:", 
                         bg="white", 
                         font=('Helvetica', 12))

# Posicionamento do label dentro do frame usando o método 'pack'.
# Sem argumentos adicionais, o label será 
        # centralizado dentro do frame.
label_entrada.pack()

# Criação de um widget de texto para entrada de 
        # dados pelo usuário.
# 'tk.Text' cria uma área de texto onde os usuários 
        # podem inserir múltiplas linhas de texto.
# 'frame_entrada' é o contêiner no qual este widget 
        # de texto é colocado.
# 'height=4' define a altura do widget de texto em 
        # linhas de texto visíveis.
# 'width=50' define a largura do widget em 
        # caracteres médios.
# 'font=('Helvetica', 12)' define a fonte e tamanho do 
        # texto dentro do widget de texto.
entrada_texto = tk.Text(frame_entrada, 
                        height=4, 
                        width=50, 
                        font=('Helvetica', 12))

# Posicionamento do widget de texto dentro do seu 
        # contêiner usando 'pack'.
# 'pady=5' adiciona um espaço vertical de 5 pixels 
        # acima e abaixo do widget para separá-lo 
        # de outros elementos.
entrada_texto.pack(pady=5)

# Criação de um frame adicional na janela principal 
        # para agrupar botões de ação.
# 'tk.Frame' cria um contêiner que pode conter outros widgets.
# 'bg="white"' define a cor de fundo do frame como branca.
frame_botoes = tk.Frame(janela_principal, bg="white")

# Posicionamento do frame de botões dentro da 
        # janela principal usando 'pack'.
# 'pady=20' adiciona um espaço vertical de 20 
        # pixels acima e abaixo do frame para 
        # separá-lo de outros elementos.
frame_botoes.pack(pady=20)

# Criação do botão que dispara a geração do QR Code.
# 'tk.Button' cria um botão clicável.
# 'frame_botoes' é o contêiner no qual este 
        # botão é colocado.
# 'text="Gerar QR Code"' define o texto exibido no botão.
# 'command=gerar_qrcode' vincula o botão à 
        # função 'gerar_qrcode', que é chamada quando o botão é clicado.
# 'font=('Helvetica', 12)' define a fonte e o 
        # tamanho do texto no botão.
botao_gerar = tk.Button(frame_botoes, 
                        text="Gerar QR Code", 
                        command=gerar_qrcode, 
                        font=('Helvetica', 12))

# Posicionamento do botão de gerar dentro do frame usando 'pack'.
# 'side=tk.LEFT' coloca o botão à esquerda dentro do frame.
# 'padx=10' adiciona um espaço horizontal de 10 pixels 
        # entre este botão e outros elementos ou margens do frame.
botao_gerar.pack(side=tk.LEFT, padx=10)

# Criação do botão que permite ao usuário baixar o QR Code gerado.
# 'tk.Button' é utilizado para criar um botão na interface gráfica. 
        # É um widget que os usuários podem clicar para executar uma ação.
# 'frame_botoes' é o contêiner (Frame) onde este botão será colocado. 
        # Todos os botões ficam agrupados neste frame para organização visual.
# 'text="Baixar QR Code"' define o texto que aparece no botão. Este 
        # texto é o que o usuário verá e entenderá o que o botão faz.
# 'command=baixar_qrcode' estabelece que, quando o botão é clicado, a 
        # função 'baixar_qrcode' será executada.
# Esta função é responsável por gerar novamente o QR Code baseado no 
        # texto inserido e oferecer uma opção para salvar a 
        # imagem em um arquivo.
# 'font=('Helvetica', 12)' configura a fonte do texto no botão. 
        # 'Helvetica' é o tipo de fonte e '12' é o tamanho da fonte.
botao_baixar = tk.Button(frame_botoes, 
                         text="Baixar QR Code", 
                         command=baixar_qrcode, 
                         font=('Helvetica', 12))

# Posicionamento do botão dentro do frame de botões usando o método 'pack'.
# 'side=tk.LEFT' coloca o botão à esquerda dentro do frame. 
        # Isso é útil quando há múltiplos botões, alinhando-os 
        # horizontalmente da esquerda para a direita.
# 'padx=10' adiciona um espaçamento horizontal de 10 pixels 
        # entre este botão e outros elementos ou margens 
        # dentro do frame.
# Este espaçamento ajuda a separar visualmente os botões, 
        # tornando a interface mais clara e fácil de usar.
botao_baixar.pack(side=tk.LEFT, padx=10)


# Criação de um label para exibir a imagem do QR Code gerado.
# 'tk.Label' cria um espaço de exibição para texto ou imagem.
# 'janela_principal' é o contêiner no qual este label é colocado.
# 'bg="white"' define a cor de fundo do label como branca.
label_imagem = tk.Label(janela_principal, bg="white")

# Posicionamento do label na janela principal usando 'pack'.
# 'pady=10' adiciona um espaço vertical de 10 pixels 
        # acima e abaixo do label para separá-lo de outros elementos.
label_imagem.pack(pady=10)

# Início do loop principal da interface gráfica.
# 'mainloop()' mantém a janela aberta, respondendo a 
        # eventos como cliques de botão até que a 
        # janela seja fechada.
janela_principal.mainloop()