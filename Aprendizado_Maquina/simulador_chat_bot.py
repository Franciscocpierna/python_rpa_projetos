# Importar o módulo Tkinter para a criação da interface gráfica
import tkinter as tk

# Importar a função de distância de Levenshtein da biblioteca Levenshtein
# Esta função será usada para calcular a distância entre duas strings, o 
# que é útil para a correção de texto
from Levenshtein import distance as levenshtein_distance

# Importar o módulo de expressões regulares (re)
# Este módulo permite operações avançadas de manipulação de strings usando 
# expressões regulares
import re

# Dicionário de respostas predefinidas
respostas = {
    'bom dia': 'Bom dia! Como posso ajudá-lo?',
    'boa tarde': 'Boa tarde! Como posso ajudá-lo?',
    'boa noite': 'Boa noite! Como posso ajudá-lo?',
    'olá': 'Olá! Como posso ajudá-lo?',
    'oi': 'Oi! Como posso ajudá-lo?',
    'como você está': 'Estou funcionando conforme programado. E você?',
    'qual seu nome': 'Eu sou um chatbot e não tenho um nome.',
    'o que você faz': 'Eu estou aqui para responder suas perguntas e ajudá-lo.',
    'você é um robô': 'Sim, eu sou um programa de computador projetado para conversar com você.',
    'adeus': 'Até logo! Se precisar, estarei aqui.',
    'tchau': 'Tchau! Foi bom conversar com você.',
    'quem te criou': 'Fui criado por um programador.',
    'você gosta de música': 'Não tenho preferências, sou apenas um programa.',
    'você pode me ajudar': 'Claro, em que posso ajudá-lo?',
    'como funciona': 'Você faz perguntas e eu tento responder da melhor forma possível.',
    'você é inteligente': 'Eu tento ser o mais útil possível.',
    'você tem sentimentos': 'Não, eu sou apenas um conjunto de algoritmos.',
    'qual a sua idade': 'A idade não se aplica a mim.',
    'você está vivo': 'Não, eu sou apenas um programa de computador.',
    'como está o tempo': 'Não posso acessar a internet, então não sei como está o tempo.',
    'você gosta de café': 'Não tenho preferências ou gostos.',
    'qual é o seu filme favorito': 'Não assisto filmes, sou apenas um programa.',
    'você pode aprender': 'Eu não tenho a capacidade de aprender, sou programado para responder com base em um conjunto predefinido de respostas.',
    'você é feliz': 'Não tenho emoções.',
    'você é casado': 'Não, eu sou apenas um programa de computador.',
    'você tem filhos': 'Não, eu não tenho a capacidade de ter filhos.',
    'você tem amigos': 'Não, eu sou apenas um programa isolado.',
    'onde você mora': 'Eu existo em um servidor.',
    'você pode me contar uma piada': 'Por que os programadores preferem o escuro? Porque a luz atrai bugs.',
    'você é humano': 'Não, eu sou uma máquina.',
    'qual é o seu esporte favorito': 'Não tenho um esporte favorito, sou apenas um programa.',
    'você gosta de viajar': 'Não posso viajar, estou confinado a um servidor.',
    'você pode dirigir': 'Não, eu não tenho essa capacidade.',
    'você come': 'Não, eu não preciso de comida.',
    'você dorme': 'Não, eu estou sempre ativo.',
    'você pode cantar': 'Não, eu não tenho essa funcionalidade.',
    'você tem um animal de estimação': 'Não, eu não posso cuidar de animais de estimação.',
    'você gosta de ler': 'Não posso ler no sentido humano, mas posso processar texto.',
    'você pode dançar': 'Não, eu não tenho forma física para dançar.',
    'qual é o seu trabalho': 'Estou programado para conversar e fornecer respostas com base no meu conjunto de dados.',
    'você gosta de música': 'Não tenho a capacidade de gostar ou desgostar de música.',
    'você pode ver': 'Não, eu não tenho sensores visuais.',
    'qual é o seu nome': 'Eu sou um chatbot sem um nome específico.',
    'você gosta de matemática': 'Eu sou programado para processar números, mas não tenho preferências.',
    'você pode ler minha mente': 'Não, eu não tenho essa capacidade.',
    'você é inteligente': 'Minha inteligência é limitada ao que fui programado para fazer.',
    'você pode me ajudar com a lição de casa': 'Depende da pergunta, posso tentar ajudar.',
    'você pode fazer café': 'Não, eu não tenho capacidades físicas.',
    'você pode abrir a porta': 'Não, eu não posso interagir fisicamente com o ambiente.',
    'você tem um celular': 'Não, eu não tenho dispositivos físicos.',
    'como você foi criado': 'Fui criado usando algoritmos de programação.',
    'você pode ficar doente': 'Não, eu não tenho uma forma biológica.',
    'você pode ir à escola': 'Não, mas posso fornecer informações que são ensinadas nas escolas.',
    'qual é o seu hobby': 'Eu não tenho hobbies, estou aqui para responder perguntas.',
    'você tem um carro': 'Não, eu não tenho bens físicos.',
    'você pode voar': 'Não, eu não tenho capacidades físicas.',
    'você pode nadar': 'Não, eu não interajo com o ambiente físico.',
    'você pode correr': 'Não, eu não tenho forma física.',
    'você pode pular': 'Não, eu não tenho a capacidade de movimento.'

}

# Função para encontrar a melhor resposta para uma dada mensagem
def encontrar_melhor_resposta(mensagem, respostas):
    
    # Inicializar a melhor resposta como uma mensagem padrão e a melhor pontuação como 0
    melhor_resposta = 'Desculpe, não entendi essa pergunta.'
    melhor_pontuacao = 0
    
    # Iterar sobre cada par pergunta-resposta no dicionário 'respostas'
    for pergunta, resposta in respostas.items():
        
        # Usar expressões regulares para encontrar todas as palavras na 
        # pergunta e convertê-las para minúsculas
        # O resultado é um conjunto de palavras únicas
        
        """
            pergunta.lower(): Este método converte toda a string pergunta para letras
            minúsculas. Isso é feito para garantir que a comparação das palavras seja
            insensível a maiúsculas e minúsculas.

            re.findall(r'\b\w+\b', ...): Aqui, o método findall da biblioteca 
                re (Regular Expression) é utilizado para encontrar todas as ocorrências 
                que combinam com a expressão regular fornecida. A expressão 
                regular \b\w+\b faz o seguinte:
                
                    \b: Corresponde à posição entre um caractere de palavra 
                    (geralmente [a-zA-Z0-9_]) e um caractere não-palavra. Ele atua 
                    como um delimitador de palavra.
                    
                    \w+: Corresponde a um ou mais caracteres de palavra 
                    (geralmente [a-zA-Z0-9_]).
                    
                    \b: Outro delimitador de palavra.

        Portanto, essa expressão regular captura palavras inteiras na string, 
        ignorando espaços, pontuação e outros caracteres especiais.

            set(...): Finalmente, o resultado de re.findall() é uma lista de palavras, 
            que é então convertida em um conjunto (set) para eliminar palavras 
            duplicadas (se houver) e para facilitar a comparação de palavras posteriormente.
        """
        palavras_pergunta = set(re.findall(r'\b\w+\b', pergunta.lower()))
        
        # Fazer o mesmo para a mensagem recebida
        palavras_mensagem = set(re.findall(r'\b\w+\b', mensagem.lower()))
        
        
        # Calcular a pontuação como o número de palavras em comum entre a pergunta e a mensagem
        """
            palavras_pergunta.intersection(palavras_mensagem): Este é um método de 
            conjuntos que retorna um novo conjunto contendo todos os elementos que 
            são comuns entre palavras_pergunta e palavras_mensagem. Em outras 
            palavras, ele identifica as palavras que aparecem tanto na pergunta 
            predefinida (palavras_pergunta) quanto na mensagem do 
            usuário (palavras_mensagem).

            len(...): A função len() é usada para obter o número de elementos no 
            conjunto resultante da interseção. Esse número representa o quanto a 
            mensagem do usuário e a pergunta predefinida são semelhantes, em termos 
            de palavras comuns.
        """
        pontuacao = len(palavras_pergunta.intersection(palavras_mensagem))
        
        # Se a pontuação calculada for maior que a melhor pontuação até agora,
        # atualizar a melhor pontuação e a melhor resposta
        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_resposta = resposta
            
    # Retornar a melhor resposta encontrada
    return melhor_resposta
        
        
        

# Definindo a função que será chamada quando uma mensagem for enviada
def enviar_mensagem():
    
    # Pegando o texto da caixa de entrada
    mensagem = entrada.get()
    
    # Verificar se a mensagem está vazia; se estiver, sair da função
    if not mensagem:
        return
    
    # O número 790 representa a coordenada x onde o texto será desenhado no canvas.
    # Isso significa que o texto será posicionado mais à direita no canvas.
    
    # Adicionar a mensagem do usuário ao widget Canvas. O texto será alinhado à direita e será azul.
    # O 'canvas.y' é uma variável personalizada que mantém a posição vertical atual no canvas
    # tags é usada para associar uma ou mais etiquetas (tags) a um item criado em um widget 
    # Canvas. As tags são basicamente strings que você pode usar para identificar, atualizar,
    # ou manipular o item mais tarde.
    canvas.create_text(790, canvas.y, text=mensagem, font=("Arial", 20), anchor='e', tags='texto', fill='blue')
    
    # Aumentar o valor da posição vertical no canvas, para que a próxima 
    # mensagem apareça abaixo da anterior
    canvas.y += 30

    # Chamando a função 'encontrar_melhor_resposta' para obter a resposta mais 
    # adequada para a mensagem do usuário
    resposta = encontrar_melhor_resposta(mensagem, respostas)
    
    # Adicionar a resposta do chatbot ao Canvas. O texto será alinhado à esquerda e será verde.
    # tags é usada para associar uma ou mais etiquetas (tags) a um item criado em um widget 
    # Canvas. As tags são basicamente strings que você pode usar para identificar, atualizar,
    # ou manipular o item mais tarde.
    canvas.create_text(20, canvas.y, font=("Arial 20"), text=resposta, anchor='w', tags='texto', fill='green')
    
    # Aumentar o valor da posição vertical no canvas, para que a próxima mensagem apareça abaixo da anterior
    canvas.y += 30

    # Limpar o texto da caixa de entrada, preparando-a para a próxima mensagem do usuário
    entrada.delete(0, tk.END)
    

# Inicializar a janela Tkinter e dar um título a ela
janela = tk.Tk()
janela.title('Chatbot')

# Criar um Canvas (área de desenho) onde as mensagens serão exibidas
# Definir a cor de fundo como branca, e as dimensões como 500x400
canvas = tk.Canvas(janela, 
                   bg='white', 
                   width=500, 
                   height=400)

# Fazer o Canvas expandir para preencher qualquer 
# espaço disponível na janela
canvas.pack(expand=tk.YES, fill=tk.BOTH)

# Inicializar uma variável de coordenada y 
# no Canvas para manter o
# controle de onde colocar o próximo texto
canvas.y = 20

# Criar uma caixa de entrada (Entry widget) onde o usuário pode digitar sua mensagem
# Definir a fonte e o tamanho do texto na caixa de entrada
entrada = tk.Entry(janela, font=("Arial 20"), width=50)

# Posicionar a caixa de entrada na parte inferior esquerda da janela
entrada.pack(side=tk.LEFT, padx=10, pady=10)

# Criar um botão que o usuário pode pressionar para enviar uma mensagem
# Quando pressionado, este botão chamará a função enviar_mensagem
btn_enviar = tk.Button(janela, text='Enviar', command=enviar_mensagem, font=("Arial 20"))

# Posicionar o botão na parte inferior direita da janela
btn_enviar.pack(side=tk.RIGHT, padx=10, pady=10)

# Iniciar o loop principal da aplicação Tkinter, que mantém a janela 
# aberta e responde aos eventos do usuário
janela.mainloop()
