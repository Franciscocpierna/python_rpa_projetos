frase = "ola estou  aqui python"
print("python" in frase) #True
print("python" not in frase) # False


posicao = frase.find("python")
print(posicao) # 16
posicao1 = "python" in frase # True
 
print(posicao1) # True
print(frase[posicao:posicao+6]) # python
print(frase[posicao:]) # python

posicao2 = "python"
print(posicao2[0])
for i in posicao2:
    print(i)
pos = 0
print("************************")
print(len(posicao2))
while  pos < len(posicao2): 
     print(posicao2[pos])
     pos += 1
if "python" in frase:
    print("Existe")
    
print("************************")   
print(frase.count("python")) # 1
print(frase.count("o")) # 3

campo = "olá, mundo"
parte = campo[4:8]
print(parte) # mund


print(campo[4:]) # mundo
print(campo[:4]) # olá,
print(campo[:]) # olá, mundo
print(campo[::2]) # o, ud
print(campo[1::2]) # lá mn

print(campo[:-6]) # olá 
print(campo[-6:]) # mundo    
print(campo[:5]) # olá, 
print(campo[5:]) # mundo

palvras = campo.split(",")
print(palvras) # ['olá', ' mundo']
palvras = campo.split()# separa por espaço
print(palvras) # ['olá,', 'mundo']

palavras= ["olá", "mundo"]
frase5 = " ".join(palavras)# separa por espaço
print(frase5) # olá mundo
frase6 = "-".join(palavras)# separa por - 
print(frase6) # olá-mundo

texto = "*********ola*********"
print(texto.strip("*")) # ola
print(texto.lstrip("*")) # ola********* 
print(texto.rstrip("*")) # *********ola
print(texto.replace("*", "")) # ola

texto = "   ola  "
print(texto.strip()) # ola remove espaços