print("Compreensão de Dicionários (Dictionary Comprehension)")
#Sintaxe Básica:

#{chave: valor for item in iterável}
#Suponha que queremos criar um dicionário onde as chaves 
#são números de 1 a 5 e os valores são seus quadrados.

quadrados = {x: x**2 for x in range(1, 6)}
print(quadrados)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
x=2
quadrados1 = x**2 if  x > 0 else x 
print(quadrados1)  #4


print("List Comprehensions",[x**2 for x in range(10)]) 


quadrados = {}

# Itera sobre os números de 1 a 5 (o intervalo vai até 6, mas o 6 não está incluído)
for x in range(1, 6):
    
    # Para cada número "x", cria uma entrada no dicionário com "x" como chave 
    # e o quadrado de "x" como valor
    quadrados[x] = x**2


    
print(quadrados)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#2. Converter chaves em valores e valores em chaves:

#Dado um dicionário, podemos querer inverter suas chaves e valores.
print("\nConverter chaves em valores e valores em chaves:")
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: chave for chave, valor in original.items()}
print(invertido)  # Output: {1: 'a', 2: 'b', 3: 'c'}

#Usando um loop for tradicional, ficaria assim:
print("\nUsando um loop for tradicional, ficaria assim:")
# Inicializa um dicionário chamado "original" com pares chave-valor
original = {"a": 1, "b": 2, "c": 3}
print(original)

# Inicializa um dicionário vazio chamado "invertido"
invertido = {}

# Itera sobre cada par chave-valor do dicionário "original"
for chave, valor in original.items():
    
    # Para cada par, adiciona uma entrada ao dicionário "invertido" 
    # com o "valor" como chave e a "chave" original como valor
    invertido[valor] = chave


print(invertido)  # Output: {1: 'a', 2: 'b', 3: 'c'}

print("\nqueremos filtrar apenas os produtos que custam mais de 50")
# Iniciando um dicionário chamado 'precos'
precos = {
    "laptop": 1000,       # Chave: "laptop", Valor: 1000
    "mouse": 25,          # Chave: "mouse", Valor: 25
    "monitor": 200,       # Chave: "monitor", Valor: 200
    "teclado": 30,        # Chave: "teclado", Valor: 30
    "cabo hdmi": 10       # Chave: "cabo hdmi", Valor: 10
}

print(precos)

caros = {produto: preco for produto, preco in precos.items() if preco > 50}
print(caros)  # Output: {'laptop': 1000, 'monitor': 200}

print("\nUsando um loop for tradicional, ficaria assim:")
# Inicializa um dicionário vazio chamado "caros"
caros = {}

# Itera sobre cada par chave-valor do dicionário "precos"
for produto, preco in precos.items():
    
    # Verifica se o "preco" é maior que 50
    if preco > 50:
        
        # Se o "preco" for maior que 50, adiciona a entrada correspondente ao dicionário "caros"
        caros[produto] = preco


print(caros)  # Output: {'laptop': 1000, 'monitor': 200}
 
print("\nDicionário com palavras e seus comprimentos")
#4. Dicionário com palavras e seus comprimentos:

#Dado uma lista de palavras, criar um dicionário com as 
#palavras como chaves e seus comprimentos como valores.

palavras = ["Python", "compreensão", "dicionário"]
print(palavras)
comprimentos = {palavra: len(palavra) for palavra in palavras}
print(comprimentos)  # Output: {'Python': 6, 'compreensão': 11, 'dicionário': 10}

#Usando um loop for tradicional, você faria o seguinte:
print("\nUsando um loop for tradicional, você faria o seguinte:")
palavras = ["Python", "compreensão", "dicionário"]

# Inicializa um dicionário vazio chamado "comprimentos"
comprimentos = {}

# Itera sobre cada "palavra" na lista "palavras"
for palavra in palavras:
    
    # Para cada "palavra", calcula o seu comprimento usando a função "len()"
    # e adiciona uma entrada ao dicionário "comprimentos" com a "palavra" como chave 
    # e seu comprimento como valor
    comprimentos[palavra] = len(palavra)


print(comprimentos)  # Output: {'Python': 6, 'compreensão': 11, 'dicionário': 10}
