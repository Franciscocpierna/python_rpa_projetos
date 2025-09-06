"""
Reprodutor de Música com Lista Encadeada

Objetivo: Neste exercício, você deverá desenvolver um reprodutor 
de música simples utilizando a biblioteca pygame para a reprodução das 
músicas e tkinter para a interface gráfica. O diferencial deste reprodutor 
é que as músicas devem ser armazenadas em uma lista encadeada, ao invés de 
uma lista comum.

Especificações:

    1. Lista Encadeada: Você deve criar uma classe No que representará cada 
        elemento da lista encadeada. Cada nó deve conter o título da música, o 
        caminho do arquivo e a referência para o próximo nó.

    2. Lista de Músicas: Crie uma classe ListaMusica que representará a lista 
        encadeada. Ela deve possuir métodos para adicionar músicas e buscar o 
        caminho de uma música pelo título.

    3. Reprodutor: Crie uma classe ReprodutorMusica que será responsável por 
        gerenciar a lista de músicas e interagir com a biblioteca pygame para 
        reproduzir, parar e trocar as músicas.

    4. Interface Gráfica: Desenvolva uma interface gráfica utilizando tkinter 
        onde o usuário possa:
            - Adicionar músicas à lista
            - Visualizar as músicas adicionadas
            - Reproduzir uma música selecionada
            - Parar a música que está tocando
            - Avançar para a próxima música
            - Retornar para a música anterior

Observação: As músicas devem ser do tipo .MP3.
"""

# Importando o módulo tkinter como tk para criar a interface gráfica.
import tkinter as tk

# Importando duas classes específicas do tkinter:
# filedialog: para obter janelas de diálogo do sistema operacional para seleção de arquivos.
# ttk: para usar widgets estilizados do tkinter.
from tkinter import filedialog, ttk

# Importando a biblioteca pygame, que será utilizada para reprodução das músicas.
import pygame

# Definição da classe "No" que representa um nó de uma lista encadeada.
class No:
    
    # Método inicializador da classe.
    def __init__(self, titulo, caminho):
        
        # Atributo que armazena o título da música.
        self.titulo = titulo
        
        # Atributo que guarda o caminho do arquivo da música no sistema de arquivos.
        self.caminho = caminho
        
        # Atributo que aponta para o próximo nó na lista encadeada. 
        # Inicialmente é definido como None, indicando que não há um próximo nó.
        self.proximo = None
        
# Definição da classe "ListaMusica" que representa uma lista encadeada 
# para armazenar músicas.
class ListaMusica:
    
    # Método inicializador da classe.
    def __init__(self):
        
        # Atributo que aponta para o primeiro nó da lista encadeada.
        self.inicio = None
        
        # Atributo que aponta para o último nó da lista encadeada.
        self.final = None
        
        
    # Método para adicionar uma nova música à lista encadeada.
    def adicionar(self, titulo, caminho):
        
        # Criando um novo nó com o título e o caminho da música fornecidos.
        novo_no = No(titulo, caminho)
        
        # Se a lista estiver vazia (ou seja, o início for None),
        # fazemos o início e o final da lista apontarem para o novo nó.
        if self.inicio is None:
            
            self.inicio = novo_no
            self.final = novo_no
            
        else:
            
            # Se a lista já contiver nós, o próximo nó do nó final atual apontará 
            # para o novo nó,
            # e o novo nó torna-se o novo nó final da lista.
            self.final.proximo = novo_no
            self.final = novo_no

        
        
    # Define um método para buscar o caminho de uma música com base no seu título.
    def obter_caminho(self, titulo):
        
        # Inicializa a variável 'atual' com o primeiro nó da lista encadeada.
        atual = self.inicio

        # Enquanto 'atual' não for None (isto é, enquanto não chegarmos 
        # ao fim da lista):
        while atual:
            
            # Verifica se o título do nó atual corresponde ao 
            # título fornecido como argumento.
            if atual.titulo == titulo:
                
                # Se corresponder, retorna o caminho associado a esse nó.
                return atual.caminho

            # Caso o título do nó atual não corresponda, avança para 
            # o próximo nó da lista encadeada.
            atual = atual.proximo

        # Se sair do loop e não encontrar o título fornecido, retorna None.
        return None
        
        
# Definição da classe ReprodutorMusica, que servirá para gerenciar a reprodução das músicas.
class ReprodutorMusica:

    # Método construtor da classe.
    def __init__(self):
        
        # Inicializa o módulo pygame. O pygame é uma biblioteca para criação de jogos e 
        # aplicações multimídia, e aqui é usado para reproduzir músicas.
        pygame.init()
        
        # Inicializa o mixer do pygame, que é responsável por gerenciar operações de áudio.
        pygame.mixer.init()
        
        # Cria uma instância da classe ListaMusica (que representa uma lista 
        # encadeada de músicas)
        # e associa a essa instância à variável 'musicas'. Esta será a lista 
        # onde armazenaremos todas
        # as músicas que o usuário adicionar ao reprodutor.
        self.musicas = ListaMusica()

    
    # Método para adicionar uma música à lista encadeada de músicas.
    def adicionar_musica(self, titulo, caminho):
        
        # Usa o método 'adicionar' da instância 'musicas' (que é uma ListaMusica) para adicionar
        # a música com o título e caminho especificados à lista.
        self.musicas.adicionar(titulo, caminho)
        
    # Método para reproduzir uma música específica.
    def tocar(self, titulo):
        
        # Obtém o caminho da música com o título especificado usando o método 'obter_caminho'
        # da instância 'musicas' (que é uma ListaMusica).
        caminho_musica = self.musicas.obter_caminho(titulo)

        # Se o caminho da música foi encontrado (ou seja, a música existe na lista):
        if caminho_musica:
            
            # Carrega a música no mixer do pygame usando o caminho obtido.
            pygame.mixer.music.load(caminho_musica)

            # Inicia a reprodução da música.
            pygame.mixer.music.play()
            
    # Método para parar a reprodução da música atualmente em execução.
    def parar(self):
        
        # Usa o método 'stop' do mixer do pygame para parar a música que está sendo reproduzida.
        pygame.mixer.music.stop()

        

# Função que permite ao usuário escolher uma música usando uma janela de diálogo.
def escolher_musica():
    
    # Abre uma janela de diálogo para o usuário escolher um arquivo. 
    # O diretório inicial é o diretório atual ("."),
    # o título da janela é "Escolha uma Música",
    # e somente arquivos com extensão .mp3 são permitidos para seleção.
    caminho = filedialog.askopenfilename(initialdir=".", title="Escolha uma Música", filetypes=(("Arquivos MP3", "*.mp3"),))
    
    # Se o usuário não selecionar nenhum arquivo (ou seja, clicar em cancelar), a função termina aqui.
    if not caminho:
        return
    
    # Extrai o nome da música do caminho completo. 
    # Por exemplo, se o caminho for "/pasta/subpasta/musica.mp3", 
    # nome_musica será "musica.mp3".
    nome_musica = caminho.split("/")[-1]
    
    # Adiciona o nome da música à lista visual (interface gráfica) para o usuário.
    lista_interface.insert(tk.END, nome_musica)
    
    # Adiciona a música à lista encadeada do reprodutor com o nome e caminho especificados.
    reprodutor.adicionar_musica(nome_musica, caminho)
        

# Função para tocar a música selecionada pelo usuário na interface gráfica.
def tocar_selecionada():
    
    # Obtém o nome da música atualmente selecionada na interface gráfica.
    musica_escolhida = lista_interface.get(lista_interface.curselection())
    
    # Se há uma música selecionada (a variável 'musica_escolhida' não está vazia), 
    # toca essa música.
    if musica_escolhida:
        reprodutor.tocar(musica_escolhida)
        

# Função para parar a reprodução da música atual.
def parar_musica():
    reprodutor.parar()
    

# Função para tocar a música anterior na lista de reprodução.
def musica_anterior():
    
    # Obtém o índice da música atualmente selecionada na interface gráfica.
    indice_atual = lista_interface.curselection()
    
    # Verifica se há uma música selecionada.
    if indice_atual:
        
        # Calcula o índice da música anterior.
        indice_anterior = indice_atual[0] - 1
        
        # Verifica se o índice anterior é válido (ou seja, não é negativo).
        if indice_anterior >= 0:
            
            # Desseleciona a música atual na interface gráfica.
            lista_interface.select_clear(indice_atual)
            
            # Seleciona a música anterior na interface gráfica.
            lista_interface.select_set(indice_anterior)
            
            # Toca a música anterior.
            tocar_selecionada()
            
# Função para tocar a próxima música na lista de reprodução.
def proxima_musica():
    
    # Obtém o índice da música atualmente selecionada na interface gráfica.
    indice_atual = lista_interface.curselection()
    
    # Calcula o índice da próxima música, somando 1 ao índice atual.
    indice_proximo = indice_atual[0] + 1
    
    # Verifica se o índice da próxima música é válido (ou seja, 
    # não ultrapassa o tamanho da lista de músicas).
    if indice_proximo < lista_interface.size():
        
        # Desseleciona a música atual na interface gráfica.
        lista_interface.select_clear(indice_atual)
        
        # Seleciona a próxima música na interface gráfica.
        lista_interface.select_set(indice_proximo)
        
        # Toca a próxima música.
        tocar_selecionada()
        
        
# Cria uma janela principal usando a biblioteca tkinter.
janela = tk.Tk()

# Define o título da janela como "Reprodutor de Música".
janela.title("Reprodutor de Música")

# Cria um painel (frame) para conter os botões de controle. Este painel 
# será adicionado à janela principal.
painel_controle = ttk.Frame(janela)

# Organiza (empacota) o painel na janela com um padding vertical de 20 pixels.
painel_controle.pack(pady=20)

# Cria um botão para tocar a música selecionada.
botao_tocar = ttk.Button(painel_controle, 
                         text="Tocar", 
                         command=tocar_selecionada)

# Posiciona o botão "Tocar" na primeira linha e primeira coluna do painel, com 
# um padding horizontal de 10 pixels.
botao_tocar.grid(row=0, column=0, padx=10)

# Cria um botão para parar a música que está tocando.
botao_parar = ttk.Button(painel_controle, 
                         text="Parar", 
                         command=parar_musica)

# Posiciona o botão "Parar" na primeira linha e segunda coluna do painel, ao lado
# do botão "Tocar".
botao_parar.grid(row=0, column=1, padx=10)

# Cria um botão para tocar a próxima música da lista.
botao_proximo = ttk.Button(painel_controle, 
                           text="Próxima", 
                           command=proxima_musica)

# Posiciona o botão "Próxima" na primeira linha e terceira coluna do painel.
botao_proximo.grid(row=0, column=2, padx=10)

# Cria um botão para tocar a música anterior da lista.
botao_anterior = ttk.Button(painel_controle, 
                            text="Anterior", 
                            command=musica_anterior)

# Posiciona o botão "Anterior" na primeira linha e quarta coluna do painel.
botao_anterior.grid(row=0, column=3, padx=10)

# Cria um botão para adicionar músicas à lista.
botao_adicionar = ttk.Button(janela, 
                             text="Adicionar Música", 
                             command=escolher_musica)

# Organiza (empacota) o botão na janela com um padding vertical de 20 pixels.
botao_adicionar.pack(pady=20)


# Cria uma lista visual (listbox) para mostrar as músicas
# adicionadas. Ela tem fundo preto, texto verde, largura 50 e 
# fonte Arial tamanho 14.
lista_interface = tk.Listbox(janela, 
                             bg="black", 
                             fg="green", 
                             width=50, 
                             font=('Arial', 14))

# Organiza (empacota) a lista na janela com um padding vertical de 20 pixels.
lista_interface.pack(pady=20)

# Instancia um objeto reprodutor da classe ReprodutorMusica, responsável 
# por gerenciar e tocar as músicas.
reprodutor = ReprodutorMusica()

# Inicia o loop principal da janela, mantendo-a aberta e interativa.
janela.mainloop()