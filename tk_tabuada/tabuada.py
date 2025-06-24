# Importa o módulo tkinter e renomeia para 'tk'. Tkinter é 
        # a biblioteca padrão de interface gráfica do Python.
import tkinter as tk

# Importa o módulo messagebox de tkinter. Usado para mostrar 
        # janelas de mensagem (alertas, erros, informações) ao usuário.
from tkinter import messagebox


# Define a função gerar_tabuada que é responsável por 
        # criar a tabuada de um número dado.
def gerar_tabuada():

    # Recupera o texto do campo de entrada 'entrada_numero' e 
            # remove espaços em branco desnecessários.
    numero = entrada_numero.get().strip()

    # Verifica se o campo de entrada está vazio após a 
            # remoção de espaços.
    if not numero:
        
        # Se estiver vazio, exibe uma mensagem de aviso 
                # informando o usuário que ele precisa inserir um número.
        messagebox.showwarning("Aviso", "Por favor, insira um número.")
        
        # Interrompe a execução da função para que não 
                # continue com a entrada vazia.
        return

    try:
        
        # Tenta converter o texto recuperado para um número inteiro.
        numero = int(numero)
        
    except ValueError:
        
        # Se a conversão falhar, captura a exceção ValueError. 
        # Isso ocorre quando o texto não pode ser convertido 
                # para inteiro (por exemplo, se contiver letras 
                # ou caracteres especiais).
        # Exibe uma mensagem de erro informando o usuário que ele 
                # precisa inserir um número inteiro válido.
        messagebox.showerror("Erro", "Por favor, insira um número inteiro válido.")
        
        # Interrompe a execução da função, pois sem um número 
                # inteiro válido, a tabuada não pode ser gerada.
        return


    # Cria uma lista vazia para armazenar os resultados da tabuada.
    resultados = []
    
    # Loop que percorre os números de 1 a 10 para gerar a 
            # tabuada do número inserido.
    for i in range(1, 11):
        
        # Calcula o resultado da multiplicação do número 
                # fornecido pelo usuário por 'i'.
        resultado = numero * i
        
        # Adiciona uma string formatada com o cálculo e o 
                # resultado à lista de resultados.
        # Formata a string para mostrar o cálculo de forma 
                # clara, por exemplo, "5 x 1 = 5".
        resultados.append(f"{numero} x {i} = {resultado}")
    
    # Antes de inserir os novos resultados, limpa todo o 
            # conteúdo anterior do widget Text 'texto_resultados'.
    # O argumento "1.0" indica o início do texto (linha 1, coluna 0) 
            # e tk.END indica o fim do texto no widget.
    texto_resultados.delete("1.0", tk.END)
    
    # Insere todos os resultados da tabuada no widget Text, 
            # unindo-os em uma única string com quebras de 
            # linha entre cada resultado.
    # O método 'join' concatena cada elemento da lista 
            # 'resultados' com uma quebra de linha ("\n") entre eles.
    # Insere o texto concatenado no final do conteúdo atual 
            # do widget Text, embora o texto já tenha 
            # sido limpo anteriormente.
    texto_resultados.insert(tk.END, "\n".join(resultados))

       

# Configuração da janela principal
# Cria a janela principal para a aplicação usando a 
        # classe Tk do Tkinter.
janela_principal = tk.Tk()

# Define o título da janela que aparecerá na barra de 
        # título do sistema operacional.
janela_principal.title("Exercício Tabuada")

# Configura a cor de fundo da janela para branco. 
        # Essa propriedade define a cor padrão para todos os 
        # componentes da janela que não especificarem uma cor de fundo.
janela_principal.configure(bg="white")

# Centralizar a janela na tela do usuário
# Determina a largura da janela que será criada, 
        # neste caso, 300 pixels.
largura_janela = 300

# Determina a altura da janela que será criada, 
        # neste caso, 400 pixels.
altura_janela = 400

# Obtém a largura total da tela do dispositivo onde a 
        # aplicação está sendo executada. Essa informação é 
        # usada para ajudar a centralizar a janela.
largura_tela = janela_principal.winfo_screenwidth()

# Obtém a altura total da tela do dispositivo onde a 
        # aplicação está sendo executada. Essa informação é 
        # usada para ajudar a centralizar a janela.
altura_tela = janela_principal.winfo_screenheight()

# Calcula a posição horizontal (X) para a janela, de 
        # modo que ela fique centralizada na tela. 
# A posição é determinada subtraindo metade da largura da 
        # janela de metade da largura total da tela.
posicao_x = (largura_tela // 2) - (largura_janela // 2)

# Calcula a posição vertical (Y) para a janela, de modo 
        # que ela fique centralizada na tela. 
# A posição é determinada subtraindo metade da altura da 
        # janela de metade da altura total da tela.
posicao_y = (altura_tela // 2) - (altura_janela // 2)

# Define a geometria da janela principal com as dimensões 
        # especificadas e as coordenadas calculadas para centralização.
# O formato é "largura x altura + X + Y", que especifica a 
        # largura, a altura, e as posições horizontal e 
        # vertical da janela na tela.
janela_principal.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")


# Frame para a entrada de dados
# Cria um frame dentro da janela principal para organizar os 
        # widgets de entrada de dados de forma estruturada.
# O frame age como um contêiner para agrupar elementos 
        # relacionados, mantendo a interface limpa e organizada.
frame_entrada = tk.Frame(janela_principal, bg="white")

# Configura o frame com uma cor de fundo branca para manter a 
        # consistência visual com o resto da interface.
# Usa o método 'pack' para posicionar o frame dentro 
        # da janela principal.
# O parâmetro 'pady=10' adiciona um espaçamento vertical 
        # de 10 pixels acima e abaixo do frame, separando-o 
        # dos outros componentes da interface.
frame_entrada.pack(pady=10)

# Número a ser inserido
# Cria um rótulo (label) dentro do frame de entrada, que 
        # serve como um indicador para o usuário sobre qual 
        # dado deve ser inserido no campo de entrada.
label_numero = tk.Label(frame_entrada, text="Número:", bg="white", font=('Helvetica', 12))

# Configura o rótulo com o texto "Número:", uma cor de fundo 
        # branca, e a fonte Helvetica de tamanho 12 para boa legibilidade.
# Usa o método 'grid' para posicionar o rótulo dentro 
        # do frame de entrada.
# O rótulo é colocado na primeira linha (row=0) e na 
        # primeira coluna (column=0) do grid.
# O parâmetro 'padx=5' adiciona um espaçamento horizontal 
        # de 5 pixels à esquerda e à direita do rótulo, 
        # e 'pady=5' adiciona um espaçamento vertical 
        # de 5 pixels acima e abaixo do rótulo.
label_numero.grid(row=0, column=0, padx=5, pady=5)

# Cria um campo de entrada para que o usuário possa 
        # digitar o número cujo resultado da tabuada 
        # será calculado.
entrada_numero = tk.Entry(frame_entrada, width=20, font=('Helvetica', 12))

# Configura o campo de entrada com uma largura de 20 
        # caracteres, o que determina a quantidade de 
        # texto visível no campo.
# A fonte é configurada para Helvetica de tamanho 12 para 
        # manter a consistência com o rótulo e garantir 
        # boa legibilidade.
# Usa o método 'grid' para posicionar o campo de entrada 
        # ao lado do rótulo correspondente, na primeira 
        # linha (row=0) e na segunda coluna (column=1).
# Os parâmetros 'padx=5' e 'pady=5' adicionam espaçamento 
        # horizontal e vertical ao redor do campo de 
        # entrada, semelhante ao rótulo.
entrada_numero.grid(row=0, column=1, padx=5, pady=5)


# Botão para gerar a tabuada
# Cria um botão na janela principal que, quando 
        # clicado, chama a função 'gerar_tabuada'.
# O botão permite ao usuário solicitar a geração da 
        # tabuada para o número inserido.
botao_gerar = tk.Button(janela_principal, 
                        text="Gerar Tabuada", 
                        command=gerar_tabuada, 
                        font=('Helvetica', 12))

# Configura o texto do botão para "Gerar Tabuada", 
        # especifica a função a ser chamada quando o botão é clicado,
        # e define a fonte como Helvetica de tamanho 12 para 
        # consistência e legibilidade.

# Usa o método 'pack' para adicionar o botão à janela 
        # principal com um espaçamento vertical (pady) de 10 pixels,
        # o que separa o botão de outros elementos da 
        # interface e proporciona um layout mais limpo.
botao_gerar.pack(pady=10)

# Texto para exibir a tabuada
# Cria um widget Text na janela principal, que é 
        # usado para exibir a tabuada gerada.
# O widget Text permite a exibição de múltiplas 
        # linhas de texto, ideal para mostrar a 
        # lista de multiplicações.
texto_resultados = tk.Text(janela_principal, 
                           width=25, 
                           height=10, 
                           font=('Helvetica', 12))

# Configura o widget Text com uma largura de 25 
        # caracteres e uma altura de 10 linhas,
# o que define o tamanho do campo de texto visível na janela.
# Define a fonte do texto como Helvetica de 
        # tamanho 12 para manter a legibilidade e a 
        # consistência visual com outros elementos.

# Usa o método 'pack' para adicionar o widget Text à 
        # janela principal com um espaçamento 
        # vertical (pady) de 10 pixels,
# garantindo que o campo de texto esteja bem separado dos 
        # outros elementos e fácil de visualizar.
texto_resultados.pack(pady=10)

# Inicia o loop principal da interface gráfica, que 
        # mantém a janela aberta e responsiva a 
        # interações do usuário.
# Esse loop aguarda eventos, como cliques de botão ou 
        # entradas de texto, e atualiza a 
        # interface de acordo.
janela_principal.mainloop()