"""
Exercicio Gestão de Pilha Interativa com Tkinter

Enunciado:

A estrutura de dados "pilha" é uma das mais fundamentais em ciência da computação. 
Sua característica principal é ser uma coleção de itens onde o último elemento 
inserido é o primeiro a ser removido (Last In, First Out - LIFO).

Seu desafio é criar uma aplicação gráfica usando o módulo Tkinter em Python 
para interagir e gerenciar uma pilha de números inteiros. A aplicação deve 
fornecer as seguintes funcionalidades:

    - Adicionar à pilha: O usuário deve ser capaz de digitar um número inteiro
        em um campo de texto e, ao clicar em um botão, adicionar esse número 
        ao topo da pilha.
        
    - Remover da pilha: O usuário deve ser capaz de clicar em um botão para 
        remover o número no topo da pilha. Após a remoção, uma janela de mensagem 
        deve mostrar o número removido.
        
    - Visualizar o topo da pilha: O usuário deve ser capaz de clicar em um botão 
        para visualizar o número atual no topo da pilha.
    
    - Verificar se a pilha está vazia: Ao clicar em um botão, o usuário deve ser 
        informado se a pilha está vazia ou não.
        
    - Obter o tamanho da pilha: Ao clicar em um botão, uma janela de mensagem 
        deve mostrar o tamanho atual da pilha.
        
    - Visualizar a pilha inteira: A aplicação deve mostrar a pilha atualizada 
        em tempo real em uma lista. O topo da pilha deve ser claramente identificado 
        como o primeiro item da lista.


Boa sorte!
"""


# Solução

# Primeiro, importamos os módulos necessários:
# `tkinter` é o módulo padrão em Python para criar interfaces 
# gráficas e `messagebox` e `ttk` são submódulos específicos de `tkinter`.

import tkinter as tk
from tkinter import messagebox, ttk

# Em seguida, definimos uma classe chamada 'Pilha'. Esta classe 
# representa a estrutura de dados chamada pilha, que é uma coleção 
# de itens que segue o princípio LIFO (Last In, First Out).

class Pilha:
    
    # O método `__init__` é o construtor da classe. Ele é executado 
    # automaticamente cada vez que um novo objeto desta classe é criado.
    # O objetivo deste construtor é inicializar a pilha como uma lista vazia.
    def __init__(self):
        self.itens = []  # `self.itens` é uma lista vazia que armazenará os itens da pilha.
    
    # O método `push` é usado para adicionar (ou empurrar) um novo item para o topo da pilha.
    def push(self, item):
        
        # Aqui, utilizamos o método `append` das listas para adicionar o novo item ao final da lista.
        # Como estamos usando uma lista para representar a pilha, o final da lista é, essencialmente, o topo da pilha.
        self.itens.append(item)
        
    # O método `pop` é usado para remover (ou retirar) o item do topo da pilha e retorná-lo.
    def pop(self):
        
        # Usamos uma construção condicional em uma única linha.
        # Primeiro, verifica-se com `self.isEmpty()` se a pilha está vazia.
        # Se não estiver vazia (`not self.isEmpty()`), usamos o método `pop` 
        # da lista para remover e retornar o último item.
        # Se a pilha estiver vazia, retornamos `None` para indicar que não havia nada
        # para ser removido.
        return self.itens.pop() if not self.isEmpty() else None
    
    # O método `peek` é usado para visualizar (ou espiar) o item no topo da pilha sem removê-lo.
    def peek(self):
        
        # Semelhante ao método anterior, primeiro verificamos se a pilha não está vazia.
        # Se não estiver vazia, retornamos o último item da lista (ou seja, o topo da pilha) com `self.itens[-1]`.
        # Se estiver vazia, retornamos `None`.
        return self.itens[-1] if not self.isEmpty() else None
    
    
    # O método `isEmpty` é uma função auxiliar que verifica se a pilha está vazia.
    # Ele faz isso verificando se o comprimento da lista de itens é 0.
    def isEmpty(self):
        
        # Retorna True se a pilha estiver vazia e False caso contrário.
        return len(self.itens) == 0
    
    
    # O método `getSize` retorna o número atual de itens na pilha.
    # Como estamos usando uma lista para representar a pilha, podemos usar o 
    # método `len` do Python para obter esse número.
    def getSize(self):
        
        # Retorna o número de itens na pilha.
        return len(self.itens)
        
        
# Esta é a classe responsável por criar a interface gráfica 
# para gerenciar a pilha.
class PilhaApp:

    # O construtor da classe (__init__) é o método que é chamado quando 
    # criamos uma nova instância desta classe.
    # Neste caso, ele espera um argumento: 'master', que é o widget principal 
    # ou janela da aplicação tkinter.
    def __init__(self, master):
        
        # Armazena uma referência ao widget principal (geralmente é a janela 
        # principal da aplicação).
        self.master = master
        
        # Define o título da janela principal usando o método 'title' de 'master'.
        self.master.title("Gestão de Pilha Interativa")
        
        # Cria uma nova instância da classe 'Pilha'. Esta será a pilha que 
        # será gerenciada pela interface.
        self.pilha = Pilha()

        # Abaixo, vamos criar alguns widgets para a interface:

        # Criação de um rótulo (label) para exibir o título da aplicação.
        # 'text' define o que será exibido no rótulo.
        # 'font' especifica a fonte e o tamanho do texto no rótulo.
        self.title_label = tk.Label(self.master, 
                                    text="Gestão de Pilha Interativa", 
                                    font=("Arial", 20))
        
        # 'pack' é um método usado para posicionar e exibir o widget na janela principal.
        # 'pady' é um argumento que adiciona espaço acima e abaixo do 
        # widget (para melhorar a estética).
        self.title_label.pack(pady=20)

        # Criação de outro rótulo para instruir o usuário a digitar um número.
        self.entry_label = tk.Label(self.master, 
                                    text="Digite um número:")
        
        # Exibe o rótulo na janela principal.
        self.entry_label.pack(pady=5)
        
        # Criação de um widget de entrada (Entry) onde os usuários podem digitar
        # informações (neste caso, números).
        self.number_entry = tk.Entry(self.master)
        
        # Exibe o entry na janela principal.
        self.number_entry.pack(pady=5)

        # Criação de um botão (Button) que, quando clicado, executará a função 
        # 'push_item' para adicionar um item à pilha.
        # 'text' define o que será exibido no botão.
        # 'command' especifica a função que será chamada quando o botão for clicado.
        self.push_btn = tk.Button(self.master, 
                                  text="Adicionar à pilha (push)", 
                                  command=self.push_item)

        # Posiciona o botão 'push_btn' na janela principal.
        self.push_btn.pack(pady=5)
        
        
        # Criação de outro botão que, quando clicado, executará a função 
        # 'pop_item' para remover um item do topo da pilha.
        self.pop_btn = tk.Button(self.master, 
                                 text="Remover da pilha (pop)", 
                                 command=self.pop_item)

        # Posiciona o botão 'pop_btn' na janela principal.
        self.pop_btn.pack(pady=5)
        
        
        # Criação de um botão que, quando clicado, executará a função
        # 'peek_item' para visualizar o item do topo da pilha.
        self.peek_btn = tk.Button(self.master, 
                                  text="Visualizar topo da pilha (peek)", 
                                  command=self.peek_item)

        # Posiciona o botão 'peek_btn' na janela principal.
        self.peek_btn.pack(pady=5)
        
        
        # Criação de um botão para verificar se a pilha está vazia.
        self.is_empty_btn = tk.Button(self.master, 
                                      text="A pilha está vazia?", 
                                      command=self.is_empty)

        # Posiciona o botão 'is_empty_btn' na janela principal.
        self.is_empty_btn.pack(pady=5)
        
        
        
        # Criação de um botão para obter e mostrar o tamanho da pilha.
        self.size_btn = tk.Button(self.master, 
                                  text="Obter tamanho da pilha", 
                                  command=self.get_size)

        # Posiciona o botão 'size_btn' na janela principal.
        self.size_btn.pack(pady=5)

        
        # Criação de um rótulo (Label) para indicar que a Listbox abaixo mostrará os itens da pilha.
        self.listbox_label = tk.Label(self.master, 
                                      text="Pilha Atual:")

        # Posiciona o rótulo 'listbox_label' na janela principal.
        self.listbox_label.pack(pady=10)
        
        
        # Criação de uma caixa de listagem (Listbox) para exibir os itens da pilha.
        # 'height' define a altura da caixa de listagem (número de linhas visíveis).
        # 'width' define a largura da caixa de listagem em caracteres.
        # 'font' especifica a fonte e o tamanho do texto dentro da Listbox.
        self.pilha_display = tk.Listbox(self.master, 
                                        height=10, 
                                        width=50, 
                                        font=("Arial", 20))

        # Posiciona a caixa de listagem 'pilha_display' na janela principal.
        self.pilha_display.pack(pady=5)
        
    
    # Método para atualizar a exibição da pilha na interface gráfica.
    def update_display(self):
        
        # Deleta todos os itens da Listbox.
        # 'delete' é um método da Listbox que remove um ou mais itens.
        # Aqui, deletamos todos os itens, do primeiro (index 0) ao último (tk.END).
        self.pilha_display.delete(0, tk.END)
        
        # Itera sobre os itens da pilha em ordem inversa (o topo da pilha será o primeiro).
        # A pilha é representada por uma lista em Python, e 'reversed' inverte a ordem dos itens.
        for item in reversed(self.pilha.itens):
            
            # 'insert' é um método da Listbox que adiciona um item.
            # Aqui, estamos adicionando cada item ao final (tk.END) da Listbox.
            self.pilha_display.insert(tk.END, item)
            
        
    # Método para adicionar (push) um item à pilha.
    def push_item(self):
        
        try:
            
            # Tenta pegar o valor digitado pelo usuário no widget de entrada (Entry).
            # 'get' é um método do widget Entry que retorna o texto nele.
            # A seguir, tentamos converter esse texto para um número inteiro.
            num = int(self.number_entry.get())

            # Se a conversão foi bem-sucedida, o número é adicionado à pilha.
            self.pilha.push(num)

            # Atualiza a exibição da pilha na interface gráfica.
            self.update_display()

            # Limpa o widget de entrada (Entry) para o usuário poder digitar um novo número.
            # 'delete' é usado para remover texto do widget Entry. Aqui, remove-se todo o texto.
            self.number_entry.delete(0, tk.END)
            
        except ValueError:
            
            # Caso ocorra um erro na conversão do texto para um número (ValueError),
            # uma mensagem de erro é exibida para o usuário.
            # 'showerror' é um método de 'messagebox' que mostra uma janela de erro.
            messagebox.showerror("Erro", "Por favor, digite um número válido.")
            
            
            
    # Método para remover (pop) um item do topo da pilha.
    def pop_item(self):
        
        # Invoca o método 'pop' da pilha.
        item = self.pilha.pop()

        # Verifica se o item obtido não é None. Se não for, significa que havia um 
        # item para remover.
        if item is not None:
            
            # Atualiza a visualização da pilha na interface gráfica.
            self.update_display()
            
            # Exibe uma mensagem informando o número que foi removido do topo da pilha.
            messagebox.showinfo("Pop", f"Número {item} removido do topo da pilha!")
            
        else:
            
            # Se o item obtido é None, significa que a pilha estava vazia e não havia 
            # nada para remover.
            # Exibe uma mensagem informando que a pilha está vazia.
            messagebox.showinfo("Pilha Vazia", "A pilha já está vazia!")
            
    # Método para visualizar o item no topo da pilha sem removê-lo.
    def peek_item(self):
        
        # Invoca o método 'peek' da pilha para obter o item do topo.
        item = self.pilha.peek()

        # Se o item obtido não for None, mostra uma mensagem com o número que está no topo.
        if item is not None:
            
            messagebox.showinfo("Peek", f"Número no topo da pilha: {item}")
            
        else:
            
            # Se o item for None, a pilha está vazia.
            messagebox.showinfo("Pilha Vazia", "A pilha está vazia!")
            
    
    # Método para verificar se a pilha está vazia.
    def is_empty(self):
        
        # Verifica se a pilha está vazia invocando o método 'isEmpty'.
        if self.pilha.isEmpty():
            
            # Se estiver vazia, exibe uma mensagem informando o fato.
            messagebox.showinfo("Pilha Vazia", "A pilha está vazia!")
            
        else:
            
            # Caso contrário, informa que a pilha não está vazia.
            messagebox.showinfo("Pilha", "A pilha não está vazia!")
            
            
    # Método para obter e exibir o tamanho atual da pilha.
    def get_size(self):
        
        # Obtém o tamanho da pilha invocando o método 'getSize'.
        size = self.pilha.getSize()
        
        # Exibe uma mensagem informando o tamanho atual da pilha.
        messagebox.showinfo("Tamanho da Pilha", f"Tamanho da pilha: {size}")
        
            

# Verifica se este script é o ponto de entrada principal. Em outras 
# palavras, verifica se o script está sendo executado diretamente e não 
# sendo importado como um módulo.
if __name__ == "__main__":
    
    # Cria a janela principal do tkinter.
    root = tk.Tk()
    
    # Instancia o aplicativo, passando a janela principal como argumento. 
    # Isso efetivamente inicializa toda a interface gráfica do nosso aplicativo de pilha.
    app = PilhaApp(root)
    
    # Inicia o loop principal da interface gráfica. 
    # Isso mantém a janela aberta e ouve por eventos, como cliques de botão, 
    # até que a janela seja fechada.
    root.mainloop()