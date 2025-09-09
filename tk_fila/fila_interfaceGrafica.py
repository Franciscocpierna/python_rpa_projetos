"""
Exercício Fila de Prioridades com Interface Gráfica

Objetivo:
Desenvolva um programa gráfico para gerenciar uma fila de prioridades.

Descrição:

Uma fila de prioridades é uma estrutura de dados onde os elementos 
são adicionados com um valor de prioridade. Quando um item é chamado da 
fila, o item com a maior prioridade (no contexto deste problema, a prioridade 
mais alta é representada por um número menor) é removido antes dos outros.

Seu aplicativo deve ter as seguintes funcionalidades:

    - Adicionar Item à Fila: O usuário pode inserir um item e sua 
        respectiva prioridade.
    
    - Chamar Próximo Item: Quando acionado, o programa deve chamar e 
        remover o item com a prioridade mais alta.
        
    - Visualizar a Fila: O programa deve mostrar todos os itens na 
        fila, ordenados pela prioridade.

Requisitos Técnicos:

    Utilize a biblioteca heapq para gerenciar a fila de prioridades internamente.
    Utilize o tkinter para criar a interface gráfica.
"""

# Importa a biblioteca heapq, que fornece funções para manipular filas 
# de prioridade usando listas.
import heapq

# Importa o módulo tkinter, que é usado para criar interfaces gráficas.
import tkinter as tk

# Do módulo tkinter, importa os componentes específicos necessários:
# messagebox (para exibir caixas de diálogo),
# Entry (para criar campos de entrada de texto), Label (para criar rótulos) e
# Button (para criar botões).
from tkinter import messagebox, Entry, Label, Button

# Criação da classe FilaDePrioridades que irá implementar a estrutura de uma
# fila de prioridades.
class FilaDePrioridades:

    # O construtor da classe. É chamado automaticamente quando um objeto
    # desta classe é criado.
    def __init__(self):
        
        # Inicializa a propriedade 'fila' como uma lista vazia. 
        # Esta lista será usada em conjunto com a biblioteca heapq para 
        # implementar a fila de prioridades.
        self.fila = []
        
    # Método 'enqueue' é utilizado para adicionar um elemento à fila de prioridades.
    def enqueue(self, prioridade, elemento):
        
        # Utiliza a função 'heappush' do módulo heapq para adicionar o elemento na fila.
        # A função garante que o elemento seja inserido na posição correta, baseado na prioridade.
        # Os elementos são adicionados como tuplas, onde o primeiro valor é a prioridade 
        # e o segundo é o elemento em si.
        heapq.heappush(self.fila, (prioridade, elemento))
        
        
    # Método 'dequeue' é utilizado para remover e retornar o 
    # elemento com a maior prioridade da fila.
    def dequeue(self):
        
        # Antes de tentar remover um item, verifica se a fila está vazia usando o método 'isEmpty'.
        if not self.isEmpty():
            
            # Se a fila não estiver vazia, utiliza a função 'heappop' do módulo heapq 
            # para remover e retornar o elemento de maior prioridade.
            # Uma vez que os elementos são armazenados como tuplas, o '[1]' no final 
            # garante que apenas o elemento (e não sua prioridade) seja retornado.
            return heapq.heappop(self.fila)[1]
        
        else:
            
            # Se a fila estiver vazia, retorna uma mensagem indicando isso.
            return "A fila está vazia!"

    # Método 'isEmpty' verifica se a fila está vazia.
    def isEmpty(self):
        
        # Retorna True se o tamanho da fila for 0 (ou seja, está vazia) e False caso contrário.
        return len(self.fila) == 0
    
    
    # Método 'getSize' retorna o número de elementos atualmente na fila.
    def getSize(self):
        
        # Retorna o tamanho da fila usando a função len.
        return len(self.fila)
    
        
# Implementação da interface gráfica
class App:

    # Método construtor da classe App
    def __init__(self, root):
        
        # Inicializa uma instância da classe FilaDePrioridades.
        # Essa instância será usada para gerenciar a fila de 
        # prioridades através da interface gráfica.
        self.queue = FilaDePrioridades()
        
        # Título
        # Cria um label (rótulo) que será usado como título para a janela da aplicação.
        # Esse rótulo terá o texto "Fila de Prioridades" e usará a fonte Arial no tamanho 16.
        self.title_label = Label(root, text="Fila de Prioridades", font=("Arial", 16))
        
        # Usa o método 'pack' para adicionar o rótulo na janela principal.
        # O parâmetro 'pady' adiciona um espaçamento vertical de 20 pixels acima e abaixo do rótulo.
        self.title_label.pack(pady=20)
        
        # Frame para entradas
        # Cria um novo frame (container) que conterá os campos de entrada da aplicação.
        # Esse frame é usado para agrupar visualmente os elementos relacionados.
        self.input_frame = tk.Frame(root, pady=20)
        
        # Usa o método 'pack' para adicionar o frame na janela principal.
        # O parâmetro 'fill=tk.X' garante que o frame se expanda horizontalmente para preencher toda a largura da janela.
        # O parâmetro 'padx' adiciona um espaçamento horizontal de 20 pixels à esquerda e à direita do frame.
        self.input_frame.pack(fill=tk.X, padx=20)
        
        # Criação do rótulo 'Prioridade'
        # Define um rótulo (label) chamado 'priority_label' dentro do frame 'input_frame' com o texto "Prioridade:"
        self.priority_label = Label(self.input_frame, 
                                    text="Prioridade:",
                                    font="Arial 18")
        
        # Usa o método 'grid' para posicionar o rótulo no frame 'input_frame'.
        # Ele será posicionado na primeira linha (row=0) e na primeira coluna (column=0).
        # 'padx' define o espaçamento horizontal à esquerda (0) e à direita (10) do rótulo.
        # 'pady' define o espaçamento vertical acima e abaixo do rótulo como 5 pixels.
        self.priority_label.grid(row=0, column=0, padx=(0, 10), pady=5)
        
        
        # Cria um campo de entrada (entry) chamado 'priority_entry' dentro do 
        # frame 'input_frame' para inserir a prioridade.
        self.priority_entry = Entry(self.input_frame,
                                    font="Arial 18")
        
        # Usa o método 'grid' para posicionar o campo de entrada no frame 'input_frame'.
        # Ele será posicionado na primeira linha (row=0) e na segunda coluna (column=1) ao lado do rótulo 'Prioridade'.
        # 'pady' define o espaçamento vertical acima e abaixo do campo como 5 pixels.
        self.priority_entry.grid(row=0, column=1, pady=5)
        
        
        # Criação do rótulo 'Item'
        # Define um rótulo chamado 'item_label' dentro do frame 'input_frame' com o texto "Item:"
        self.item_label = Label(self.input_frame, 
                                    text="Item:",
                                    font="Arial 18")
        
        # Posiciona o rótulo na segunda linha (row=1) e na primeira coluna (column=0) do frame 'input_frame'.
        self.item_label.grid(row=1, column=0, padx=(0, 10), pady=5)
        
        
        # Cria um campo de entrada chamado 'item_entry' dentro do frame 'input_frame'
        # para inserir o item.
        self.item_entry = Entry(self.input_frame,
                                    font="Arial 18")
        
        # Posiciona o campo de entrada na segunda linha (row=1) e na segunda 
        # coluna (column=1) ao lado do rótulo 'Item'.
        self.item_entry.grid(row=1, column=1, pady=5)
        
        # Frame para botões
        # Cria um novo frame (container) chamado 'button_frame' que conterá os botões da aplicação.
        self.button_frame = tk.Frame(root, pady=20)
        
        # Posiciona o frame na janela principal (root).
        # O frame se expandirá horizontalmente para preencher a largura da janela.
        # 'padx' adiciona um espaçamento horizontal à esquerda e à direita do frame.
        self.button_frame.pack(fill=tk.X, padx=20)
        
        
        # Botão "Incluir na Fila"
        # Cria um botão chamado 'add_btn' dentro do frame 'button_frame' com o texto "Incluir na Fila".
        # Ao clicar neste botão, o método 'self.add_to_queue' será executado (definido pelo parâmetro 'command').
        self.add_btn = Button(self.button_frame, text="Incluir na Fila", font="Arial 14", command=self.add_to_queue)
        
        # Posiciona o botão no lado esquerdo (LEFT) do 'button_frame'.
        # 'padx' adiciona um espaçamento horizontal à esquerda e à direita do botão.
        self.add_btn.pack(side=tk.LEFT, padx=10)
        
        
        # Botão "Chamar próximo"
        # Cria outro botão chamado 'call_btn' dentro do frame 'button_frame' com o texto "Chamar próximo".
        # Ao clicar neste botão, o método 'self.call_next' será executado.
        self.call_btn = Button(self.button_frame, text="Chamar próximo", font="Arial 14", command=self.call_next)
        
        # Posiciona o botão no lado direito (RIGHT) do 'button_frame'.
        self.call_btn.pack(side=tk.RIGHT, padx=10)
        
        
        # Rótulo para mostrar a fila
        # Cria um rótulo chamado 'queue_label' na janela principal (root) com o texto "Fila atual:".
        # Esse rótulo tem uma fonte definida para Arial tamanho 14.
        self.queue_label = Label(root, text="Fila atual:", font=("Arial", 14))
        
        # Posiciona o rótulo na janela principal (root).
        # 'pady' adiciona um espaçamento vertical acima e abaixo do rótulo, enquanto 'padx' faz o mesmo horizontalmente.
        self.queue_label.pack(pady=5, padx=20)
        
        
        # Rótulo para exibir os itens da fila
        # Cria um rótulo chamado 'queue_display' na janela principal (root) com o texto inicial vazio ("").
        # Esse rótulo também tem uma fonte definida para Arial tamanho 16 e o texto será justificado à esquerda.
        self.queue_display = Label(root, text="", font=("Arial", 16), justify=tk.LEFT)
        
        # Posiciona o rótulo na janela principal (root) logo abaixo do rótulo 'queue_label'.
        self.queue_display.pack(pady=10, padx=20)
        
        
        # Atualiza a exibição da fila.
        # Chama o método 'self.update_display' para preencher e mostrar os itens da fila no rótulo 'queue_display'.
        self.update_display()
        
        
    # Esse método tenta adicionar um item à fila de prioridades. Primeiro, 
    # ele obtém os valores das entradas de prioridade e item. Se o campo do item 
    # estiver vazio, mostra uma mensagem de erro. Se a entrada de prioridade não 
    # for um número válido, ele também mostra uma mensagem de erro. Caso contrário, 
    # ele adiciona o item à fila, atualiza a exibição e limpa os campos de entrada.
    def add_to_queue(self):
        
        # Tenta executar o bloco de código dentro do 'try'
        try:
            
            # Recupera o valor da entrada 'priority_entry' (onde o usuário define a prioridade do item)
            # e tenta convertê-lo para um número inteiro.
            # Se a conversão falhar (por exemplo, se o usuário inserir texto não numérico), 
            # isso acionará a exceção 'ValueError'.
            priority = int(self.priority_entry.get())

            # Recupera o valor da entrada 'item_entry' (onde o usuário define o nome do item)
            item = self.item_entry.get()

            # Se o 'item' estiver vazio (ou seja, se o usuário não inseriu nenhum texto no campo do item)
            if not item:
                
                # Mostra uma caixa de mensagem de erro informando ao usuário para digitar um item.
                messagebox.showerror("Erro", "Digite um item.")
                
                return  # Retorna do método sem fazer mais nada.

            # Chama o método 'enqueue' da fila para adicionar o item com a sua prioridade.
            self.queue.enqueue(priority, item)

            # Atualiza a exibição da fila para refletir a inclusão do novo item.
            self.update_display()

            # Limpa os campos de entrada para permitir a inclusão de novos itens.
            # Deleta tudo desde o início (índice 0) até o final do campo.
            self.priority_entry.delete(0, tk.END)
            self.item_entry.delete(0, tk.END)
            

        # Caso ocorra uma exceção do tipo 'ValueError' (por exemplo, se a entrada de prioridade não for um número válido)
        except ValueError:
            
            # Mostra uma caixa de mensagem de erro informando ao usuário para digitar uma prioridade válida.
            messagebox.showerror("Erro", "Digite uma prioridade válida.")
            
            
    # O método call_next é responsável por chamar o próximo item na fila 
    # com base em sua prioridade e atualizar a exibição da fila
    def call_next(self):
        
        # Chama o método 'dequeue' da fila para obter o próximo item com base na prioridade.
        item = self.queue.dequeue()

        # Se o retorno do método 'dequeue' for a string "A fila está vazia!",
        # isso significa que não há mais itens na fila.
        if item == "A fila está vazia!":
            
            # Mostra uma caixa de mensagem informando ao usuário que a fila está vazia.
            messagebox.showinfo("Informação", item)
            
        else:
            
            # Caso contrário, mostra uma caixa de mensagem informando ao usuário qual é o próximo item chamado.
            messagebox.showinfo("Próximo Item", f"Item chamado: {item}")
            
            # Atualiza a exibição da fila para refletir a remoção do item chamado.
            self.update_display()
            
            
    # O método update_display atualiza a exibição da fila no aplicativo. 
    # Ele primeiro ordena os itens na fila com base na prioridade, depois cria 
    # uma string representando a fila, e finalmente atualiza o rótulo no aplicativo 
    # para mostrar essa string. Se a fila estiver vazia, ele mostra "Fila vazia".
    def update_display(self):

        # Ordena a fila com base na prioridade para exibição.
        # A função 'sorted' é usada para ordenar a fila.
        # O argumento 'key' define o critério de ordenação, que neste caso é a prioridade do item.
        sorted_queue = sorted(self.queue.fila, key=lambda x: x[0])
        
        # Cria uma lista de strings representando cada item e sua prioridade na fila.
        # Em seguida, junta essa lista em uma única string usando '\n' como separador.
        display_text = "\n".join([f"{item[1]} (Prioridade: {item[0]})" for item in sorted_queue])
        
        # Se 'display_text' estiver vazio (ou seja, se não houver itens na fila)
        if not display_text:
            
            # Define o texto a ser mostrado como "Fila vazia".
            display_text = "Fila vazia"
            
        # Configura o rótulo 'queue_display' para mostrar o texto atualizado da fila.
        self.queue_display.config(text=display_text)
        
        
# Verifica se este script está sendo executado diretamente e não importado em outro script.
if __name__ == "__main__":

    # Cria uma instância da classe Tkinter, que representa a janela principal da aplicação.
    root = tk.Tk()
    
    # Define o título da janela como "Interface Fila de Prioridades".
    root.title("Interface Fila de Prioridades")
    
    # Define as dimensões da janela como 400 pixels de largura por 500 pixels de altura.
    root.geometry("400x500")
    
    # Cria uma instância da classe 'App', que representa a aplicação de fila de prioridades,
    # passando a janela principal como argumento.
    app = App(root)
    
    # Inicia o loop principal do Tkinter. Isso mantém a janela aberta e ouve eventos do usuário,
    # como cliques de botão ou entradas de teclado.
    root.mainloop()