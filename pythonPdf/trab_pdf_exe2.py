# Importa a classe PdfReader do módulo PyPDF2.
# PdfReader é uma classe que permite ler o conteúdo de arquivos PDF.
from PyPDF2 import PdfReader

# Cria um objeto 'arquivoPDF' usando a classe PdfReader.
# 'PdfReader' é usada para abrir e interagir com o conteúdo de um arquivo PDF.
# O arquivo "Evolução_Amazon.pdf" é especificado como argumento, indicando o arquivo a ser lido.
# Esse arquivo deve estar localizado no mesmo diretório que o script Python, ou um caminho completo deve ser fornecido.
arquivoPDF = PdfReader("C:\python_projetos\python_rpa_projetos\pythonPdf\Evolução_Amazon.pdf")

# A variável 'contaNumeroPaginas' é definida para armazenar o número total de páginas no arquivo PDF.
# 'len(arquivoPDF.pages)' é utilizado para contar quantas páginas existem no documento PDF.
# 'arquivoPDF.pages' retorna uma lista de objetos de página, e 'len()' conta o número de elementos nessa lista.
contaNumeroPaginas = len(arquivoPDF.pages)

# Imprime o número total de páginas do arquivo PDF na tela.
print(contaNumeroPaginas)

# Cria um objeto 'pagina' que representa a primeira página do arquivo PDF.
# O acesso às páginas é feito por meio de índices baseados em zero, então 'arquivoPDF.pages[0]' se refere à primeira página.
pagina = arquivoPDF.pages[0]

# Extrai o texto da primeira página do arquivo PDF e o armazena na variável 'textoPagina1'.
# O método 'extract_text()' é usado para extrair o texto da página representada pelo objeto 'pagina'.
textoPagina1 = pagina.extract_text()

# Imprime o texto extraído da primeira página do arquivo PDF na tela.
print(textoPagina1)