# Importa o módulo tkinter como 'tk'. Tkinter é 
        # uma biblioteca padrão do Python para criar 
        # interfaces gráficas de usuário (GUI).
import tkinter as tk

# Importa o módulo messagebox do tkinter. É usado para exibir 
        # caixas de diálogo que podem mostrar erro, 
        # alerta ou informações ao usuário.
from tkinter import messagebox

# Importa o módulo random. Este módulo contém funções 
        # que permitem a geração de números aleatórios.
import random

# Importa o módulo time. Este módulo fornece várias funções 
        # relacionadas ao tempo, como pausar a execução de um programa.
import time


# Define a função sortear_numero que é chamada quando o 
        # usuário clica no botão para sortear um número.
def sortear_numero():
    
    try:
        
        # Tenta obter os números de entrada dos campos de 
                # texto. Estes são os limites entre os 
                # quais o número será sorteado.
        # Converte o texto do campo de entrada 'entrada_inicio' 
                # para um inteiro.
        inicio = int(entrada_inicio.get())

        # Converte o texto do campo de entrada 'entrada_fim' 
                # para um inteiro.
        fim = int(entrada_fim.get())
        
        # Verifica se o valor inicial é maior que o valor 
                # final, o que seria um erro lógico para o sorteio.
        if inicio > fim:
            
            # Se o número inicial for maior, levanta uma 
                    # exceção ValueError com uma mensagem explicativa.
            raise ValueError("O número inicial deve ser menor ou igual ao número final")
        
        # Desativa o botão de sorteio e os campos de entrada 
                # para evitar mudanças enquanto o sorteio 
                # está em andamento.
        # Isso previne que o usuário altere os inputs ou 
                # inicie um novo sorteio antes do atual ser concluído.
        # Muda o estado do botão para DISABLED, 
                # tornando-o inativo.
        botao_sortear.config(state=tk.DISABLED)

        # Muda o estado do campo de entrada do número 
                # inicial para DISABLED.
        entrada_inicio.config(state=tk.DISABLED)

        # Muda o estado do campo de entrada do número 
                # final para DISABLED.
        entrada_fim.config(state=tk.DISABLED)

        
        # Inicia um loop que conta regressivamente de 5 até 1, 
                # utilizado para criar uma tensão antes do 
                # resultado do sorteio ser revelado.
        for i in range(5, 0, -1):
            
            # Configura o texto do rótulo 'label_resultado' para 
                    # informar ao usuário que o sorteio está 
                    # acontecendo em 'i' segundos.
            label_resultado.config(text=f"Sorteando em {i}...")
            
            # Força a janela principal a processar todos os eventos 
                    # pendentes na fila de eventos, garantindo que a 
                    # interface seja atualizada imediatamente.
            janela_principal.update()
            
            # Pausa a execução do código por 1 segundo, criando um 
                    # efeito de suspense enquanto o número ainda não é sorteado.
            time.sleep(1)
        
        # Após a contagem regressiva, sorteia um número aleatoriamente 
                # dentro do intervalo especificado pelos valores 'inicio' e 'fim'.
        numero_sorteado = random.randint(inicio, fim)

        # Atualiza o rótulo 'label_resultado' para mostrar o 
                # número que foi sorteado.
        label_resultado.config(text=f"Número Sorteado: {numero_sorteado}")
        
    # Bloco para tratamento de exceções específicas.
    except ValueError as ve:

        # Exibe uma mensagem de erro caso haja um ValueError, 
                # relacionado a problemas com a conversão de 
                # tipos ou lógica de validação.
        messagebox.showerror("Erro", f"Entrada inválida: {ve}")
    
    except Exception as e:
        
        # Captura qualquer outra exceção não especificada 
                # anteriormente e exibe uma mensagem de erro genérica.
        messagebox.showerror("Erro", f"Erro inesperado: {e}")
    
    finally:
        
        # O bloco finally é executado após a tentativa de execução 
                # dos blocos try e except, independentemente de uma 
                # exceção ter sido levantada ou não.
        # Reativa o botão de sorteio e os campos de entrada, 
                # permitindo que o usuário faça um novo sorteio.
        # Muda o estado do botão para NORMAL, tornando-o ativo novamente.
        botao_sortear.config(state=tk.NORMAL)

        # Muda o estado do campo de entrada do número 
                # inicial para NORMAL.
        entrada_inicio.config(state=tk.NORMAL)

        # Muda o estado do campo de entrada do número 
                # final para NORMAL.
        entrada_fim.config(state=tk.NORMAL)


# Configuração da janela principal
# Cria uma nova instância de Tk, que é a janela 
        # principal da aplicação de interface gráfica.
janela_principal = tk.Tk()

# Define o título da janela principal, que aparecerá na 
        # barra de título da janela.
janela_principal.title("Sorteador de Número")

# Configura a cor de fundo da janela para branco. 
        # Essa configuração será aplicada a todo o 
        # espaço da janela principal,
        # criando um fundo uniforme e claro.
janela_principal.configure(bg="white")

# Centralizar a janela
# Define a largura desejada para a janela principal da 
        # aplicação em pixels. Aqui, a largura é 
        # definida como 400 pixels.
largura_janela = 400

# Define a altura desejada para a janela principal da 
        # aplicação em pixels. Aqui, a altura é 
        # definida como 300 pixels.
altura_janela = 300

# Utiliza um método de 'janela_principal' para obter a 
        # largura total da tela do dispositivo onde a 
        # aplicação está sendo executada.
largura_tela = janela_principal.winfo_screenwidth()

# Utiliza um método de 'janela_principal' para obter a 
        # altura total da tela do dispositivo onde a 
        # aplicação está sendo executada.
altura_tela = janela_principal.winfo_screenheight()

# Calcula a posição horizontal (posição X) para a 
        # janela principal, de modo que ela fique 
        # centralizada na tela.
# O cálculo envolve subtrair metade da largura da 
        # janela da metade da largura da tela.
posicao_x = (largura_tela // 2) - (largura_janela // 2)

# Calcula a posição vertical (posição Y) para a janela 
        # principal, de modo que ela fique centralizada na tela.
# O cálculo envolve subtrair metade da altura da 
        # janela da metade da altura da tela.
posicao_y = (altura_tela // 2) - (altura_janela // 2)

# Define a geometria da janela principal usando as 
        # dimensões calculadas, especificando a largura, 
        # altura e as posições X e Y.
# O formato da string é "largura x altura + X + Y", o 
        # que determina a posição exata e o tamanho da 
        # janela na tela do usuário.
janela_principal.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")


# Frame para as entradas
# Cria um frame dentro da janela principal para organizar 
        # visualmente os campos de entrada. O frame serve 
        # como um contêiner para outros widgets.
frame_entradas = tk.Frame(janela_principal, bg="white")

# Configura a cor de fundo do frame como branca para manter a 
        # consistência com o design geral da interface.
# Utiliza o método 'pack' para adicionar o frame à janela 
        # principal. 'pady=20' adiciona um espaçamento 
        # vertical de 20 pixels acima e abaixo do frame,
        # ajudando a separar visualmente este frame de 
        # outros elementos ou seções da interface.
frame_entradas.pack(pady=20)

# Entrada para o número inicial
# Cria um rótulo dentro do frame_entradas para 
        # identificar claramente onde o usuário deve 
        # inserir o número inicial para o sorteio.
label_inicio = tk.Label(frame_entradas, 
                        text="Número Inicial:", 
                        bg="white", 
                        font=('Helvetica', 12))

# Configura o rótulo com um fundo branco e a fonte Helvetica 
        # de tamanho 12 para garantir legibilidade.
# Posiciona o rótulo usando o gerenciador de layout 'grid'. 
        # Este rótulo é colocado na primeira linha (row=0) e 
        # primeira coluna (column=0) do grid.
# 'padx=5' e 'pady=5' adicionam espaçamento horizontal e 
        # vertical de 5 pixels, respectivamente, ao redor do 
        # rótulo para um design arejado e acessível.
label_inicio.grid(row=0, column=0, padx=5, pady=5)

# Cria um campo de entrada no frame de entradas para 
        # que o usuário possa inserir o número inicial do sorteio.
entrada_inicio = tk.Entry(frame_entradas, 
                          
                          width=10,  # Define a largura do campo de 
                                              # entrada como 10 caracteres.
                                     # Isso determina quantos caracteres podem 
                                              # ser visíveis no campo ao mesmo tempo.
                                     # O valor de 10 é geralmente suficiente para a 
                                              # entrada de números típicos usados em sorteios.
                          
                          font=('Helvetica', 12))  # Configura a fonte do texto 
                                                            # dentro do campo de entrada.
                                                   # 'Helvetica' é uma fonte limpa e fácil de ler.
                                                   # O tamanho 12 da fonte é grande o 
                                                            # suficiente para uma leitura clara,
                                                   # mas não tão grande a ponto de o campo ocupar 
                                                            # espaço excessivo na interface.

# O widget Entry é adicionado ao 'frame_entradas', que é um container 
        # especificado para manter os elementos relacionados à 
        # entrada de dados.
# Isso mantém a interface organizada e facilita a gestão do 
        # layout e do estilo dos componentes relacionados.



# Configura o campo de entrada com uma largura suficiente para 
        # números típicos (10 caracteres) e usa a mesma fonte 
        # Helvetica tamanho 12 para consistência.
# Posiciona o campo de entrada na mesma linha do rótulo 
        # correspondente, na segunda coluna (column=1), 
        # usando 'grid' para alinhamento preciso.
# 'padx=5' e 'pady=5' mantêm o espaçamento uniforme ao 
        # redor do campo de entrada, como no rótulo.
entrada_inicio.grid(row=0, column=1, padx=5, pady=5)

# Entrada para o número final
# Cria um rótulo dentro do frame de entradas, identificando o 
        # campo onde o usuário deve inserir o número final 
        # para o intervalo de sorteio.
label_fim = tk.Label(frame_entradas, 
                     text="Número Final:", 
                     bg="white", 
                     font=('Helvetica', 12))

# Configura o rótulo com fundo branco e fonte Helvetica 
        # tamanho 12 para manter a consistência visual. 
        # Posiciona este rótulo na grid.
# O rótulo é posicionado na segunda linha (row=1) e na 
        # primeira coluna (column=0), com um espaçamento de 
        # 5 pixels (padx e pady) para margens adequadas.
label_fim.grid(row=1, column=0, padx=5, pady=5)

# Cria um campo de entrada para que o usuário possa 
        # digitar o número final do intervalo de sorteio.
entrada_fim = tk.Entry(frame_entradas, 
                       width=10, 
                       font=('Helvetica', 12))

# Define o tamanho e a fonte do campo de entrada, 
        # assegurando que ele seja visualmente 
        # compatível com o campo de entrada do número inicial.
# Posiciona o campo de entrada na segunda linha (row=1) e 
        # na segunda coluna (column=1), alinhado ao 
        # rótulo correspondente.
entrada_fim.grid(row=1, column=1, padx=5, pady=5)

# Botão para sortear o número
# Cria um botão na janela principal que, quando 
        # clicado, acionará a função 'sortear_numero'.
botao_sortear = tk.Button(janela_principal, 
                          text="Sortear Número", 
                          command=sortear_numero, 
                          font=('Helvetica', 12))

# Configura o botão com o texto, a função que será chamada ao 
        # clicar e a fonte usada. Empacota o botão com um 
        # espaçamento vertical (pady) de 20 pixels.
botao_sortear.pack(pady=20)

# Label para exibir o resultado
# Cria um rótulo na janela principal para exibir o resultado 
        # do sorteio. Inicialmente, o texto está vazio até 
        # que um número seja sorteado.
label_resultado = tk.Label(janela_principal, 
                           text="", 
                           bg="white", 
                           font=('Helvetica', 16))

# Configura o rótulo com um tamanho de fonte maior (16) para 
        # destacar o resultado e fundo branco para consistência 
        # com o resto da interface.
# Empacota o rótulo com um espaçamento vertical (pady) de 
        # 20 pixels, garantindo que o resultado seja 
        # facilmente visível para o usuário.
label_resultado.pack(pady=20)

# Inicia o loop principal da interface gráfica, que mantém a 
        # janela aberta e responde a interações do usuário, 
        # como cliques no botão.
janela_principal.mainloop()