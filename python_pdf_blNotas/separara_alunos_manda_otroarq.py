#Abrir o arquivo de texto
#calcula média e exibe o resultado
#Verifica se a professora é Carolina e exibe somente os alunos dela
#Passa os dados da professora Carolina para o arquivo arquivoProfessoraCarolina

#w - Escrever no arquivo de texto
#r - Ler os dados do arquivo de texto
arquivoProfessoraCarolina = open('C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\ProfessoraCarolina.txt', 'w')
arquivo = open('C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\Alunos.txt', 'r')
arquivoBlocoDeNotas = arquivo.readlines()

nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
faltas = 0

#for - para
#para cada linha do arquivoBlocoDeNotas
for linha in arquivoBlocoDeNotas:
    
    #Escola;Professora;ID;Aluno;Nota 1;Nota 2;Nota 3;Nota 4;Faltas
    #split - Quebra o texto em partes
    quebraLinha = linha.split(',')
    
    #print(quebraLinha)
    
    #Faz uma única divisão e paga os itens a partir da coluna 1
    linha = [item.split(';', 1)[1] for item in quebraLinha]
    
    #Separando a linhas em colunas através o delimitador que é o ;
    separaLinhaEmColunas = linha[0].split(';')
    
    #print(separaLinhaEmColunas)
    
    #Pego a posição 0 que é o nome da professora
    professora = separaLinhaEmColunas[0]  
    
    if professora == "Carolina":
        
        print("Professora: ", professora)
    
        #Pego o nome do aluno que está na coluna 3 por que sempre começa na coluna 0
        nome = separaLinhaEmColunas[2]    


        #Eu verifico se é o titulo
        if separaLinhaEmColunas[3] == "Nota 1":

            #print(nome)
            print("------ Título ---------")

        #Faço os calculos e tratamento a partir da segunda linha
        else:

            print(nome)

            nota1 = int(separaLinhaEmColunas[3])
            nota2 = int(separaLinhaEmColunas[4])
            nota3 = int(separaLinhaEmColunas[5])
            nota4 = int(separaLinhaEmColunas[6])
            faltas = int(separaLinhaEmColunas[7])

            print("Nota 1: ", nota1)
            print("Nota 2: ", nota2)
            print("Nota 3: ", nota3)
            print("Nota 4: ", nota4)
            print("Faltas: ", faltas)

            media = (nota1 + nota2 + nota3 + nota4) / 4

            print("Média: ", media)

            if faltas >= 4:

                print("Reprovado(a) por falta")
                
                #Escrevendo os itens e o resultado no arquivo de texto
                arquivoProfessoraCarolina.write(nome + ', Média: ' + str(media) + ', Faltas: ' + str(faltas) + ' - Reprovado(a) por falta\n')

            else:

                #if - Se / elif - Senão Se
                if media >= 6:

                    print("Aprovado(a)")
                    
                    #Escrevendo os itens e o resultado no arquivo de texto
                    arquivoProfessoraCarolina.write(nome + ', Média: ' + str(media) + ', Faltas: ' + str(faltas) + ' - Aprovado(a)\n')


                elif media >= 4:

                    print("Recuperação")
                    
                    #Escrevendo os itens e o resultado no arquivo de texto
                    arquivoProfessoraCarolina.write(nome + ', Média: ' + str(media) + ', Faltas: ' + str(faltas) + ' - Recuperação\n')


                else:

                    print("Reprovado(a) por Média")
                    
                    #Escrevendo os itens e o resultado no arquivo de texto
                    arquivoProfessoraCarolina.write(nome + ', Média: ' + str(media) + ', Faltas: ' + str(faltas) + ' - Reprovado(a) por Média\n')


            print("-----------------------")