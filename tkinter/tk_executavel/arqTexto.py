#Caminho para abrir o arquivo de texto
arquivo = open("C:\\python_projetos\\python_rpa_projetos\\tkinter\\tk_executavel\\CEP.txt")
arquivoBlocoDeNotas = arquivo.readlines()

#for - para
for linha in arquivoBlocoDeNotas:
    
    #Remove a quebra de linhas
    linha = linha.rstrip("\n")
    print(linha)