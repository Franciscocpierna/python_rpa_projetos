#Abrir o arquivo de texto
arquivo = open('C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\Alunos.txt')
arquivoBlocoDeNotas = arquivo.readlines()

#for - para
#para cada linha do arquivoBlocoDeNotas
for linha in arquivoBlocoDeNotas:
    
    #Escola;Professora;ID;Aluno;Nota 1;Nota 2;Nota 3;Nota 4;Faltas
    #split - Quebra o texto em partes
    quebraLinha = linha.split(',')
    print()
    print(quebraLinha)
    
    #Faz uma única divisão e paga os itens a partir da coluna 1
    linha = [item.split(';', 1)[1] for item in quebraLinha]
    
    #Separando a linhas em colunas através o delimitador que é o ;
    separaLinhaEmColunas = linha[0].split(';')
    print(separaLinhaEmColunas)
    #Pego o nome do aluno que está na coluna 3 por que sempre começa na coluna 0
    nome = separaLinhaEmColunas[2]
    print()
    print()
    print(nome)