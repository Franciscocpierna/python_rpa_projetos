nome = "Alice"
idade = 25
altura = 1.65
mensagem = f"Olá, meu nome é {nome}. tenho {idade} anos e Altura {altura:.2f}"
print(mensagem)
print(mensagem.upper()) # função upper() para deixar a mensagem em maiúsculo
print(mensagem.lower()) # função lower() para deixar a mensagem em minúsculo
print(mensagem.capitalize()) # função capitalize() para deixar a primeira letra em maiúsculo
print(mensagem.title()) # função title() para deixar a primeira letra de cada palavra em maiúsculo
print(mensagem.swapcase()) # função swapcase() para inverter as letras maiúsculas e minúsculas
print(mensagem.replace("Alice", "Bob")) # função replace() para substituir uma palavra por outra
print(mensagem.count("a")) # função count() para contar quantas vezes uma letra aparece
print(mensagem.find("Alice")) # função find() para encontrar a posição de uma palavra
print(mensagem.startswith("Olá")) # função startswith() para verificar se a mensagem começa com uma palavra
print(mensagem.endswith("altura")) # função endswith() para verificar se a mensagem termina com uma palavra
print(mensagem.split()) # função split() para separar a mensagem em palavras

palavra = "python versao 3.13.2"
palavra1 = palavra.split()[0]	
print(palavra1) # python
palavra2 = palavra.split()[1]
print(palavra2) # versao
palavra3 = palavra.split()[2]
print(palavra3) # 3.13.2
print(palavra3.split(".")[0]) # 3 # pegando a primeira parte da versão
print(palavra3.split(".")[1]) # 13 # pegando a segunda parte da versão
print(palavra3.split(".")[2]) # 2 # pegando a terceira parte da versão
print(palavra3.split(".")[0:2]) # ['3', '13'] # pegando a primeira e a segunda parte da versão