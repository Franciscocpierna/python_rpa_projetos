# Importando a biblioteca tkinter e renomeando-a
        # para tk para simplificar seu uso
import tkinter as tk


# Função para destacar a célula, coluna e linha ao passar o mouse
def destacar_celula(event):
    
    # Inicia um loop que itera por todas as linhas da tabela (total de 10 linhas)
    for i in range(10):
        
        # Dentro de cada linha, inicia um loop que itera por todas as 
                # colunas (total de 5 colunas)
        for j in range(5):
            
            # Configura a célula na posição [i][j] da tabela para ter um 
                    # fundo branco (bg="white"),
            # texto preto (fg="black"), e usa a fonte Arial tamanho 10.
            # Essa configuração serve para "limpar" quaisquer destaques anteriores,
            # garantindo que as células voltem ao estado padrão antes de 
                    # aplicar novos destaques.
            tabela[i][j].config(bg="white", fg="black", font=("Arial", 10))


    # Obter a célula atual em que o mouse está posicionado.
    # 'event.widget' refere-se ao widget que disparou o evento, neste 
            # caso, a célula do mouse está sobre.
    # 'grid_info()' retorna um dicionário contendo informações sobre a 
            # posição do widget na grade.
    # 'row' e 'column' são chaves desse dicionário que contêm a linha e a 
            # coluna da célula, respectivamente.
    linha = event.widget.grid_info()['row']
    coluna = event.widget.grid_info()['column']

    # Destacar a célula atual com fundo amarelo e aumento de fonte.
    # 'tabela[linha][coluna].config' acessa a célula especificada e 
            # usa o método 'config' para alterar suas configurações.
    # 'bg="yellow"' configura o fundo da célula para amarelo.
    # 'fg="black"' mantém o texto na cor preta para garantir a legibilidade.
    # 'font=("Arial", 14, "bold")' altera a fonte para Arial, tamanho 14, e 
            # negrito, tornando o texto mais visível e destacado.
    tabela[linha][coluna].config(bg="yellow", 
                                 fg="black", 
                                 font=("Arial", 14, "bold"))


    # Destacar a linha inteira onde o mouse está.
    # Inicia um loop que percorre todas as colunas da linha 
            # atual (total de 5 colunas).
    for j in range(5):
        
        # Verifica se a coluna atual é diferente da coluna onde o mouse está.
        # Isso é feito para evitar que o destaque da célula específica em 
                # que o mouse está seja sobrescrito.
        if j != coluna:  
            
            # Configura todas as outras células na mesma linha para 
                    # terem um fundo cinza claro.
            # Isso serve para destacar toda a linha, exceto a célula 
                    # que já está destacada em amarelo.
            tabela[linha][j].config(bg="lightgray")

    # Destacar a coluna inteira onde o mouse está.
    # Inicia um loop que percorre todas as linhas da coluna 
            # atual (total de 10 linhas).
    for i in range(10):
        
        # Verifica se a linha atual é diferente da linha onde o mouse está.
        # Assim como antes, isso evita que o destaque específico da 
                # célula onde o mouse está seja sobrescrito.
        if i != linha:
            
            # Configura todas as outras células na mesma coluna para 
                    # terem um fundo cinza claro.
            # Isso serve para destacar toda a coluna, exceto a célula 
                    # que já está destacada em amarelo.
            tabela[i][coluna].config(bg="lightgray")


# Função para restaurar o destaque ao remover o mouse da célula
def restaurar_celula(event):
    
    # Obtém a linha e a coluna da célula de onde o mouse está 
            # saindo usando o widget do evento.
    # 'grid_info()' retorna um dicionário com informações de 
            # posicionamento do widget na grid.
    linha = event.widget.grid_info()['row']
    coluna = event.widget.grid_info()['column']

    # Laço duplo para iterar por todas as células da 
            # tabela (10 linhas por 5 colunas)
    for i in range(10):
        for j in range(5):
            
            # Restaura o fundo, a cor do texto e a fonte de 
                    # cada célula para o estado padrão.
            # 'bg="white"' define o fundo da célula para branco.
            # 'fg="black"' define a cor do texto para preto.
            # 'font=("Arial", 10)' configura a fonte para Arial, tamanho 10.
            tabela[i][j].config(bg="white", 
                                fg="black", 
                                font=("Arial", 10))


                    

# Criação da janela principal do aplicativo Tkinter.
janela = tk.Tk()
            
# Define o título da janela que aparecerá na barra 
        # de título da janela.
janela.title("Tabela Interativa")

# Inicia a criação de uma lista vazia que será usada para 
        # armazenar referências às células da tabela.
tabela = []

# Laço de repetição que cria 10 linhas na tabela.
for i in range(10):
    
    # Inicia uma lista vazia que representará uma linha de células.
    linha = []
    
    # Dentro de cada linha, este laço cria 5 células.
    for j in range(5):
        
        # Criação de um objeto Label (rótulo) do Tkinter para 
                # representar uma célula individual.
        # 'janela' é a janela onde o Label será colocado.
        # 'text=f"L{i+1} C{j+1}"' define o texto da célula como L1 C1, L1 C2, ..., 
                # das posições i e j.
        # 'bg="white"' define a cor de fundo da célula para branco.
        # 'fg="black"' define a cor do texto para preto.
        # 'width=12' e 'height=3' definem a largura e altura da célula.
        # 'borderwidth=1' e 'relief="solid"' definem a espessura da borda e o 
                # estilo de relevo para a borda, tornando-a visível.
        # 'font=("Arial", 10)' define a fonte do texto para Arial tamanho 10.
        celula = tk.Label(janela, text=f"L{i+1} C{j+1}", 
                          bg="white", 
                          fg="black", 
                          width=12, 
                          height=3, 
                          borderwidth=1, 
                          relief="solid", 
                          font=("Arial", 10))
        
        # Coloca a célula na grade da janela principal.
        # 'row=i' e 'column=j' definem a posição da célula na grade 
                # usando índices de linha e coluna.
        # 'sticky="nsew"' faz a célula expandir-se e aderir a todas as 
                # direções (norte, sul, leste, oeste) dentro de sua célula de grade.
        celula.grid(row=i, column=j, sticky="nsew")
        
        # Vincula eventos à célula.
        # 'bind("<Enter>", destacar_celula)' vincula o evento de 
                # passar o mouse sobre a célula à função que destaca a célula.
        # 'bind("<Leave>", restaurar_celula)' vincula o evento de 
                # saída do mouse da célula à função que remove o destaque.
        celula.bind("<Enter>", destacar_celula)
        celula.bind("<Leave>", restaurar_celula)
        
        # Adiciona a célula criada à lista que representa a linha atual.
        linha.append(celula)
    
    # Após criar todas as células de uma linha, adiciona a linha à 
            # lista principal 'tabela'.
    # Isso constrói a tabela como uma lista de listas, onde cada 
            # lista interna é uma linha da tabela.
    tabela.append(linha)


# Configurar as colunas para ajustar o tamanho conforme a 
        # tabela é redimensionada
# Inicia um laço de repetição que percorre cada uma 
        # das 5 colunas da tabela (de 0 a 4).
for j in range(5):
    
    # Configura cada coluna individualmente para que se ajuste 
            # automaticamente ao redimensionar a janela.
    # 'grid_columnconfigure(j, weight=1)' é uma função que 
            # configura a coluna 'j' para ter um peso de '1'.
    # O parâmetro 'weight=1' significa que cada coluna terá a 
            # mesma prioridade ao distribuir o espaço adicional,
            # garantindo que todas as colunas cresçam de maneira 
            # uniforme quando a janela for redimensionada.
    janela.grid_columnconfigure(j, weight=1)

# Configurar as linhas para ajustar o tamanho conforme a 
        # tabela é redimensionada.
# Inicia um laço de repetição que percorre cada uma das 10 
        # linhas da tabela (de 0 a 9).
for i in range(10):
    
    # Configura cada linha individualmente para que se ajuste 
            # automaticamente ao redimensionar a janela.
    # 'grid_rowconfigure(i, weight=1)' é uma função que configura a 
            # linha 'i' para ter um peso de '1'.
    # O parâmetro 'weight=1' opera da mesma forma que nas colunas, 
            # permitindo que cada linha cresça de maneira uniforme
    # quando a janela for redimensionada. Isso assegura que a tabela 
            # mantenha sua proporção relativa, independentemente das 
            # mudanças no tamanho da janela.
    janela.grid_rowconfigure(i, weight=1)


# Iniciar o loop principal da interface
janela.mainloop()