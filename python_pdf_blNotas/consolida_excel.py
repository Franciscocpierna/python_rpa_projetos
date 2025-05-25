import pandas as opcoesPandas
import os

arquivoTextoConsolidado = open("C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\consolidar\\Arquivo_Exercicio_Bloco_Notas_Consolidado.txt", "w")

#Caminho onde estão os arquivos
caminhoArquivos = "C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\consolidar"

#Variável onde estão todos os arquivos
listaArquivos = os.listdir(caminhoArquivos)

#print(listaArquivos)

listaCaminhoEArquivoBlocoNotas = [caminhoArquivos + '\\' + arquivo for arquivo in listaArquivos if arquivo[-3:] == 'txt']

#print(listaCaminhoEArquivoBlocoNotas)

#Criando os DataFrame para trabalhar com os Dados
dadosArquivo = opcoesPandas.DataFrame()

#Titulo
arquivoTextoConsolidado.write('Linha;Escola;ID;Aluno;Primeiro Nome;Sobrenome;CPF;Idade\n')

#Copiando todos os dados dos arquivos em dadosArquivo
for arquivo in listaCaminhoEArquivoBlocoNotas:
    
    #Pego as informações de cada bloco de notas e armazeno como um DF em Dados
    #dados = opcoesPandas.read_csv(arquivo)
    dados = opcoesPandas.read_csv(arquivo, delimiter=';')
    
    #Percorrer todo o arquivo a partir da segunda linha
    for pulaTitulo, linha in dados.iterrows():
        
        #Quebramos o texto que estava tudo na mesma linha e separamos em linhas
        #['ABC;782707;Aline Rosa Ferreira;CPF: 12345678910;36']
        linha = [item.split(';', 0)[0] for item in linha]
        
        #Resposta da segunda questão
        #Separando a linha em colunas atravé do delimitador ;
        separaLinhasEmColunas = linha[0].split(';')
        
        escola = separaLinhasEmColunas[0]
        idAluno = separaLinhasEmColunas[1]
        aluno = separaLinhasEmColunas[2]
        cpf = separaLinhasEmColunas[3]
        idade = separaLinhasEmColunas[4]
        
        #Resposta da terceira questão
        #split quebra o nome em colunas através do espaço em branco
        #pego a posição 0 que é a primeira coluna
        primeiroNome = aluno.split(' ')[0] #Quebro em coluna e pego a coluna 0
        
        #split quebra o nome em colunas através do espaço em branco
        #pego a posição última coluna
        sobrenome = aluno.split(' ')[-1] #Quebro em coluna e pego a última coluna
        
        #Resposta da quarta questão
        #CPF: 12345678910
        #Pegando partes do CPF que veio dos arquivo de texto do bloco de notas
        cpf_parte1 = cpf[5:8] #três números a partir da 5 posição
        cpf_parte2 = cpf[8:11] #três números a partir da 8 posição
        cpf_parte3 = cpf[11:14] #três números a partir da 11 posição
        cpf_parte4 = cpf[14:16] #dois números a partir da 14 posição
        
        #No CPF estou juntando as partes e formando o CPF com os pontos e traço
        cpf = str(cpf_parte1) + "." + str(cpf_parte2) + "." + str(cpf_parte3) + "-" + str(cpf_parte4)
              
        #Salvo os dados em formato que o pandas reconhece para salvar no Excel
        #Salvo no Bloco de Notas
        arquivoTextoConsolidado.write(';' + escola + ';' + idAluno + ';' + aluno + ';' + primeiroNome + ';' + sobrenome + ';' + cpf + ';' + idade + '\n')
        

#Fecho o bloco de notas que tem todos os dados consolidados
arquivoTextoConsolidado.close() 

idiomaParaAcentosDoArquivo = 'cp1252'

#Abro o arquivo do bloco de notas como csv
lerArquivoBlocoNotasConsolidado = opcoesPandas.read_csv("C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\consolidar\\Arquivo_Exercicio_Bloco_Notas_Consolidado.txt", encoding=idiomaParaAcentosDoArquivo)

#Criando uma nova planilha e passando os dados dos arquivos
#dadosArquivo.to_excel("A:\\Python RPA\\Arquivo Texto e PDF\\Arquivo Consolidado.xlsx")
lerArquivoBlocoNotasConsolidado.to_csv('C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\consolidar\\Arquivo Final Exercicio Texto.csv', encoding='utf-8-sig')

