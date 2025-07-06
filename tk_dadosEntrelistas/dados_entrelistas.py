# Importa o módulo tkinter para a criação de interfaces gráficas.
import tkinter as tk

# Importa o módulo messagebox de tkinter para 
        # exibir mensagens de alerta.
from tkinter import messagebox


# Define a função 'adicionar_item', que manipula a 
        # transferência de itens entre duas listas.
def adicionar_item():
    
    # Obtém o índice do item atualmente selecionado 
            # na lista esquerda.
    selecionado = lista_esquerda.curselection()
    
    # Verifica se algum item foi realmente selecionado.
    if selecionado:
        
        # Recupera o item selecionado da lista 
                # esquerda usando o índice.
        item = lista_esquerda.get(selecionado)
        
        # Insere o item recuperado no final da lista direita.
        lista_direita.insert(tk.END, item)
        
        # Remove o item selecionado da lista esquerda, 
                # pois agora está na lista direita.
        lista_esquerda.delete(selecionado)
        
    # Executa este bloco se nenhum item estiver selecionado 
            # ao tentar adicionar.
    else:
        
        # Exibe uma mensagem de aviso informando que 
                # nenhum item foi selecionado.
        messagebox.showwarning("Seleção Inválida", "Selecione um item para adicionar.")


# Define a função 'remover_item' para mover itens selecionados 
        # de volta da lista direita para a lista esquerda.
def remover_item():
    
    # Obtém o índice do item atualmente selecionado na lista direita.
    selecionado = lista_direita.curselection()
    
    # Verifica se algum item foi realmente selecionado na lista direita.
    if selecionado:
        
        # Recupera o item selecionado na lista direita usando o índice obtido.
        item = lista_direita.get(selecionado)
        
        # Insere o item recuperado no final da lista esquerda, 
                # retornando-o para sua lista original.
        lista_esquerda.insert(tk.END, item)
        
        # Remove o item da lista direita, já que foi movido 
                # de volta para a lista esquerda.
        lista_direita.delete(selecionado)
        
    # Executa este bloco se nenhum item estiver 
            # selecionado ao tentar remover.
    else:
        
        # Exibe uma mensagem de aviso informando que nenhum 
                # item foi selecionado para remoção.
        messagebox.showwarning("Seleção Inválida", "Selecione um item para remover.")
        


# Define a função 'mover_todos_para_direita' que transfere 
        # todos os itens da lista da esquerda para a lista da direita.
def mover_todos_para_direita():
    
    # Recupera todos os itens da lista esquerda, desde o primeiro 
            # item (índice 0) até o último (tk.END).
    itens = lista_esquerda.get(0, tk.END)
    
    # Itera sobre cada item obtido da lista esquerda.
    for item in itens:
        
        # Insere cada item no final da lista direita.
        lista_direita.insert(tk.END, item)
        
    # Apaga todos os itens da lista esquerda após terem sido 
            # transferidos para a lista direita.
    lista_esquerda.delete(0, tk.END)


# Define a função 'mover_todos_para_esquerda' que transfere todos 
            # os itens da lista da direita para a lista da esquerda.
def mover_todos_para_esquerda():
    
    # Recupera todos os itens da lista direita, desde o primeiro 
            # item (índice 0) até o último (tk.END).
    itens = lista_direita.get(0, tk.END)
    
    # Itera sobre cada item obtido da lista direita.
    for item in itens:
        
        # Insere cada item no final da lista esquerda.
        lista_esquerda.insert(tk.END, item)
        
    # Apaga todos os itens da lista direita após terem 
            # sido transferidos para a lista esquerda.
    lista_direita.delete(0, tk.END)


# Cria a janela principal da aplicação usando Tkinter.
janela = tk.Tk()

# Define o título da janela principal, que aparece na 
        # barra de título da janela.
janela.title("Passar Dados entre Listas")

# Define um estilo de fonte comum para usar nos widgets da 
        # interface, especificamente a fonte Arial de tamanho 14.
fonte = ("Arial", 14)

# Cria uma caixa de listagem (Listbox) que será usada para 
        # mostrar e selecionar itens na parte esquerda da janela.
# 'selectmode=tk.SINGLE' permite a seleção de apenas um item por vez.
lista_esquerda = tk.Listbox(janela, 
                            selectmode=tk.SINGLE, 
                            font=fonte)

# Organiza a 'lista_esquerda' na janela principal.
# 'side=tk.LEFT' coloca a lista no lado esquerdo da janela.
# 'padx=10' e 'pady=10' adicionam um espaçamento de 10 
        # pixels em todas as direções ao redor da lista.
lista_esquerda.pack(side=tk.LEFT, 
                    padx=10, 
                    pady=10)


# Cria uma segunda caixa de listagem (Listbox) que será 
        # usada para mostrar e selecionar itens na parte direita da janela.
# Assim como a lista esquerda, esta lista permite a seleção 
        # de apenas um item por vez com 'selectmode=tk.SINGLE'.
lista_direita = tk.Listbox(janela, 
                           selectmode=tk.SINGLE, 
                           font=fonte)

# Organiza a 'lista_direita' na janela principal.
# 'side=tk.RIGHT' coloca a lista no lado direito da 
        # janela, oposto à lista esquerda.
# 'padx=10' e 'pady=10' adicionam um espaçamento de 10 
        # pixels em todas as direções ao redor da lista.
lista_direita.pack(side=tk.RIGHT, padx=10, pady=10)

# Cria um botão chamado 'btn_adicionar' para mover itens 
        # selecionados da lista esquerda para a direita.
# 'text="Adicionar →"' define o texto do botão, indicando a 
        # ação de adicionar (mover itens para a direita).
# 'command=adicionar_item' associa este botão à função 
        # 'adicionar_item', que é executada quando o botão é clicado.
btn_adicionar = tk.Button(janela, 
                          text="Adicionar →", 
                          command=adicionar_item, 
                          font=fonte)

# Organiza o botão 'btn_adicionar' abaixo das listas 
        # na janela principal.
# 'pady=5' adiciona um espaçamento vertical de 5 pixels 
        # acima e abaixo do botão para separá-lo visualmente 
        # de outros elementos.
btn_adicionar.pack(pady=5)


# Cria um botão chamado 'btn_remover' para mover itens 
        # selecionados da lista direita de volta para a esquerda.
# 'text="← Remover"' define o texto do botão, indicando a 
        # ação de remover (mover itens para a esquerda).
# 'command=remover_item' associa este botão à função 
        # 'remover_item', que é executada quando o botão é clicado.
btn_remover = tk.Button(janela, 
                        text="← Remover", 
                        command=remover_item, 
                        font=fonte)

# Organiza o botão 'btn_remover' abaixo do botão 
        # 'btn_adicionar' na janela principal.
# 'pady=5' adiciona um espaçamento vertical de 5 pixels 
        # acima e abaixo do botão para separá-lo 
        # visualmente de outros elementos.
btn_remover.pack(pady=5)

# Cria um botão chamado 'btn_mover_todos_direita' para 
        # mover todos os itens da lista esquerda para a direita.
# 'text="Mover Todos →"' define o texto do botão, indicando a 
        # ação de mover todos os itens para a direita.
# 'command=mover_todos_para_direita' associa este botão à 
        # função 'mover_todos_para_direita', que é executada 
        # quando o botão é clicado.
btn_mover_todos_direita = tk.Button(janela, 
                                    text="Mover Todos →", 
                                    command=mover_todos_para_direita, 
                                    font=fonte)

# Organiza o botão 'btn_mover_todos_direita' abaixo do 
        # botão 'btn_remover' na janela principal.
# 'pady=5' adiciona um espaçamento vertical de 5 pixels acima e 
        # abaixo do botão para separá-lo visualmente de outros elementos.
btn_mover_todos_direita.pack(pady=5)


# Cria um botão chamado 'btn_mover_todos_esquerda' para 
        # mover todos os itens da lista direita de volta para a esquerda.
# 'text="← Voltar Todos"' define o texto do botão, indicando a 
        # ação de mover todos os itens de volta para a esquerda.
# 'command=mover_todos_para_esquerda' associa este botão à função 
        # 'mover_todos_para_esquerda', que é executada quando o botão é clicado.
btn_mover_todos_esquerda = tk.Button(janela, 
                                     text="← Voltar Todos", 
                                     command=mover_todos_para_esquerda, 
                                     font=fonte)

# Organiza o botão 'btn_mover_todos_esquerda' abaixo do 
        # botão 'btn_mover_todos_direita' na janela principal.
# 'pady=5' adiciona um espaçamento vertical de 5 pixels acima e 
        # abaixo do botão para separá-lo visualmente de outros elementos.
btn_mover_todos_esquerda.pack(pady=5)

# Inicia o processo de adicionar itens na lista da esquerda.
# Gera uma lista de strings 'Item 1' a 'Item 15' 
        # usando compreensão de lista.
itens = [f"Item {i+1}" for i in range(15)]

# Itera sobre cada item gerado.
for item in itens:
    
    # Insere cada item gerado no final da lista da esquerda.
    # 'tk.END' assegura que cada novo item seja adicionado 
            # no final da lista.
    lista_esquerda.insert(tk.END, item)


# Iniciar o loop principal da interface
janela.mainloop()