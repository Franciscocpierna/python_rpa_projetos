# Importa o módulo tkinter e dá a ele o nome de tk, facilitando
        # as chamadas futuras a este módulo.
import tkinter as tk

# Importa o componente messagebox do módulo tkinter, que é 
        # usado para exibir caixas de diálogo de alerta e erro.
from tkinter import messagebox


# Define uma função chamada texto_para_binario, que 
        # aceita um argumento 'texto'.
def texto_para_binario(texto):
    
    # A função retorna uma string. Vamos analisar a 
            # expressão dentro do return:
    # 1. ' '.join(...) - Junta elementos de uma lista em
            # uma string, separando-os com espaço.
    # 2. format(ord(char), '08b') for char in texto - Este é um 
            # gerador que itera sobre cada caractere no texto.
    #    a. ord(char) - Converte o caractere para seu 
            # equivalente numérico ASCII.
    #    b. format(..., '08b') - Formata o número ASCII para uma 
            # representação binária de 8 bits.
    # O resultado é uma sequência de números binários separados 
            # por espaços, representando o texto original.
    return ' '.join(format(ord(char), '08b') for char in texto)



# Define a função binario_para_texto que aceita um argumento 'binario'.
def binario_para_texto(binario):
    
    # Tenta executar o bloco de código dentro do 'try'.
    try:
        
        # 1. binario.split(' ') - Divide a string 'binario' em 
                # uma lista de strings cada vez que encontra um espaço.
        # 2. int(b, 2) - Converte cada elemento 'b' da lista (um 
                # número binário em forma de string) para um número decimal.
        # 3. chr(...) - Converte o número decimal para o 
                # caractere ASCII correspondente.
        # 4. ''.join(...) - Junta todos os caracteres ASCII para 
                # formar uma string de texto.
        # A variável 'texto' recebe o resultado do processo de 
                # junção desses caracteres.
        texto = ''.join(chr(int(b, 2)) for b in binario.split(' '))
        
        # Retorna a string de texto convertida.
        return texto
        
    # Se ocorrer um erro de valor durante a tentativa de 
            # conversão (por exemplo, se a string binária for inválida),
    # o código dentro do bloco 'except' será executado.
    except ValueError:
        
        # Mostra uma mensagem de erro ao usuário usando uma caixa de 
                # diálogo, indicando que o código binário é inválido.
        messagebox.showerror("Erro", "Código binário inválido.")
        
        # Retorna uma string vazia, indicando que a conversão falhou.
        return ""


# Define a função 'converter_para_binario', que não aceita 
                # nenhum argumento.
def converter_para_binario():
    
    # Recupera o texto do widget de entrada 'entrada_texto'. 
            # O método .get("1.0", tk.END) obtém todo o texto
    # desde a linha 1, coluna 0 até o fim do widget de texto. 
            # O método .strip() remove espaços em branco extras no início e no fim.
    texto = entrada_texto.get("1.0", tk.END).strip()
    
    # Verifica se a variável 'texto' está vazia, o que significaria 
            # que não há texto para converter.
    if not texto:
        
        # Mostra uma mensagem de aviso ao usuário pedindo para 
                # inserir algum texto para conversão.
        messagebox.showwarning("Aviso", "Por favor, insira algum texto para converter.")
        
        # Sai da função retornando None, já que não há texto para processar.
        return
    
    # Chama a função 'texto_para_binario' passando o 'texto' como 
            # argumento. Esta função é definida
    # em outra parte do código e é responsável por converter o 
            # texto em uma string binária.
    resultado_binario = texto_para_binario(texto)
    
    # Limpa o widget de texto 'saida_texto', que é usado para 
            # mostrar o resultado. O método .delete("1.0", tk.END)
    # remove todo o texto desde a linha 1, coluna 0 até o fim do widget.
    saida_texto.delete("1.0", tk.END)
    
    # Insere o 'resultado_binario' no widget 'saida_texto'. 
            # O método .insert(tk.END, resultado_binario)
    # adiciona o texto ao fim do widget, mostrando o resultado 
            # da conversão para o usuário.
    saida_texto.insert(tk.END, resultado_binario)

    

# Define a função 'converter_para_texto', que é projetada 
            # para converter código binário em texto.
def converter_para_texto():
    
    # Recupera o texto do widget de entrada chamado 'entrada_texto'.
    # O método .get("1.0", tk.END) obtém todo o texto desde a 
            # linha 1, coluna 0 até o final do widget.
    # O método .strip() é usado para remover espaços em branco no 
            # início e no fim da string recuperada.
    binario = entrada_texto.get("1.0", tk.END).strip()
    
    # Verifica se a string 'binario' está vazia. Isso é feito para 
            # garantir que não se tente converter uma string vazia,
            # o que causaria um erro ou resultaria em saída inútil.
    if not binario:
        
        # Mostra uma caixa de diálogo de aviso ao usuário pedindo 
                # que insira algum código binário para conversão.
        messagebox.showwarning("Aviso", "Por favor, insira algum código binário para converter.")
        
        # Sai da função sem fazer mais nada, pois não há 
                # dados para processar.
        return
    
    # Chama a função 'binario_para_texto', passando a 
            # string 'binario' como argumento.
    # Esta função tenta converter a string binária de volta para 
            # texto, manipulando-a conforme definido anteriormente.
    resultado_texto = binario_para_texto(binario)
    
    # Limpa o widget de texto 'saida_texto', que é usado para 
            # exibir o resultado da conversão.
    # O método .delete("1.0", tk.END) remove todo o texto desde a 
            # linha 1, coluna 0 até o final do widget.
    saida_texto.delete("1.0", tk.END)
    
    # Insere o texto convertido (resultado_texto) no widget 'saida_texto'.
    # O método .insert(tk.END, resultado_texto) adiciona o 
            # texto convertido ao final do widget,
            # permitindo que o usuário veja o resultado da conversão.
    saida_texto.insert(tk.END, resultado_texto)    


# Define a função 'mostrar_regras' que exibe as regras de 
            # conversão de texto para binário e vice-versa.
def mostrar_regras():
    
    # Cria uma nova janela de nível superior que aparece acima da 
            # janela principal. 'janela_principal' deve ser a 
            # janela já criada anteriormente.
    regras_janela = tk.Toplevel(janela_principal)
    
    # Define o título da nova janela.
    regras_janela.title("Regras da Conversão")
    
    # Configura a cor de fundo da janela para branco.
    regras_janela.configure(bg="white")
    
    # Define a largura e a altura da janela de regras.
    largura_janela_regras = 600
    altura_janela_regras = 300
    
    # Obtém a largura e a altura da tela do dispositivo onde a 
            # janela está sendo exibida.
    # Isso inclui a resolução total da tela em que o programa 
            # está rodando, como 1920x1080 pixels.
    largura_tela_regras = regras_janela.winfo_screenwidth()
    altura_tela_regras = regras_janela.winfo_screenheight()
    
    # Calcula a posição x (horizontal) para centralizar a janela na tela.
    # Para isso, subtrai metade da largura da janela das regras da 
            # metade da largura total da tela.
    # Isso resulta em um valor que, quando usado como coordenada X, 
            # posiciona a janela exatamente no centro da tela horizontalmente.
    posicao_x_regras = (largura_tela_regras // 2) - (largura_janela_regras // 2)
    
    # Calcula a posição y (vertical) de maneira similar à posição x.
    # Subtrai metade da altura da janela das regras da metade da altura total da tela.
    # Esse cálculo assegura que a janela seja centralizada verticalmente na tela.
    posicao_y_regras = (altura_tela_regras // 2) - (altura_janela_regras // 2)
    
    # Configura a geometria da janela com as dimensões e posições 
            # calculadas, formatadas como uma string.
    # A string de geometria define a largura e a altura da 
            # janela, bem como sua posição na tela.
    # O formato geral é "largura x altura + posX + posY", onde posX e posY 
            # são as coordenadas para o canto superior esquerdo da janela.
    regras_janela.geometry(f"{largura_janela_regras}x{altura_janela_regras}+{posicao_x_regras}+{posicao_y_regras}")


    # Define o texto que explica as regras de conversão, dividido em 
            # duas partes para texto para binário e binário para texto.
    texto_regras = (
        "Conversão de Texto para Código Binário:\n"
        "1. Cada caractere é convertido para seu código ASCII.\n"
        "2. O código ASCII é então convertido para uma representação binária de 8 bits.\n"
        "3. Todos os bits são agrupados com espaços entre eles.\n\n"
        "Conversão de Código Binário para Texto:\n"
        "1. O código binário é dividido em grupos de 8 bits.\n"
        "2. Cada grupo de 8 bits é convertido para um número decimal (código ASCII).\n"
        "3. O código ASCII é convertido para o caractere correspondente."
    )

    # Cria um rótulo (label) na janela de regras, que exibe o texto das regras.
    # O rótulo é um componente visual que exibe texto ou imagens. 
            # Neste caso, é usado para mostrar as instruções de conversão.
    label_regras = tk.Label(regras_janela,  # especifica que o rótulo deve ser colocado na janela 'regras_janela'.
        text=texto_regras,  # define o texto a ser exibido no rótulo. 'texto_regras' contém as instruções detalhadas.
        justify="left",  # alinha o texto à esquerda do rótulo para melhor leitura, já que o texto é formatado em várias linhas.
        bg="white",  # define a cor de fundo do rótulo como branco, o que ajuda na leitura ao fornecer contraste.
        padx=10,  # adiciona um preenchimento horizontal interno de 10 pixels. Isso evita que o texto toque nas bordas horizontais do rótulo.
        pady=10,  # adiciona um preenchimento vertical interno de 10 pixels, evitando que o texto toque nas bordas verticais do rótulo.
        font=('Helvetica', 12)  # define a fonte do texto como 'Helvetica' tamanho 12, que é uma fonte limpa e fácil de ler.
    )
    
    # Adiciona o rótulo à janela de regras, preenchendo todo o espaço 
            # disponível e permitindo que ele expanda, se necessário.
    # O método 'pack' é usado para gerenciar o layout do rótulo 
            # dentro da janela 'regras_janela'.
    label_regras.pack(

        # indica que o rótulo deve expandir para preencher todo o
                # espaço disponível na direção X (horizontal) e Y (vertical).
        fill="both",  

        # permite que o rótulo expanda para ocupar qualquer espaço adicional
                # na janela, garantindo que as regras sejam claramente visíveis.
        expand=True  
        
    )
    

# Configuração da janela principal
# Cria uma nova janela Tkinter. A variável 'janela_principal' 
        # representa a janela principal da aplicação.
janela_principal = tk.Tk()

# Define o título da janela, que aparece na barra de título da 
        # janela. Neste caso, o título é "Conversor de Código Binário".
janela_principal.title("Conversor de Código Binário")

# Configura a cor de fundo da janela principal como branco. 
        # Isso define a cor de fundo para todos os componentes da janela,
        # a menos que especificado de outra forma em cada componente individual.
janela_principal.configure(bg="white")

# Centralizar a janela
# Define a largura e a altura da janela principal em pixels.
largura_janela = 600
altura_janela = 400

# Obtém a largura e a altura da tela do dispositivo onde a 
        # janela está sendo exibida. 
# Isso é útil para posicionar a janela corretamente no centro da tela.
largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()

# Calcula a posição x (horizontal) para centralizar a janela na tela.
# A posição x é determinada subtraindo metade da largura da 
        # janela da metade da largura total da tela.
posicao_x = (largura_tela // 2) - (largura_janela // 2)

# Calcula a posição y (vertical) para centralizar a janela na tela.
# A posição y é calculada subtraindo metade da altura da 
        # janela da metade da altura total da tela.
posicao_y = (altura_tela // 2) - (altura_janela // 2)

# Configura a geometria da janela, especificando sua 
        # largura, altura e posições x e y calculadas.
# O formato da string é "largura x altura + posX + posY", onde 
        # posX e posY são as coordenadas do canto superior esquerdo da janela.
janela_principal.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")


# Frame para a entrada de texto
# Cria um frame dentro da janela principal para agrupar 
        # elementos relacionados à entrada de texto.
# Um frame é um contêiner que ajuda a organizar e agrupar 
        # widgets visualmente na interface.
frame_entrada = tk.Frame(janela_principal, 
                         bg="white")  # Define a cor de fundo do frame como branco.

# Adiciona o frame à janela principal com um espaçamento
        # vertical de 10 pixels.
frame_entrada.pack(pady=10)  

# Cria um rótulo (label) dentro do frame de entrada, que 
        # serve para indicar ao usuário onde inserir o texto ou o código binário.
label_entrada = tk.Label(frame_entrada, 
                         text="Texto ou Código Binário:", 
                         bg="white", 
                         font=('Helvetica', 12))

# Define a cor de fundo do label como branco e usa a 
        # fonte Helvetica tamanho 12 para o texto.
label_entrada.pack()  # Adiciona o label ao frame de entrada.

# Cria uma área de texto (widget Text) dentro do frame de 
        # entrada, permitindo ao usuário inserir múltiplas linhas de texto.
entrada_texto = tk.Text(frame_entrada, 
                        height=8, 
                        width=70, 
                        font=('Helvetica', 12))

# Define a altura do widget para 8 linhas, largura para 70 
        # colunas e usa a fonte Helvetica tamanho 12.

# Adiciona a área de texto ao frame com um espaçamento
        # vertical de 5 pixels.
entrada_texto.pack(pady=5)  

# Frame para os botões de conversão
# Cria outro frame dentro da janela principal para 
        # agrupar os botões de conversão.
frame_botoes = tk.Frame(janela_principal, 
                        bg="white")  # Define a cor de fundo do frame como branco.

# Adiciona o frame à janela principal com um espaçamento
        # vertical de 10 pixels.
frame_botoes.pack(pady=10)  


# Cria um botão dentro do frame 'frame_botoes'. Este botão é 
        # para converter o texto inserido em código binário.
botao_para_binario = tk.Button(

    # Indica que o botão deve ser colocado no frame destinado aos botões.
    frame_botoes,  

    # Define o texto que aparecerá no botão.
    text="Converter para Binário",  

    # Associa este botão à função 'converter_para_binario', que é
            # chamada quando o botão é clicado.
    command=converter_para_binario,  

    # Define a fonte e o tamanho do texto no botão.
    font=('Helvetica', 12)  
    
)

# Posiciona o botão no layout do frame usando o 
        # gerenciador de layout 'grid'.
# 'row=0' e 'column=0' posicionam o botão na primeira 
        # linha e primeira coluna do grid.
# 'padx=10' adiciona um espaçamento horizontal de 10 pixels ao 
        # redor do botão para evitar que fique muito
        # próximo de outros elementos.
botao_para_binario.grid(row=0, column=0, padx=10)

# Cria outro botão no mesmo frame para converter 
        # código binário de volta para texto.
botao_para_texto = tk.Button(
    frame_botoes,
    text="Converter para Texto",  # Texto do botão.
    command=converter_para_texto,  # Associa este botão à função 'converter_para_texto'.
    font=('Helvetica', 12)
)

# Posiciona este botão ao lado do primeiro, na 
        # mesma linha mas na segunda coluna.
botao_para_texto.grid(row=0, column=1, padx=10)

# Cria um terceiro botão no frame para mostrar as 
        # regras da conversão de texto para binário e vice-versa.
botao_regras = tk.Button(
    frame_botoes,
    text="Regras",  # Texto do botão.
    command=mostrar_regras,  # Associa este botão à função 'mostrar_regras'.
    font=('Helvetica', 12)
)

# Posiciona este botão na terceira coluna, mantendo-o na 
        # mesma linha que os outros botões.
botao_regras.grid(row=0, column=2, padx=10)


# Frame para a saída de texto
# Cria um frame dentro da janela principal destinado a 
        # mostrar o resultado das conversões.
# Especifica que este frame é um filho da janela principal.
frame_saida = tk.Frame(janela_principal, 

                       # Define a cor de fundo do frame como branca para
                               # manter a consistência visual da interface.
                       bg="white")  

# Adiciona o frame à janela principal com um espaçamento
        # vertical de 10 pixels entre este frame e outros componentes.
frame_saida.pack(pady=10)  

# Cria um rótulo (label) dentro do frame de saída que 
        # serve para identificar onde o resultado será exibido.
label_saida = tk.Label(frame_saida,  

                       # Especifica que o label está dentro do frame de saída.
                       text="Resultado:",  # Define o texto do label.

                       # Define a cor de fundo do label como branca.
                       bg="white",  

                       # Define a fonte e o tamanho do texto para manter a legibilidade e consistência.
                       font=('Helvetica', 12))  

# Adiciona o label ao frame de saída.
label_saida.pack()  

# Cria uma área de texto dentro do frame de saída para 
        # exibir os resultados das conversões.

# Especifica que este widget de texto está dentro do frame de saída.
saida_texto = tk.Text(frame_saida,  

                      # Define a altura do widget de texto para 8 linhas.
                      height=8,  

                      # Define a largura do widget de texto para 70 colunas.
                      width=70,  

                      # Define a fonte e o tamanho do texto para manter a legibilidade.
                      font=('Helvetica', 12))  

# Adiciona a área de texto ao frame com um espaçamento vertical de 5 pixels.
saida_texto.pack(pady=5)  

# Inicia o loop principal da interface gráfica.
# Esta chamada faz com que a janela principal fique 
        # visível e responsiva a eventos, como cliques em botões.
# O loop continua até que a janela seja fechada pelo usuário.
janela_principal.mainloop()