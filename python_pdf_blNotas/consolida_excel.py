import pandas as opcoesPandas
import os
 
arquivoTextoConsolidado = open("C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\consolidar\\Arquivo_Exercicio_Bloco_Notas_Consolidado.txt", "w")
 
caminhoArquivos = "C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\consolidar"
 
listaArquivos = os.listdir(caminhoArquivos)
 
# Lista somente arquivos .txt que não contenham 'Consolidado' no nome
listaCaminhoEArquivoBlocoNotas = [
    os.path.join(caminhoArquivos, arquivo)
    for arquivo in listaArquivos
    if arquivo.endswith('.txt') and 'Consolidado' not in arquivo
]
 
# Escreve o cabeçalho no arquivo consolidado
arquivoTextoConsolidado.write('Linha;Escola;ID;Aluno;Primeiro Nome;Sobrenome;CPF;Idade\n')
 
for arquivo in listaCaminhoEArquivoBlocoNotas:
    try:
        dados = opcoesPandas.read_csv(arquivo, encoding='cp1252', sep=';', header=0)
 
        for _, linha in dados.iterrows():
            escola = str(linha['Escola'])
            idAluno = str(linha['ID'])
            aluno = str(linha['Aluno'])
            cpf = str(linha['CPF'])
            idade = str(linha['Idade'])
 
            primeiroNome = aluno.split(' ')[0]
            sobrenome = aluno.split(' ')[-1]
 
            # Ex: CPF: 12345678910
            cpf_num = cpf.replace("CPF: ", "")
            cpf_formatado = f"{cpf_num[:3]}.{cpf_num[3:6]}.{cpf_num[6:9]}-{cpf_num[9:11]}"
 
            linha_final = f";{escola};{idAluno};{aluno};{primeiroNome};{sobrenome};{cpf_formatado};{idade}\n"
            arquivoTextoConsolidado.write(linha_final)
 
    except Exception as e:
        print(f"Erro ao processar o arquivo {arquivo}: {e}")
 
arquivoTextoConsolidado.close()
 
# Agora converte para CSV
lerArquivoBlocoNotasConsolidado = opcoesPandas.read_csv(
    "C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\consolidar\\Arquivo_Exercicio_Bloco_Notas_Consolidado.txt",
    encoding='cp1252',
    sep=';'
)
 
lerArquivoBlocoNotasConsolidado.to_csv(
    'C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\consolidar\\Arquivo Final Exercicio Texto.csv',
    encoding='utf-8-sig',
    index=False
)
