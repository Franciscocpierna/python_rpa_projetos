"""
PyPDF2

PyPDF2 é uma biblioteca em Python usada para trabalhar
com arquivos PDF. Ela oferece uma série de funcionalidades 
para manipular esses arquivos, incluindo:

    Leitura de informações de arquivos PDF, como texto, 
    metadados e número de páginas.

    Modificação de PDFs, que pode incluir mesclar ou dividir 
    documentos, rotacionar páginas, adicionar marcas d'água, etc.

    Extrair conteúdo, como texto ou outras informações, de arquivos PDF.

PyPDF2 é especialmente útil para automação de tarefas que envolvem 
manipulação de arquivos PDF em programas Python.


Tabula

Tabula é uma ferramenta de software livre que é usada para extrair
tabelas de arquivos PDF. Ela é normalmente utilizada por pessoas que 
trabalham com dados e precisam converter informações contidas em tabelas 
de PDFs para um formato mais manipulável, como CSV ou Excel. O Tabula tem 
uma interface gráfica que permite aos usuários identificar visualmente e 
extrair tabelas de documentos PDF.


tabula-py

tabula-py é uma biblioteca em Python que atua como um wrapper
para o Tabula, mencionado acima. Ela permite que os usuários 
utilizem as funcionalidades do Tabula diretamente de seus scripts 
Python. Com o tabula-py, é possível automatizar a extração de tabelas 
de PDFs e convertê-las em DataFrames do pandas, facilitando a análise e 
manipulação de dados em Python.

pathlib

pathlib é um módulo da biblioteca padrão do Python que fornece uma 
abordagem orientada a objetos para trabalhar com caminhos de arquivos e
diretórios. Ele oferece várias classes que representam os caminhos do 
sistema de arquivos e fornece métodos e propriedades fáceis de usar para 
lidar com operações comuns relacionadas a caminhos, como:

    Construir caminhos de maneira intuitiva e portátil entre 
    diferentes sistemas operacionais.

    Ler e escrever arquivos.

    Manipular estruturas de diretórios, como criar novos diretórios ou
    listar arquivos dentro de um diretório.

A principal vantagem do pathlib é a sua interface intuitiva e a maneira 
como simplifica muitas das operações de sistema de arquivos que normalmente 
requerem múltiplas chamadas para funções em módulos como os e os.path.
"""
print()



import PyPDF2 as opcoesPDF

#Ler um arquivo PDF
opcoesPDF.PdfFileReader

#Cria / Escreve um arquivo PDF
#Não vamos consegui alterar os dados em um arquivo PDF
opcoesPDF.PdfFileWriter

#Junta dois ou mais arquivos de PDF
opcoesPDF.PdfFileMerger


# Importa a classe PdfReader do módulo PyPDF2.
# PdfReader é a classe atualizada usada para ler arquivos PDF
from PyPDF2 import PdfReader

# Define o caminho para o arquivo PDF que será lido.
caminhoArquivo = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Mercado_Livre.pdf"

# Cria um objeto 'arquivo_Mercado_Livre' usando a classe 'PdfReader' da biblioteca PyPDF2.
# 'PdfReader' é usada para abrir e ler o conteúdo de um arquivo PDF.
arquivo_Mercado_Livre = PdfReader(caminhoArquivo)

# A variável 'numeroPaginas' é definida para armazenar o número total de páginas do arquivo PDF.
# O número de páginas pode ser obtido acessando o atributo 'pages' e usando a função 'len' para contar os elementos.
numeroPaginas = len(arquivo_Mercado_Livre.pages)

# Imprime na tela a quantidade de páginas do arquivo PDF.
print(f"{numeroPaginas} páginas")

# Para acessar as informações do documento, como autor, título, etc., 
# é necessário utilizar a propriedade apropriada.
# As informações do documento podem não estar disponíveis diretamente
# através de uma propriedade específica como 'document_info'.
# Podemos tentar acessar as informações através dos métodos disponíveis 
# na documentação atual da biblioteca.

# Tentativa de acessar as informações do documento.
try:
    
    # Acesso às Informações do Documento por metadata
    informacoes = arquivo_Mercado_Livre.metadata
    
    # Imprime as informações do documento PDF na tela.
    # Essas informações podem incluir o título do documento, autor, assunto, entre outros.
    print(informacoes)
    
except AttributeError:
    print("Não foi possível acessar as informações do documento.")