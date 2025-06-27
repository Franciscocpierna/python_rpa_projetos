# Importando a biblioteca tkinter para criação
        # de interfaces gráficas.
import tkinter as tk

# Importa a classe StringVar, usada para armazenar 
        # strings em aplicações Tkinter.
from tkinter import StringVar

# Importa a classe datetime do módulo datetime 
        # para trabalhar com datas e horas.
from datetime import datetime

# Importa a biblioteca pytz, que permite 
        # trabalhar com fusos horários.
import pytz

# Define a classe RelogioMundialApp, que criará o 
        # aplicativo do relógio mundial.
class RelogioMundialApp:
    
    # Método construtor, chamado automaticamente ao 
            # criar uma instância da classe.
    def __init__(self, janela):
        
        # Atribui o objeto tk.Tk() recebido ao atributo self.janela. 
                # Este objeto representa a janela principal do aplicativo.
        self.janela = janela
        
        # Configura o título da janela principal.
        self.janela.title("Relógio Mundial")
        
        # Define as dimensões da janela principal (900 pixels de 
                # largura por 500 pixels de altura).
        self.janela.geometry("900x500")
        
        # Configura a cor de fundo da janela principal 
                # para um tom escuro de azul.
        self.janela.configure(bg="#1E2A38")  # Cor de fundo escura


        # Dicionário que armazena os fusos horários e 
                # seus respectivos identificadores.
        # Cada cidade é mapeada ao seu identificador de 
                # fuso horário correspondente.
        self.fusos_horarios = {
            'UTC': 'Etc/UTC',
            'Nova Iorque': 'America/New_York',
            'São Paulo': 'America/Sao_Paulo',
            'Londres': 'Europe/London',
            'Paris': 'Europe/Paris',
            'Tóquio': 'Asia/Tokyo',
            'Sidney': 'Australia/Sydney'
        }


        # Definição de variáveis para armazenamento dos 
                # dados de tempo e data.
        # Variáveis do tipo StringVar são usadas em interfaces 
                # gráficas Tkinter para armazenar strings de uma 
                # maneira que o Tkinter possa monitorar 
                # automaticamente por mudanças.
        # Isso é útil porque permite que a interface gráfica 
                # atualize automaticamente quando os valores 
                # dessas variáveis mudam.
        # Aqui, são criados dois dicionários usando 
                # dictionary comprehensions.
        
        # Dicionário self.relogio_vars armazena as variáveis de 
                # tempo para cada fuso horário.
        # Cada chave é o nome de uma cidade e cada valor é uma 
                # instância de StringVar, que irá armazenar o 
                # horário atual para aquele fuso horário.
        self.relogio_vars = {nome: StringVar() for nome in self.fusos_horarios.keys()}
        
        # Dicionário self.data_vars armazena as variáveis de 
                # data para cada fuso horário.
        # Similarmente ao dicionário de relógio_vars, cada 
                # chave é o nome de uma cidade e cada valor é uma 
                # instância de StringVar, que irá armazenar a 
                # data atual para aquele fuso horário.
        self.data_vars = {nome: StringVar() for nome in self.fusos_horarios.keys()}
        
        # Configuração do layout da interface gráfica.
        # Chama o método self.configurar_layout() que 
                # está definido na classe.
        # Este método é responsável por organizar visualmente os 
                # componentes da interface, como labels, botões, etc.
        # Configura todos os elementos gráficos que serão 
                # mostrados ao usuário.
        self.configurar_layout()
        
        # Inicialização do método que atualiza o relógio.
        # Chama o método self.atualizar_relogio() que também 
                # está definido na classe.
        # Este método é crucial porque é responsável por 
                # manter o relógio atualizado.
        # Ele faz isso ao redefinir continuamente os valores 
                # de self.relogio_vars e self.data_vars com os 
                # tempos e datas corretos a cada segundo.
        # O método utiliza a função 'after' do Tkinter para se 
                # chamar repetidamente a cada 1000 milissegundos 
                # (ou seja, a cada segundo).
        self.atualizar_relogio()


    # Definição do método configurar_layout dentro da 
            # classe RelogioMundialApp.
    # Este método é responsável por configurar e organizar 
            # visualmente todos os componentes da interface 
            # gráfica do usuário (GUI).
    def configurar_layout(self):
        
        # Dicionários que definem os estilos para os 
                # rótulos da interface.
        # 'estilo_rotulo' define o estilo padrão para os 
                # rótulos com fonte Arial, tamanho 14, negrito, 
                # fundo escuro (#1E2A38) e texto branco (#FFFFFF).
        estilo_rotulo = {'font': ("Arial", 14, 'bold'), 'bg': "#1E2A38", 'fg': "#FFFFFF"}
        
        # 'estilo_info' é semelhante ao 'estilo_rotulo', mas com a 
                # cor do texto em azul claro (#B0BEC5), usado para 
                # informações menos importantes ou detalhadas.
        estilo_info = {'font': ("Arial", 14), 'bg': "#1E2A38", 'fg': "#B0BEC5"}
        
        # 'estilo_hora' é usado especificamente para exibir 
                # horas, destacando-as com a cor azul (#00C1D2), 
                # indicativo de sua importância.
        estilo_hora = {'font': ("Arial", 14, 'bold'), 'bg': "#1E2A38", 'fg': "#00C1D2"}
        
        # Criação de um widget Label (rótulo) que serve como 
                # título da aplicação.
        # 'self.titulo' armazena o widget, que exibe o 
                # texto "Relógio Mundial".
        # O título usa a fonte Arial tamanho 18 em negrito, com o 
                # mesmo esquema de cores do fundo e texto 
                # definido em 'estilo_rotulo'.
        self.titulo = tk.Label(self.janela, 
                               text="Relógio Mundial", 
                               font=("Arial", 18, 'bold'), 
                               bg="#1E2A38", 
                               fg="#FFFFFF")
        
        # O método 'pack' é usado para adicionar o 
                # widget de título à janela.
        # 'pady=10' adiciona um espaçamento vertical de 10 
                # pixels acima e abaixo do título para separá-lo 
                # visualmente dos outros componentes da interface.
        self.titulo.pack(pady=10)
    
        # Criação de um Frame (quadro), que é um 
                # container para outros widgets.
        # 'frame_relogio' é usado para agrupar e organizar 
                # visualmente os componentes relacionados ao 
                # relógio, como os rótulos para cada fuso horário.
        # O Frame usa o mesmo esquema de cores de fundo 
                # definido para os rótulos.
        frame_relogio = tk.Frame(self.janela, bg="#1E2A38")
        
        
        # O método 'pack' adiciona 'frame_relogio' à janela principal.
        # 'pady=20' proporciona um espaçamento vertical 
                # de 20 pixels acima e abaixo do frame para 
                # evitar que os elementos fiquem visualmente amontoados.
        frame_relogio.pack(pady=20)


        # Criação de rótulos para cada fuso horário especificado 
                # no dicionário self.fusos_horarios.
        # Um loop 'for' é usado para iterar sobre os itens do 
                # dicionário self.fusos_horarios, que contém os 
                # nomes das cidades e seus respectivos fusos.
        for i, (cidade, _) in enumerate(self.fusos_horarios.items()):
            
            # Cria um novo Frame para cada cidade dentro do 
                    # frame_relogio. Este frame contém o nome da 
                    # cidade, a hora e a data.
            # 'bg="#1E2A38"' define a cor de fundo do frame 
                    # para um azul escuro.
            # O método grid é usado para posicionar cada frame 
                    # em uma nova linha (row=i) e na primeira 
                    # coluna (column=0) dentro do frame_relogio.
            # 'padx=20' e 'pady=5' adicionam espaçamento horizontal 
                    # de 20 pixels e vertical de 5 pixels ao redor do frame.
            # 'sticky=tk.W' alinha o frame à esquerda (West) dentro da grid.
            frame = tk.Frame(frame_relogio, bg="#1E2A38")
            frame.grid(row=i, column=0, padx=20, pady=5, sticky=tk.W)
            
            # Criação do Label para o nome da cidade. 'text=cidade' 
                    # usa o nome da cidade do dicionário como texto do label.
            # '**estilo_rotulo' aplica o estilo definido anteriormente 
                    # para os rótulos, incluindo fonte, cor de fundo e 
                    # cor de texto.
            # Este label é colocado na primeira coluna (column=0) 
                    # do frame e alinhado à esquerda.
            # 'padx=10' e 'pady=5' adicionam um espaçamento 
                    # interno ao redor do label.
            label_nome = tk.Label(frame, text=cidade, **estilo_rotulo)
            label_nome.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
            
            # Criação do Label para a hora. 'textvariable=self.relogio_vars[cidade]' 
                    # vincula este label a uma variável StringVar que 
                    # contém a hora atualizada do fuso horário.
            # '**estilo_hora' aplica um estilo visual específico 
                    # para a exibição das horas.
            # Este label é colocado na segunda coluna (column=1) 
                    # do frame e alinhado à esquerda.
            label_hora = tk.Label(frame, textvariable=self.relogio_vars[cidade], **estilo_hora)
            label_hora.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
            
            # Criação do Label para a data. 'textvariable=self.data_vars[cidade]' 
                    # vincula este label a uma variável StringVar que 
                    # contém a data atualizada.
            # '**estilo_info' aplica um estilo visual que é um pouco 
                    # menos proeminente que o estilo_hora, indicado para 
                    # informações adicionais como a data.
            # Este label é colocado na terceira coluna (column=2) do 
                    # frame e alinhado à esquerda.
            label_data = tk.Label(frame, textvariable=self.data_vars[cidade], **estilo_info)
            label_data.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)


    # Definição do método 'atualizar_relogio' dentro da 
            # classe 'RelogioMundialApp'.
    def atualizar_relogio(self):
        
        # Descrição do método: atualiza o horário exibido para 
                # cada cidade listada nos fusos horários e agenda a 
                # si mesmo para rodar novamente a cada segundo.
        """Atualiza o relógio para cada fuso horário e agenda uma atualização a cada segundo."""
        
        # Laço 'for' que percorre cada par de chave-valor no 
                # dicionário 'self.fusos_horarios'.
        # 'cidade' é a chave (nome da cidade) e 'fuso' é o 
                # valor (identificador do fuso horário).
        for cidade, fuso in self.fusos_horarios.items():
            
            # Obtém o objeto de fuso horário correspondente ao 
                    # identificador do fuso usando a biblioteca 'pytz'.
            timezone = pytz.timezone(fuso)
            
            # Obtém a data e hora atuais para o fuso horário 
                    # especificado.
            agora = datetime.now(timezone)
            
            # Formata a hora atual no formato de 
                    # hora: minuto: segundo (HH:MM:SS).
            hora_atual = agora.strftime('%H:%M:%S')
            
            # Formata a data atual no formato 'dia da semana, dia 
                    # do mês de mês de ano'.
            data_atual = agora.strftime('%A, %d de %B de %Y')  # Dia da semana, dia do mês e ano em português
            
            # Chama o método 'traduzir_data' para converter os 
                    # nomes dos dias da semana e meses para o português.
            data_atual = self.traduzir_data(data_atual)
            
            # Atualiza a variável StringVar correspondente ao 
                    # horário da cidade no dicionário 'self.relogio_vars'.
            self.relogio_vars[cidade].set(hora_atual)
            
            # Atualiza a variável StringVar correspondente à data da 
                    # cidade no dicionário 'self.data_vars'.
            self.data_vars[cidade].set(data_atual)
        
        # Agenda a execução deste mesmo método ('self.atualizar_relogio') 
                # para daqui a 1000 milissegundos (1 segundo).
        # Isso cria um loop que faz com que o relógio seja atualizado continuamente.
        # Atualiza o relógio a cada 1000 milissegundos (1 segundo)
        self.janela.after(1000, self.atualizar_relogio)


    # Definição do método 'traduzir_data' dentro da classe 'RelogioMundialApp'.
    # O objetivo deste método é traduzir os nomes dos dias da semana e 
                # dos meses do inglês para o português.
    def traduzir_data(self, data):
        
        # Descrição do propósito do método. Este comentário explica que o 
                # método modifica a string de data para substituir nomes 
                # em inglês por equivalentes em português.
        """Traduz o dia da semana e o mês para português."""
    
        # Dicionário contendo as traduções dos dias da semana e dos 
                # meses do ano do inglês para o português.
        # As chaves do dicionário são os termos em inglês e os valores 
                # são os equivalentes em português.
        traducoes = {
            'Monday': 'Segunda-feira',
            'Tuesday': 'Terça-feira',
            'Wednesday': 'Quarta-feira',
            'Thursday': 'Quinta-feira',
            'Friday': 'Sexta-feira',
            'Saturday': 'Sábado',
            'Sunday': 'Domingo',
            'January': 'Janeiro',
            'February': 'Fevereiro',
            'March': 'Março',
            'April': 'Abril',
            'May': 'Maio',
            'June': 'Junho',
            'July': 'Julho',
            'August': 'Agosto',
            'September': 'Setembro',
            'October': 'Outubro',
            'November': 'Novembro',
            'December': 'Dezembro'
        }
    
        # Laço de repetição que percorre cada par de chave-valor no 
                # dicionário 'traducoes'.
        # 'ingles' representa a chave (termo em inglês) e 'portugues' 
                # representa o valor (termo em português).
        for ingles, portugues in traducoes.items():
            
            # O método 'replace' é chamado sobre a string 'data'.
            # Ele substitui todas as ocorrências do termo em inglês (chave) 
                    # pelo termo em português (valor) dentro da string.
            data = data.replace(ingles, portugues)
    
        # O método retorna a string 'data' após todas as substituições 
                # terem sido feitas.
        return data



# Esta condição verifica se o script está sendo executado 
        # como o programa principal.
# '__name__' é uma variável especial do Python que é definida 
        # como '__main__' quando o script é executado diretamente.
# Isso não acontece quando o script é importado como um 
        # módulo em outro script.
if __name__ == "__main__":
    
    # Criação da janela principal da aplicação utilizando a 
            # biblioteca tkinter.
    # 'tk.Tk()' inicializa a janela principal do Tkinter, que 
            # servirá como a janela raiz da aplicação.
    janela_principal = tk.Tk()
    
    # Criação de uma instância da classe 'RelogioMundialApp'.
    # 'app_relogio_mundial' é o objeto que representa nossa aplicação. 
    # O objeto recebe 'janela_principal', que é a janela raiz, 
            # como parâmetro para a inicialização.
    app_relogio_mundial = RelogioMundialApp(janela_principal)
    
    # Chamada do método 'mainloop()' sobre o objeto 'janela_principal'.
    # 'mainloop()' é um método do Tkinter que inicia o loop de 
            # eventos da interface gráfica.
    # Este loop espera por eventos, como cliques do mouse e 
            # entradas do teclado, e os processa enquanto a 
            # aplicação estiver rodando.
    # É essencial para a janela permanecer aberta e responsiva.
    janela_principal.mainloop()