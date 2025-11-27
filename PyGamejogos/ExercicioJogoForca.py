# Importa o módulo tkinter como 'tk' para criar
        # interfaces gráficas.
import tkinter as tk

# Importa o módulo messagebox de tkinter para exibir 
        # caixas de diálogo e alertas.
from tkinter import messagebox

# Importa o módulo random para gerar escolhas aleatórias, como 
        # selecionar uma palavra aleatória da lista.
import random

# Importa o módulo shelve para criar um banco de dados local 
        # simples onde os dados podem ser armazenados de forma persistente.
import shelve

# Cria uma lista de strings com palavras que serão usadas no jogo da forca.
# Estas palavras representam termos comuns na área de 
        # desenvolvimento web e computação.
palavras = ['javascript', 'css', 'html', 'navegador', 'programar', 'internet', 'computador', 'teclado', 'mouse', 'monitor']

# Inicialização de variáveis globais utilizadas no controle do jogo:
palavra_secreta = ''           # Armazena a palavra atual que está sendo adivinhada no jogo.
letras_descobertas = []        # Lista que armazena o estado atual da palavra sendo adivinhada, com letras reveladas ou ocultas.
erros = 0                      # Contador de erros do jogador. Aumenta quando uma letra errada é escolhida.
acertos = 0                    # Contador de acertos do jogador. Aumenta quando uma letra correta é escolhida.
max_erros = 7                  # Define o número máximo de erros permitidos antes de o jogador perder o jogo.
pontuacao = 0                  # Armazena a pontuação do jogador ao longo das partidas.
indice_palavra = 0             # Índice para acessar a próxima palavra da lista 'palavras' a ser usada no jogo.


# O bloco 'with' é utilizado para abrir o banco de dados 
        # 'pontuacao_db' de forma segura. 
# Ele garante que o recurso seja fechado corretamente após 
        # sua utilização, mesmo que ocorram exceções.
# 'shelve.open' é chamado para abrir um banco de dados tipo 
        # prateleira que pode armazenar objetos Python persistentemente.
with shelve.open('pontuacao_db') as db:
    
    # Aqui, tenta-se recuperar o valor da pontuação armazenada 
            # sob a chave 'pontuacao'.
    # Se não existir um valor armazenado, o método 'get' 
            # retorna '0' como valor padrão.
    pontuacao = db.get('pontuacao', 0)
    
    # Similar ao comando anterior, este comando tenta recuperar o 
            # valor do índice da última palavra usada,
            # que é armazenado sob a chave 'indice_palavra'. Se não houver 
            # um valor armazenado, retorna '0' como padrão.
    # Isso permite que o jogo continue de onde parou na última sessão.
    indice_palavra = db.get('indice_palavra', 0)


# Definição da função 'escolher_palavra_secreta' que 
        # não recebe argumentos.
def escolher_palavra_secreta():
    
    # Uso da declaração 'global' para modificar as variáveis 
            # globais 'palavra_secreta', 'letras_descobertas', 
            # e 'indice_palavra' dentro do escopo da função.
    global palavra_secreta, letras_descobertas, indice_palavra
    
    # Verifica se o índice da palavra atual está dentro do 
            # limite da lista de palavras.
    # Isso é importante para evitar acessar um índice fora 
            # do intervalo da lista 'palavras'.
    if indice_palavra < len(palavras):
        
        # Se o índice ainda está dentro dos limites, seleciona a 
                # palavra na posição 'indice_palavra' da lista 'palavras'.
        # Isso garante uma sequência ordenada de palavras antes 
                # de começar a escolher aleatoriamente.
        palavra_secreta = palavras[indice_palavra]
        
    else:
        
        # Caso o índice ultrapasse o número de palavras disponíveis na lista,
                # escolhe uma palavra aleatoriamente. Isso proporciona 
                # variedade após todas as palavras iniciais serem usadas.
        palavra_secreta = random.choice(palavras)
    
    # Cria uma lista de underscores ('_') com a mesma quantidade de 
            # caracteres que a palavra secreta.
    # Cada underscore representa uma letra não descoberta da palavra 
            # secreta, sendo um elemento visual chave para o jogo da forca.
    letras_descobertas = ['_' for _ in palavra_secreta]



# Definição da função 'desenhar_forca' que não recebe argumentos.
def desenhar_forca():
    
    # Remove qualquer desenho anterior do boneco no canvas, 
            # garantindo que o desenho comece limpo.
    # O tag 'boneco' é usado para agrupar todos os elementos 
            # gráficos do boneco, permitindo sua fácil remoção e gerenciamento.
    canvas.delete('boneco')

    # Desenha a base da forca no canvas, usando linhas 
            # para criar a estrutura.
    # Cada chamada de 'create_line' adiciona uma linha no 
            # canvas nas coordenadas especificadas com uma certa largura.
    canvas.create_line(50, 250, 150, 250, width=2)  # Linha base horizontal da forca.
    canvas.create_line(100, 250, 100, 50, width=2)  # Linha vertical principal da forca.
    canvas.create_line(100, 50, 200, 50, width=2)   # Linha superior horizontal da forca.
    canvas.create_line(200, 50, 200, 70, width=2)   # Pequena linha vertical de onde a corda será pendurada.

    # Desenha o boneco parte por parte, dependendo do número 
            # de erros que o jogador acumulou.
    if erros >= 1:
        
        # Desenha a cabeça do boneco: A função 'create_oval' é usada 
                # para desenhar a cabeça como um oval.
        # As coordenadas (180, 70) e (220, 110) definem respectivamente 
                # os pontos superior esquerdo e inferior direito do oval,
                # criando uma forma circular que representa a cabeça. 
        # A espessura da linha é definida em 2 pixels.
        canvas.create_oval(180, 70, 220, 110, width=2, tags='boneco')
    
    if erros >= 2:
        
        # Desenha o corpo do boneco: A função 'create_line' desenha 
                # uma linha vertical que representa o corpo.
        # As coordenadas (200, 110) a (200, 170) definem os pontos 
                # inicial e final da linha do corpo, diretamente abaixo da cabeça.
        # Isso cria a impressão de um corpo pendurado pela cabeça no jogo.
        canvas.create_line(200, 110, 200, 170, width=2, tags='boneco')
    
    if erros >= 3:
        
        # Desenha o braço esquerdo: Utiliza-se 'create_line' para 
                # desenhar uma linha que representa o braço esquerdo.
        # As coordenadas (200, 120) a (170, 150) formam um ângulo, 
                # representando o braço estendido para o lado esquerdo.
        canvas.create_line(200, 120, 170, 150, width=2, tags='boneco')
    
    if erros >= 4:
        
        # Desenha o braço direito: Similar ao braço esquerdo, 
                # porém estendido para o lado direito.
        # As coordenadas (200, 120) a (230, 150) formam o ângulo 
                # oposto ao do braço esquerdo, representando o braço direito.
        canvas.create_line(200, 120, 230, 150, width=2, tags='boneco')
    
    if erros >= 5:
        
        # Desenha a perna esquerda: 'create_line' é novamente 
                # utilizada para desenhar a perna esquerda.
        # As coordenadas (200, 170) a (180, 210) criam uma 
                # linha diagonal para baixo, representando a perna esquerda.
        canvas.create_line(200, 170, 180, 210, width=2, tags='boneco')
    
    if erros >= 6:
        
        # Desenha a perna direita: Usando coordenadas que formam 
                # uma linha diagonal para baixo na direção oposta à perna esquerda.
        # As coordenadas (200, 170) a (220, 210) formam a perna direita.
        canvas.create_line(200, 170, 220, 210, width=2, tags='boneco')
    
    if erros >= 7:
        
        # Desenha um "X" nos olhos do boneco, simbolizando a morte 
                # do personagem no jogo.
        # Quatro linhas são usadas para formar dois "X", um em 
                # cada olho, nas coordenadas definidas.
        # Essas linhas cruzadas criam a impressão visual de olhos 
                # fechados em X, um indicativo clássico em cartoons 
                # de que o personagem não sobreviveu.
        canvas.create_line(190, 80, 195, 85, width=2, tags='boneco')
        canvas.create_line(195, 80, 190, 85, width=2, tags='boneco')
        canvas.create_line(205, 80, 210, 85, width=2, tags='boneco')
        canvas.create_line(210, 80, 205, 85, width=2, tags='boneco')




# Definição da função 'atualizar_palavra_secreta' que não recebe argumentos.
def atualizar_palavra_secreta():
    
    # Atualiza o texto do widget 'lbl_palavra' para mostrar o 
            # estado atual da palavra secreta.
    # As letras descobertas são exibidas e as não descobertas são 
            # mostradas como underscores.
    # Os elementos da lista 'letras_descobertas' são unidos em uma 
            # string com espaço entre eles para melhor visualização.
    lbl_palavra.config(text=' '.join(letras_descobertas))
    


# Definição da função 'criar_botoes_alfabeto' que não recebe argumentos.
def criar_botoes_alfabeto():
    
    # Itera sobre todos os widgets (botões neste caso) presentes 
            # no 'frame_botoes' e os destrói.
    # Isso é útil para limpar os botões antigos antes de criar 
            # novos, por exemplo, ao reiniciar o jogo.
    for widget in frame_botoes.winfo_children():
        widget.destroy()

    # Define a disposição das letras do alfabeto em um layout de 
            # teclado QWERTY dividido em três linhas.
    keyboard_layout = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    
    # Itera sobre cada linha do layout do teclado.
    for row in keyboard_layout:
        
        # Cria um novo frame para cada linha do teclado dentro do 
                # frame principal 'frame_botoes'.
        frame_row = tk.Frame(frame_botoes)
        
        # Empacota o frame da linha no frame principal, um abaixo do outro.
        frame_row.pack()
        
        # Inicia um laço 'for' que irá iterar sobre cada caractere em 
                # uma string específica de 'row'.
        # Cada 'row' contém uma sequência de caracteres que representa 
                # uma linha de teclado QWERTY, como "qwertyuiop".
        for letra in row:
            
            # Cria um botão utilizando a classe Button do módulo tkinter.
            # A opção 'text' define o texto exibido no botão, que é a letra atual 
                    # da iteração convertida para maiúscula com o método .upper().
            # A opção 'width' define a largura do botão. Aqui, é configurado 
                    # para ter largura 4, o que ajuda a manter a uniformidade visual dos botões.
            # A opção 'command' define uma função a ser chamada quando o 
                    # botão é pressionado. A função lambda é utilizada aqui para 
                    # passar a letra atual como argumento para a função 'escolher_letra'.
            # O uso de 'lambda l=letra' é crucial porque sem isso, o comando 
                    # capturaria sempre o último valor de 'letra' ao final do 
                    # laço devido ao escopo tardio de vinculação das funções lambda.
            btn = tk.Button(frame_row, 
                            text=letra.upper(), 
                            width=4, 
                            command=lambda l=letra: escolher_letra(l))
            
            # Empacota o botão dentro do 'frame_row', que é um 
                    # contêiner específico para a linha atual do teclado.
            # 'side='left'' faz com que os botões sejam alinhados 
                    # horizontalmente da esquerda para a direita dentro do frame.
            # 'padx=2' e 'pady=2' adicionam um pequeno espaço entre os 
                    # botões horizontalmente e verticalmente, respectivamente,
                    # para evitar que os botões fiquem visualmente aglomerados e 
                    # para melhorar a estética geral da interface.
            btn.pack(side='left', padx=2, pady=2)



# Definição da função 'escolher_letra' que recebe uma 
        # letra como argumento.
def escolher_letra(letra):
    
    # Declaração para permitir o acesso e modificação das variáveis 
            # globais 'erros', 'acertos' e 'pontuacao'.
    global erros, acertos, pontuacao
    
    # Inicializa a variável 'acertou' como False. Essa variável será 
            # usada para determinar se a letra escolhida está na palavra secreta.
    acertou = False
    
    # Itera sobre cada caractere (char) e seu índice (idx) na palavra 
            # secreta usando a função enumerate, que fornece pares de índice e valor.
    for idx, char in enumerate(palavra_secreta):
        
        # Compara cada caractere da palavra secreta com a letra escolhida.
        if char == letra:
            
            # Se a letra estiver na palavra secreta, substitui o underscore no 
                    # índice correspondente pela letra correta e em maiúscula.
            letras_descobertas[idx] = letra.upper()
            
            # A variável 'acertou' é marcada como True, indicando um acerto.
            acertou = True
            
            # Incrementa o contador de acertos.
            acertos += 1
    
    # Chama a função para atualizar a exibição da palavra 
            # secreta na interface do usuário.
    atualizar_palavra_secreta()
    
    # Itera sobre todos os frames dentro do 'frame_botoes', que 
            # contém os botões de letras.
    for frame in frame_botoes.winfo_children():
        
        # Itera sobre cada botão dentro do frame atual.
        for btn in frame.winfo_children():
            
            # Verifica se o texto do botão, convertido para minúsculo, 
                    # corresponde à letra escolhida.
            if btn['text'].lower() == letra:
                
                # Se a letra foi acertada, desabilita o botão e muda sua 
                        # cor de fundo para azul e o texto para branco.
                if acertou:
                    btn.config(state='disabled', bg='blue', fg='white')
                    
                # Se a letra não foi acertada, desabilita o botão e muda 
                        # sua cor de fundo para cinza.
                else:
                    btn.config(state='disabled', bg='gray')
                    
                # Sai do laço interno após encontrar e modificar o 
                        # botão correspondente.
                break
    
    # Se a letra não estiver na palavra secreta, 
            # incrementa o contador de erros.
    if not acertou:
        
        erros += 1
        
        # Chama a função para desenhar uma parte do boneco na forca.
        desenhar_forca()
    
    # Após cada tentativa de adivinhar uma letra, verifica se o jogo 
            # terminou, seja por vitória ou derrota.
    verificar_fim_de_jogo()





# Definição da função 'verificar_fim_de_jogo' que não 
                # recebe argumentos externos.
def verificar_fim_de_jogo():
    
    # Acessa as variáveis globais 'pontuacao' e 'indice_palavra' 
            # para poder modificá-las dentro da função.
    global pontuacao, indice_palavra

    # Verifica se o número de erros cometidos pelo jogador é 
            # igual ao máximo de erros permitidos.
    if erros == max_erros:
        
        # Se verdadeiro, o jogador perdeu o jogo. Exibe uma mensagem 
                # informando a derrota e a palavra que era para adivinhar.
        # A função 'showinfo' cria uma caixa de diálogo informativa 
                # com o título 'Jogo da Forca' e a mensagem de derrota.
        messagebox.showinfo('Jogo da Forca', 'Você perdeu! A palavra era: {}'.format(palavra_secreta.upper()))

        # Chama a função 'desabilitar_botoes' para desativar todos os 
                # botões de letras, evitando mais interações após o fim do jogo.
        desabilitar_botoes()

        # Chama a função 'salvar_pontuacao' para armazenar a pontuação 
                # atual e o índice da última palavra usada.
        salvar_pontuacao()

    # Verifica se o número de acertos é igual ao comprimento da 
            # palavra secreta, indicando que todas as letras foram descobertas.
    elif acertos == len(palavra_secreta):
        
        # Se verdadeiro, o jogador venceu o jogo. Exibe uma 
                # mensagem informando a vitória.
        messagebox.showinfo('Jogo da Forca', 'Você venceu!')

        # Incrementa a pontuação em 1 para cada vitória.
        pontuacao += 1

        # Incrementa o índice da palavra, para passar à próxima 
                # palavra na próxima rodada do jogo.
        indice_palavra += 1

        # Atualiza a exibição da pontuação na interface gráfica, 
                # refletindo a nova pontuação.
        lbl_pontuacao.config(text='Pontuação: {}'.format(pontuacao))

        # Salva a nova pontuação e o novo índice de palavras para 
                # manter o progresso entre sessões do jogo.
        salvar_pontuacao()

        # Reinicia o jogo automaticamente ao iniciar uma nova 
                # rodada com uma nova palavra.
        reiniciar_jogo_automatico()


# Definição da função 'desabilitar_botoes', que não 
                # recebe argumentos.
def desabilitar_botoes():
    
    # Este laço externo itera sobre todos os 'frames' dentro do 
            # contêiner 'frame_botoes'.
    # 'frame_botoes' é um widget que agrupa todos os botões de letras, 
            # organizados em frames para cada linha do teclado.
    for frame in frame_botoes.winfo_children():
        
        # Este laço interno itera sobre cada botão ('btn') 
                # dentro do frame atual.
        # 'winfo_children()' retorna uma lista de todos os widgets 
                # filhos dentro de 'frame', que neste caso são os botões de letras.
        for btn in frame.winfo_children():
            
            # O método 'config' é chamado em cada botão para 
                    # modificar suas propriedades.
            # 'state='disabled'' altera o estado do botão para 
                    # desativado, impedindo que ele seja clicado ou interaja com o usuário.
            btn.config(state='disabled')


# Definição da função 'reiniciar_jogo_automatico' que 
            # não recebe argumentos externos.
def reiniciar_jogo_automatico():
    
    # Utilização da palavra-chave 'global' para modificar as variáveis 
            # globais 'erros' e 'acertos' dentro desta função.
    global erros, acertos
    
    # Zera os contadores de 'erros' e 'acertos' para o novo jogo.
    # Isso é necessário para começar o jogo sem qualquer 
            # penalidade ou vantagem prévia.
    erros = 0
    acertos = 0

    # Chama a função 'escolher_palavra_secreta' para selecionar 
            # uma nova palavra secreta para a próxima rodada do jogo.
    # Esta função também inicializa 'letras_descobertas' com underscores 
            # correspondentes às letras da nova palavra.
    escolher_palavra_secreta()

    # Atualiza a exibição da palavra secreta no jogo.
    # Isso reflete na interface gráfica a nova palavra com underscores 
            # onde as letras ainda não foram descobertas.
    atualizar_palavra_secreta()

    # Chama a função 'criar_botoes_alfabeto' para reconstruir o 
            # layout dos botões do alfabeto.
    # Isso é necessário para reativar os botões que foram 
            # desativados ao final do jogo anterior.
    criar_botoes_alfabeto()

    # Remove qualquer desenho prévio do 'boneco' no canvas, limpando a 
            # representação gráfica de erros do jogo anterior.
    canvas.delete('boneco')

    # Chama a função 'desenhar_forca' para recriar a estrutura 
            # básica da forca sem o boneco.
    # Isso prepara o visual para a nova rodada, mantendo a forca 
            # pronta para os erros que podem ser cometidos.
    desenhar_forca()


# Função para reiniciar o jogo manualmente (se necessário)
def reiniciar_jogo():
    reiniciar_jogo_automatico()



# Definição da função 'salvar_pontuacao', que não recebe 
        # argumentos externos.
def salvar_pontuacao():
    
    # Utiliza a instrução 'with' juntamente com 'shelve.open' para 
            # abrir um arquivo de banco de dados chamado 'pontuacao_db'.
    # 'shelve.open' retorna um objeto similar a um dicionário que 
            # pode ser usado para persistir dados entre sessões do jogo.
    # O uso do 'with' garante que o recurso do arquivo seja gerenciado 
            # corretamente, fechando-o automaticamente ao final do bloco.
    with shelve.open('pontuacao_db') as db:
        
        # Armazena o valor da variável global 'pontuacao' no banco de 
                # dados sob a chave 'pontuacao'.
        # Isso atualiza o valor armazenado com a pontuação atual do 
                # jogo, permitindo que ela seja recuperada na 
                # próxima execução do jogo.
        db['pontuacao'] = pontuacao
        
        # Armazena o valor da variável global 'indice_palavra' no 
                # banco de dados sob a chave 'indice_palavra'.
        # Isso salva a posição atual da lista de palavras, permitindo 
                # que o jogo continue do ponto onde parou na próxima sessão.
        db['indice_palavra'] = indice_palavra



# Cria uma nova instância da classe Tk, que serve como a janela 
        # principal para a aplicação do jogo da forca.
janela = tk.Tk()

# Define o título da janela principal, que aparecerá na 
        # barra de título da janela.
# 'Jogo da Forca' é o nome dado à janela, ajudando o 
        # usuário a identificar o conteúdo da aplicação.
janela.title('Jogo da Forca')

# Cria um widget de texto (Label) dentro da janela principal. 
# Este label mostra a pontuação atual do jogador.
# O texto inicial é formatado para incluir a pontuação atual, 
        # que é passada como argumento na função format.
# O parâmetro 'font=('Arial', 16)' define a fonte e o tamanho 
        # do texto, escolhendo Arial tamanho 16 para uma boa legibilidade.
lbl_pontuacao = tk.Label(janela, 
                         text='Pontuação: {}'.format(pontuacao), 
                         font=('Arial', 16))

# O método 'pack' é usado para adicionar o label à janela 
        # principal. 
# O parâmetro 'pady=10' adiciona um espaçamento vertical de 10 pixels 
        # acima e abaixo do label, ajudando a separar visualmente 
        # este elemento de outros na interface.
lbl_pontuacao.pack(pady=10)

# Cria um Canvas, que é um widget usado para desenhar gráficos 
        # como linhas, formas ou imagens.
# Aqui, o canvas é configurado com uma largura de 300 pixels e 
        # uma altura de 300 pixels, proporcionando espaço suficiente
        # para desenhar a forca e o boneco conforme o jogo progride.
canvas = tk.Canvas(janela, 
                   width=300, 
                   height=300)

# O método 'pack' é usado novamente para adicionar o canvas à 
        # janela principal. Sem parâmetros adicionais, o canvas
        # será centralizado dentro da janela.
canvas.pack()

# Cria um widget de texto (Label) para mostrar a 
        # palavra secreta no jogo.
# Inicialmente, o texto do label está vazio (''), pois a 
        # palavra ainda não foi escolhida ou está oculta.
# A fonte é definida como Arial tamanho 24, o que facilita a 
        # leitura e destaca a palavra no layout do jogo.
lbl_palavra = tk.Label(janela, 
                       text='', 
                       font=('Arial', 24))

# O método 'pack' adiciona o label ao layout da 
        # janela principal. 
# O parâmetro 'pady=10' adiciona um espaçamento 
        # vertical de 10 pixels acima e abaixo do label, 
        # proporcionando um visual limpo e separado dos 
        # outros elementos da interface.
lbl_palavra.pack(pady=10)

# Cria um Frame dentro da janela principal. 
# Um Frame é um contêiner que pode agrupar outros widgets, 
        # como botões, dentro de uma área definida da interface.
# Neste caso, ele é usado para conter todos os botões do 
        # alfabeto usados para adivinhar a palavra secreta.
frame_botoes = tk.Frame(janela)

# O método 'pack' é usado para adicionar o frame à 
        # janela principal.
# Sem parâmetros adicionais de layout, o frame é adicionado 
        # na posição padrão, que é centralizada na janela.
frame_botoes.pack()

# Cria um botão para permitir ao usuário reiniciar o 
        # jogo a qualquer momento.
# O texto no botão é 'Reiniciar Jogo', e a função 
        # 'reiniciar_jogo' é chamada quando o botão é clicado.
# Esta função é responsável por reiniciar todas as variáveis e
        # preparar o jogo para uma nova rodada.
btn_reiniciar = tk.Button(janela, 
                          text='Reiniciar Jogo', 
                          command=reiniciar_jogo)

# O método 'pack' adiciona o botão ao layout da janela principal.
# O parâmetro 'pady=10' garante um espaçamento vertical 
        # de 10 pixels acima e abaixo do botão, ajudando a 
        # separá-lo visualmente de outros elementos.
btn_reiniciar.pack(pady=10)

# Inicializa o jogo escolhendo uma palavra secreta do 
        # conjunto predefinido de palavras.
# A função 'escolher_palavra_secreta' seleciona aleatoriamente 
        # uma palavra da lista ou segue a sequência especificada.
# Esta função também prepara a lista de 'letras_descobertas' 
        # com underscores correspondendo a cada letra da palavra secreta.
escolher_palavra_secreta()

# Atualiza a exibição da palavra secreta na interface do usuário.
# A função 'atualizar_palavra_secreta' configura o texto do 
        # label 'lbl_palavra' para mostrar a palavra secreta com
        # letras ainda não descobertas representadas por underscores.
atualizar_palavra_secreta()

# Cria os botões para cada letra do alfabeto.
# A função 'criar_botoes_alfabeto' organiza os botões 
        # alfabeticamente em três linhas, permitindo ao usuário 
        # clicar em cada letra para tentar adivinhar a palavra.
criar_botoes_alfabeto()

# Desenha a estrutura inicial da forca no canvas.
# A função 'desenhar_forca' adiciona a base da forca no 
        # canvas, preparando-o para o jogo.
# Esta função não desenha o boneco ainda, pois não houve 
        # erros cometidos pelo jogador.
desenhar_forca()

# Inicia o loop principal da interface gráfica.
janela.mainloop()