"""
Uma matriz de strings é basicamente uma lista de listas em 
que cada elemento interno é uma string. Vamos a um exemplo prático:

Vamos considerar uma matriz 2x2, onde cada elemento é uma string 
representando um nome de animal:

    Coluna 0    Coluna 1
0   "Gato"     "Cachorro"
1   "Pássaro"  "Peixe"

"""


# Criar e imprimir essa matriz:

# Criando a matriz 2x2 de strings
animais = [
    ["Gato", "Cachorro"],
    ["Pássaro", "Peixe"]
]

print(animais)
for linha in range(2):
    
    for coluna in range(2):
        print(animais[linha][coluna], end=" ")
        print()

print()
print(animais)       
for linha in animais:
    
    # Extrai o nome do aluno da lista atual
    print(linha[0])
    
    # Extrai as notas do aluno da lista atual
    print(linha[1:])
    #print(linha[1])
# Criando a matriz 4x4
nomes = [
    ["Ana", "Bruno", "Carlos", "Alice"],
    ["Amanda", "Beatriz", "Clara", "Arnaldo"],
    ["Alfredo", "Bianca", "Cesar", "Ariel"],
    ["Alberto", "Beto", "Camila", "Adriana"]
]
nomes_a=[] 
print(nomes)    
for linha in range(4):   
   for coluna in range(4):
       print(nomes[linha][coluna][0])
       if nomes[linha][coluna][0]=="A":
            print(nomes[linha][coluna][0]) 
            nomes_a.append(nomes[linha][coluna])  
            print(nomes[linha][coluna])   
            
print(nomes_a)            

matriz_pessoas = [
    [["Ana", 25], ["Bruno", 31], ["Carlos", 29], ["Alice", 34]],  # Primeira linha da matriz
    [["Amanda", 22], ["Beatriz", 45], ["Clara", 30], ["Arnaldo", 27]],  # Segunda linha da matriz
    [["Alfredo", 35], ["Bianca", 28], ["Cesar", 32], ["Ariel", 23]],  # Terceira linha da matriz
    [["Alberto", 40], ["Beto", 24], ["Camila", 21], ["Adriana", 37]]  # Quarta linha da matriz
]
print("os nomes das pessoas com mais de 30 anos")
for linha in range(4):
    for coluna in range(4):
        if  matriz_pessoas[linha][coluna][1] > 30:
          print(matriz_pessoas[linha][coluna][0]," ",matriz_pessoas[linha][coluna][1], end=" ")
          print()
          
          