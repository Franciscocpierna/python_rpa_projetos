# Importar a biblioteca Tkinter para criar a interface gráfica
import tkinter as tk

from tkinter import ttk

# Importar a biblioteca de fontes do Tkinter para estilizar o texto da interface
from tkinter import font

from tkinter import Text

# Importar a biblioteca de expressões regulares para realizar operações de
# correspondência de texto
import re

# Importar a biblioteca requests para fazer chamadas de API HTTP
import requests

# Definir uma função chamada obter_cotacao_dolar para buscar a cotação atual do dólar
def obter_cotacao_dolar():
    
    # Definir a URL da API que fornece as taxas de câmbio
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    try:
        
        # Fazer uma chamada GET para a API para obter as taxas de câmbio
        # A flag verify=False é usada aqui para desativar a verificação 
        # SSL (não recomendado para produção)
        resposta = requests.get(api_url, verify=False)
        
        # Converter a resposta da API em um objeto JSON para fácil manipulação
        dados = resposta.json()
        
        # Retornar a taxa de câmbio do dólar em relação ao real brasileiro,
        # que está sob a chave 'BRL' no JSON
        return dados['rates']['BRL']
        
    
    # Capturar e manipular qualquer exceção que possa ocorrer durante o processo
    except Exception as e:
        
        # Retornar uma mensagem de erro informando o que deu errado
        return f"Erro ao obter cotação: {e}"
    
    
# Definir uma função chamada somar_numeros que aceita uma lista de números como argumento
def somar_numeros(numeros):
    
    # Utilizar a função built-in sum para somar todos os números na lista e 
    # retornar o resultado
    return sum(numeros)

# Definir uma função chamada subtrair_numeros que aceita uma lista de 
# números como argumento
def subtrair_numeros(numeros):
    
    # Subtrair a soma dos números a partir do segundo elemento da lista do primeiro número
    # A função sum é usada para somar todos os números da lista a partir do 
    # índice 1 (ou seja, números[1:])
    return numeros[0] - numeros[1]
    

    
# Definir uma função chamada multiplicar_numeros que aceita uma lista de
# números como argumento
def multiplicar_numeros(numeros):
    
    # Inicializar uma variável chamada resultado com o valor 1
    resultado = 1
    
    # Utilizar um loop for para iterar sobre cada número na lista de números
    for num in numeros:
        
        # Multiplicar o valor atual de resultado pelo número atual na lista
        # resultado = resultado * num
        resultado *= num
    
    # Retornar o resultado final da multiplicação
    return resultado


# Definir uma função chamada dividir_numeros que aceita uma lista 
# de números como argumento
def dividir_numeros(numeros):
    
    # Tente executar o bloco de código seguinte
    try:
    
        # Inicializar uma variável chamada resultado com o valor
        # do primeiro número na lista
        resultado = numeros[0]
        
        # Utilizar um loop for para iterar sobre cada número na lista, 
        # começando pelo segundo número (índice 1)
        for num in numeros[1:]:
            
            # Dividir o valor atual de resultado pelo número atual na lista
            resultado /= num
        
        # Retornar o resultado final da divisão
        return resultado
    
    # Capturar qualquer erro de divisão por zero
    except ZeroDivisionError:
        
        # Retornar uma mensagem de erro informando que a divisão por zero não é permitida
        return "Divisão por zero não permitida"

    
def tratar_mensagem(mensagem):
    
    # Converter toda a mensagem para minúsculas
    # Isso torna a comparação de strings insensível a maiúsculas e minúsculas,
    # facilitando a identificação de palavras-chave.
    mensagem = mensagem.lower()
    
    # Usar expressões regulares para encontrar todos os números na mensagem.
    # A função re.findall retorna todas as ocorrências de dígitos na mensagem como uma lista de strings.
    # Essas strings são então convertidas para inteiros usando uma list comprehension.
    numeros = [int(x) for x in re.findall(r'\d+', mensagem)]
    
    # Inicializar uma lista vazia chamada 'respostas' para armazenar as respostas geradas.
    respostas = []
    
    # Verificar se a palavra "some" está presente na mensagem.
    if "some" in mensagem:
        
        # Se a lista 'numeros' não estiver vazia, calcular a soma dos números.
        if numeros:
            respostas.append(f"A soma dos números é {somar_numeros(numeros)}")
            
            
     # Verificar se a palavra "subtraia" está presente na mensagem.
    if "subtraia" in mensagem:
        
        # Se a lista 'numeros' não estiver vazia, calcular a subtração dos números.
        if numeros:
            respostas.append(f"A subtração dos números é {subtrair_numeros(numeros)}")
    
    # Verificar se a palavra "multiplique" está presente na mensagem.
    if "multiplique" in mensagem:
        
        # Se a lista 'numeros' não estiver vazia, calcular a multiplicação dos números.
        if numeros:
            respostas.append(f"A multiplicação dos números é {multiplicar_numeros(numeros)}")
            
            
    # Verificar se a palavra "divida" está presente na mensagem.
    if "divida" in mensagem:
        
        # Se a lista 'numeros' não estiver vazia, calcular a divisão dos números.
        if numeros:
            respostas.append(f"A divisão dos números é {dividir_numeros(numeros)}")
            
    
    # Verificar se a palavra "dólar" está presente na mensagem.
    if "dólar" in mensagem:
        
        # Obter a cotação atual do dólar e adicioná-la à lista de respostas.
        cotacao = obter_cotacao_dolar()
        respostas.append(f"A cotação atual do dólar é {cotacao} BRL")
        
        
    # Tratar a mensagem para destacar números e palavras-chave

    # Primeiro, a mensagem original é dividida em palavras 
    # individuais usando o método `split()`.
    # Isso cria uma lista de palavras.
    palavras = mensagem.split()

    # Inicializamos uma lista vazia chamada `palavras_tratadas` para
    # armazenar as palavras após o tratamento.
    palavras_tratadas = []

    # Usamos um loop `for` para iterar sobre cada palavra na lista `palavras`.
    for palavra in palavras:

        # Usamos a função `fullmatch` do módulo `re` para verificar se a
        # palavra é inteiramente composta de dígitos.
        # A expressão regular r'\d+' significa "um ou mais dígitos".
        if re.fullmatch(r'\d+', palavra):  # Se for um número

            # Se a palavra é um número, adicionamos colchetes em torno dela.
            # Usamos f-string para fazer isso de forma eficiente.
            palavras_tratadas.append(f"[{palavra}]")

        # Caso contrário, verificamos se a palavra é uma das 
        # palavras-chave especificadas: "some", "subtraia", "multiplique", "divida".
        elif palavra in ["some", "subtraia", "multiplique", "divida"]:

            # Se for uma palavra-chave, transformamos ela em maiúsculas para destacá-la.
            palavras_tratadas.append(palavra.upper())

        # Se a palavra não se encaixa em nenhuma das categorias acima, mantemos ela como está.
        else:

            # Adicionamos a palavra original à lista `palavras_tratadas`.
            palavras_tratadas.append(palavra)
            
            
        
    # Finalmente, unimos todas as palavras tratadas em uma única string,
    # separadas por espaços.
    # Usamos o método `join` para fazer isso.
    mensagem_tratada = " ".join(palavras_tratadas)


    # Configurar o Text widget para permitir modificações
    text_area.config(state=tk.NORMAL)
        
    # Adicionar a mensagem do usuário

    # `pos_fim_usuario` e `pos_inicio_usuario` armazenam a posição do cursor no widget de texto.
    # Isso é feito para saber onde a mensagem do usuário termina e onde a do bot começa.
    # `tk.INSERT` é uma constante que aponta para a posição atual do cursor no widget de texto.
    pos_fim_usuario = text_area.index(tk.INSERT)
    pos_inicio_usuario = text_area.index(tk.INSERT)

    # Adicionar a mensagem do bot

    # Verificamos se há alguma resposta gerada pelo bot. `respostas` é
    # uma lista que pode conter uma ou mais respostas.
    if respostas:

        # Unimos todas as respostas em uma única string, separadas por quebras de linha.
        resposta = "\n".join(respostas)

        # Inserimos a mensagem do bot no widget de texto, na posição do fim do texto (`tk.END`).
        # A mensagem é prefixada por "Bot:" para indicar que é o bot que está falando.
        text_area.insert(tk.END, f"Bot: {resposta}\n\n")

        # Obtemos a nova posição do cursor após inserir o texto do bot.
        pos_fim_bot = text_area.index(tk.INSERT)

        # Aplicamos a formatação de cor ao texto do bot.
        # Usamos o método `tag_add` para adicionar uma tag ("cor_bot") ao
        # texto entre `pos_fim_usuario` e `pos_fim_bot`.
        # Em seguida, usamos o método `tag_config` para definir a cor do texto
        # com essa tag como verde.
        text_area.tag_add("cor_bot", pos_fim_usuario, pos_fim_bot)
        text_area.tag_config("cor_bot", foreground="green")

    # Caso não haja resposta, inserimos uma mensagem padrão.
    else:
        text_area.insert(tk.END, "Bot: Desculpe, não entendi sua solicitação.\n\n")

    # Desativamos a edição do widget de texto para que o usuário não
    # possa modificar as mensagens.
    # Isso é feito definindo o estado do widget de texto como `tk.DISABLED`.
    text_area.config(state=tk.DISABLED)

    # Retornamos a resposta do bot como uma string, ou uma mensagem padrão
    # se não houver resposta.
    return "\n".join(respostas) if respostas else "Desculpe, não entendi sua solicitação."
        
        

        
    
# Definição da função `enviar_mensagem` que será chamada quando o
# usuário clicar no botão "Enviar"
def enviar_mensagem():
    
    # Obter o texto inserido pelo usuário no widget Entry e 
    # armazená-lo na variável `mensagem`
    mensagem = entrada.get()
    
    # Verificar se a mensagem está vazia. Se estiver, a função retorna e nada mais é feito
    if not mensagem:
        return
    
    # Ativar o widget Text para permitir a inserção de novas mensagens
    # Isso é feito mudando o estado do widget para NORMAL
    text_area.config(state=tk.NORMAL)
    
    # Inserir a mensagem do usuário no widget Text
    # A mensagem é prefixada com "Você: " para indicar que o usuário está falando
    text_area.insert(tk.END, f"Você: {mensagem}\n")
    
    # Chamar a função `tratar_mensagem` para processar a mensagem 
    # do usuário e obter uma resposta
    resposta = tratar_mensagem(mensagem)
    
    # Inserir a resposta do bot no widget Text e destacá-la em verde
    # Primeiro, obtemos a posição do cursor antes de inserir a resposta do bot
    inicio = text_area.index(tk.INSERT)
    
    # Inserir a resposta do bot no widget Text
    text_area.insert(tk.END, f"Bot: {resposta}\n")
    
    # Obter a posição do cursor após a inserção para saber onde a mensagem do bot termina
    fim = text_area.index(tk.INSERT)
    
    # Usar o método `tag_add` para adicionar uma tag ("resposta_bot") ao 
    # texto entre `inicio` e `fim`
    text_area.tag_add("resposta_bot", inicio, fim)
    
    # Configurar a tag "resposta_bot" para ter a cor de texto verde
    text_area.tag_config("resposta_bot", foreground="green")
    
    # Desativar o widget Text para evitar edições manuais
    # Isso é feito mudando o estado do widget para DISABLED
    text_area.config(state=tk.DISABLED)
    
    # Limpar o widget Entry para que o usuário possa inserir uma nova mensagem
    entrada.delete(0, tk.END)
    
    # Fazer com que o widget Text role para a parte mais recente do chat
    # Isso é útil quando o histórico do chat se torna muito longo
    text_area.see(tk.END)
    
    
# Inicializar a janela principal do Tkinter
janela = tk.Tk()

# Definir o título da janela
janela.title('Chatbot')

# Criar o widget Text para mostrar as mensagens
# O Text widget é uma área onde o texto pode ser exibido e/ou editado.
# Vamos definir a fonte como Arial com tamanho 14, o texto será quebrado por palavras (wrap=tk.WORD),
# e definir a largura e a altura em termos de caracteres e linhas, respectivamente.
text_area = Text(janela, font=("Arial 14"), wrap=tk.WORD, width=50, height=20)

# Empacotar o Text widget na janela principal (janela) e permitir que ele se expanda
# e preencha tanto a largura quanto a altura da janela (expand=tk.YES, fill=tk.BOTH).
# Isso permite que o widget Text ocupe todo o espaço disponível na janela.
text_area.pack(expand=tk.YES, fill=tk.BOTH)

# Desativar a edição no widget Text.
# Isso é feito configurando o estado do widget para DISABLED.
# Essa é uma boa prática para evitar que o usuário edite manualmente as mensagens no histórico do chat.
text_area.config(state=tk.DISABLED)

# Inicializar uma variável y no objeto Canvas para controlar a posição vertical das mensagens
# Isso ajudará a colocar as mensagens em posições diferentes na vertical
#canvas.y = 20

# Criar um campo de entrada de texto (Entry) para o usuário digitar suas mensagens
# Definir a fonte como Arial com tamanho 20 e a largura como 50 caracteres
entrada = tk.Entry(janela, font=("Arial", 20), width=50)

# Empacotar o campo de entrada na janela, alinhando-o à esquerda e adicionando padding
entrada.pack(side=tk.LEFT, padx=10, pady=10)


# Criar um botão para enviar a mensagem. Quando clicado, ele chamará a função enviar_mensagem
btn_enviar = tk.Button(janela, text='Enviar', command=enviar_mensagem)

# Empacotar o botão na janela, alinhando-o à direita e adicionando padding
btn_enviar.pack(side=tk.RIGHT, padx=10, pady=10)

# Iniciar o loop principal do Tkinter para manter a janela aberta
janela.mainloop()